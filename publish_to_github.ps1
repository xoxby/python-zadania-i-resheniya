# Один раз: войти в GitHub, затем создать ПРИВАТНЫЙ репозиторий и отправить ветку main.
# Запуск: правый клик -> "Выполнить с помощью PowerShell" ИЛИ в терминале:
#   cd "путь\к\python_assignments_solutions"
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
#   .\publish_to_github.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

$env:Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path", "User")

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "Установи GitHub CLI: winget install GitHub.cli"
    exit 1
}

gh auth status 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Нужен вход в GitHub (откроется браузер). Выполни шаги в окне."
    gh auth login -h github.com -p https -w
}

# Имя репозитория на GitHub (можно поменять)
$repoName = "python-zadania-i-resheniya"

Write-Host "Создаю приватный репозиторий $repoName и делаю push..."
git branch -M main

# Если remote уже есть — только push
$hasOrigin = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0) {
    git push -u origin main
    Write-Host "Готово: git push выполнен."
    exit 0
}

gh repo create $repoName --private --source . --remote origin --push --description "Python: 20 moduley — zadaniya i resheniya"
Write-Host "Готово. Репозиторий: https://github.com/$(gh api user -q .login)/$repoName"
