import streamlit as st
from datetime import datetime
import random

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Coach", "About", "Countdown"])
if page == "Coach":
    # ------------------------ Training Plan Generator Functions ------------------------
    easy_run_variants = ["Easy run", "Hill run", "Steady state run", "Recovery jog"]
    speedwork_variants = ["Intervals (1 mile x 4)", "Tempo run", "Fartlek", "Hill repeats", "Pyramid intervals"]
    cross_training_variants = ["Cross-training (cycling)", "Cross-training (climbing)", "Strength training", "Core workout"]

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
        
        light = f"{random.choice(easy_run_variants)} (2-{long_run_distance / 2:.1f} miles)"
        moderate = f"{random.choice(speedwork_variants)} ({long_run_distance / 3:.1f} miles)"
        hard = f"Long run ({long_run_distance:.1f} miles)"
        cross_train = f"{random.choice(cross_training_variants)}"
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

    # Race distance dictionary
    race_distances = {
        "5K": 3.1,
        "10K": 6.2,
        "Half Marathon": 13.1,
        "Marathon": 26.2
    }

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

            # Display the weekly plan
            for week in plan:
                st.subheader(f"Week {week['Week']}")
                for day, activity in week.items():
                    if day != "Week":
                        st.text(f"{day}: {activity}")
elif page == "About":
    st.title("How to use the app")

    st.header("App Overview")
    st.write("""
    This app customizes a training plan for your race preparation. 
    The app generates a detailed training plan that includes a mix of easy runs, speed workouts, long runs, cross-training, and rest days based on your current fitness level and the time remaining until your race.
    """)

    st.header("App Instructions")
    st.write("""
    1. Go to the "Coach" page.
    2. **Select your race goal**: choose the race distance you are training for (5K, 10K, Half Marathon, or Marathon).
    3. **Input your current long run**: enter the longest distance you have run recently.
    4. **Set your race date**: pick the date of your race.
    5. **Choose your preferred running days**: select the days you prefer to run from the dropdown menu.
    6. **Generate plan**: click the "Generate Plan" button to create your custom training plan.
    7. **Countdown**: go to the "Countdown" page to see how many days are left
    """)


    st.header("Workout Variants")
    st.write("""
    ### Easy Run Variants
    - **Easy run:** a comfortable, conversational pace run.
    - **Hill run:** a run that includes hills to build strength and endurance.
    - **Steady state run:** a run at a consistent pace, usually faster than an easy run but not as intense as speedwork.
    - **Recovery jog:** a very slow and easy run to help with recovery.
    
    ### Speedwork Variants
    - **Intervals (1 mile x 4):** repeated runs of 1 mile with short recovery periods in between.
    - **Tempo run:** a run at a comfortably hard pace, usually sustained for 20-40 minutes.
    - **Fartlek:** a run that includes varied paces, from easy to sprinting, in no set order.
    - **Hill repeats:** repeated runs up a hill with jog-down recoveries.
    - **Pyramid intervals:** intervals that increase and then decrease in distance and/or intensity.

    ### Cross-Training Variants
    - **Cross-training (cycling):** a low-impact aerobic workout on a bike.
    - **Cross-training (climbing):** a full-body workout, usually at a climbing gym or wall.
    - **Strength training:** exercises that build muscle strength using weights or body weight.
    - **Core workout:** exercises that strengthen the core muscles (abs, back).
    """)
elif page == "Countdown":
    st.title("Countdown to Race Day")
    
    # User inputs the race date
    race_date = st.date_input("When is the race again?")
    
    # Calculate the number of days until the race
    today = datetime.now().date()
    days_until_race = (race_date - today).days
    
    if days_until_race > 0:
        st.subheader(f"{days_until_race} days until your race!")
    else:
        st.subheader("Race day is here! Good luck and have fun!")
        
    # Assuming weeks_to_race is already calculated from race_date
    weeks_to_race = max(1, (race_date - today).days // 7)
    progress = min(1.0, weeks_to_race / (weeks_to_race + 1))
    st.progress(progress)

    # Show progress messages
    if progress == 1.0:
        st.markdown("🎉 You're ready for the race! 🎉")
    elif progress > 0.75:
        st.markdown("🏃‍♂️ Almost there! 🏃‍♀️")
    elif progress > 0.5:
        st.markdown("💪 Keep pushing! 💪")
    else:
        st.markdown("👟 Let's get moving! 👟")