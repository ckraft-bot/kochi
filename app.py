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

    def generate_generic_plan(current_long_run, weeks_to_race, easy_run_variants, speedwork_variants, cross_training_variants, race_distance, preferred_days):
        """
        Generates a training plan for a specific race based on current long run distance and weeks to race.
        """

        plan = []
        long_run_distance = current_long_run
        
        # Define weekly increase based on race timeline
        weekly_increase = calculate_weekly_increase(weeks_to_race)
        
        # Cap the long run distance during build phase
        build_peak_distance = 12

        for week in range(1, weeks_to_race + 1):
            long_run_distance = adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race)
            
            weekly_plan = {"Week": week}
            
            # Create the weekly workout plan based on the preferred days
            weekly_plan = assign_workouts_to_days(weekly_plan, long_run_distance, easy_run_variants, speedwork_variants, cross_training_variants, preferred_days)
            
            # Add to the final plan
            plan.append(weekly_plan)

        return plan


    def calculate_weekly_increase(weeks_to_race):
        """
        Calculates the weekly increase in distance based on the number of weeks to race.
        """
        if weeks_to_race <= 7:
            return 1.0  # Larger increase for short training periods
        elif weeks_to_race <= 10:
            return 0.75  # Moderate increase for medium training periods
        else:
            return 0.5  # Smaller increase for longer training periods


    def adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race):
        """
        Adjusts the long run distance based on the week of training (Base, Build, Taper).
        """
        if week <= int(0.6 * weeks_to_race):  # Base phase
            long_run_distance = min(long_run_distance + weekly_increase, build_peak_distance)
        elif week <= int(0.8 * weeks_to_race):  # Build phase
            long_run_distance = min(long_run_distance + weekly_increase * 1.5, build_peak_distance)
        else:  # Taper phase
            long_run_distance = max(long_run_distance - 1, current_long_run)
        
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
        if weeks_to_race < 4:
            st.warning("You need at least 4 weeks to prepare for a race.")
        else:
            race_distance = race_distances.get(goal, 0)

            # Call the function to generate the training plan
            plan = generate_generic_plan(current_long_run, weeks_to_race, easy_run_variants, speedwork_variants, cross_training_variants, race_distance, preferred_days)

            # Display the generated plan
            st.success("Training plan generated!")

            # Display the weekly plan with days in a fixed order
            for week in plan:
                st.subheader(f"Week {week['Week']}")

                # Define the correct order of days
                days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

                # Loop through days in the desired order and display the activities
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
    st.markdown("""
    | **Race**           | **Distance (km)** | **Distance (miles)** |
    |--------------------|-------------------|----------------------|
    | **5K**             | 5 km              | 3.1 miles            |
    | **10K**            | 10 km             | 6.2 miles            |
    | **Half Marathon**  | 21.1 km           | 13.1 miles           |
    | **Marathon**       | 42.2 km           | 26.2 miles           |
    """)

    st.header("Recommended Training Periods")
    st.markdown("""
    | **Phase**   | **5K**    | **10K**   | **Half Marathon** | **Marathon** |
    |-------------|-----------|-----------|-------------------|--------------|
    | **Base**    | 4–6 wks   | 6–8 wks   | 8–10 wks          | 10–12 wks    |
    | **Build**   | 3–4 wks   | 4–6 wks   | 4–6 wks           | 4–8 wks      |
    | **Taper**   | 1–2 wks   | 1–2 wks   | 2 wks             | 2–3 wks      |
    """)

    st.header("Phases")
    st.markdown("""
    - **Base:** Easy runs, strides, long runs, and cross-training.
    - **Build:** Introduce tempo, intervals, and race-pace long runs.
    - **Taper:** Focus on sharpening workouts while reducing volume.
    """)

    st.header("Variants")
    st.subheader("Easy Run Variants")
    st.markdown("""
    - **Easy run:** A comfortable, conversational pace run.
    - **Hill run:** A run that includes hills to build strength and endurance.
    - **Steady state run:** A run at a consistent pace, usually faster than an easy run but not as intense as speedwork.
    - **Recovery jog:** A very slow and easy run to help with recovery.
    """)

    st.subheader("Speedwork Variants")
    st.markdown("""
    - **Intervals (1 mile x 4):** Repeated runs of 1 mile with short recovery periods in between.
    - **Tempo run:** A run at a comfortably hard pace, usually sustained for 20-40 minutes.
    - **Fartlek:** A run that includes varied paces, from easy to sprinting, in no set order.
    - **Hill repeats:** Repeated runs up a hill with jog-down recoveries.
    - **Pyramid intervals:** Intervals that increase and then decrease in distance and/or intensity.
    """)

    # Cross-Training
    st.subheader("Cross-Training Variants")
    st.markdown("""
    - **Cross-training (cycling):** A low-impact aerobic workout on a bike.
    - **Cross-training (climbing):** A full-body workout, usually at a climbing gym or wall.
    - **Strength training:** Exercises that build muscle strength using weights or body weight.
    - **Core workout:** Exercises that strengthen the core muscles (abs, back).
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
