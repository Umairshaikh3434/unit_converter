import streamlit as st
#Functionality
def distance_converter(from_unit,to_unit,value):
    units = {
        "Meters": 1,
        "Kilometers": 1000,
        "Feet": 0.3048,
        "Miles": 1609.34,
    }
    results = value * units[from_unit] / units[to_unit]
    return results

def temperature_converter(from_unit,to_unit,value):
     if from_unit == "Celsius" and to_unit == "Fahreneit":
        result = (value * 9/5) + 32
     elif from_unit == "Fahreneit" and to_unit == "Celsius":
        result = (value - 32) * 5/9
     else:
        result = value
     return result 

def weight_converter(from_unit,to_unit,value):
    units = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495,
    }
    results = value * units[from_unit] / units[to_unit]
    return results

def pressure_converter(from_unit,to_unit,value):
    units = {
        "Pascals": 1,
        "Hectopascals": 100,
        "Kilopascals": 1000,
        "Bar": 100000,
    }
    results = value * units[from_unit] / units[to_unit]
    return results    
           

#ui
st.title("Unit Converter")

category = st.selectbox("Select Category", ["Distance", "Temperature", "Weight", "Pressure"])

if category == "Distance":
    from_unit = st.selectbox("From",["Meters", "Kilometers", "Feet", "Miles"])
    to_unit = st.selectbox("To",["Meters", "Kilometers", "Feet", "Miles"])
    value = st.number_input("Enter Value")
    if st.button("Convert"):
       result = distance_converter(from_unit,to_unit,value)
       st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

elif category == "Temperature":
        from_unit = st.selectbox("From",["Celsius", "Fahreneit"])
        to_unit = st.selectbox("To",["Celsius", "Fahreneit"])
        value = st.number_input("Enter Value")
        if st.button("Convert"):
          result = temperature_converter(from_unit,to_unit,value)
          st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
elif category == "Weight":
        from_unit = st.selectbox("From",["Kilograms", "Grams", "Pounds", "Ounces"])
        to_unit = st.selectbox("To",["Kilograms", "Grams", "Pounds", "Ounces"])
        value = st.number_input("Enter Value")
        if st.button("Convert"):
          result = weight_converter(from_unit,to_unit,value)
          st.success(f"{value} {from_unit} = {result:.2f} {to_unit}") 
elif category == "Pressure":
        from_unit = st.selectbox("From",["Pascals", "Hectopascals", "Kilopascals", "Bar"])
        to_unit = st.selectbox("To",["Pascals", "Hectopascals", "Kilopascals", "Bar"])
        value = st.number_input("Enter Value")
        if st.button("Convert"):
          result = pressure_converter(from_unit,to_unit,value)
          st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")             
