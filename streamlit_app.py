# streamlit_app.py
# Lightweight, Streamlit-Cloud-safe version for AI in Education Dashboard

import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="AI in Education Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📘 AI in Education – Executive Analytics Dashboard")
st.caption("Synthetic data | Decision-focused | Streamlit Cloud optimized")

# --------------------------------------------------
# DATA LOADERS (SEPARATE + CACHED)
# --------------------------------------------------
@st.cache_data
def load_professor_data():
    return pd.read_csv("data/ai_education_professor_data.csv")

@st.cache_data
def load_student_data():
    return pd.read_csv("data/ai_education_student_data.csv")

@st.cache_data
def load_combined_data():
    return pd.read_csv("data/ai_education_combined_data.csv")

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------
page = st.sidebar.radio(
    "Navigate",
    [
        "Executive Overview",
        "Student Insights",
        "Professor Insights",
        "AI Adoption & Outcomes"
    ]
)

# --------------------------------------------------
# EXECUTIVE OVERVIEW (LIGHTWEIGHT FIRST LOAD)
# --------------------------------------------------
if page == "Executive Overview":
    df = load_combined_data()

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Institutions", df["institution_id"].nunique())
    col2.metric("Total Students", df["student_id"].nunique())
    col3.metric("Avg AI Adoption (%)", round(df["ai_usage_level"].mean(), 1))

    st.subheader("AI Usage Distribution")
    fig = px.histogram(
        df,
        x="ai_usage_level",
        nbins=20,
        title="Distribution of AI Usage Across Institutions"
    )
    st.plotly_chart(fig, use_container_width=True)

# --------------------------------------------------
# STUDENT INSIGHTS
# --------------------------------------------------
elif page == "Student Insights":
    df = load_student_data()

    st.subheader("Student Engagement vs Performance")
    fig = px.scatter(
        df,
        x="ai_tool_usage_hours",
        y="academic_performance_score",
        color="education_level",
        title="AI Tool Usage vs Academic Performance"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Performance by Education Level")
    fig2 = px.box(
        df,
        x="education_level",
        y="academic_performance_score",
        title="Academic Performance Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# PROFESSOR INSIGHTS
# --------------------------------------------------
elif page == "Professor Insights":
    df = load_professor_data()

    st.subheader("AI Adoption by Teaching Experience")
    fig = px.bar(
        df,
        x="years_of_experience",
        y="ai_adoption_score",
        title="AI Adoption vs Teaching Experience",
        labels={"years_of_experience": "Years of Experience"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Faculty Perception of AI Effectiveness")
    fig2 = px.histogram(
        df,
        x="perceived_ai_effectiveness",
        nbins=10,
        title="Perceived AI Effectiveness"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# AI ADOPTION & OUTCOMES
# --------------------------------------------------
elif page == "AI Adoption & Outcomes":
    df = load_combined_data()

    st.subheader("AI Usage vs Student Outcomes")
    fig = px.line(
        df.sort_values("ai_usage_level"),
        x="ai_usage_level",
        y="average_student_outcome",
        title="Relationship Between AI Usage and Outcomes"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Institution Type Comparison")
    fig2 = px.bar(
        df,
        x="institution_type",
        y="average_student_outcome",
        title="Outcomes by Institution Type"
    )
    st.plotly_chart(fig2, use_container_width=True)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.markdown("---")
st.caption("This dashboard uses synthetic data generated for academic demonstration purposes only.")
