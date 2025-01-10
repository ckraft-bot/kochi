import streamlit as st
from datetime import datetime, timedelta, date
import random
import dictionary
from dictionary import *

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Coach", "About", "Countdown"])
if page == "Coach":
    # ------------------------ Training Plan Generator Functions ------------------------
    categories = {
        "Easy Run Variants": easy_run_variants,
        "Speedwork Variants": speedwork_variants,
        "Cross-Training Variants": cross_training_variants
    }

    def generate_generic_plan(current_long_run, weeks_to_race, easy_run_variants, speedwork_variants, cross_training_variants, race_distance, preferred_days, goal):
        """
        Generates a training plan for a specific race based on current long run distance and weeks to race.
        """
        
        plan = []
        long_run_distance = current_long_run
        
        # Set build_peak_distance as goal distance minus 1 mile
        build_peak_distance = race_distances[goal] - 1
        
        for week in range(1, weeks_to_race + 1):
            weekly_increase = calculate_weekly_increase(goal, weeks_to_race, week)
            long_run_distance = adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race, goal)
            
            weekly_plan = {"Week": week}
            
            # Create the weekly workout plan based on the preferred days
            weekly_plan = assign_workouts_to_days(weekly_plan, long_run_distance, easy_run_variants, speedwork_variants, cross_training_variants, preferred_days)
            
            plan.append(weekly_plan)
        
        return plan

    def calculate_weekly_increase(goal, weeks_to_race, current_week):
        """
        Calculates the weekly increase in distance based on race distance and the current week of training.
        
        Parameters:
        - goal (str): One of '5K', '10K', 'Half Marathon', or 'Marathon'.
        - weeks_to_race (int): The total number of weeks remaining until the race.
        - current_week (int): The current week of training (starting from 1).

        Returns:
        - float: The recommended weekly increase in distance.
        """
        
        # Define phase durations based on the race goal
        phase_durations = {
            '5K': {"Base": (4, 6), "Build": (3, 4), "Taper": (1, 2)},
            '10K': {"Base": (6, 8), "Build": (4, 6), "Taper": (1, 2)},
            'Half Marathon': {"Base": (8, 10), "Build": (4, 6), "Taper": (2, 2)},
            'Marathon': {"Base": (10, 12), "Build": (4, 8), "Taper": (2, 3)}
        }
        
        # Get the duration ranges for the selected goal
        base_range, build_range, taper_range = phase_durations[goal].values()
        
        # Calculate the number of weeks allocated for each phase
        total_phase_weeks = sum(base_range) + sum(build_range) + sum(taper_range)
        scaling_factor = weeks_to_race / total_phase_weeks
        
        base_weeks = int(sum(base_range) * scaling_factor)
        build_weeks = int(sum(build_range) * scaling_factor)
        taper_weeks = weeks_to_race - base_weeks - build_weeks
        
        # Determine which phase the current week falls into
        if current_week <= base_weeks:
            weekly_increase = 0.5  # Base phase increase
        elif current_week <= base_weeks + build_weeks:
            weekly_increase = 0.8  # Build phase increase
        else:
            weekly_increase = 0.3  # Taper phase reduction
        
        return weekly_increase

    def adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race, goal):
        """
        Adjusts the long run distance based on the week of training (Base, Build, Taper) and the race goal.
        
        Parameters:
        - week (int): Current week of training.
        - long_run_distance (float): Current long run distance.
        - weekly_increase (float): Weekly increase in distance.
        - build_peak_distance (float): Maximum peak distance during the Build phase.
        - current_long_run (float): Initial long run distance at the start of the plan.
        - weeks_to_race (int): Total number of weeks in the training plan.
        - goal (str): The race goal ('5K', '10K', 'Half Marathon', 'Marathon').

        Returns:
        - float: Adjusted long run distance for the given week.
        """
        
        # Define phase durations based on the goal
        phase_durations = {
            '5K': {"Base": (4, 6), "Build": (3, 4), "Taper": (1, 2)},
            '10K': {"Base": (6, 8), "Build": (4, 6), "Taper": (1, 2)},
            'Half Marathon': {"Base": (8, 10), "Build": (4, 6), "Taper": (2, 2)},
            'Marathon': {"Base": (10, 12), "Build": (4, 8), "Taper": (2, 3)}
        }
        
        # Get the durations for each phase for the selected goal
        base_range, build_range, taper_range = phase_durations[goal].values()
        
        # Calculate the total number of weeks in each phase using scaling
        total_phase_weeks = sum(base_range) + sum(build_range) + sum(taper_range)
        scaling_factor = weeks_to_race / total_phase_weeks
        
        base_weeks = int(sum(base_range) * scaling_factor)
        build_weeks = int(sum(build_range) * scaling_factor)
        taper_weeks = weeks_to_race - base_weeks - build_weeks

        if week <= base_weeks:
            # Base phase: gradual increase in long run distance
            long_run_distance = min(long_run_distance + weekly_increase, build_peak_distance)
        
        elif week <= base_weeks + build_weeks:
            # Build phase: slightly faster increase, but capped at the peak distance
            long_run_distance = min(long_run_distance + weekly_increase * 1.5, build_peak_distance)
        
        else:
            # Taper phase: gradual reduction in long run distance for recovery
            long_run_distance = max(long_run_distance - weekly_increase, current_long_run)
        
        return long_run_distance

    def assign_workouts_to_days(weekly_plan, long_run_distance, easy_run_variants, speedwork_variants, cross_training_variants, preferred_days):
        """
        Assigns workouts to the selected days based on the preferred days.
        """
        
        # Randomly pick workout types from the keys of each variant dictionary
        light = f"{random.choice(list(easy_run_variants.keys()))} (2-{long_run_distance / 2:.1f} miles)"
        moderate = f"{random.choice(list(speedwork_variants.keys()))} ({long_run_distance / 3:.1f} miles)"
        hard = f"Long run ({long_run_distance:.1f} miles)"
        cross_train = f"{random.choice(list(cross_training_variants.keys()))}"
        rest = "Rest or walk"

        # Define plans for common combinations
        day_plans = {
            "Monday-Wednesday-Friday": {
                "Monday": light,
                "Wednesday": moderate,
                "Friday": hard,
                "Tuesday": cross_train,
                "Thursday": cross_train,
                "Saturday": rest,
                "Sunday": rest
            },
            "Tuesday-Thursday-Sunday": {
                "Monday": cross_train,
                "Tuesday": light,
                "Wednesday": cross_train,
                "Thursday": moderate,
                "Friday": rest,
                "Saturday": rest,
                "Sunday": hard
            },
            "Wednesday-Friday-Saturday": {
                "Monday": rest,
                "Tuesday": rest,
                "Wednesday": light,
                "Thursday": cross_train,
                "Friday": moderate,
                "Saturday": hard,
                "Sunday": rest
            }
        }

        # Assign workouts to days
        day_plan = day_plans.get(preferred_days, {})
        
        for day in day_plan:
            weekly_plan[day] = day_plan[day]
        
        return weekly_plan

    # ------------------------ User Input Form ------------------------

    # Title and description of the app
    st.title("Create Your Custom Training Plan")
    st.write("""
    Hey there! Ready to train for your next big race? Whether it's a 5K, 10K, Half Marathon, or Marathon, I've got your back. 
    We'll tailor a training plan that fits your timeline and fitness level. Remember, it's all about progression and having fun with the process. 
    So lace up those running shoes, stay consistent, and let's crush those goals together!
    """)

    # User inputs
    goal = st.selectbox("What race are your training for?", ["5K", "10K", "Half Marathon", "Marathon"])
    current_long_run = st.number_input("What is your current longest run (in miles)?", min_value=0.0, step=0.5)
    race_date = st.date_input("When is the race?")

    preferred_days = st.selectbox(
        "Select your preferred running days:",
        ["Monday-Wednesday-Friday", "Tuesday-Thursday-Sunday", "Wednesday-Friday-Saturday"]
    )

    # Generate the training plan when the button is pressed
    if st.button("Generate Plan"):
        weeks_to_race = (race_date - datetime.now().date()).days // 7

        min_weeks_required = {
            "5K": 6,
            "10K": 8,
            "Half Marathon": 12,
            "Marathon": 16
        }

        if weeks_to_race < min_weeks_required[goal]:
            st.warning(f"You need at least {min_weeks_required[goal]} weeks to prepare for a {goal}.")
        else:
            race_distance = race_distances.get(goal, 0)

            plan = generate_generic_plan(current_long_run, weeks_to_race, easy_run_variants, speedwork_variants, cross_training_variants, race_distance, preferred_days)

            st.success("Training plan generated!")

            for week in plan:
                st.subheader(f"Week {week['Week']}")

                days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

                for day in days_of_week:
                    if day in week:
                        st.text(f"{day}: {week[day]}")
                        
elif page == "About":
    st.title("Understand the App")

    st.header("Overview")
    st.write("""
    This app customizes a training plan for your race preparation. 
    The app generates a detailed training plan that includes a mix of easy runs, speed workouts, long runs, cross-training, and rest days based on your current fitness level and the time remaining until your race.
    """)

    st.header("Instructions")
    st.write("""
    1. Go to the "Coach" page.
    2. **Select your race goal**: choose the race distance you are training for (5K, 10K, Half Marathon, or Marathon).
    3. **Input your current long run**: enter the longest distance you have run recently.
    4. **Set your race date**: pick the date of your race.
    5. **Choose your preferred running days**: select the days you prefer to run from the dropdown menu.
    6. **Generate plan**: click the "Generate Plan" button to create your custom training plan.
    7. **Countdown**: go to the "Countdown" page to see how many days are left
    """)

    st.title("Understand Running")

    st.header("Race Distances")
    st.subheader("Conversion Table")
    st.markdown("""
    | **Race**           | **Distance (km)** | **Distance (miles)** |
    |--------------------|-------------------|----------------------|
    | **5K**             | 5 km              | 3.1 miles            |
    | **10K**            | 10 km             | 6.2 miles            |
    | **Half Marathon**  | 21.1 km           | 13.1 miles           |
    | **Marathon**       | 42.2 km           | 26.2 miles           |
    """)

    st.subheader("Minimum Weeks to Train By Distance")
    st.markdown("""
    | **Race**           | **Minimum Weeks** |
    |--------------------|-------------------|
    | **5K**             | 6 weeks           |
    | **10K**            | 8 weeks           |
    | **Half Marathon**  | 12 weeks          |
    | **Marathon**       | 16 weeks          |
    """)

    st.header("Phases")
    st.markdown("""
    - **Base:** Easy runs, strides, long runs, and cross-training.
    - **Build:** Introduce tempo, intervals, and race-pace long runs.
    - **Taper:** Focus on sharpening workouts while reducing volume.
    """)

    st.subheader("Recommended Phases By Distance")
    st.markdown("""
    | **Phase**   | **5K**    | **10K**   | **Half Marathon** | **Marathon** |
    |-------------|-----------|-----------|-------------------|--------------|
    | **Base**    | 4–6 weeks   | 6–8 weeks   | 8–10 weeks          | 10–12 weeks    |
    | **Build**   | 3–4 weeks   | 4–6 weeks   | 4–6 weeks           | 4–8 weeks      |
    | **Taper**   | 1–2 weeks   | 1–2 weeks   | 2 weeks             | 2–3 weeks      |
    """)

    st.header("Variants")
    st.subheader("Easy Run Variants")
    st.markdown("""
    - **Easy run**: A comfortable, conversational pace run meant to build endurance without exerting too much effort.
    - **Hill run**: A run that includes hills to build strength and endurance by challenging the muscles.
    - **Steady state run**: A run at a consistent pace, faster than an easy run but not as intense as speedwork; it improves stamina.
    - **Recovery jog**: A very slow and easy run to help with recovery, usually done after intense workouts or races.
    - **Long run**: A run longer than your typical daily runs, aimed at improving endurance and preparing for race distances.
    - **Trail run**: A run on unpaved, often uneven terrain, which challenges your balance, strength, and mental focus.
    - **Base-building run**: A moderate-paced run intended to build a strong aerobic base for future speedwork and racing.
    """)

    st.subheader("Speedwork Variants")
    st.markdown("""
    - **Intervals (e.g., 400m x 8, 800m x 6, 1 mile x 4)**: Repeating a set distance (usually short) at a fast pace with recovery jogs in between. This helps improve speed and cardiovascular fitness.
    - **Tempo run (continuous or intervals)**: A run at a challenging but sustainable pace, often referred to as your "threshold pace," which helps improve lactate threshold and endurance.
    - **Fartlek (structured or unstructured)**: A Swedish term meaning "speed play," where you vary your pace between easy and fast sections throughout the run, helping to improve both speed and endurance.
    - **Hill repeats (short, long, sprint-back, alternating effort)**: Running up and down a hill, either at full speed or at a moderate pace, to build strength and speed.
    - **Pyramid intervals**: A set of intervals that increase in distance (e.g., 400m, 800m, 1200m) and then decrease in distance (e.g., 1200m, 800m, 400m), providing a varied and challenging workout.
    - **Ladder intervals**: Similar to pyramid intervals but with varying rest times or interval distances, which helps in improving speed and stamina.
    - **Progression run**: A run that gradually increases in pace, starting slow and finishing at a faster pace, aimed at building endurance and mental toughness.
    - **Negative split run**: A run where the second half is faster than the first, promoting improved pacing strategies and stamina.
    - **Strides (100m accelerations with full recovery)**: Short bursts of acceleration at maximum effort for 100 meters, followed by complete rest, which enhances speed and running form.
    """)

    # Cross-Training
    st.subheader("Cross-Training Variants")
    st.markdown("""
    - **Cross-training (cycling)**: A low-impact activity using a bicycle, either outdoors or on a stationary bike, to improve cardiovascular fitness and leg strength.
    - **Cross-training (climbing)**: Using rock climbing or indoor climbing to enhance upper body strength, grip, and coordination while also building cardiovascular endurance.
    - **Cross-training (swimming)**: A full-body, low-impact workout in the pool that improves cardiovascular endurance, flexibility, and muscle strength.
    - **Strength training (upper body, lower body, full body)**: Exercises aimed at building muscle strength and endurance, targeting different parts of the body through weights, resistance bands, or bodyweight exercises.
    - **Core workout (planks, crunches, leg raises)**: Exercises that target the core muscles, including the abdominals, obliques, and lower back, to improve stability and posture.
    - **Yoga or flexibility training**: Exercises focused on flexibility, balance, and relaxation, helping with recovery, injury prevention, and overall body mobility.
    - **Rowing**: A full-body workout using a rowing machine or rowing on water that engages both upper and lower body muscles while providing a great cardiovascular workout.
    - **Elliptical**: A low-impact cardio exercise performed on an elliptical machine that simulates walking, running, or climbing, providing a full-body workout.
    - **Aqua jogging**: Running in water, typically in a pool, which reduces impact on joints while providing an excellent cardiovascular workout.
    - **Pilates**: A workout that focuses on strengthening the core, improving flexibility, and enhancing overall body alignment and posture, often involving bodyweight exercises or equipment like reformers.
    """)

elif page == "Countdown":
    st.title("Countdown to Race Day")

    # User inputs the race date
    race_date = st.date_input("When is the race again?")

    # Calculate the number of days until the race
    today = datetime.now().date()
    days_until_race = (race_date - today).days
    total_days = 16 * 7  # Total days in 16 weeks

    if days_until_race > 0:
        st.subheader(f"{days_until_race} days until your race!")

        # Calculate progress based on the benchmark periods (estimated)
        # the week of the race will be 100%
        if days_until_race <= 7:
            progress = 1.0
        # ~ a week out from the race
        elif days_until_race <= 11:
            progress = 0.9
        # ~ a mounth out from the race
        elif days_until_race <= 28:
            progress = 0.75
        # ~ two months out from the race
        elif days_until_race <= 56:
            progress = 0.5
        # ~ three months out from the race 
        elif days_until_race <= 84:
            progress = 0.25
        else:
            progress = 0.0

        st.progress(progress)

        # Show progress messages
        if progress == 1.0:
            st.markdown("🎉 You're ready for the race! 🎉")
        elif progress >= 0.75:
            st.markdown("🏃‍♂️ Almost there! 🏃‍♀️")
        elif progress >= 0.5:
            st.markdown("💪 Keep pushing! 💪")
        else:
            st.markdown("👟 Let's get moving! 👟")

    elif days_until_race < 0:
        st.subheader(f"The race has past, how did you do?")
    else:
        st.subheader("Race day is here! Good luck and have fun!")
