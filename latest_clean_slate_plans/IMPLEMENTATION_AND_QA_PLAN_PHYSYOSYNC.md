# IMPLEMENTATION, QA & DATA PRESERVATION MASTER PLAN
# PhysioSync AI: Multi-Specialist Triage Engine & Anti-Anchoring Architecture
**Document Version:** 1.0.0  
**Target System:** PhysioSync AI Biomechanical Workout Matrix & Engine  
**Date:** October 3, 2026  
**Status:** Ready for Execution  

---

## 1. Plan Overview & Objectives

This plan operationalizes the requirements defined in **[PRD_PHYSYOSYNC_AI_BIOMECHANICAL_ENGINE.md](file:///Users/nipunmehra/Desktop/ai-exercise-blueprint/PRD_PHYSYOSYNC_AI_BIOMECHANICAL_ENGINE.md)**. 

### Core Deliverables:
1. **AI Governance Layer (`AGENTS.md`):** Codify mandatory isolated specialist checks and the stateless fresh-session anti-anchoring protocol.
2. **Interactive UI Triage Engine (`interactive_muscle_feedback.html`, `index.html`, and desktop copy):**
   - Real-time pain/failure detection hook.
   - Interactive **Multi-Specialist Clinical Triage Modal** with 4 dedicated persona views + 1 Arbiter synthesis view.
   - On-demand `[ 🩺 Multi-Specialist Triage Check ]` trigger button on every active exercise card.
3. **Structured Telemetry Clipboard Export:** Enhance `copySessionLogForChat()` to auto-generate the complete stateless hydration payload for seamless AI chat diagnosis.
4. **Data Loss Prevention & Storage Safety:** Zero-loss versioned `localStorage` migration with backward compatibility across all legacy keys.
5. **Automated QA & Visual Verification:** End-to-end headless browser test suite verifying modal triggers, persona tab switching, persistence, and visual rendering.

---

## 2. Phase-by-Phase Execution Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ PHASE 1: DATA PRESERVATION & SAFETY BACKUP                                                      │
│ • Snapshot all existing active workout files, journals, and local storage seed data.            │
│ • Verify baseline checksums across all 3 HTML file mirrors.                                     │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 2: SYSTEM PROTOCOL UPDATE (AGENTS.md)                                                     │
│ • Implement Section 5: Mandatory Multi-Specialist Clinical Council Protocol.                    │
│ • Implement Section 6: Stateless Fresh-Session Telemetry Hydration & Anti-Anchoring Contract.   │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 3: FRONTEND UI & SPECIALIST KNOWLEDGE BASE IMPLEMENTATION                                │
│ • Build `SPECIALIST_KNOWLEDGE_BASE` covering all 24 exercises across Days 1–7.                  │
│ • Implement `triggerMultiSpecialistTriage()` and responsive CSS modal component.                │
│ • Add manual `[ 🩺 Multi-Specialist Triage Check ]` button next to exercise metadata.           │
│ • Upgrade `copySessionLogForChat()` with structured Anti-Anchoring Telemetry Injection.         │
│ • Synchronize all 3 HTML files byte-for-byte.                                                   │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 4: AUTOMATED QA SUITE & HEADLESS BROWSER VERIFICATION                                     │
│ • Execute automated Playwright script testing clean logging, pain trigger, and modal rendering. │
│ • Capture and audit screenshots of all 4 persona tabs + Arbiter synthesis in the UI.            │
│ • Validate clipboard payload structure and JSON export integrity.                               │
├─────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PHASE 5: USER ACCEPTANCE & DOCUMENTATION FREEZE                                                 │
│ • Present verified screenshots and test results to user.                                        │
│ • Update master tech fixes ledger and journal.                                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Detailed Component Specifications

### 3.1 Phase 1: Data Preservation & Zero-Loss Guardrails
* **Pre-Execution Snapshot:** Create timestamped backups of `interactive_muscle_feedback.html`, `index.html`, and `AGENTS.md` before applying any code edits.
* **Storage Key Integrity:**
  * Active key remains: `"physiosync_vault_v6_forearms_decoupled_20261001"`.
  * Ensure `LEGACY_STORAGE_KEYS` array retains all historical keys so no user data from prior sessions is orphaned.
  * Verified golden records in `SEED_WORKOUT_HISTORY` (Day 1 & Day 2) remain fully intact.

### 3.2 Phase 2: AI Governance Updates in `AGENTS.md`
* **Section 5 (Clinical Council):** Formally define the 4 mandatory persona audit blocks:
  1. `@persona:foot_posture_pt` (Ground-up chain, tripod, talus block, calcaneal eversion).
  2. `@persona:functional_patterns` (AOS, POS, transverse rotational shear, axial decompression).
  3. `@persona:tendon_specialist` (Keith Baar isometrics, depth clamping, 24-hr latency).
  4. `@persona:hypertrophy_specialist` (Mechanical tension preservation, RIR, loaded deficit alternatives).
* **Section 6 (Stateless Anti-Anchoring Engine):** Enforce that when subsequent feedback or symptoms are submitted, the AI must evaluate the appended telemetry as a fresh, unanchored session—preventing false confirmation of initial hypotheses.

### 3.3 Phase 3: Web Tracker UI Enhancements
* **Specialist Knowledge Engine (`SPECIALIST_KNOWLEDGE_BASE`):**
  A modular JavaScript dictionary mapping each exercise ID to pre-calibrated domain checks for each of the 4 personas. Examples:
  * `goblet_squat`: Foot PT audits tripod/toe flare; FP audits pelvic shift/corkscrew; Tendon audits VMO/patellar shear; Arbiter recommends 15°–20° heel wedge.
  * `deficit_press`: Foot/Postural PT audits scapular plane; FP audits ribcage elevation; Tendon audits 45° arrowhead tuck; Arbiter calibrates 16–18 kg baseline.
  * `overhead_press`: Foot PT audits standing tripod; FP audits serratus engagement; Tendon audits ear-level depth clamp to eliminate elbow click; Arbiter enforces 3–4s eccentric.
  * `broad_jump_stick`: Foot PT bans flat-foot landing; FP enforces hip-pocket deceleration; Tendon enforces 2s freeze; Arbiter substitutes PRI 90/90 if back pain $\ge 2/10$.
  * `b_stance_hip_thrust`: Foot PT audits heel drive; FP enforces contralateral glute drive; Tendon audits zero lumbar hyperextension; Arbiter enforces Rule of Weaker Side First.
* **UI Modal (`#specialist-triage-modal`):**
  * Modern dark-mode glassmorphic modal with glowing cyan/amber accents.
  * Tabbed navigation: `[ 🦶 Foot PT ]`, `[ 🧬 Functional Patterns ]`, `[ 🛡️ Tendon & Joint ]`, `[ 🏋️ Hypertrophy ]`, `[ ⚖️ Arbiter Directive ]`.
  * Renders automatically when `status === 'pain'` or `severity >= 2`, or on-demand via the new header button.
* **Structured Clipboard Payload (`copySessionLogForChat`):**
  * Automatically appends the complete Context Hydration Schema + Appended Telemetry block so pasting into chat instantly triggers the stateless fresh-session clinical panel.

### 3.4 Phase 4: Automated QA & Testing Suite
We will write and execute a dedicated automated Playwright test script (`qa_test_triage_engine.py`):
1. **Test 1: App Boot & Zero Data Loss:** Verify that opening the app loads all existing Day 1 & Day 2 golden records and week selections.
2. **Test 2: On-Demand Triage Button:** Click `[ 🩺 Multi-Specialist Triage Check ]` on Day 1 Goblet Squats and verify the modal opens with all 4 specialist tabs populated.
3. **Test 3: Interactive Pain Trigger:** Select Day 6 Broad Jump, enter Set 1 as `Pain 3/5 in Right Lower Back`, save set, and verify that the Multi-Specialist Triage Modal automatically pops up with specific flat-foot/pogo clinical warnings.
4. **Test 4: Tab Switching Verification:** Test clicking each specialist tab in the modal and confirm correct content visibility.
5. **Test 5: Clipboard Payload Formatting:** Run `copySessionLogForChat()` via browser evaluation and assert that the output contains the `[STATELESS CLINICAL TRIAGE DIRECTIVE]` token and all required hydration metadata.
6. **Test 6: Synchronization Check:** Run `diff` across all 3 HTML files to verify 100% byte-for-byte parity.

---

## 4. Rollback & Safety Strategy

If any step fails during testing:
1. Automated rollback restores the pre-execution backup files within <5 seconds.
2. `localStorage` data remains untouched because all operations are strictly additive.
3. User is provided with detailed error logs and diff output before any further action.

---

## 5. Next Step
Upon your confirmation, I will execute this plan sequentially starting with the pre-execution backup and Phase 2/3 implementation.
