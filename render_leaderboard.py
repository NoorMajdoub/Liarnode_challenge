import pandas as pd

csv_path = "leaderboard/leaderboard.csv"
md_path = "leaderboard/leaderboard.md"

# Load CSV safely
df = pd.read_csv(csv_path)

# Normalize column names
df.columns = [c.strip().lower() for c in df.columns]

# Ensure required columns exist
if "team" not in df.columns or "score" not in df.columns:
    raise ValueError(f"Invalid leaderboard.csv format. Found columns: {df.columns}")

# Convert score to float
df["score"] = df["score"].astype(float)

# Sort
df = df.sort_values(by="score", ascending=False)

# Build Markdown
md_table = ["| Team | Score |", "|------|-------|"]
for _, row in df.iterrows():
    md_table.append(f"| {row['team']} | {row['score']:.4f} |")

with open(md_path, "w") as f:
    f.write("\n".join(md_table))

print(f"Rendered {len(df)} entries to {md_path}")
