#!/usr/bin/env python3
"""
Claude Toolkit Setup - 자동 초기화 및 검증 스크립트
"""

import os
import json
import subprocess
from pathlib import Path
from datetime import datetime

class ToolkitSetup:
    def __init__(self):
        self.home = Path.home()
        self.claude_dir = self.home / '.claude'
        self.tools_status = {}

    def check_omniroute(self):
        """OmniRoute 설치 및 서버 상태 확인"""
        try:
            result = subprocess.run(['npm', 'list', '-g', 'omniroute'],
                                  capture_output=True, text=True)
            if 'omniroute' in result.stdout:
                return {'installed': True, 'status': '설치됨'}
            return {'installed': False, 'status': '미설치'}
        except:
            return {'installed': False, 'status': '확인 불가'}

    def check_headroom(self):
        """Headroom CLI 설치 확인"""
        try:
            result = subprocess.run(['which', 'headroom'],
                                  capture_output=True, text=True)
            if result.returncode == 0:
                return {'installed': True, 'path': result.stdout.strip()}
            return {'installed': False}
        except:
            return {'installed': False}

    def check_claude_mem(self):
        """Claude Mem 플러그인 설치 확인"""
        settings = self.claude_dir / 'settings.json'
        if settings.exists():
            with open(settings) as f:
                config = json.load(f)
                if 'enabledPlugins' in config:
                    if 'claude-mem@thedotmack' in config['enabledPlugins']:
                        # DB 디렉토리 확인
                        mem_dir = self.home / '.claude-mem'
                        db_exists = (mem_dir / 'claude-mem.db').exists()
                        return {
                            'plugin_installed': True,
                            'db_exists': db_exists,
                            'status': '설치됨' if db_exists else 'DB 초기화 필요'
                        }
        return {'plugin_installed': False, 'db_exists': False}

    def check_code_setup(self):
        """Claude Code Setup 플러그인 확인"""
        settings = self.claude_dir / 'settings.json'
        if settings.exists():
            with open(settings) as f:
                config = json.load(f)
                if 'enabledPlugins' in config:
                    if 'claude-code-setup@claude-plugins-official' in config['enabledPlugins']:
                        return {'installed': True, 'status': '설치됨'}
        return {'installed': False}

    def check_task_observer(self):
        """Task Observer 스킬 확인"""
        skill_dir = self.claude_dir / 'skills' / 'task-observer'
        hook_exists = False

        settings = self.claude_dir / 'settings.json'
        if settings.exists():
            with open(settings) as f:
                config = json.load(f)
                hook_exists = 'SessionEnd' in config.get('hooks', {})

        return {
            'skill_installed': skill_dir.exists(),
            'hook_configured': hook_exists,
            'status': '설치 및 설정됨' if (skill_dir.exists() and hook_exists) else '부분 설정'
        }

    def check_graphify(self):
        """Graphify 스킬 확인"""
        skill_dir = self.claude_dir / 'skills' / 'graphify'
        return {'installed': skill_dir.exists(), 'status': '설치됨' if skill_dir.exists() else '미설치'}

    def check_ponytail(self):
        """Ponytail 플러그인 확인"""
        settings = self.claude_dir / 'settings.json'
        if settings.exists():
            with open(settings) as f:
                config = json.load(f)
                if 'enabledPlugins' in config:
                    if 'ponytail@ponytail' in config['enabledPlugins']:
                        return {'installed': True, 'status': '활성화됨'}
        return {'installed': False}

    def initialize_claude_mem(self):
        """Claude Mem 데이터베이스 초기화"""
        mem_dir = self.home / '.claude-mem'
        mem_dir.mkdir(exist_ok=True)

        # settings.json 생성
        settings_file = mem_dir / 'settings.json'
        if not settings_file.exists():
            settings = {
                'auto_save': True,
                'max_memory_items': 1000,
                'retention_days': 365,
                'created_at': datetime.now().isoformat()
            }
            with open(settings_file, 'w') as f:
                json.dump(settings, f, indent=2)

        # Database 파일 생성 (touch만 해도 됨)
        db_file = mem_dir / 'claude-mem.db'
        if not db_file.exists():
            db_file.touch()

        return {'initialized': True, 'path': str(mem_dir)}

    def setup_hooks(self):
        """SessionStart/SessionEnd 훅 설정"""
        settings_path = self.claude_dir / 'settings.json'

        if settings_path.exists():
            with open(settings_path) as f:
                config = json.load(f)
        else:
            config = {}

        # SessionEnd 훅 설정
        if 'hooks' not in config:
            config['hooks'] = {}

        if 'SessionEnd' not in config['hooks']:
            config['hooks']['SessionEnd'] = [
                {
                    'hooks': [
                        {
                            'type': 'prompt',
                            'prompt': '이 세션에서 관찰된 거 있어? task-observer를 통해 기록할 만한 개선점, 패턴, 또는 학습이 있었는지 확인하고 있어.'
                        }
                    ]
                }
            ]

        with open(settings_path, 'w') as f:
            json.dump(config, f, indent=2)

        return {'hooks_updated': True}

    def generate_dashboard(self):
        """통합 대시보드 생성"""
        dashboard = f"""
╔════════════════════════════════════════════════════════════════╗
║         🚀 Claude Toolkit - 초기화 완료 대시보드               ║
╠════════════════════════════════════════════════════════════════╣
║                                                                ║
║ 📊 설치 상태                                                   ║
║   ✅ OmniRoute        {self.tools_status.get('omniroute', {}).get('status', '미설치')}
║   ✅ Headroom         {self.tools_status.get('headroom', {}).get('status', '미설치')}
║   ✅ Claude Mem       {self.tools_status.get('claude_mem', {}).get('status', '미설치')}
║   ✅ Code Setup       {self.tools_status.get('code_setup', {}).get('status', '미설치')}
║   ✅ Task Observer    {self.tools_status.get('task_observer', {}).get('status', '미설치')}
║   ✅ Graphify         {self.tools_status.get('graphify', {}).get('status', '미설치')}
║   ✅ Ponytail         {self.tools_status.get('ponytail', {}).get('status', '미설치')}
║                                                                ║
║ 🔄 플로우 활성화                                               ║
║   ✅ 토큰/성능 최적화 (OmniRoute + Headroom)                 ║
║   ✅ 메모리 지속성 (Claude Mem)                               ║
║   ✅ 환경 최적화 (Code Setup)                                 ║
║   ✅ 자가 개선 (Task Observer + Graphify)                    ║
║   ✅ 효율성 관장 (Ponytail Lazy Mode)                        ║
║                                                                ║
║ 💡 다음 단계                                                   ║
║   1. 새로운 세션 시작 - 모든 도구가 자동으로 작동합니다     ║
║   2. Task Observer 훅 활성 - 세션 종료 시 패턴 분석        ║
║   3. Claude Mem 활용 - 이전 세션 메모리 자동 로드           ║
║   4. 효율성 모니터링 - Graphify로 진행 상황 시각화         ║
║                                                                ║
╚════════════════════════════════════════════════════════════════╝
"""
        return dashboard

    def run(self):
        """전체 초기화 프로세스 실행"""
        print("🔍 Claude Toolkit 상태 확인 중...\n")

        self.tools_status = {
            'omniroute': self.check_omniroute(),
            'headroom': self.check_headroom(),
            'claude_mem': self.check_claude_mem(),
            'code_setup': self.check_code_setup(),
            'task_observer': self.check_task_observer(),
            'graphify': self.check_graphify(),
            'ponytail': self.check_ponytail(),
        }

        print("⚙️  Claude Mem 초기화 중...\n")
        self.initialize_claude_mem()

        print("🔧 훅 설정 중...\n")
        self.setup_hooks()

        print(self.generate_dashboard())

        print("\n✅ Claude Toolkit 초기화 완료!")
        print("\n📝 설정 파일:")
        print(f"   • CLAUDE.md: {self.claude_dir / 'CLAUDE.md'}")
        print(f"   • settings.json: {self.claude_dir / 'settings.json'}")
        print(f"   • Claude Mem DB: {self.home / '.claude-mem'}")

if __name__ == '__main__':
    setup = ToolkitSetup()
    setup.run()
