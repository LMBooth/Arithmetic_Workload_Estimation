param(
    [string]$DatasetId = "",
    [string]$ArchiveUrl = "",
    [string]$Target = "data/bids_arithmetic",
    [string]$Config = "analysis_pipeline/config/pipeline.yaml",
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

python @downloadArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

python analysis_pipeline/run_pipeline.py --config $Config
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}

Write-Host "End-to-end run complete."
