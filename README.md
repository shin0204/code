# Claude Toolkit

Claude Code 세션을 매번 동일하게 구성하는 7개 도구 묶음 + 설치 스크립트.

## 7개 도구

| # | 도구 | 형태 | 출처 | 역할 |
|---|------|------|------|------|
| 1 | Claude Code Setup | 플러그인 | `claude-code-setup@claude-plugins-official` | 프로젝트 타입 인식 · 설정 추천 |
| 2 | Headroom | CLI + 플러그인 | `chopratejas/headroom` | 토큰 압축 (프록시 `127.0.0.1:8787`) |
| 3 | OmniRoute | npm 전역 | `npm i -g omniroute` | 모델 라우팅 (대시보드 `:20128`) |
| 4 | Claude Mem | 플러그인 | `thedotmack/claude-mem` | 세션 간 장기 메모리 (MCP) |
| 5 | Task Observer | 스킬 | `rebelytics/one-skill-to-rule-them-all` | 작업 패턴 분석 · 자가개선 |
| 6 | Ponytail | 플러그인 | `DietrichGebert/ponytail` | Lazy Mode (YAGNI) |
| 7 | Graphify | 스킬 + CLI | 이 저장소 `skills/graphify` | 지식 그래프 생성 |

## 추가 스킬/플러그인

- `document-skills@anthropic-agent-skills` — docx / pdf / pptx / xlsx
- `example-skills@anthropic-agent-skills` — canvas-design, frontend-design, mcp-builder 등
- `caveman@caveman` — 출력 토큰 압축 (JuliusBrussee/caveman)
- `humanizer` — AI 티 나는 문장 교정 (`npx skills add blader/humanizer`)

## 설치

```powershell
git clone https://github.com/shin0204/code.git
cd code
PowerShell -ExecutionPolicy Bypass -File .\install.ps1
```

설치 후 `settings.template.json` 을 `~/.claude/settings.json` 으로 옮기고 Claude Code 를 재시작한다.

## 실행 플로우

- **SessionStart** — OmniRoute(모델 선택) → Claude Mem(메모리 로드) → Code Setup(환경)
- **작업 중** — Headroom(토큰 압축) + Ponytail(최소 코드) + Task Observer(패턴, 백그라운드)
- **SessionEnd** — Task Observer(분석) → Graphify(그래프) → Claude Mem(저장)

상태 확인: `PowerShell -ExecutionPolicy Bypass -File .\toolkit-start.ps1`

## 구성

```
install.ps1              전체 설치
toolkit-start.ps1        7개 도구 상태 확인 / 기동
settings.template.json   ~/.claude/settings.json 템플릿 (로컬 값·자격증명 제외)
CLAUDE.md                오케스트레이션 지침
skills/graphify/         로컬 전용 스킬
skills/claude-toolkit-setup/
```

## 주의

`settings.template.json` 에는 자격증명이 없다. API 키는 각 도구의 자체 설정(OmniRoute 대시보드, `.env`)에 두고 커밋하지 않는다.
