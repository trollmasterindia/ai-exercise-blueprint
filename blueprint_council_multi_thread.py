"""
AI Exercise Blueprint: Stage 1 Strategic Blueprint Council (Multi-Thread)
Task: Generate the Strategic 6-Month Exercise Blueprint (Subsystem Weightages,
Boundary Guardrails, Progression Rules, and Deep Domain Diagnostic Questions).
NOTE: Focus is on master architectural rules, NOT daily workout spreadsheets.
"""

import json
from concurrent.futures import ThreadPoolExecutor

USER_PROFILE = {
    "athlete": "Nipun",
    "equipment": ["5-40kg Adjustable Dumbbells", "Pull-Up Bar", "Bed/Floor", "Resistance Bands (Zero Gym Bench)"],
    "baselines": {
        "floor_press": "28-29 kg DBs x 8-10 reps",
        "row": "32 kg DB x 8-10 reps",
        "pull_up": "Bodyweight x 10 easy; +15kg caused forearm/inner elbow discomfort",
        "overhead_triceps": "15 kg DB x 10-12 reps",
        "plyo_bed_jump": "4 feet away onto 3-foot bed",
        "broad_jump": "170 cm"
    },
    "pathologies": {
        "desk_sitting": "10+ hours/day, rightward postural lean",
        "infant_history": "Inward feet / pronation history",
        "knee": "Mild left knee strain",
        "calf_achilles": "Past jump landing strain in lower calf/Achilles"
    }
}

# -------------------------------------------------------------------------
# THREAD 1: Hypertrophy Specialist (Strategic Blueprint RFP)
# -------------------------------------------------------------------------
def run_hypertrophy_blueprint(profile: dict) -> dict:
    return {
        "specialist": "Hypertrophy & Regional Muscle Architecture",
        "proposed_subsystem_weightage": {
            "Hypertrophy (V-Taper Lats, Delts, Arms, Quads, Neck)": 60,
            "Tendon Preservation & Pre-hab": 15,
            "Ankle/Foot Motor Control": 10,
            "Athletic Elasticity & Rotary": 15
        },
        "blueprint_mandates": [
            "Weekly volume must deliver 10-16 direct working sets per target muscle group (Lats, Delts, Chest, Triceps, Quads).",
            "Proximity to failure rule: Every main lift must operate within 0-2 RIR.",
            "Regional selection rule: Floor press targets sternal pecs; bed-deficit pushups target clavicular head; overhead triceps targets long head."
        ],
        "non_negotiable_boundary_rules": [
            "Never allow mobility/primer work to exceed 20% of session time (must not blunt glycogen or neural drive for mechanical tension)."
        ],
        "deep_diagnostic_questions": [
            "1. When doing 28-29kg floor press, is muscular failure reached in the chest or do triceps burn out first? (Determines chest vs triceps stimulus ratio).",
            "2. For direct neck training, is cervical flexion (chin to chest) or cervical extension (rear neck) the aesthetic/functional priority?",
            "3. What is your historical muscle-building response to high-frequency (2x/week) vs moderate frequency (1x/week) for back/lats?"
        ]
    }

# -------------------------------------------------------------------------
# THREAD 2: Tendon & Connective Tissue Specialist (Strategic Blueprint RFP)
# -------------------------------------------------------------------------
def run_tendon_blueprint(profile: dict) -> dict:
    return {
        "specialist": "Tendon, Joint & Connective Tissue Architecture",
        "proposed_subsystem_weightage": {
            "Hypertrophy": 40,
            "Tendon Remodeling & Collagen Synthesis": 35,
            "Ankle/Foot Motor Control": 15,
            "Athletic Elasticity": 10
        },
        "blueprint_mandates": [
            "Tendon Lag Principle: Muscle strength (actin-myosin cross-bridges) adapts in 2-4 weeks; tendon collagen turnover takes 8-12 weeks. Heavy pull-ups must be constrained until structural tendon remodeling catches up.",
            "Rate-of-Force (RFD) Deload: Limit fast eccentric turnaround on pulls and floor presses. Mandatory 2-3s controlled eccentric lowering.",
            "Joint Centration Pre-Flight: Elbow synovial flush & patellar isometric hold are mandatory gates before any load touches the joint."
        ],
        "non_negotiable_boundary_rules": [
            "BANNED: Any explosive stretch-shortening vertical pull until 6 weeks of pain-free isometric/eccentric loading are logged.",
            "BANNED: High-frequency plyometric impacts on unforgiving surfaces (concrete/tile)."
        ],
        "deep_diagnostic_questions": [
            "1. Forearm Discomfort Location: Is the ache strictly on the inner elbow bone (medial epicondyle / golfer's elbow) or on the top/outer forearm muscle belly (brachioradialis)?",
            "2. Pain Timing: Did the discomfort occur during the 8th rep of the set, or did it throb 20-30 minutes after letting go of the bar? (Distinguishes acute tendon shear from vascular inflammatory tendinopathy).",
            "3. Knee Symptoms: Does the mild left knee strain flare going downstairs, in deep squat flexion, or after sitting for prolonged desk hours (moviegoer's knee / patellofemoral tracking)?"
        ]
    }

# -------------------------------------------------------------------------
# THREAD 3: Foot, Ankle & Motor Control Specialist (Strategic Blueprint RFP)
# -------------------------------------------------------------------------
def run_foot_blueprint(profile: dict) -> dict:
    return {
        "specialist": "Foot, Ankle & Motor Control Architecture",
        "proposed_subsystem_weightage": {
            "Hypertrophy": 35,
            "Ankle/Foot Motor Control & Joint Centration": 35,
            "Tendon Preservation": 20,
            "Athletic Elasticity": 10
        },
        "blueprint_mandates": [
            "The Upstream Domino Rule: A desk worker with infant inward foot history will leak torque through the kinetic chain. Left knee strain is almost certainly secondary to a lack of posterior talus glide during ankle dorsiflexion.",
            "Foot Tripod Pre-requisite: No bilateral heavy loaded squats without prior foot tripod calibration (1st MTP, 5th MTP, Calcaneus).",
            "Heel Elevation Mandate: Artificial heel wedge must be utilized to artificially bypass dorsiflexion restrictions until talocrural mobility reaches 12cm on knee-to-wall test."
        ],
        "non_negotiable_boundary_rules": [
            "BANNED: Bilateral flat-ground barbell/dumbbell squats with knees driven forward without heel wedge.",
            "MANDATORY: Single-leg balance and sensory drills must be performed 100% barefoot."
        ],
        "deep_diagnostic_questions": [
            "1. Knee-to-Wall Ankle Test: When lunging barefoot toward a wall with your big toe 4 inches away, does your left knee touch the wall with the heel staying glued to the floor, or does the heel lift / arch collapse inward?",
            "2. Weight Distribution: In a natural standing desk posture, do your shoes wear down more on the inside edge (pronation) or outside edge (supination)?",
            "3. Desk Ergonomics: During your 10+ hours of sitting, do you cross your legs or sit on one foot, reinforcing pelvic torsion?"
        ]
    }

# -------------------------------------------------------------------------
# THREAD 4: Athletic Elasticity & Rotary Power Specialist (Strategic Blueprint RFP)
# -------------------------------------------------------------------------
def run_athletic_blueprint(profile: dict) -> dict:
    return {
        "specialist": "Athletic Elasticity & Rotary Power Architecture",
        "proposed_subsystem_weightage": {
            "Hypertrophy": 45,
            "Athletic Elasticity & Vertical Power": 30,
            "Tendon Preservation": 15,
            "Ankle/Foot Motor Control": 10
        },
        "blueprint_mandates": [
            "Concentric-Dominant Power Strategy: Leverage the athlete's 4-foot to 3-foot bed jump capacity by prioritizing high-box concentric takeoffs where landing impact force is zero.",
            "Braking Power Before Speed: The 170cm broad jump must be paired with eccentric deceleration training (2s isometric stick) before multi-hop reactive bounding.",
            "Transverse Rotary Sling: Core work must emphasize contralateral diagonal power (high-to-low chops) to translate dumbbell strength into court sport agility."
        ],
        "non_negotiable_boundary_rules": [
            "BANNED: Depth drops from heights >18 inches onto hard ground (preserves Achilles).",
            "MANDATORY: Minimum 48 hours recovery between high-rate plyometric sessions and heavy quad sessions."
        ],
        "deep_diagnostic_questions": [
            "1. Jump Takeoff Profile: Do you feel more explosive taking off off one foot on the run (speed-dominant) or off two feet with a deep knee plant (power-dominant)?",
            "2. Broad Jump Landing: When landing your 170cm broad jump, do your knees track straight over your toes, or do they collapse inward towards each other?",
            "3. Achilles Sensation: Has the past Achilles/lower calf discomfort occurred during the explosive push-off phase or upon ground collision?"
        ]
    }

# -------------------------------------------------------------------------
# HEAD COACH ARBITER: STRATEGIC BLUEPRINT SYNTHESIS & TENSION MATRIX
# -------------------------------------------------------------------------
def run_head_coach_blueprint_synthesis(proposals: dict) -> dict:
    # 1. Reconcile Subsystem Weightage (Must sum exactly to 100%)
    # Hypertrophy wanted 60%, Tendon wanted 40%, Foot wanted 35%, Athletic wanted 45%
    reconciled_weightage = {
        "Hypertrophy (Aesthetic V-Taper, Upper Body, Quads, Neck)": 45,
        "Tendon Remodeling & Joint Preservation (Collagen Lag Safety)": 25,
        "Foot & Ankle Motor Control (Talus Glide & Pelvic Decompression)": 15,
        "Athletic Elasticity & Rotary Power (Zero-Impact Bed Jump & Chops)": 15
    }
    
    # Compile Consensus Rules
    consensus_rules = [
        "RULE 1 (The Heel-Wedge Bridge): 1.5-inch heel elevation allows Hypertrophy (45%) to deeply train teardrop VMO quads without violating the Foot Specialist's ankle dorsiflexion lockout.",
        "RULE 2 (The Pulling Bifurcation): Heavy lat overload is shifted to Bed-Braced Rows (32-40kg) where torso support isolates lats with zero grip shear, allowing Pull-Ups to serve Tendon Remodeling (BW, 3s eccentric).",
        "RULE 3 (Concentric-Only High Plyo): Exploit the 3-foot bed jump for maximal vertical power with zero downward landing shock, while strictly enforcing 2s landing sticks on broad jumps.",
        "RULE 4 (Desk Posture Neutralization): Mandatory daily primers (Elbow synovial flush, talus distraction, foot tripod, couch stretch) before touching dumbbells."
    ]

    # Aggregate Deep Diagnostic Questions by Specialist
    all_questions = {}
    for key, p in proposals.items():
        all_questions[p["specialist"]] = p["deep_diagnostic_questions"]

    return {
        "status": "BLUEPRINT_CONSENSUS_REACHED",
        "reconciled_subsystem_weightage": reconciled_weightage,
        "master_architectural_rules": consensus_rules,
        "specialist_diagnostic_inquiries": all_questions
    }

def main():
    print("=================================================================")
    print("🧠 STAGE 1: MULTI-THREAD BLUEPRINT COUNCIL (STRATEGIC RFP)")
    print("=================================================================\n")

    with ThreadPoolExecutor(max_workers=4) as executor:
        f_hyp = executor.submit(run_hypertrophy_blueprint, USER_PROFILE)
        f_ten = executor.submit(run_tendon_blueprint, USER_PROFILE)
        f_foot = executor.submit(run_foot_blueprint, USER_PROFILE)
        f_plyo = executor.submit(run_athletic_blueprint, USER_PROFILE)

        proposals = {
            "hypertrophy": f_hyp.result(),
            "tendon": f_ten.result(),
            "foot": f_foot.result(),
            "plyo": f_plyo.result()
        }

    for key, prop in proposals.items():
        print(f"--- [BLUEPRINT PROPOSAL: {prop['specialist'].upper()}] ---")
        print(json.dumps(prop, indent=2))
        print("\n")

    print("=================================================================")
    print("🏛️ HEAD COACH ARBITER: STRATEGIC BLUEPRINT CONSENSUS")
    print("=================================================================\n")

    blueprint = run_head_coach_blueprint_synthesis(proposals)
    print(json.dumps(blueprint, indent=2))

if __name__ == "__main__":
    main()
