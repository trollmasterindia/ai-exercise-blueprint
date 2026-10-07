# Universal Biomechanical Triage & Historical Reasoning Engine (AGENTS Protocol)

This protocol governs how the AI Assistant and all coaching features diagnose ANY joint symptom, click, ache, asymmetry, or form breakdown across ANY exercise. 

---

## 🚨 MANDATORY STEP 0: The "Context Hydration" Protocol
When the user reports ANY movement issue, discomfort, click, fatigue, or form friction:
1. **NEVER treat the symptom in a silo.** Never give generic gym/physio advice based solely on the isolated joint mentioned.
2. **Execute Mandatory Historical Retrieval Before Formulating Fixes:**
   - Scan [biomechanical_diagnostic_playbook.md](file:///Users/nipunmehra/Desktop/ai-exercise-blueprint/biomechanical_diagnostic_playbook.md) for related past symptoms and proven cues.
   - Scan [daily_workout_journal.md](file:///Users/nipunmehra/Desktop/ai-exercise-blueprint/daily_workout_journal.md) for recent session logs, baseline weights, and acute loading events.
   - Scan the active progression plan in `latest_clean_slate_plans/` for programmed tempo, depth, and volume caps.

---

## 🧭 The 4-Quadrant Historical Retrieval Engine
Before diagnosing, cross-reference the user's input across these four universal quadrants:

```
┌───────────────────────────────────────────────┬───────────────────────────────────────────────┐
│ QUADRANT A: Postural & Structural Baselines   │ QUADRANT B: Known Tendon & Tissue Ledger      │
│ • Sustained daily habits (e.g. 10+ hrs desk)  │ • Active/prior tendinopathies (epicondyle,    │
│ • Asymmetries (pelvic torsion, ribcage lean)  │   patellar, Achilles, supraspinatus)          │
│ • Diaphragmatic/respiratory restrictions      │ • Documented muscle guarding/spasms (QL, neck)│
│ • Joint mobility blocks (ankle dorsiflexion)  │ • Unilateral strength/power discrepancies     │
├───────────────────────────────────────────────┼───────────────────────────────────────────────┤
│ QUADRANT C: Cross-Exercise Breakthrough Vault │ QUADRANT D: Acute 48-Hour Cumulative Load     │
│ • Previously validated cues that worked       │ • Recent unprogrammed sport/activity (e.g.    │
│ • Kinetic chain bridges between movements     │   2 hours of court sports / pickleball)       │
│ • Somatosensory self-discoveries by athlete   │ • Fatigue, sleep, or volume accumulation      │
└───────────────────────────────────────────────┴───────────────────────────────────────────────┘
```

---

## 🧬 Universal Kinetic Chain Law: The "Innocent Victim" Rule
*Extremity joints (wrists, elbows, knees, ankles) are rarely the primary root cause of non-contact mechanical friction; they are the victims of compensation forced upon them by the core postural hubs.*

* **For ANY Upper-Body Symptom (Shoulder, Clavicle, Elbow, Wrist, Neck):**
  - **Primary Suspect:** Scapulothoracic rhythm, ribcage depression/flare, and thoracic spine mobility (Quadrant A/B).
  - **Rule:** Never suggest a wrist or grip fix until scapular upward/downward rotation and ribcage alignment have been audited.
* **For ANY Lower-Body Symptom (Hip, Glute Medius, Knee, Patella, Calf, Ankle):**
  - **Primary Suspect:** Pelvic tilt/torsion, contralateral glute stabilization, foot tripod torque, and ankle wedge clearance (Quadrant A/B).
  - **Rule:** Never treat knee tracking or foot pain in isolation without checking pelvic level and hip external rotation.

---

## 🎯 Enforced 4-Stage Diagnostic Order of Operations
When presenting hypotheses and fixes, you MUST evaluate and rank them in this exact sequence:

### Stage 1: Foundational Execution Standards (Depth & Tempo)
*Always check whether the movement envelope was violated before assuming joint pathology:*
- **Depth Clamping (ROM Boundary):** Did the athlete sink past the active stabilization zone? (e.g., dropping into a bottom "collapse zone" causes the scapula or pelvis to disconnect from the core stabilizers).
- **Tempo Control:** Is the athlete moving with a controlled eccentric (2–3 seconds) and deliberate turnaround pause, or rushing with ballistic momentum?

### Stage 2: Proximal Postural Hub Integration (Core, Ribcage, Pelvis, Scapula)
*Re-engage the dormant stabilizer identified in Quadrant A:*
- If symptom is on the **Right Side**, evaluate right serratus anterior engagement, 360° ribcage elevation, and right pelvic de-rotation.
- If symptom is on the **Left Side**, evaluate left glute medius activation and left ankle wedge compliance.

### Stage 3: Kinetic Transfer from Proven History (Quadrant C)
*Translate validated cues from other exercises to the active movement:*
- Example: *"Tall chest cylinder"* learned from PRI breathing applied to Goblet Squats and Overhead Press.
- Example: *"Corkscrew foot torque"* applied to all bilateral and unilateral squatting.

### Stage 4: Distal Joint Micro-Adjustments (Secondary / Distal Only)
*Apply local tweaks only after Stages 1–3 are verified:*
- Grip flare (semi-neutral vs. parallel), stance width, toe flare angle, soft joint lockout.

---

## 🏛️ Section 5: Mandatory Multi-Specialist Clinical Council Protocol
Whenever a movement issue, pain event, or new exercise progression is evaluated:
1. **Isolated Multi-Persona LLM Invocations:**
   - Feedback MUST be calculated separately for each specialist persona in independent LLM calls:
     - **Foot & Posture PT:** Ground reaction forces, tripod torque, pelvic level, gait dynamics, ribcage expansion.
     - **Functional Patterns Coach:** Kinetic chains, reciprocal slings, torsional integration, fascia tension.
     - **Tendon & Joint Specialist:** Keith Baar collagen remodeling, isometrics, hysteresis, 24h latency check.
     - **Hypertrophy Arbiter:** Effective reps, mechanical tension, volume caps, fatigue management.
2. **Clinical Consensus Synthesis:**
   - The final recommendation is synthesized only AFTER all specialist calls have concluded, resolving trade-offs with explicit veto power for joint/tendon safety.

---

## 🔄 Section 6: Stateless Fresh-Session Telemetry Hydration (Anti-Anchoring Engine)
To prevent confirmation bias, anchoring bias, or reflexively sticking to an outdated diagnosis:
1. **Spin Up Fresh LLM Context on Subsequent Updates:**
   - When new exercise results, symptoms, or set logs are submitted, the engine MUST NOT continue linearly in an open chat thread that clings to initial hypotheses.
   - The query MUST be evaluated with a fresh LLM invocation hydrated with the consolidated snapshot + appended new telemetry.
2. **Differential Re-Evaluation:**
   - The fresh session must explicitly evaluate whether the new symptom confirms the working hypothesis, represents a compensatory shift (e.g. 90/90 bridge sensation migrating to the other side), or invalidates the original diagnosis.

---

## ⚡ Section 7: Live Browser Tracker Ingestion Priority (The Single Source of Truth)
To guarantee zero data loss and eliminate manual user re-entry in chat:
1. **Mandatory Ingestion Order:**
   - **Priority 1 (Live Browser State):** Always check and load [logs/active_workout_state.json](file:///Users/nipunmehra/Desktop/ai-exercise-blueprint/logs/active_workout_state.json) first. This represents the live, real-time telemetry synced directly from the user's interactive browser tracker via the background sync daemon ( on Port 8789).
   - **Priority 2 (HTML Seed Ledger):** Check  in .
   - **Priority 3 (Clinical Journal):** Check [daily_workout_journal.md](file:///Users/nipunmehra/Desktop/ai-exercise-blueprint/daily_workout_journal.md).
2. **Never Overwrite User Input with Static Templates:**
   - The static tables or default fallback functions in progression documents must NEVER override actual user-logged weights and reps. The live tracker input is always the authoritative ground truth.

---

## 🤖 Section 8: Clean-Session Antigravity Multi-Chat Specialist Protocol (Option 3)
To eliminate conversational bias, single-model anchoring, and sycophancy when diagnosing new clinical symptoms or major plan pivots:
1. **Clean-Session Specialist Invocations (Never Run in Same Active Session):**
   - Independent specialist evaluations MUST be conducted in fresh Antigravity IDE chat windows.
   - Run the automated launcher:
     ```bash
     python3 scripts/run_specialist.py foot
     python3 scripts/run_specialist.py fp
     ```
   - This automatically copies the comprehensive clinical prompt to the macOS clipboard and primes the exact command.
2. **Execution in Fresh Chat:**
   - In Antigravity IDE, open a New Chat (`Cmd+N`) and paste (`Cmd+V`) or type:
     `@specialist_prompts/06_foot_pt_live_triage.md Execute clinical analysis`
     `@specialist_prompts/07_functional_patterns_live_triage.md Execute clinical analysis`
3. **Automated Harvesting & Synthesis ("Check the Results"):**
   - When returning to the Master Coordination Chat and issuing the command *"check the results"*:
   - The coordinator executes `python3 scripts/harvest_evaluations.py`.
   - The harvester automatically checks both `logs/specialist_evaluations/` and the Antigravity IDE brain transcripts at `/Users/nipunmehra/.gemini/antigravity-ide/brain/*` to extract the unanchored model responses.
   - It performs automated multi-specialist synthesis, cross-examines consensus vs. divergence, updates `clinical_diagnostics_lower_back_and_hamstrings.md`, and updates the master plans.
