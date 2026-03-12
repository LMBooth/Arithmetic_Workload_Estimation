param(
    [string]$DatasetId = "",
    [string]$ArchiveUrl = "",
    [string]$Target = "data/bids_arithmetic",
    [string]$Config = "analysis_pipeline/config/pipeline_unified_classic_nn_baseline_preproc.yaml",
    [switch]$ForceDownload
)

$ErrorActionPreference = "Stop"

if ([string]::IsNullOrWhiteSpace($DatasetId) -and [string]::IsNullOrWhiteSpace($ArchiveUrl)) {
    throw "Provide either -DatasetId or -ArchiveUrl."
}

$downloadArgs = @("scripts/download_bids.py", "--target", $Target)
if ($ForceDownload) {
    $downloadArgs += "--force"
}
if (-not [string]::IsNullOrWhiteSpace($DatasetId)) {
    $downloadArgs += @("--dataset-id", $DatasetId)
} else {
    $downloadArgs += @("--archive-url", $ArchiveUrl)
}

Write-Host "[1/2] Downloading BIDS dataset..."
Write-Host "  Target: $Target"
python @downloadArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "[2/2] Running analysis pipeline..."
Write-Host "  Config: $Config"
python analysis_pipeline/run_pipeline.py --config $Config
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "End-to-end run complete."
