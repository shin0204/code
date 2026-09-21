# toolkit-orchestration
Claude Toolkit (7 key tools integrated flow) will be automatically active for every session.

## 🎯 7가지 핵심 도구 통합

### 1️⃣ OmniRoute - 토큰/성능 최적화
- **목표**: 다양한 Claude 모델로 자동 전환하여 비용-성능 최적화
- **활성 모델**: claude-opus-5, claude-sonnet-5, claude-haiku-4-5-20251001
- **예상 효율**: 토큰 92% 효율화

### 2️⃣ Headroom - 토큰 압축
- **목표**: 동일 작업을 더 적은 토큰으로 수행
- **압축 전략**: aggressive
- **목표 압축율**: 15%

### 3️⃣ Claude Mem - 메모리 지속성
- **목표**: 세션 간 장기 메모리 저장 및 자동 로드
- **위치**: ~/.claude/projects/G--------/memory/
- **메모리 슬롯**: 8개

### 4️⃣ Code Setup - 프로젝트 환경 최적화
- **목표**: 프로젝트별 최적 설정 추천 및 자동 구성
- **프로젝트 타입 자동 인식**: 활성화
- **팀 설정 동기화**: 지원

### 5️⃣ Task Observer - 패턴 인식
- **목표**: 작업 패턴 자동 분석 및 개선 기회 식별
- **패턴 학습**: 3개 패턴 인식 중
- **자가개선 제안**: 자동 생성

### 6️⃣ Graphify - 지식 그래프 시각화
- **목표**: 지식을 그래프 형태로 구조화 및 시각화
- **노드 수**: 127개 관리 중
- **학습 효과**: 극대화

### 7️⃣ Ponytail - 효율성 관장
- **목표**: Lazy Mode로 최소 필요 코드만 작성 (YAGNI 원칙)
- **모드**: full
- **기술 부채**: 최소화

## 📋 Flows
- **Optimize Performance**: OmniRoute (Model Selection) + Headroom (Token Compression)
- **Session Memory**: Claude Mem (Long-term Memory persistence)
- **Workspace Setup**: Claude Code Setup (Project configuration recommendations)
- **Self Improvement**: Task Observer (Pattern recognition) + Graphify (Knowledge Graph visualization)
- **Code Efficiency**: Ponytail (Lazy Mode / YAGNI rule)

## 🔄 Automatic Execution Hooks

### SessionStart Flow
1. **OmniRoute**: 모델 상태 확인 및 최적 모델 선택
2. **Claude Mem**: 관련 메모리 자동 로드
3. **Code Setup**: 프로젝트 최적 설정 제안
4. **Graphify**: 이전 세션 지식 그래프 로드

### Task Execution Flow
- **Headroom**: 필요시 토큰 압축 (선택적)
- **Ponytail**: 항상 활성화 (최소 필요 코드 원칙)
- **Task Observer**: 패턴 인식 (백그라운드)

### SessionEnd Flow
1. **Task Observer**: 관찰된 패턴 분석 및 개선사항 식별
2. **Graphify**: 세션 내용을 지식 그래프로 시각화
3. **Claude Mem**: 세션 요약 및 인사이트 저장
4. **다음 세션**: 추천 구성 자동 생성

## ✅ 설치 상태 (2026-09-21 검증)
- [x] OmniRoute 3.8.49 (npm 전역, Anthropic 연결됨)
- [x] Headroom 0.37.0 (CLI + 플러그인, 프록시 127.0.0.1:8787)
- [x] Claude Mem 13.15.0 (플러그인, MCP 연결됨)
- [x] Code Setup 1.0.0 (플러그인)
- [x] Task Observer (스킬 ~/.claude/skills/task-observer)
- [x] Graphify CLI 0.9.30 (스킬 ~/.claude/skills/graphify)
- [x] Ponytail 4.8.4 (플러그인, Lazy Mode full)
- [x] settings.json 생성 및 구성
- [x] 자동화 훅 적용

## 🚀 빠른 시작

### 첫 시작 (원타임)
```powershell
# 1. Toolkit 초기화 (모든 도구 확인)
PowerShell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.claude\toolkit-start.ps1"

# 2. Claude Code 재시작 (플러그인 활성화)
# → VS Code / Claude Code 앱 재시작

# 3. 세션 시작 (자동화 활성화)
# → 첫 세션: OmniRoute → Claude Mem → Code Setup 자동 실행
```

### 매 세션마다 자동 실행
1. **SessionStart**: OmniRoute (모델 선택) → Claude Mem (메모리 로드) → Code Setup
2. **TaskExecution**: Headroom (토큰 압축) + Ponytail (YAGNI) + Task Observer (패턴)
3. **SessionEnd**: Task Observer → Graphify → Claude Mem (저장)

### 수동 스킬 실행
```
/task-observer   # 패턴 분석 및 개선사항
/graphify        # 지식 그래프 시각화
/claude-mem      # 메모리 관리
```
