# Kochi :billed_cap:

## Overview
**Kochi (코치)** is a Korean term derived from the English word "coach." This application serves as your virtual coach, designed to assist runners, such as yourself, in formulating a personalized training regimen for their races. Regardless of whether you are preparing for a 5K, 10K, half marathon, or marathon, the application will produce a comprehensive plan tailored to your current fitness level and the time remaining before your race. The plan encompasses easy runs, speed workouts, long runs, cross-training sessions, and designated rest days.

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
7. **Countdown:** Go to the "Countdown" page to see how many days are left until your race.

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

### Race Distances  

| **Race**           | **Distance (km)** | **Distance (miles)** |
|--------------------|-------------------|----------------------|
| **5K**             | 5 km              | 3.1 miles            |
| **10K**            | 10 km             | 6.2 miles            |
| **Half Marathon**  | 21.1 km           | 13.1 miles           |
| **Marathon**       | 42.2 km           | 26.2 miles           |

### Recommended Training Periods 

| **Phase**   | **5K**    | **10K**   | **Half Marathon** | **Marathon** |
|-------------|-----------|-----------|-------------------|--------------|
| **Base**    | 4–6 wks   | 6–8 wks   | 8–10 wks          | 10–12 wks    |
| **Build**   | 3–4 wks   | 4–6 wks   | 4–6 wks           | 4–8 wks      |
| **Taper**   | 1–2 wks   | 1–2 wks   | 2 wks             | 2–3 wks      |

### Phases

- **Base:** Easy runs, strides, long runs, and cross-training.
- **Build:** Introduce tempo, intervals, and race-pace long runs.
- **Taper:** Focus on sharpening workouts while reducing volume.

### Variants

#### Easy Run Variants
- **Easy run:** A comfortable, conversational pace run.
- **Hill run:** A run that includes hills to build strength and endurance.
- **Steady state run:** A run at a consistent pace, usually faster than an easy run but not as intense as speedwork.
- **Recovery jog:** A very slow and easy run to help with recovery.

#### Speedwork Variants
- **Intervals (1 mile x 4):** Repeated runs of 1 mile with short recovery periods in between.
- **Tempo run:** A run at a comfortably hard pace, usually sustained for 20-40 minutes.
- **Fartlek:** A run that includes varied paces, from easy to sprinting, in no set order.
- **Hill repeats:** Repeated runs up a hill with jog-down recoveries.
- **Pyramid intervals:** Intervals that increase and then decrease in distance and/or intensity.

#### Cross-Training Variants
- **Cross-training (cycling):** A low-impact aerobic workout on a bike.
- **Cross-training (climbing):** A full-body workout, usually at a climbing gym or wall.
- **Strength training:** Exercises that build muscle strength using weights or body weight.
- **Core workout:** Exercises that strengthen the core muscles (abs, back).

---

Happy running and good luck with your training! 🏃‍♂️🏃‍♀️
