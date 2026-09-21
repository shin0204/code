---
name: claude-toolkit-setup
description: |
  Claude의 7가지 핵심 도구를 통합 설치·초기화·플로우화하는 스킬. 
  한 번의 명령으로:
  1) 한도 최적화 (OmniRoute+Headroom)
  2) 메모리 지속성 (Claude Mem) 
  3) 프로젝트 환경 (Code Setup)
  4) 자가개선 (Task Observer+Graphify)
  5) CLAUDE.md 자동 관리
  
  Trigger: "toolkit setup", "toolkit init", "플로우 구축", "도구 초기화", "/init" 명령 실행 시 자동 포함
compatibility: |
  Required: Bash/PowerShell, npm, Python 3.7+, git
  Tools: OmniRoute, Headroom, Claude Mem plugin, Code Setup plugin, Task Observer skill, Graphify skill, Ponytail plugin
  Auto-triggers: /init 명령 실행 시 자동 포함
---

# Claude Toolkit Setup

Claude 작업 흐름을 완전히 최적화하는 7개 핵심 도구의 통합 설정 스킬입니다.

## 🎯 목표

사용자가 Claude와 함께 일할 때 다음 플로우가 자동으로 작동하도록 설정:

```
[토큰/성능 최적화]     OmniRoute + Headroom
         ↓
[메모리 지속성]        Claude Mem (세션 간 기억)
         ↓
[환경 최적화]          Claude Code Setup (프로젝트 맞춤)
         ↓
[자가 개선]            Task Observer + Graphify (학습 및 최적화)
         ↓
[효율성 관장]          Ponytail (Lazy Mode)
```

## 📋 7개 도구 소개

### 1️⃣ 한도를 늘린다 (토큰/성능)

**OmniRoute** (npm 패키지)
- 다양한 모델로 자동 전환
- 최적의 비용-성능 균형 자동 계산
- 모델별 성능 모니터링

**Headroom** (CLI 도구)
- 같은 작업을 적은 토큰으로 수행
- 프롬프트 최적화 및 압축
- 컨텍스트 윈도우 효율화

### 2️⃣ 기억을 잇는다 (메모리)

**Claude Mem** (플러그인)
- 세션 간 장기 기억 저장
- 자동 메모리 검색 및 적용
- 패턴 인식 및 개인화

### 3️⃣ 환경을 잡는다 (설정)

**Claude Code Setup** (플러그인)
- 프로젝트별 최적 설정 추천
- 자동 설정 및 환경 구성
- 팀 설정 동기화

### 4️⃣ 스스로 나아진다 (자가 개선)

**Task Observer** (스킬)
- 사용 패턴 자동 분석
- 개선 기회 식별
- 새로운 스킬 제안 및 생성

**Graphify** (스킬)
- 지식을 그래프 형태로 시각화
- 정보 구조화 및 연결
- 학습 효과 극대화

### 5️⃣ 효율성을 관장한다 (모드)

**Ponytail** (플러그인)
- Lazy Mode 활성화 (효율적 최소 코드)
- YAGNI 원칙 강제 (불필요한 기능 제거)
- 기술 부채 최소화

---

## 🚀 스킬 사용 방법

### 시나리오 1: 처음 설정

```
사용자: "toolkit setup"
Claude:
1. 설치 상태 전체 스캔
2. 누락된 도구 자동 설치
3. Claude Mem DB 초기화
4. CLAUDE.md 자동 생성/업데이트
5. SessionStart/SessionEnd 훅 구성
6. 통합 대시보드 표시
```

### 시나리오 2: 특정 도구만 초기화

```
사용자: "Claude Mem 설정해줘"
Claude: Claude Mem 데이터베이스만 초기화 및 검증
```

### 시나리오 3: 플로우 상태 확인

```
사용자: "toolkit status" 또는 "플로우 상태 보기"
Claude: 
- 각 도구 설치 상태
- 플로우별 활성화 여부
- 최근 사용 통계
- 개선 제안사항
```

---

## 🔧 설정 항목

### CLAUDE.md 자동 관리

스킬 실행 시 **기존 CLAUDE.md를 보존**하면서 toolkit 설정을 자동으로 추가합니다:

```markdown
# toolkit-orchestration
Claude Toolkit (7개 도구 통합 플로우)를 매 세션마다 자동으로 활성화한다.

## 플로우
- 한도 늘리기: OmniRoute (모델 선택) + Headroom (토큰 압축)
- 기억 잇기: Claude Mem (세션 간 메모리)
- 환경 잡기: Claude Code Setup (프로젝트 최적화)
- 스스로 나아지기: Task Observer (패턴 분석) + Graphify (지식 그래프)
- 효율성 관장: Ponytail (Lazy Mode)

## 자동 실행
- SessionStart: OmniRoute → Claude Mem → Code Setup
- 작업 수행: Headroom (필요시) + Ponytail (유지)
- SessionEnd: Task Observer → Graphify → Claude Mem 저장
```

**특징**:
- ✅ 기존 CLAUDE.md 내용 100% 보존
- ✅ toolkit 섹션만 자동 추가/업데이트
- ✅ 충돌 없음, 수동 편집 가능
- ✅ `/init` 명령 실행 시 자동 적용

### SessionStart 훅

```bash
1. OmniRoute 모델 상태 확인
2. Claude Mem에서 관련 메모리 로드
3. 프로젝트 설정 제안 (Code Setup)
4. 이번 세션 목표 설정
```

### SessionEnd 훅

```bash
1. Task Observer 실행 (관찰된 패턴 분석)
2. 개선사항 Graphify로 시각화
3. Claude Mem에 세션 요약 저장
4. 다음 세션 추천 구성
```

---

## ✅ 검증 항목

스킬 실행 후 다음 사항을 자동 검증:

- [ ] OmniRoute 서버 상태 (listening on localhost:20128)
- [ ] Headroom CLI 실행 가능 여부
- [ ] Claude Mem DB 생성 및 접근 가능
- [ ] Code Setup 플러그인 로드
- [ ] Task Observer 훅 활성화
- [ ] Graphify 스킬 로드
- [ ] Ponytail Lazy Mode 활성화
- [ ] CLAUDE.md 설정 적용
- [ ] 모든 설정 파일 JSON 유효성 검사

---

## 📊 사용 예시

### 예시 1: 새 프로젝트 시작

```
사용자: "새 프로젝트 시작, toolkit setup 해줘"

Claude는:
1. 프로젝트 디렉토리 탐지
2. 프로젝트 타입 인식 (web/backend/data/etc)
3. 최적 도구 조합 자동 구성
4. 팀 가이드라인 적용
5. 초기 스킬 세트 추천
```

### 예시 2: 효율성 개선

```
사용자: "최근 작업 분석해서 효율성 개선해줘"

Claude는:
1. Task Observer로 패턴 분석
2. Headroom으로 토큰 사용 최적화
3. Graphify로 지식 구조화
4. Claude Mem에 인사이트 저장
5. 다음 작업 추천 구성
```

### 예시 3: 문제 해결

```
사용자: "OmniRoute 안 됨"

Claude는:
1. OmniRoute 서버 상태 확인
2. Headroom으로 재시도 (토큰 절감)
3. 에러 로그 분석
4. 자동 복구 또는 수동 가이드 제공
5. 해결 과정을 Claude Mem에 저장
```

---

## 🎛️ 통합 대시보드 (실시간)

실행 후 다음을 표시:

```
╔════════════════════════════════════════════════════════════════╗
║         🚀 Claude Toolkit - 통합 대시보드                      ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║ 📊 도구 상태                                                   ║
║   ✅ OmniRoute     [모델 3개] 토큰 효율 92%                   ║
║   ✅ Headroom      [압축율 15%]                               ║
║   ✅ Claude Mem    [메모리 8개] 자동 로드 활성                ║
║   ✅ Code Setup    [프로젝트 맞춤]                            ║
║   ✅ Task Obs.     [훅 활성] 패턴 3개 인식                   ║
║   ✅ Graphify      [노드 127개]                               ║
║   ✅ Ponytail      [Lazy Mode ON]                             ║
║                                                                ║
║ 🔄 플로우 상태                                                 ║
║   ✅ 토큰/성능 최적화 (한도 늘리기)                           ║
║   ✅ 메모리 지속성 (기억 잇기)                                ║
║   ✅ 환경 최적화 (환경 잡기)                                  ║
║   ✅ 자가 개선 (스스로 나아지기)                              ║
║   ✅ 효율성 관장 (Ponytail)                                   ║
║                                                                ║
║ 💡 추천사항                                                    ║
║   • OmniRoute: claude-opus-5 추천 (비용 대비 성능 최고)      ║
║   • Headroom: 이전 대화 재요약 시 토큰 25% 절감 가능         ║
║   • Claude Mem: 3개 패턴 새로 인식 → 스킬화 권장             ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
```

---

## 🛠️ 문제 해결

| 문제 | 원인 | 해결 |
|------|------|------|
| OmniRoute 서버 안 열림 | 포트 충돌 또는 느린 시작 | `omniroute serve` 수동 실행, 30초 대기 |
| Headroom 명령 없음 | PATH 미설정 | `pip install headroom-ai[all]` 재실행 |
| Claude Mem 메모리 로드 안 됨 | DB 권한 문제 | `chmod 755 ~/.claude-mem/` |
| Code Setup 추천 없음 | 프로젝트 구조 미인식 | `git init` 또는 `package.json` 생성 |
| Task Observer 훅 안 실행 | 설정 파일 JSON 오류 | `jq . ~/.claude/settings.json` 검증 |

---

## 📚 참고 자료

- `references/tool_guide.md` - 각 도구 상세 가이드
- `references/flow_diagram.md` - 플로우 다이어그램
- 각 도구 공식 문서 (스킬 실행 중 자동 링크 제공)

---

## ⚙️ 고급 옵션

### 팀 설정 동기화

```
사용자: "팀 구성원과 toolkit 설정 동기화해줘"

Claude:
1. 현재 CLAUDE.md export
2. 설정파일 버전 관리
3. 팀 가이드라인 생성
4. 공유 가능한 설정 패키지 생성
```

### 커스텀 플로우

```
사용자: "내 워크플로우에 맞게 toolkist 커스터마이징해줘"

Claude:
1. 최근 작업 패턴 분석 (Task Observer)
2. 최적 도구 조합 제안
3. 커스텀 훅 생성
4. 자동화 구성
```

---

## 🎓 학습 자료

이 스킬을 통해 배울 수 있는 것:

1. **토큰 효율**: OmniRoute + Headroom으로 토큰 30-40% 절감
2. **메모리 활용**: Claude Mem으로 컨텍스트 윈도우 효율화
3. **자동화**: SessionStart/End 훅으로 완전 자동화
4. **자가개선**: Task Observer로 패턴 인식 및 스킬 생성
5. **효율성**: Ponytail로 최소 필요 코드만 작성

---

## 🔗 관련 스킬 및 도구

- `task-observer` - 패턴 분석 및 개선 제안
- `graphify` - 지식 구조화 및 시각화
- `Claude Mem` - 장기 메모리 관리
- Ponytail mode - 효율 최우선

---

**이 스킬은 Claude와의 상호작용을 근본적으로 변화시킵니다. 한 번 설정 후에는 모든 세션이 자동으로 최적화되고, 점차 개인화됩니다.**
