import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Healthcare Operations Dashboard", layout="wide")

st.title("Healthcare Operations Dashboard")
st.write("This dashboard tracks patient volume, wait times, bed usage, staffing, satisfaction, and readmissions.")

data = pd.DataFrame({
    "Department": ["ER", "Clinic", "Surgery", "Pediatrics", "Behavioral Health"],
    "Patients Seen": [120, 95, 40, 70, 35],
    "Average Wait Time": [45, 30, 25, 20, 50],
    "Beds Occupied": [85, 60, 40, 55, 30],
    "Available Beds": [15, 25, 10, 20, 8],
    "Staff Scheduled": [25, 18, 12, 15, 10],
    "Patient Satisfaction": [78, 85, 90, 88, 72],
    "Readmissions": [12, 8, 5, 6, 10]
})

total_patients = data["Patients Seen"].sum()
avg_wait = round(data["Average Wait Time"].mean(), 1)
avg_satisfaction = round(data["Patient Satisfaction"].mean(), 1)
total_readmissions = data["Readmissions"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Patients Seen", total_patients)
col2.metric("Average Wait Time", f"{avg_wait} min")
col3.metric("Patient Satisfaction", f"{avg_satisfaction}%")
col4.metric("Total Readmissions", total_readmissions)

st.subheader("Dashboard Data")
st.dataframe(data)

st.subheader("Patients Seen by Department")
fig1 = px.bar(data, x="Department", y="Patients Seen", title="Patient Volume")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Average Wait Time by Department")
fig2 = px.bar(data, x="Department", y="Average Wait Time", title="Wait Times")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Bed Usage")
fig3 = px.bar(
    data,
    x="Department",
    y=["Beds Occupied", "Available Beds"],
    title="Occupied vs Available Beds",
    barmode="group"
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Patient Satisfaction")
fig4 = px.line(data, x="Department", y="Patient Satisfaction", markers=True, title="Satisfaction Scores")
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Readmissions by Department")
fig5 = px.pie(data, names="Department", values="Readmissions", title="Readmission Breakdown")
st.plotly_chart(fig5, use_container_width=True)

st.subheader("Summary")
st.write("""
This healthcare dashboard helps administrators quickly review hospital performance.
It shows patient volume, wait times, bed usage, staffing, satisfaction scores, and readmissions.
These visuals can help identify problems such as long wait times, low satisfaction, or high readmission rates.
""")
