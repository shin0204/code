# Claude Toolkit 연결 상태

7개 핵심 도구 + 4개 추가 스킬/마켓플레이스, 총 11개 연결 확인.

## 1-7. 핵심 도구
| # | 도구 | 종류 | 상태 | 버전/출처 |
|---|------|------|------|-----------|
| 1 | Claude Code Setup | plugin | 연결됨 | claude-code-setup@claude-plugins-official v1.0.0 |
| 2 | Headroom | CLI | 연결됨 | v0.38.0, `~/.local/bin/headroom.exe` |
| 3 | OmniRoute | npm 패키지 | 연결됨 | omniroute@3.8.49 (global) |
| 4 | Claude Mem | plugin | 연결됨 | claude-mem@thedotmack v13.15.0 |
| 5 | Task Observer | skill | 연결됨 | `~/.claude/skills/task-observer` |
| 6 | Ponytail | plugin | 연결됨 | ponytail@ponytail v4.8.4 |
| 7 | Graphify | skill | 연결됨 | `~/.claude/skills/graphify` |

## 8-11. 마켓플레이스 / 스킬
| # | 항목 | 상태 |
|---|------|------|
| 8 | marketplace add anthropics/skills → document-skills 설치 | 완료 (anthropic-agent-skills) |
| 9 | example-skills 설치 | 완료 |
| 10 | npx skills add blader/humanizer | 완료 (skills-dir, v3.0.0) |
| 11 | marketplace add JuliusBrussee/caveman | 완료 (caveman@caveman v2.7.0) |

## 플로우 (SessionStart hook, config/settings.json 참고)
OmniRoute(모델선택) → Headroom(토큰절감) → Claude Mem(메모리) → Code Setup(환경) → Task Observer(패턴) → Graphify(그래프) → Ponytail(효율)

## 포함 파일
- `config/settings.json` — 전역 hooks/enabledPlugins/marketplaces 설정
- `config/installed_plugins.json` — 설치된 플러그인 목록
- `skills/task-observer/SKILL.md`
- `skills/graphify/SKILL.md`

개인정보/세션 데이터(claude-mem.db 등)는 제외함.
