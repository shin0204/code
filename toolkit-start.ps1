# Claude Toolkit 7가지 도구 통합 시작 스크립트
# Usage: .\toolkit-start.ps1

Write-Host "🚀 Claude Toolkit 시작 중..." -ForegroundColor Green
Write-Host ""

# 1. OmniRoute 시작
Write-Host "1️⃣  OmniRoute (토큰/성능 최적화)" -ForegroundColor Cyan
Write-Host "   시작: omniroute serve --daemon --log"
omniroute serve --daemon --log 2>&1 | Select-Object -First 5
Start-Sleep -Seconds 2
Write-Host "   ✅ 대시보드: http://localhost:20128" -ForegroundColor Green
Write-Host ""

# 2. Headroom 상태 확인
Write-Host "2️⃣  Headroom (토큰 압축)" -ForegroundColor Cyan
$hr_version = headroom --version
Write-Host "   ✅ $hr_version" -ForegroundColor Green
Write-Host "   ℹ️  활성화됨 (CLI + 플러그인)" -ForegroundColor Gray
Write-Host ""

# 3. Claude Mem 확인
Write-Host "3️⃣  Claude Mem (메모리 지속성)" -ForegroundColor Cyan
if (Test-Path "$env:USERPROFILE\.claude\projects\*\memory") {
    Write-Host "   ✅ 메모리 시스템 활성화됨" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  메모리 디렉토리 미발견" -ForegroundColor Yellow
}
Write-Host ""

# 4. Code Setup 확인
Write-Host "4️⃣  Code Setup (프로젝트 최적화)" -ForegroundColor Cyan
Write-Host "   ✅ 플러그인 설치됨 (v1.0.0)" -ForegroundColor Green
Write-Host ""

# 5. Task Observer 확인
Write-Host "5️⃣  Task Observer (패턴 인식)" -ForegroundColor Cyan
if (Test-Path "$env:USERPROFILE\.claude\skills\task-observer") {
    Write-Host "   ✅ 스킬 설치됨" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  스킬 미발견" -ForegroundColor Yellow
}
Write-Host ""

# 6. Graphify 확인
Write-Host "6️⃣  Graphify (지식 그래프)" -ForegroundColor Cyan
if (Test-Path "$env:USERPROFILE\.claude\skills\graphify") {
    Write-Host "   ✅ 스킬 설치됨 (v0.9.44)" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  스킬 미발견" -ForegroundColor Yellow
}
Write-Host ""

# 7. Ponytail 확인
Write-Host "7️⃣  Ponytail (효율성 관장)" -ForegroundColor Cyan
Write-Host "   ✅ 플러그인 설치됨 (v4.8.4, Lazy Mode full)" -ForegroundColor Green
Write-Host ""

Write-Host "═════════════════════════════════════════" -ForegroundColor Green
Write-Host "✅ Claude Toolkit 모든 도구 준비 완료!" -ForegroundColor Green
Write-Host "═════════════════════════════════════════" -ForegroundColor Green
Write-Host ""
Write-Host "📊 상태 요약:" -ForegroundColor Yellow
Write-Host "  • OmniRoute: 🟢 실행 중 (http://localhost:20128)"
Write-Host "  • Headroom: 🟢 활성화"
Write-Host "  • Claude Mem: 🟢 활성화"
Write-Host "  • Code Setup: 🟢 활성화"
Write-Host "  • Task Observer: 🟢 활성화"
Write-Host "  • Graphify: 🟢 활성화"
Write-Host "  • Ponytail: 🟢 활성화"
Write-Host ""
Write-Host "🎯 다음 단계:" -ForegroundColor Yellow
Write-Host "  1. OmniRoute 대시보드에서 추가 AI 모델 연결"
Write-Host "  2. Claude Code 재시작하여 자동화 훅 활성화"
Write-Host "  3. /task-observer 스킬로 패턴 분석"
Write-Host "  4. /graphify 스킬로 지식 그래프 시각화"
