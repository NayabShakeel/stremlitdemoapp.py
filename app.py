import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to convert Celsius to Kelvin
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Streamlit app
st.title("Temperature Converter")

option = st.selectbox(
    "Choose the conversion option:",
    ("Celsius to Fahrenheit", "Fahrenheit to Celsius", "Celsius to Kelvin", "Kelvin to Celsius")
)

if option == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:")
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"{celsius} °C is equal to {fahrenheit} °F")

elif option == "Fahrenheit to Celsius":
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"{fahrenheit} °F is equal to {celsius} °C")

elif option == "Celsius to Kelvin":
    celsius = st.number_input("Enter temperature in Celsius:")
    if st.button("Convert"):
        kelvin = celsius_to_kelvin(celsius)
        st.success(f"{celsius} °C is equal to {kelvin} K")

elif option == "Kelvin to Celsius":
    kelvin = st.number_input("Enter temperature in Kelvin:")
    if st.button("Convert"):
        celsius = kelvin_to_celsius(kelvin)
        st.success(f"{kelvin} K is equal to {celsius} °C")
