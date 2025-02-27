# Imports
import streamlit as st

# Set up Streamlit App
st.set_page_config(page_title="Unit Converter 🔄", page_icon="🔄", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        body {
            color: white;
            background-color: #1f1f1f;
        }
        .stApp {
            background-color: #252525;
        }
        h1 {
            text-align: center;
            color: #00ccff;
        }
        .stSelectbox, .stTextInput, .stNumberInput, .stRadio {
            background-color: #2a2a2a;
            color: white;
        }
        .stButton>button {
            background-color: #ff7b00;
            color: white;
            border-radius: 10px;
            width: 100%;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #ff9f33;
        }
        .stSuccess {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            color: #00ff99;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Unit Converter 🔄</h1>", unsafe_allow_html=True)
st.write("Convert Length, Weight, and Temperature with a sleek and modern interface! 🎨")

# Dropdown for conversion types
conversion_type = st.selectbox("Select conversion type:", ["Length", "Weight", "Temperature"])

# Dictionary for conversions
conversion_factors = {
    "Length": {
        "Meter": 1,
        "Kilometer": 0.001,
        "Centimeter": 100,
        "Millimeter": 1000,
        "Mile": 0.000621371,
        "Yard": 1.09361,
        "Foot": 3.28084,
        "Inch": 39.3701
    },
    "Weight": {
        "Gram": 1,
        "Kilogram": 0.001,
        "Milligram": 1000,
        "Pound": 0.00220462,
        "Ounce": 0.035274
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}

# Conversion Logic
if conversion_type == "Temperature":
    # Temperature Conversion
    col1, col2 = st.columns(2)
    with col1:
        temp_unit_from = st.selectbox("From:", list(conversion_factors["Temperature"].keys()))
    with col2:
        temp_unit_to = st.selectbox("To:", list(conversion_factors["Temperature"].keys()))

    temp_value = st.number_input("Enter value:", format="%.2f")

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    if st.button("Convert 🔄"):
        result = convert_temperature(temp_value, temp_unit_from, temp_unit_to)
        st.markdown(f"<p class='stSuccess'>Converted Value: {result:.2f} {temp_unit_to} 🎯</p>", unsafe_allow_html=True)

else:
    # Length & Weight Conversion
    col1, col2 = st.columns(2)
    with col1:
        unit_from = st.selectbox("From:", list(conversion_factors[conversion_type].keys()))
    with col2:
        unit_to = st.selectbox("To:", list(conversion_factors[conversion_type].keys()))

    value = st.number_input("Enter value:", format="%.2f")

    if st.button("Convert 🔄"):
        result = (value / conversion_factors[conversion_type][unit_from]) * conversion_factors[conversion_type][unit_to]
        st.markdown(f"<p class='stSuccess'>Converted Value: {result:.4f} {unit_to} 🎯</p>", unsafe_allow_html=True)
