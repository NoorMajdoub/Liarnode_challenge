import pandas as pd
import sys

def validate_submission(submission_file):
    df = pd.read_csv(submission_file)

    # basic checks
    if "cell_type" not in df.columns:
        raise ValueError("Missing column: cell_type")

    if df.isnull().any().any():
        raise ValueError("Submission contains NaNs")

    print("VALID")

def score_submission(submission_file, truth_file):
    from sklearn.metrics import accuracy_score  # lazy import

    submission = pd.read_csv(submission_file)
    truth = pd.read_csv(truth_file)

    score = accuracy_score(truth["cell_type"], submission["cell_type"])
    print(f"SCORE={score:.4f}")

if __name__ == "__main__":
    if sys.argv[1] == "--validate-only":
        # validate all csvs in submissions/
        import glob
        for file in glob.glob("submissions/*.csv"):
            validate_submission(file)
    else:
        submission_file = sys.argv[1]
        truth_file = sys.argv[2]
        score_submission(submission_file, truth_file)
