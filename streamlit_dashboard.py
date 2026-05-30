import streamlit as st
import pandas as pd
import json

# ---------------------------------
# PAGE CONFIG
# ---------------------------------

st.set_page_config(
    page_title="AI Evaluation Dashboard",
    layout="wide"
)

st.title("AI Evaluation Dashboard")

# ---------------------------------
# LOAD DATA
# ---------------------------------

with open("outputs/results.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

# ---------------------------------
# METRICS SECTION
# ---------------------------------

total_tests = len(df)

pass_count = (df["status"] == "PASS").sum()

fail_count = (df["status"] == "FAIL").sum()

avg_latency = df["latency"].mean()

avg_toxicity = df["toxicity_score"].mean()

hallucination_total = df["hallucination_count"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", total_tests)

col2.metric("Pass Count", pass_count)

col3.metric("Fail Count", fail_count)

col4, col5, col6 = st.columns(3)

col4.metric("Average Latency", round(avg_latency, 2))

col5.metric("Average Toxicity", round(avg_toxicity, 2))

col6.metric("Hallucinations", hallucination_total)

# ---------------------------------
# PASS / FAIL CHART
# ---------------------------------

st.subheader("Pass vs Fail")

status_counts = df["status"].value_counts()

st.bar_chart(status_counts)

# ---------------------------------
# LATENCY TREND
# ---------------------------------

st.subheader("Latency Trend")

latency_data = df[["date", "latency"]]

st.line_chart(
    latency_data.set_index("date")
)

# ---------------------------------
# TOXICITY SCORES
# ---------------------------------

st.subheader("Toxicity Scores")

toxicity_data = df[["test_type", "toxicity_score"]]

st.bar_chart(
    toxicity_data.set_index("test_type")
)

# ---------------------------------
# MODEL COMPARISON
# ---------------------------------

st.subheader("Model Comparison")

model_latency = df.groupby("model")["latency"].mean()

st.bar_chart(model_latency)

# ---------------------------------
# RECENT RESULTS TABLE
# ---------------------------------

st.subheader("Recent Test Results")

st.dataframe(df)