# Kochi :billed_cap:

## Overview
Kochi (코치) is a Korean term derived from the English word "coach." This [application](https://kochi-training-plan.streamlit.app/) serves as your virtual coach, designed to assist runners, such as yourself, in formulating a personalized training regimen for their races. Regardless of whether you are preparing for a 5K, 10K, half marathon, or marathon, the application will produce a comprehensive plan tailored to your current fitness level and the time remaining before your race. The plan encompasses easy runs, speed workouts, long runs, cross-training sessions, and designated rest days.


### App - Features
- **Custom Training Plan Generation:** Input your current long run, race date, and preferred running days to get a tailored training plan.
- **Running Day Variants:** Choose from different combinations of running days (Monday-Wednesday-Friday, Tuesday-Thursday-Sunday, or Wednesday-Friday-Saturday).
- **Countdown to Race Day:** See how many days are left until your race along with a motivational progress bar.
- **App Instructions & Variants:** Detailed explanation of how to use the app and descriptions of different types of runs and cross-training workouts.

### App - How To Use
1. **Go to the "Coach" page.**
2. **Select your race goal:** Choose the race distance you are training for (5K, 10K, Half Marathon, or Marathon).
3. **Input your current long run:** Enter the longest distance you have run recently.
4. **Set your race date:** Pick the date of your race.
5. **Choose your preferred running days:** Select the days you prefer to run from the dropdown menu.
6. **Generate plan:** Click the "Generate Plan" button to create your custom training plan.
7. **Streches**: go to the "Stretches" page to see how to warm up and cool down properly.
8. **Weather:** Go to the "Weather" page to see how you should dress for your outdoor training.
9. **Store:** Go to the "Store" page to find nearby (or within 5 km/3.1 mi radius) running stores.

### App - Setup
To run this app locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory:**
    ```bash
    cd <project-directory>
    ```

3. **Install the required dependencies:**
    ```bash
    pip install streamlit
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

### Code Structure
- **Training Plan Generator Functions:** Functions to generate a training plan based on user inputs.
- **User Input Form:** Collects user inputs such as race goal, current long run, race date, and preferred running days.
- **About Page:** Provides an overview of the app, instructions on how to use it, and descriptions of workout variants.
- **Countdown Page:** Displays the number of days until the race with a progress bar and motivational messages.

## About Running

# Race Distances

## Conversion Table
| **Race**           | **Distance (km)** | **Distance (miles)** |
|--------------------|-------------------|----------------------|
| **5K**             | 5 km              | 3.1 miles            |
| **10K**            | 10 km             | 6.2 miles            |
| **Half Marathon**  | 21.1 km           | 13.1 miles           |
| **Marathon**       | 42.2 km           | 26.2 miles           |

## Minimum Weeks to Train By Distance
| **Race**           | **Minimum Weeks** |
|--------------------|-------------------|
| **5K**             | 6 weeks           |
| **10K**            | 8 weeks           |
| **Half Marathon**  | 12 weeks          |
| **Marathon**       | 16 weeks          |

# Phases
- **Base:** Easy runs, strides, long runs, and cross-training.
- **Build:** Introduce tempo, intervals, and race-pace long runs.
- **Taper:** Focus on sharpening workouts while reducing volume.

## Recommended Phases By Distance
| **Phase**   | **5K**    | **10K**   | **Half Marathon** | **Marathon** |
|-------------|-----------|-----------|-------------------|--------------|
| **Base**    | 4–6 weeks   | 6–8 weeks   | 8–10 weeks          | 10–12 weeks    |
| **Build**   | 3–4 weeks   | 4–6 weeks   | 4–6 weeks           | 4–8 weeks      |
| **Taper**   | 1–2 weeks   | 1–2 weeks   | 2 weeks             | 2–3 weeks      |

# Variants

## Easy Run Variants
- **Easy run**: A comfortable, conversational pace run meant to build endurance without exerting too much effort.
- **Hill run**: A run that includes hills to build strength and endurance by challenging the muscles.
- **Steady state run**: A run at a consistent pace, faster than an easy run but not as intense as speedwork; it improves stamina.
- **Recovery jog**: A very slow and easy run to help with recovery, usually done after intense workouts or races.
- **Long run**: A run longer than your typical daily runs, aimed at improving endurance and preparing for race distances.
- **Trail run**: A run on unpaved, often uneven terrain, which challenges your balance, strength, and mental focus.
- **Base-building run**: A moderate-paced run intended to build a strong aerobic base for future speedwork and racing.

## Speedwork Variants
- **Intervals (e.g., 400m x 8, 800m x 6, 1 mile x 4)**: Repeating a set distance (usually short) at a fast pace with recovery jogs in between. This helps improve speed and cardiovascular fitness.
- **Tempo run (continuous or intervals)**: A run at a challenging but sustainable pace, often referred to as your "threshold pace," which helps improve lactate threshold and endurance.
- **Fartlek (structured or unstructured)**: A Swedish term meaning "speed play," where you vary your pace between easy and fast sections throughout the run, helping to improve both speed and endurance.
- **Hill repeats (short, long, sprint-back, alternating effort)**: Running up and down a hill, either at full speed or at a moderate pace, to build strength and speed.
- **Pyramid intervals**: A set of intervals that increase in distance (e.g., 400m, 800m, 1200m) and then decrease in distance (e.g., 1200m, 800m, 400m), providing a varied and challenging workout.
- **Ladder intervals**: Similar to pyramid intervals but with varying rest times or interval distances, which helps in improving speed and stamina.
- **Progression run**: A run that gradually increases in pace, starting slow and finishing at a faster pace, aimed at building endurance and mental toughness.
- **Negative split run**: A run where the second half is faster than the first, promoting improved pacing strategies and stamina.
- **Strides (100m accelerations with full recovery)**: Short bursts of acceleration at maximum effort for 100 meters, followed by complete rest, which enhances speed and running form.

## Cross-Training Variants
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

---

Happy running and good luck with your training! 🏃‍♂️🏃‍♀️
