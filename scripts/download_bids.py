from __future__ import annotations

import argparse
import shutil
import subprocess
import tarfile
import tempfile
import urllib.request
import zipfile
from pathlib import Path


def _is_bids_root(path: Path) -> bool:
    if not path.exists() or not path.is_dir():
        return False
    if not (path / "dataset_description.json").exists():
        return False
    return any(child.is_dir() and child.name.startswith("sub-") for child in path.iterdir())


def _download_url(url: str, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, out_path.open("wb") as out:
        while True:
            chunk = response.read(1024 * 1024)
            if not chunk:
                break
            out.write(chunk)


def _extract_archive(archive_path: Path, extract_dir: Path) -> None:
    suffixes = [s.lower() for s in archive_path.suffixes]
    if suffixes and suffixes[-1] == ".zip":
        with zipfile.ZipFile(archive_path, "r") as zf:
            zf.extractall(extract_dir)
        return
    if ".tar" in suffixes or ".tgz" in suffixes or suffixes[-2:] == [".tar", ".gz"]:
        with tarfile.open(archive_path, "r:*") as tf:
            tf.extractall(extract_dir)
        return
    raise ValueError(f"Unsupported archive type: {archive_path.name}")


def _find_bids_root(search_dir: Path) -> Path:
    if _is_bids_root(search_dir):
        return search_dir
    candidates: list[Path] = []
    for desc in search_dir.rglob("dataset_description.json"):
        root = desc.parent
        if _is_bids_root(root):
            candidates.append(root)
    unique = sorted({c.resolve() for c in candidates})
    if not unique:
        raise RuntimeError("No valid BIDS root found after extraction.")
    if len(unique) > 1:
        formatted = "\n".join(f"- {p}" for p in unique)
        raise RuntimeError(f"Multiple BIDS roots found. Please pick one manually:\n{formatted}")
    return unique[0]


def _prepare_target(target: Path, force: bool) -> None:
    if target.exists():
        if not force:
            raise FileExistsError(f"Target already exists: {target}. Use --force to replace it.")
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)


def _download_from_openneuro(dataset_id: str, target: Path, snapshot: str | None) -> None:
    cli = shutil.which("openneuro")
    if cli is None:
        raise RuntimeError(
            "OpenNeuro CLI not found. Install it first:\n"
            "  pip install openneuro-py\n"
            "Then ensure 'openneuro' is on PATH."
        )

    cmd = [cli, "download", f"--dataset={dataset_id}", f"--target={target}"]
    if snapshot:
        cmd.append(f"--snapshot={snapshot}")
    subprocess.run(cmd, check=True)

    if not _is_bids_root(target):
        raise RuntimeError(f"OpenNeuro download completed but target is not a valid BIDS root: {target}")


def _download_from_archive(url: str, target: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="bids_download_") as tmp:
        tmp_dir = Path(tmp)
        archive_name = url.rstrip("/").split("/")[-1] or "bids_archive.zip"
        archive_path = tmp_dir / archive_name
        _download_url(url, archive_path)
        extract_dir = tmp_dir / "extracted"
        extract_dir.mkdir(parents=True, exist_ok=True)
        _extract_archive(archive_path, extract_dir)
        bids_root = _find_bids_root(extract_dir)
        shutil.copytree(bids_root, target)


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a BIDS dataset to a local folder.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--dataset-id", help="OpenNeuro dataset ID (example: ds003XXX).")
    source.add_argument("--archive-url", help="Direct URL to a BIDS archive (.zip/.tar/.tar.gz/.tgz).")
    parser.add_argument("--snapshot", default=None, help="Optional OpenNeuro snapshot tag/version.")
    parser.add_argument(
        "--target",
        default="data/bids_arithmetic",
        help="Local destination folder for the BIDS dataset (default: data/bids_arithmetic).",
    )
    parser.add_argument("--force", action="store_true", help="Replace target folder if it already exists.")
    args = parser.parse_args()

    target = Path(args.target).expanduser().resolve()
    _prepare_target(target, force=args.force)

    if args.dataset_id:
        _download_from_openneuro(args.dataset_id, target, args.snapshot)
        source_text = f"OpenNeuro dataset {args.dataset_id}"
    else:
        _download_from_archive(args.archive_url, target)
        source_text = args.archive_url

    print("BIDS download complete.")
    print(f"  Source: {source_text}")
    print(f"  Target: {target}")


if __name__ == "__main__":
    main()
