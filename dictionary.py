# Race distance dictionary
race_distances = {
    "5K": 3.1,
    "10K": 6.2,
    "Half Marathon": 13.1,
    "Marathon": 26.2
}

workout_variants = {
  "Easy Run Variants": [
    "Easy run",
    "Hill run",
    "Steady state run",
    "Recovery jog",
    "Long run",
    "Trail run",
    "Base-building run"
  ],
  "Speedwork Variants": [
    "Intervals (e.g., 400m x 8, 800m x 6, 1 mile x 4)",
    "Tempo run (continuous or intervals)",
    "Fartlek (structured or unstructured)",
    "Hill repeats (short, long, sprint-back, alternating effort)",
    "Pyramid intervals",
    "Ladder intervals",
    "Progression run",
    "Negative split run",
    "Strides (100m accelerations with full recovery)"
  ],
  "Cross-Training Variants": [
    "Cross-training (cycling)",
    "Cross-training (climbing)",
    "Cross-training (swimming)",
    "Strength training (upper body, lower body, full body)",
    "Core workout (planks, crunches, leg raises)",
    "Yoga or flexibility training",
    "Rowing",
    "Elliptical",
    "Pilates"
  ]
}

easy_run_variants = {
        "Easy Run": {
            "Description": "A run at a comfortable pace, where you can easily hold a conversation without feeling out of breath. It’s meant to build aerobic endurance without placing too much stress on the body.",
            "Purpose": [
                "Builds aerobic base",
                "Aids recovery between harder workouts",
                "Low risk of injury due to the manageable pace"
            ],
            "Pace": "60-70% of your maximum effort or heart rate."
        },
        "Hill Run": {
            "Description": "An easy or moderate-paced run that includes running on hills. The focus is on maintaining a steady effort uphill, not sprinting.",
            "Purpose": [
                "Builds strength and power in the legs",
                "Improves running economy and hill-running technique",
                "Adds variety to training"
            ],
            "Pace": "Keep the effort consistent, even if pace slows down on uphill sections."
        },
        "Steady State Run": {
            "Description": "A continuous run at a pace slightly faster than an easy run but slower than tempo pace.",
            "Purpose": [
                "Improves aerobic endurance and stamina",
                "Prepares you for race pace over longer distances",
                "Serves as a bridge between easy runs and tempo runs"
            ],
            "Pace": "About 75-85% of your maximum effort or heart rate."
        },
        "Recovery Jog": {
            "Description": "A very slow, short run designed to aid in active recovery after a hard workout.",
            "Purpose": [
                "Enhances recovery by improving circulation",
                "Flushes out metabolic waste after intense runs",
                "Helps maintain consistency in training without overtraining"
            ],
            "Pace": "Extremely relaxed pace, well below normal easy run pace."
        },
        "Long Run": {
            "Description": "The longest run of the week, typically done at an easy or moderate pace.",
            "Purpose": [
                "Builds endurance and aerobic capacity",
                "Trains the body to utilize fat as a fuel source",
                "Helps mental preparation for long races"
            ],
            "Pace": "Easy or steady state pace, depending on the goal of the long run."
        },
        "Trail Run": {
            "Description": "An easy to moderate run done on trails, often involving varied terrain.",
            "Purpose": [
                "Strengthens stabilizing muscles due to uneven terrain",
                "Provides a mental break and more scenic environment",
                "Reduces impact on joints compared to road running"
            ],
            "Pace": "Focus on effort rather than pace, as the terrain will naturally slow you down."
        },
        "Base-Building Run": {
            "Description": "Easy-to-moderate runs done during the early stages of a training cycle to build a solid aerobic base.",
            "Purpose": [
                "Increases aerobic fitness and mileage safely",
                "Prepares the body for more intense training later in the cycle",
                "Reduces injury risk by gradually adapting the body to higher volume"
            ],
            "Pace": "Easy to steady state pace, depending on the stage of base building."
        }
    }

speedwork_variants = {
    "Intervals": {
        "Description": "Short bursts of intense running followed by periods of recovery. These are typically done on a track or flat surface.",
        "Purpose": [
            "Improves anaerobic capacity and running economy",
            "Increases top-end speed and strength",
            "Helps the body adapt to high-intensity efforts"
        ],
        "Pace": "90-95% of maximum effort or around 5K race pace."
    },
    "Tempo Run": {
        "Description": "A sustained run at a ‘comfortably hard’ pace, intended to improve lactate threshold.",
        "Purpose": [
            "Enhances endurance by improving lactate clearance",
            "Prepares the body for sustained race pace efforts",
            "Builds mental toughness for long, sustained efforts"
        ],
        "Pace": "Approximately 10K race pace or a pace you can hold for about an hour."
    },
    "Fartlek": {
        "Description": "A form of speed play that involves alternating between faster and slower running, often unstructured.",
        "Purpose": [
            "Builds both aerobic and anaerobic fitness",
            "Improves pace control and adaptability",
            "Provides a fun, less rigid speed workout"
        ],
        "Pace": "Varies between fast bursts (80-90% effort) and recovery jogs (60-70% effort)."
    },
    "Hill Repeats": {
        "Description": "Repeated uphill efforts at high intensity, with jog or walk recovery back down.",
        "Purpose": [
            "Builds leg strength and power",
            "Improves cardiovascular fitness and hill-running ability",
            "Enhances running economy"
        ],
        "Pace": "Near maximum effort on each uphill sprint."
    },
    "Pyramid Intervals": {
        "Description": "Intervals that increase and then decrease in duration or distance, forming a pyramid structure.",
        "Purpose": [
            "Improves both speed and endurance",
            "Develops pacing skills and mental resilience",
            "Provides variety to traditional intervals"
        ],
        "Pace": "Faster than tempo pace, typically around 5K pace or slightly faster."
    },
    "Ladder Intervals": {
        "Description": "Intervals that gradually increase in duration or distance before descending back down.",
        "Purpose": [
            "Builds both speed and endurance",
            "Helps with pacing for longer intervals",
            "Improves overall aerobic capacity"
        ],
        "Pace": "About 5K pace or slightly faster for ascending intervals, slightly slower on descending intervals."
    },
    "Progression Run": {
        "Description": "A continuous run where the pace gradually increases from easy to tempo or near race pace.",
        "Purpose": [
            "Improves endurance and pacing control",
            "Teaches how to finish runs strong",
            "Simulates race conditions with a fast finish"
        ],
        "Pace": "Start at easy run pace and finish at or near tempo pace."
    },
    "Negative Split Run": {
        "Description": "A run where the second half is completed faster than the first half.",
        "Purpose": [
            "Improves endurance and mental toughness",
            "Trains the body to run efficiently on tired legs",
            "Builds confidence for race day pacing"
        ],
        "Pace": "Start at an easy or steady pace, then increase to tempo pace or faster for the second half."
    },
    "Strides": {
        "Description": "Short, controlled sprints of about 100 meters with full recovery between each effort.",
        "Purpose": [
            "Improves leg turnover and running form",
            "Builds neuromuscular coordination",
            "Prepares the body for faster running"
        ],
        "Pace": "Accelerate smoothly to near top speed, then decelerate."
    }
}

cross_training_variants = {
    "Cross-Training (Cycling)": {
        "Description": "Low-impact cardiovascular exercise performed on a stationary or outdoor bike.",
        "Purpose": [
            "Improves cardiovascular fitness without the impact of running",
            "Strengthens leg muscles, especially quads and hamstrings",
            "Provides an active recovery option"
        ],
        "Intensity": "Moderate effort, around 60-75% of maximum heart rate."
    },
    "Cross-Training (Climbing)": {
        "Description": "Climbing or bouldering activities that build upper body and core strength.",
        "Purpose": [
            "Develops grip strength and upper body endurance",
            "Improves balance and coordination",
            "Provides a fun, non-traditional strength workout"
        ],
        "Intensity": "Varies depending on climbing difficulty and pace."
    },
    "Cross-Training (Swimming)": {
        "Description": "Full-body, low-impact exercise performed in a pool or open water.",
        "Purpose": [
            "Improves cardiovascular endurance",
            "Builds strength and flexibility with minimal joint impact",
            "Enhances overall muscle coordination"
        ],
        "Intensity": "Varies based on stroke and effort, typically moderate to high."
    },
    "Strength Training (Upper Body)": {
        "Description": "Exercises targeting the upper body muscles using resistance like weights or bodyweight.",
        "Purpose": [
            "Increases upper body strength",
            "Improves posture and shoulder stability",
            "Supports muscle balance and injury prevention"
        ],
        "Intensity": "Moderate to heavy resistance, 8-12 reps per set."
    },
    "Strength Training (Lower Body)": {
        "Description": "Exercises targeting lower body muscles such as quads, hamstrings, glutes, and calves.",
        "Purpose": [
            "Increases lower body strength and power",
            "Improves running performance",
            "Supports joint stability and injury prevention"
        ],
        "Intensity": "Moderate to heavy resistance, 8-12 reps per set."
    },
    "Strength Training (Full Body)": {
        "Description": "Exercises targeting all major muscle groups in the body, typically through compound movements.",
        "Purpose": [
            "Improves overall body strength and muscle endurance",
            "Enhances functional fitness for daily activities",
            "Reduces risk of muscle imbalances and injuries"
        ],
        "Intensity": "Moderate to heavy resistance, 8-12 reps per set."
    },
    "Core Workout": {
        "Description": "Focused exercises to strengthen the core muscles, including abs, obliques, and lower back.",
        "Purpose": [
            "Improves running posture and stability",
            "Reduces risk of lower back pain and injuries",
            "Enhances overall athletic performance"
        ],
        "Intensity": "Bodyweight or light resistance, high repetition."
    },
    "Yoga or Flexibility Training": {
        "Description": "Exercises focused on improving flexibility, mobility, and balance through dynamic or static stretches.",
        "Purpose": [
            "Increases flexibility and joint range of motion",
            "Improves balance and posture",
            "Promotes recovery and relaxation"
        ],
        "Intensity": "Low to moderate, depending on session type."
    },
    "Rowing": {
        "Description": "A full-body workout using a rowing machine or rowing on water that engages both upper and lower body muscles.",
        "Purpose": [
            "Improves cardiovascular endurance",
            "Strengthens upper body, core, and legs",
            "Provides a low-impact, total-body workout"
        ],
        "Intensity": "Moderate to high intensity, depending on stroke rate and resistance."
    },
    "Elliptical": {
        "Description": "A low-impact cardio exercise performed on an elliptical machine that simulates walking, running, or climbing.",
        "Purpose": [
            "Improves cardiovascular fitness with minimal joint stress",
            "Strengthens leg muscles",
            "Provides a total-body workout with moving handlebars"
        ],
        "Intensity": "Moderate effort, can be adjusted based on resistance and speed."
    },
    "Pilates": {
        "Description": "A low-impact exercise method focusing on core strength, posture, flexibility, and overall body alignment.",
        "Purpose": [
            "Strengthens the core and improves body control",
            "Enhances flexibility and joint mobility",
            "Promotes injury prevention and rehabilitation"
        ],
        "Intensity": "Moderate, often bodyweight-based exercises with emphasis on form and control."
    }
}
