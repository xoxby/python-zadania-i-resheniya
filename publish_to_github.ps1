# Requires: gh auth login (once). Creates private repo and pushes branch main.
# Run from this folder:
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
#   .\publish_to_github.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "Install GitHub CLI: winget install GitHub.cli"
    exit 1
}

gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Not logged in. Opening browser login..."
    gh auth login -h github.com -p https -w
}

$repoName = "python-zadania-i-resheniya"

Write-Host "Creating private repo '$repoName' and pushing..."
git branch -M main

git remote get-url origin 2>$null | Out-Null
if ($LASTEXITCODE -eq 0) {
    git push -u origin main
    Write-Host "Done: push completed."
    exit 0
}

$desc = "Python: 20 modules - tasks and solutions"
gh repo create $repoName --private --source . --remote origin --push --description $desc

$user = gh api user --jq .login
$url = "https://github.com/$user/$repoName"
Write-Host "Done. Repo: $url"
