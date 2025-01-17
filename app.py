import pandas as pd
import random
import requests
import streamlit as st
from datetime import datetime, timedelta
from dictionary import *  

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Coach", "About", "Stretches", "Weather"])

if page == "Coach":
    # ------------------------ Training Plan Generator Functions ------------------------
    def generate_generic_plan(current_long_run, weeks_to_race, easy_run_variants, speedwork_variants, cross_training_variants, race_distance, preferred_days, goal):
        """
        Generates a training plan based on current long run distance, number of weeks to race, and other training parameters.
        """
        plan = []
        long_run_distance = current_long_run
        build_peak_distance = race_distances[goal] - 1  # Peak distance is race distance minus 1 mile
        
        for week in range(1, weeks_to_race + 1):
            weekly_increase = calculate_weekly_increase(goal, weeks_to_race, week)
            long_run_distance = adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race, goal)
            
            weekly_plan = {"Week": week}
            # Assign workouts to days based on preferred running days
            weekly_plan = assign_workouts_to_days(weekly_plan, long_run_distance, easy_run_variants, speedwork_variants, cross_training_variants, preferred_days)
            plan.append(weekly_plan)
        
        return plan

    def calculate_weekly_increase(goal, weeks_to_race, current_week):
        """
        Calculates the weekly increase in distance based on race distance and current training week.
        """
        phase_durations = {
            '5K': {"Base": (4, 6), "Build": (3, 4), "Taper": (1, 2)},
            '10K': {"Base": (6, 8), "Build": (4, 6), "Taper": (1, 2)},
            'Half Marathon': {"Base": (8, 10), "Build": (4, 6), "Taper": (2, 2)},
            'Marathon': {"Base": (10, 12), "Build": (4, 8), "Taper": (2, 3)}
        }
        
        base_range, build_range, taper_range = phase_durations[goal].values()
        total_phase_weeks = sum(base_range) + sum(build_range) + sum(taper_range)
        scaling_factor = weeks_to_race / total_phase_weeks
        
        base_weeks = int(sum(base_range) * scaling_factor)
        build_weeks = int(sum(build_range) * scaling_factor)
        taper_weeks = weeks_to_race - base_weeks - build_weeks
        
        if current_week <= base_weeks:
            weekly_increase = 0.5
        elif current_week <= base_weeks + build_weeks:
            weekly_increase = 0.8
        else:
            weekly_increase = 0.3
        
        return weekly_increase

    def adjust_long_run_distance(week, long_run_distance, weekly_increase, build_peak_distance, current_long_run, weeks_to_race, goal):
        """
        Adjusts the long run distance for the current week based on the race goal and training phase.
        """
        phase_durations = {
            '5K': {"Base": (4, 6), "Build": (3, 4), "Taper": (1, 2)},
            '10K': {"Base": (6, 8), "Build": (4, 6), "Taper": (1, 2)},
            'Half Marathon': {"Base": (8, 10), "Build": (4, 6), "Taper": (2, 2)},
            'Marathon': {"Base": (10, 12), "Build": (4, 8), "Taper": (2, 3)}
        }

        base_range, build_range, taper_range = phase_durations[goal].values()
        total_phase_weeks = sum(base_range) + sum(build_range) + sum(taper_range)
        scaling_factor = weeks_to_race / total_phase_weeks
        
        base_weeks = int(sum(base_range) * scaling_factor)
        build_weeks = int(sum(build_range) * scaling_factor)
        taper_weeks = weeks_to_race - base_weeks - build_weeks

        if week <= base_weeks:
            long_run_distance = min(long_run_distance + weekly_increase, build_peak_distance)
        elif week <= base_weeks + build_weeks:
            long_run_distance = min(long_run_distance + weekly_increase * 1.5, build_peak_distance)
        else:
            long_run_distance = max(long_run_distance - weekly_increase, current_long_run)
        
        return long_run_distance

    def assign_workouts_to_days(weekly_plan, long_run_distance, easy_run_variants, speedwork_variants, cross_training_variants, preferred_days):
        """
        Assigns specific workouts to the preferred running days of the week.
        """
        light = f"{random.choice(list(easy_run_variants.keys()))} (2-{long_run_distance / 2:.1f} miles)"
        moderate = f"{random.choice(list(speedwork_variants.keys()))} ({long_run_distance / 3:.1f} miles)"
        hard = f"Long run ({long_run_distance:.1f} miles)"
        cross_train = f"{random.choice(list(cross_training_variants.keys()))}"
        rest = "Rest or walk"

        day_plans = {
            # Monday-Wednesday-Friday
            "Monday-Wednesday-Friday": {
                "Monday": light,
                "Tuesday": cross_train,
                "Wednesday": moderate,
                "Thursday": cross_train,
                "Friday": hard,
                "Saturday": rest,
                "Sunday": rest 
            },
            # Tuesday-Thursday-Saturday
            "Tuesday-Thursday-Saturday": {
                "Monday": cross_train,
                "Tuesday": light,
                "Wednesday": cross_train,
                "Thursday": moderate,
                "Friday": rest,
                "Saturday": hard,
                "Sunday": rest 
            },
            # Wednesday-Friday-Sunday
            "Wednesday-Friday-Sunday": {
                "Monday": rest,
                "Tuesday": rest,
                "Wednesday": light,
                "Thursday": cross_train,
                "Friday": moderate,
                "Saturday": cross_train,
                "Sunday": hard
            }
        }

        day_plan = day_plans.get(preferred_days, {})
        for day in day_plan:
            weekly_plan[day] = day_plan[day]
        
        return weekly_plan

    # ------------------------ User Input Form --------------------------------
    def countdown(race_date):
        """
        Calculates the number of days until the specified race date and displays a progress bar indicating the time remaining. 
        """
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
            # ~ a month out from the race
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
            st.subheader(f"The race has passed, how did you do?")
        else:
            st.subheader("Race day is here! Good luck and have fun!")

    # Title and description of the app
    st.title("Create Your Custom Training Plan")
    st.write("""
    Hey there! Ready to train for your next big race? Whether it's a 5K, 10K, Half Marathon, or Marathon, we've got your back.
    We'll tailor a training plan that fits your timeline and fitness level. Remember, consistency is key, so let's get started!
    """)

    # User inputs
    goal = st.selectbox("What race are you training for?", ["5K", "10K", "Half Marathon", "Marathon"])
    current_long_run = st.number_input("What is your current longest run (in miles)?", min_value=0.0, step=0.5)
    race_date = st.date_input("When is the race?")
    
    # Validate the race date
    if race_date < datetime.now().date():
        st.error("Please select a future race date.")
    else:
        preferred_days = st.selectbox(
            "Select your preferred running days",
            ["Monday-Wednesday-Friday", "Tuesday-Thursday-Saturday", "Wednesday-Friday-Sunday"]
        )
        
        # Generate the training plan when the button is pressed
        if st.button("Generate Plan"):
            # Call the countdown function to show progress
            countdown(race_date)

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
                plan = generate_generic_plan(
                    current_long_run, weeks_to_race, 
                    easy_run_variants, speedwork_variants, 
                    cross_training_variants, race_distance, 
                    preferred_days, goal
                )

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
    7. **Streches**: go to the "Stretches" page to see how to warm up and cool down properly.
    8. **Weather:** Go to the "Weather" page to see how you should dress for your outdoor training.
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

elif page == "Stretches":
    st.title("Stretching Exercises")

    with st.expander("Dynamic Stretches"):
        st.write('''
            Alright, team! Dynamic stretches are all about getting your body warmed up 
            and ready to move. These are active movements like leg swings, arm circles, 
            and walking lunges that loosen up those muscles and get your blood flowing. 
            Always do these **before** you hit the trail—think of it as flipping the "on" switch 
            for your body. Let's prep like champions!

            Not sure where to start? No problem, check out this [video guide](https://youtu.be/sI1iHQSHOQE?si=pmnXCyl00QmnK6_8).
        ''')

    with st.expander("Static Stretches"):
        st.write('''
            Listen up, runners! Static stretches are your go-to after a good run. 
            These are the stretches where you hold a position to really work on 
            flexibility—hamstring stretches, calf stretches, triceps stretches, you name it. 
            Do these **after** your workout when your muscles are warmed up. This helps 
            keep you loose and prevents injuries down the line. Stay disciplined—flexibility 
            is just as important as endurance!
            
            Not sure where to start? No problem, check out this [video guide](https://youtu.be/12pDBWdR3I4?si=U_OoBCgNRH3rxyK-).
        ''')
        
elif page == "Weather":
    st.title("Weather Monitor 🌦️")
    def get_coordinates(city_name):
        url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
        headers = {"User-Agent": "WeatherDashboardApp/1.0 (contact@example.com)"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            location_data = response.json()
            if location_data:
                location = location_data[0]
                return float(location['lat']), float(location['lon'])
            else:
                st.warning("City not found. Try adding the country name (e.g., 'Paris, France').")
                return None, None
        else:
            st.error(f"API request failed with status code {response.status_code}: {response.text}")
            return None, None

    def get_weather_data(lat, lon, hours):
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m&forecast_days=2"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Failed to retrieve weather data.")
            return None

    st.write("Look at the weather to dress appropriately for your outdoor training session!")

    city_name = st.text_input("Enter city name", value="New York City")
    forecast_duration = st.slider("Select forecast duration (hours)", min_value=12, max_value=48, value=24, step=12)
    unit = st.radio("Select temperature unit", ["Celsius (°C)", "Fahrenheit (°F)"])
    parameter_options = st.multiselect(
        "Choose weather parameters to display",
        options=["Temperature", "Humidity", "Wind Speed"],
        default=["Temperature", "Humidity"]
    )

    if st.button("Get local weather"):
        lat, lon = get_coordinates(city_name)
        if lat and lon:
            data = get_weather_data(lat, lon, forecast_duration)
            if data:
                times = [datetime.now() + timedelta(hours=i) for i in range(forecast_duration)]
                df = pd.DataFrame({"Time": times})

                st.subheader("Current Weather Summary")
                col1, col2, col3 = st.columns(3)
                temperature = data['hourly']['temperature_2m'][0]
                if unit == "Fahrenheit (°F)":
                    temperature = (temperature * 9/5) + 32
                    temp_unit = "°F"
                else:
                    temp_unit = "°C"
                col1.metric(f"🌡️ Temperature {temp_unit}", f"{temperature:.1f}{temp_unit}")
                col2.metric("💧 Humidity (%)", f"{data['hourly']['relative_humidity_2m'][0]}%")
                col3.metric("💨 Wind Speed (m/s)", f"{data['hourly']['wind_speed_10m'][0]} m/s")

                if "Temperature" in parameter_options:
                    temperatures = data['hourly']['temperature_2m'][:forecast_duration]
                    if unit == "Fahrenheit (°F)":
                        temperatures = [(temp * 9/5) + 32 for temp in temperatures]
                    df[f"Temperature ({temp_unit})"] = temperatures
                    st.subheader(f"Temperature Forecast")
                    st.line_chart(df.set_index("Time")[f"Temperature ({temp_unit})"])

                if "Humidity" in parameter_options:
                    df["Humidity"] = data['hourly']['relative_humidity_2m'][:forecast_duration]
                    st.subheader(f"Humidity Forecast")
                    st.line_chart(df.set_index("Time")["Humidity"])
