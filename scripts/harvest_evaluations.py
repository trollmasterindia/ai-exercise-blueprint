#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Specialist Evaluation Harvester & Synthesizer
Scans Antigravity brain transcripts and logs/specialist_evaluations/ to harvest unanchored specialist evaluations.
"""

import os
import sys
import glob
import json
import time
from datetime import datetime

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EVAL_DIR = os.path.join(WORKSPACE_DIR, 'logs', 'specialist_evaluations')
BRAIN_DIR = '/Users/nipunmehra/.gemini/antigravity-ide/brain'
CURRENT_CONV_ID = '793da3af-ae03-4714-9839-9594ff7fb36d'

os.makedirs(EVAL_DIR, exist_ok=True)

def scan_antigravity_transcripts():
    results = {'foot': None, 'fp': None}
    if not os.path.exists(BRAIN_DIR):
        return results
    conv_dirs = []
    for cid in os.listdir(BRAIN_DIR):
        if cid == CURRENT_CONV_ID or cid == 'tempmediaStorage':
            continue
        cpath = os.path.join(BRAIN_DIR, cid)
        if os.path.isdir(cpath):
            log_file = os.path.join(cpath, '.system_generated', 'logs', 'transcript.jsonl')
            if os.path.exists(log_file):
                mtime = os.path.getmtime(log_file)
                if (time.time() - mtime) < 172800:
                    conv_dirs.append((mtime, cid, log_file))
    conv_dirs.sort(key=lambda x: x[0], reverse=True)
    for mtime, cid, log_path in conv_dirs:
        try:
            user_texts = []
            model_responses = []
            with open(log_path, 'r', encoding='utf-8') as f_log:
                for line in f_log:
                    try:
                        entry = json.loads(line)
                        if entry.get('type') == 'USER_INPUT':
                            user_texts.append(entry.get('content', ''))
                        elif entry.get('type') == 'PLANNER_RESPONSE':
                            content = entry.get('content', '')
                            if content and len(content.strip()) > 100:
                                model_responses.append(content)
                    except Exception:
                        continue
            all_user_str = ' '.join(user_texts).lower()
            last_resp = model_responses[-1] if model_responses else None
            if not last_resp:
                continue
            if not results['foot']:
                if '06_foot_pt' in all_user_str or ('foot' in all_user_str and ('pri' in all_user_str or 'pinching' in all_user_str)):
                    results['foot'] = {'cid': cid, 'mtime': mtime, 'text': last_resp}
                    eval_path = os.path.join(EVAL_DIR, 'eval_foot_pt.md')
                    with open(eval_path, 'w', encoding='utf-8') as ef:
                        ef.write(last_resp)
            if not results['fp']:
                if '07_functional_patterns' in all_user_str or ('functional patterns' in all_user_str and 'pinching' in all_user_str):
                    results['fp'] = {'cid': cid, 'mtime': mtime, 'text': last_resp}
                    eval_path = os.path.join(EVAL_DIR, 'eval_fp.md')
                    with open(eval_path, 'w', encoding='utf-8') as ef:
                        ef.write(last_resp)
        except Exception:
            continue
    return results

def check_disk_evaluations():
    results = {'foot': None, 'fp': None}
    foot_file = os.path.join(EVAL_DIR, 'eval_foot_pt.md')
    if os.path.exists(foot_file):
        with open(foot_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if len(content) > 100:
                results['foot'] = {'source': 'file', 'text': content}
    fp_file = os.path.join(EVAL_DIR, 'eval_fp.md')
    if os.path.exists(fp_file):
        with open(fp_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if len(content) > 100:
                results['fp'] = {'source': 'file', 'text': content}
    return results

def main():
    sep = '=' * 65
    print(sep)
    print('🔍 HARVESTING UNANCHORED SPECIALIST EVALUATIONS...')
    print(sep)
    disk_res = check_disk_evaluations()
    transcript_res = scan_antigravity_transcripts()
    foot_data = disk_res['foot'] or transcript_res['foot']
    fp_data = disk_res['fp'] or transcript_res['fp']

    foot_status = '✅ FOUND' if foot_data else '⏳ PENDING (Run in New Chat)'
    fp_status = '✅ FOUND' if fp_data else '⏳ PENDING (Run in New Chat)'
    print('👟 Foot & Posture PT Evaluation:      ' + foot_status)
    print('🧬 Functional Patterns Evaluation:    ' + fp_status)
    print(sep)

    if not foot_data and not fp_data:
        print('')
        print('⚠️  No fresh evaluations detected yet.')
        print('👉 To run in New Antigravity Chat:')
        print('   1. Run: python3 scripts/run_specialist.py foot')
        print('   2. Open New Chat (Cmd+N) and paste/execute.')
        print('   3. Run: python3 scripts/run_specialist.py fp')
        print('   4. Open New Chat (Cmd+N) and paste/execute.')
        print('   5. Return here and say: "check the results"')
        print(sep)
        print('')
        return

    print('')
    print('📊 HARVESTED EVALUATION SUMMARY:')
    if foot_data:
        print('')
        print('--- 👟 FOOT & POSTURE PT REPORT (PREVIEW) ---')
        preview = foot_data['text'][:400].replace('\n', ' ')
        print(preview + '...')
    if fp_data:
        print('')
        print('--- 🧬 FUNCTIONAL PATTERNS REPORT (PREVIEW) ---')
        preview = fp_data['text'][:400].replace('\n', ' ')
        print(preview + '...')

    if foot_data and fp_data:
        print('')
        print('🎉 BOTH SPECIALIST EVALUATIONS READY FOR FULL SYNTHESIS!')
        synth_file = os.path.join(EVAL_DIR, 'latest_consensus_synthesis.md')
        with open(synth_file, 'w', encoding='utf-8') as f_out:
            f_out.write('# UNANCHORED MULTI-SPECIALIST HARVEST & SYNTHESIS\n\n')
            f_out.write('Generated: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n\n')
            f_out.write('## 👟 Foot & Posture Physical Therapist Verdict\n\n')
            f_out.write(foot_data['text'] + '\n\n---\n\n')
            f_out.write('## 🧬 Functional Patterns Movement Specialist Verdict\n\n')
            f_out.write(fp_data['text'] + '\n')
        print('💾 Saved combined synthesis to: ' + synth_file)

    print(sep)
    print('')

if __name__ == '__main__':
    main()
