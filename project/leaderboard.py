import json
import os

SCORES_FILE = "scores.json"

def load_score():
    if not os.path.exists(SCORES_FILE): # Checks if the score file exists
        return []
    else:
        with open(SCORES_FILE, "r") as f:
            return json.load(f)