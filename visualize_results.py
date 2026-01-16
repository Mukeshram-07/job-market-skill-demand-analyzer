import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ----------------------------------------
# Create outputs folder if not exists
# ----------------------------------------
os.makedirs("outputs", exist_ok=True)

# ----------------------------------------
# Load data
# ----------------------------------------
df = pd.read_csv("skill_frequency_ready_for_stats.csv")

# ----------------------------------------
# 1. LINE PLOT — Skill Demand Over Weeks
# ----------------------------------------
plt.figure(figsize=(9, 5))

for skill in df["skills"].unique():
    skill_data = df[df["skills"] == skill].sort_values("time_index")
    plt.plot(
        skill_data["time_index"],
        skill_data["normalized_frequency"],
        marker="o",
        label=skill
    )

plt.xlabel("Week")
plt.ylabel("Normalized Skill Demand")
plt.title("Skill Demand Trends Over Time")
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.savefig("outputs/skill_trends_lineplot.png")
plt.show()

# ----------------------------------------
# 2. BAR PLOT — Skill Demand (Latest Week)
# ----------------------------------------
latest_week = df["time_index"].max()
latest_data = df[df["time_index"] == latest_week]

plt.figure(figsize=(8, 5))
sns.barplot(
    data=latest_data,
    x="normalized_frequency",
    y="skills"
)

plt.xlabel("Normalized Skill Demand")
plt.ylabel("Skill")
plt.title(f"Skill Demand Distribution (Week {latest_week})")
plt.tight_layout()

plt.savefig("outputs/skill_distribution_week3.png")
plt.show()

# ----------------------------------------
# 3. HEATMAP — Skills vs Weeks
# ----------------------------------------
pivot_table = df.pivot(
    index="skills",
    columns="time_index",
    values="normalized_frequency"
)

plt.figure(figsize=(8, 6))
sns.heatmap(
    pivot_table,
    annot=True,
    fmt=".2f",
    cmap="Blues"
)

plt.xlabel("Week")
plt.ylabel("Skill")
plt.title("Heatmap of Skill Demand Across Weeks")
plt.tight_layout()

plt.savefig("outputs/skill_demand_heatmap.png")
plt.show()

print("All plots generated and saved inside the 'outputs' folder.")
