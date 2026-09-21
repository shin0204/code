# Claude Toolkit 설치 스크립트 (7개 도구 + 추가 스킬)
# Usage: PowerShell -ExecutionPolicy Bypass -File .\install.ps1

$ErrorActionPreference = "Continue"
$ClaudeDir = "$env:USERPROFILE\.claude"

Write-Host "== 1. CLI / npm 도구 ==" -ForegroundColor Cyan
npm install -g omniroute            # OmniRoute 3.8.49 - 모델 라우팅
pipx install headroom               # Headroom 0.37.0 - 토큰 압축 (또는 pip install headroom)
npm install -g graphify-cli          # Graphify CLI 0.9.30 - 지식 그래프

Write-Host "== 2. 마켓플레이스 등록 ==" -ForegroundColor Cyan
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add anthropics/skills          # anthropic-agent-skills
claude plugin marketplace add thedotmack/claude-mem
claude plugin marketplace add chopratejas/headroom
claude plugin marketplace add DietrichGebert/ponytail
claude plugin marketplace add JuliusBrussee/caveman

Write-Host "== 3. 플러그인 설치 ==" -ForegroundColor Cyan
claude plugin install claude-code-setup@claude-plugins-official --scope user
claude plugin install claude-mem@thedotmack --scope user
claude plugin install headroom@headroom-marketplace --scope user
claude plugin install ponytail@ponytail --scope user
claude plugin install document-skills@anthropic-agent-skills --scope user
claude plugin install example-skills@anthropic-agent-skills --scope user
claude plugin install caveman@caveman --scope user

Write-Host "== 4. 스킬 설치 ==" -ForegroundColor Cyan
# Task Observer (업스트림 클론)
if (-not (Test-Path "$ClaudeDir\skills\task-observer")) {
    git clone --depth 1 https://github.com/rebelytics/one-skill-to-rule-them-all "$ClaudeDir\skills\task-observer"
}
# Humanizer (skills.sh)
npx -y skills add blader/humanizer

# 이 저장소에 포함된 로컬 스킬 복사
Copy-Item -Recurse -Force "$PSScriptRoot\skills\graphify" "$ClaudeDir\skills\"
Copy-Item -Recurse -Force "$PSScriptRoot\skills\claude-toolkit-setup" "$ClaudeDir\skills\"

Write-Host "== 5. 설정 ==" -ForegroundColor Cyan
Write-Host "settings.template.json 을 참고해 $ClaudeDir\settings.json 을 구성하세요." -ForegroundColor Yellow
Write-Host "CLAUDE.md 를 프로젝트 루트 또는 $ClaudeDir 에 배치하세요." -ForegroundColor Yellow

Write-Host "`n설치 완료. Claude Code 를 재시작하세요." -ForegroundColor Green
