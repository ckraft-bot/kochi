import streamlit as st
from dictionary import *

def tooltip_text(text, tooltip):
    """Render text with a tooltip"""
    st.markdown(f"""
    <div class="tooltip">{text}
        <span class="tooltiptext">{tooltip}</span>
    </div>
    """, unsafe_allow_html=True)


def add_tooltip_css():
    """Add CSS styling for tooltips without highlighting or underline"""
    st.markdown("""
    <style>
    .tooltip {
        position: relative;
        display: inline-block;
        /* cursor: help; /* subtle hint that it's hoverable */
        color: inherit; /* keep the default text color */
        font-weight: normal;
        text-decoration: none;
    }

    .tooltip .tooltiptext {
        visibility: hidden;
        width: 300px;
        background-color: #333;
        color: #fff;
        text-align: left;
        border-radius: 6px;
        padding: 8px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -150px;
        opacity: 0;
        transition: opacity 0.3s;
        font-size: 12px;
        line-height: 1.4;
        white-space: normal;
    }

    .tooltip .tooltiptext::after {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        margin-left: -5px;
        border-width: 5px;
        border-style: solid;
        border-color: #333 transparent transparent transparent;
    }

    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)


def get_exercise_tooltips():
    """Generate tooltips dictionary directly from dictionary.py nested dicts"""
    tooltips = {}
    
    # Easy run variants
    for exercise_name, details in easy_run_variants.items():
        tooltip_parts = [details.get("Description", "")]
        if "Purpose" in details:
            tooltip_parts.append("<br><b>Purpose:</b> " + ", ".join(details["Purpose"]))
        if "Pace" in details:
            tooltip_parts.append("<br><b>Pace:</b> " + details["Pace"])
        tooltips[exercise_name.lower()] = "<br>".join(tooltip_parts)

    # Speedwork variants
    for exercise_name, details in speedwork_variants.items():
        tooltip_parts = [details.get("Description", "")]
        if "Purpose" in details:
            tooltip_parts.append("<br><b>Purpose:</b> " + ", ".join(details["Purpose"]))
        if "Pace" in details:
            tooltip_parts.append("<br><b>Pace:</b> " + details["Pace"])
        tooltips[exercise_name.lower()] = "<br>".join(tooltip_parts)

    # Cross-training variants
    for exercise_name, details in cross_training_variants.items():
        tooltip_parts = [details.get("Description", "")]
        if "Purpose" in details:
            tooltip_parts.append("<br><b>Purpose:</b> " + ", ".join(details["Purpose"]))
        if "Intensity" in details:
            tooltip_parts.append("<br><b>Intensity:</b> " + details["Intensity"])

        tooltip_html = "<br>".join(tooltip_parts)

        # Cleaned key (without parentheses)
        clean_name = exercise_name.lower().replace("(", "").replace(")", "")
        tooltips[clean_name] = tooltip_html

        # Original key (with parentheses)
        tooltips[exercise_name.lower()] = tooltip_html

    return tooltips


def render_with_tooltip(day, workout, tooltips):
    """Render a training day with a tooltip if available"""
    key = workout.lower().split("(")[0].strip()  # normalize name, drop distances in ()
    tooltip_text = tooltips.get(key, "No description available")

    st.markdown(f"""
    <div class="tooltip">{day}: {workout}
        <span class="tooltiptext">{tooltip_text}</span>
    </div>
    """, unsafe_allow_html=True)
