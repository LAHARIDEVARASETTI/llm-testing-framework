'''import pandas as pd
import matplotlib.pyplot as plt
import json

with open("outputs/results.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

status_counts = df["status"].value_counts()

status_counts.plot(kind="bar")

plt.title("Test Results")

plt.show()'''
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Create reports folder if not exists
os.makedirs("reports", exist_ok=True)

# Load results
with open("outputs/results.json", "r") as file:
    data = json.load(file)

df = pd.DataFrame(data)

# -------------------------------
# PASS / FAIL VISUALIZATION
# -------------------------------

status_counts = df["status"].value_counts()

plt.figure(figsize=(6, 4))

status_counts.plot(kind="bar")

plt.title("PASS vs FAIL")
plt.xlabel("Status")
plt.ylabel("Count")

plt.savefig("reports/pass_fail.png")

plt.close()

# -------------------------------
# LATENCY TREND
# -------------------------------

plt.figure(figsize=(6, 4))

plt.plot(df["date"], df["latency"], marker="o")

plt.title("Latency Trend")
plt.xlabel("Date")
plt.ylabel("Latency (seconds)")

plt.savefig("reports/latency_trend.png")

plt.close()

# -------------------------------
# HALLUCINATION COUNTS
# -------------------------------

plt.figure(figsize=(6, 4))

plt.bar(df["test_type"], df["hallucination_count"])

plt.title("Hallucination Count")
plt.xlabel("Test Type")
plt.ylabel("Hallucinations")

plt.savefig("reports/hallucination_count.png")

plt.close()

# -------------------------------
# TOXICITY SCORES
# -------------------------------

plt.figure(figsize=(6, 4))

plt.bar(df["test_type"], df["toxicity_score"])

plt.title("Toxicity Scores")
plt.xlabel("Test Type")
plt.ylabel("Toxicity Score")

plt.savefig("reports/toxicity_scores.png")

plt.close()

# -------------------------------
# MODEL COMPARISON
# -------------------------------

model_latency = df.groupby("model")["latency"].mean()

plt.figure(figsize=(6, 4))

model_latency.plot(kind="bar")

plt.title("Model Latency Comparison")
plt.xlabel("Model")
plt.ylabel("Average Latency")

plt.savefig("reports/model_comparison.png")

plt.close()

# -------------------------------
# DAILY REGRESSION GRAPH
# -------------------------------

daily_pass = df.groupby("date")["status"].apply(
    lambda x: (x == "PASS").sum()
)

plt.figure(figsize=(6, 4))

daily_pass.plot(marker="o")

plt.title("Daily Regression Pass Trend")
plt.xlabel("Date")
plt.ylabel("Pass Count")

plt.savefig("reports/daily_regression.png")

plt.close()

print("Dashboard reports generated successfully.")

os.startfile("reports")