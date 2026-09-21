# Claude Toolkit - 각 도구 상세 가이드

## 1. OmniRoute (한도 늘리기)

### 용도
- 다양한 Claude 모델 간 자동 전환
- 최적 비용-성능 선택
- 모델별 성능 모니터링

### 주요 명령
```bash
omniroute serve              # 서버 시작 (localhost:20128)
omniroute setup-claude       # Claude Code 프로필 생성
omniroute launch             # 대시보드 열기
```

### 사용 패턴
- 복잡한 작업 → claude-opus-5 (성능 최우선)
- 빠른 작업 → claude-haiku (토큰 절감)
- 일반 작업 → claude-sonnet (균형)

---

## 2. Headroom (토큰 절감)

### 용도
- 동일 작업을 더 적은 토큰으로 수행
- 컨텍스트 압축 및 최적화
- 비용 감소 (30-40% 절감 가능)

### 주요 명령
```bash
headroom wrap claude         # Claude 토큰 압축
headroom check <file>       # 파일 토큰 분석
```

### 언제 사용
- 긴 대화 기록 재사용 시
- 반복되는 컨텍스트 있을 때
- 토큰 한도 접근할 때

---

## 3. Claude Mem (메모리 지속성)

### 용도
- 세션 간 장기 메모리 저장
- 자동 메모리 검색 및 적용
- 개인화된 학습 경험

### 데이터베이스 구조
```
~/.claude-mem/
├── claude-mem.db          # SQLite 데이터베이스
└── settings.json          # 설정 파일
```

### 메모리 타입
- **User**: 사용자 정보, 선호도, 스타일
- **Project**: 프로젝트별 컨텍스트, 구조, 결정사항
- **Pattern**: 식별된 사용 패턴, 습관
- **Feedback**: 이전 작업에 대한 피드백

### 자동 로드 시점
- SessionStart: 관련 메모리 자동 로드
- 프로젝트 감지: 프로젝트별 메모리 적용
- 패턴 인식: 유사 작업 시 자동 제안

---

## 4. Claude Code Setup (환경 최적화)

### 용도
- 프로젝트별 최적 설정 추천
- 팀 가이드라인 자동 적용
- 작업 효율성 최대화

### 자동 감지 항목
- 프로젝트 타입 (web, backend, data, etc)
- 사용 기술 (언어, 프레임워크)
- 팀 규모 및 워크플로우
- 기존 설정 파일

### 추천 기능
- 최적 권한 설정
- 권장 도구 조합
- 팀 표준 적용
- 자동화 규칙

---

## 5. Task Observer (패턴 분석)

### 용도
- 사용 패턴 자동 분석
- 개선 기회 식별
- 새로운 스킬 제안

### 세션 분석 항목
- 사용한 도구 및 빈도
- 작업 유형별 소요 시간
- 효율성 메트릭
- 반복되는 작업

### 인사이트 생성
- "매주 월요일 이 작업을 반복하니까 스킬로 만들까?"
- "이 두 도구 조합이 자주 함께 사용돼"
- "최근 정확도 90% 이상, 신뢰도 높음"

---

## 6. Graphify (지식 구조화)

### 용도
- 학습 내용을 그래프로 시각화
- 개념 간 연결 자동 생성
- 지식 구조 개선

### 그래프 노드 타입
- **개념**: 핵심 개념, 아이디어
- **연결**: 개념 간 관계
- **사례**: 구체적 사용 예
- **참고**: 외부 자료 링크

### 사용 시나리오
- 학습 경로 시각화
- 복잡한 개념 분해
- 프로젝트 구조 설계
- 아이디어 브레인스토밍

---

## 7. Ponytail (Lazy Mode)

### 용도
- 효율성 최우선 (최소 필요 코드)
- YAGNI 원칙 강제 (불필요한 것 제거)
- 기술 부채 최소화

### 주요 원칙
- "이것이 정말 필요한가?" → 아니면 건너뛰기
- "이미 있는가?" → 재사용하기
- "한 줄로 충분한가?" → 한 줄로
- "표준 라이브러리가 있는가?" → 그것 사용

### Lazy Mode 강화 방법
- 불필요한 추상화 제거
- 과도한 주석 제거
- 단순한 로직 우선
- 필요할 때만 최적화

---

## 통합 워크플로우

### 일반적인 작업 흐름

```
1. SessionStart (자동)
   ├─ OmniRoute: 최적 모델 결정
   ├─ Claude Mem: 관련 메모리 로드
   └─ Code Setup: 프로젝트 설정 제안

2. 작업 수행
   ├─ Headroom: 토큰 효율화 (필요시)
   ├─ Ponytail: Lazy Mode 유지
   └─ 실시간 패턴 수집

3. SessionEnd (자동)
   ├─ Task Observer: 패턴 분석
   ├─ Graphify: 지식 구조화
   ├─ Claude Mem: 세션 요약 저장
   └─ 다음 세션 추천 구성
```

### 효율성 최적화 예시

**상황**: "같은 종류의 데이터 분석을 매주 한다"

**Toolkit 반응**:
1. **Task Observer** → "반복 패턴 감지"
2. **Graphify** → "데이터 분석 프로세스 그래프화"
3. **Claude Mem** → "주간 분석 템플릿 저장"
4. **OmniRoute** → "이 작업에 최적 모델 제안 (claude-sonnet)"
5. **Headroom** → "이전 분석 컨텍스트 재사용으로 토큰 30% 절감"
6. **Ponytail** → "필수 스크립트만 유지, 보일러플레이트 제거"

결과: 같은 작업을 매주 50% 더 빨리, 비용은 30% 적게 수행

---

## 문제 해결

### OmniRoute 서버가 안 열릴 때
```bash
# 수동으로 시작
omniroute serve

# 포트 확인
lsof -i :20128

# 로그 확인
omniroute serve --verbose
```

### Headroom 명령이 없을 때
```bash
# 재설치
pip install headroom-ai[all]

# PATH 확인
echo $PATH
which headroom
```

### Claude Mem 메모리가 로드 안 될 때
```bash
# 디렉토리 권한 확인
ls -la ~/.claude-mem/

# 권한 설정
chmod 755 ~/.claude-mem/
chmod 644 ~/.claude-mem/claude-mem.db
```

---

## 성능 측정

### 효율성 지표
- **토큰 효율**: 작업당 토큰 사용량 (낮을수록 좋음)
- **시간 효율**: 작업 완료 시간 (짧을수록 좋음)
- **비용 효율**: 작업당 비용 (낮을수록 좋음)
- **정확도**: 작업 완료율 (높을수록 좋음)

### 모니터링
- Task Observer로 주간 리포트 생성
- Graphify로 진행 상황 시각화
- Claude Mem에 메트릭 저장
- 트렌드 분석 및 개선 제안

---

## 팁 & 트릭

1. **복합 작업에는 OmniRoute + Headroom 조합 사용**
2. **반복 작업은 Claude Mem에 템플릿으로 저장**
3. **주간 분석 후 Graphify로 시각화**
4. **Ponytail Mode에서 불필요한 것부터 제거**
5. **Task Observer 인사이트를 스킬로 변환**
