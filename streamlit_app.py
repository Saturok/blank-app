import streamlit as st

# This sets the title of the webpage
st.title("Elise's Shift Pay Calculator")
st.write("Enter the hours worked for the week to calculate total pay.")

# 1. Collect the pay rate using a number input box
base_rate = st.number_input("Enter normal hourly rate ($):", min_value=0.0, value=25.0, step=0.50)

# 2. Collect hours using sliders or number boxes
st.subheader("Shift Hours")
normal_hrs = st.number_input("Normal (daytime) hours:", min_value=0.0, step=0.5)
night_hrs = st.number_input("Night shift hours (6pm-8am):", min_value=0.0, step=0.5)
weekend_hrs = st.number_input("Weekend hours:", min_value=0.0, step=0.5)

# 3. Calculations (The logic stays the same!)
pay_normal = normal_hrs * base_rate
pay_night = night_hrs * (base_rate * 1.15)
pay_weekend = weekend_hrs * (base_rate * 1.5)

total_hours = normal_hrs + night_hrs + weekend_hrs
total_pay = pay_normal + pay_night + pay_weekend

# 4. Display the results on the webpage
st.divider()
st.header(f"Total Pay: ${total_pay:.2f}")

# Using columns to make it look like a real app
col1, col2, col3 = st.columns(3)
col1.metric("Normal Pay", f"${pay_normal:.2f}")
col2.metric("Night Loading", f"${pay_night:.2f}")
col3.metric("Weekend Pay", f"${pay_weekend:.2f}")

st.info(f"Total hours tracked: {total_hours}")
