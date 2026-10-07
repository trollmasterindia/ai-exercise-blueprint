#!/usr/bin/env python3
"""
Specialist Runner Automation for New Antigravity Chats
Usage:
    python3 scripts/run_specialist.py foot
    python3 scripts/run_specialist.py fp
    python3 scripts/run_specialist.py
"""

import os
import sys
import subprocess

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_DIR = os.path.join(WORKSPACE_DIR, 'specialist_prompts')

SPECIALISTS = {
    'foot': {
        'name': 'Foot & Posture Physical Therapist (PRI & Kinetic Chain)',
        'file': '06_foot_pt_live_triage.md',
        'eval_out': 'logs/specialist_evaluations/eval_foot_pt.md'
    },
    'fp': {
        'name': 'Functional Patterns Movement Specialist (Myofascial Slings & Gait)',
        'file': '07_functional_patterns_live_triage.md',
        'eval_out': 'logs/specialist_evaluations/eval_fp.md'
    }
}

def copy_to_clipboard(text: str) -> bool:
    try:
        process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
        process.communicate(text.encode('utf-8'))
        return True
    except Exception:
        return False

def main():
    persona = None
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower().strip()
        if arg in ('foot', 'pt', 'pri'):
            persona = 'foot'
        elif arg in ('fp', 'functional_patterns', 'patterns'):
            persona = 'fp'

    if not persona:
        print('=' * 65)
        print('🏃 ANTIGRAVITY SPECIALIST LAUNCHER (CLEAN-SESSION OPTION 3)')
        print('=' * 65)
        print('Choose specialist prompt to load:')
        print('  [1] Foot & Posture Physical Therapist (06_foot_pt_live_triage.md)')
        print('  [2] Functional Patterns Movement Specialist (07_functional_patterns_live_triage.md)')
        choice = input('Select (1 or 2): ').strip()
        if choice == '1':
            persona = 'foot'
        elif choice == '2':
            persona = 'fp'
        else:
            print('❌ Invalid choice. Exiting.')
            sys.exit(1)

    spec = SPECIALISTS[persona]
    prompt_path = os.path.join(PROMPTS_DIR, spec['file'])
    
    if not os.path.exists(prompt_path):
        print(f'❌ Prompt file not found: {prompt_path}')
        sys.exit(1)

    with open(prompt_path, 'r', encoding='utf-8') as f:
        prompt_content = f.read()

    copied = copy_to_clipboard(prompt_content)

    sep = '=' * 65
    print()
    print(sep)
    print(f'🌟 LOADED: {spec["name"]}')
    print(sep)
    if copied:
        print('✅ PROMPT COPIED TO MACOS CLIPBOARD AUTOMATICALLY!')
    else:
        print('⚠️ Could not copy to pbcopy. Please use file tag.')

    print()
    print('📋 NEXT STEPS FOR NEW CHAT:')
    print('  1. In Antigravity IDE, open a New Chat window (Cmd+N or + icon).')
    print('  2. Paste from clipboard (Cmd+V) OR type:')
    print(f'     @specialist_prompts/{spec["file"]} Execute clinical analysis')
    print('  3. Let the specialist finish generating in that fresh session.')
    print('  4. Return to your Master Coordination Chat and say:')
    print('     ➡️  "check the results"')
    print(sep)
    print()

if __name__ == '__main__':
    main()
