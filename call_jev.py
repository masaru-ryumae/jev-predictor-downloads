"""
call_jev.py — Call the real TypeSafe System One API directly, no playground UI.

From The Engineering Dad, "You Do Not Need To Know How To Code To Build A
College Admissions Predictor Tonight"
https://theengineeringdad.substack.com/p/the-easiest-first-build

Read the free section of that article for the five-minute version. The paid
section explains what request_template.json's fields mean, how the Common
Data Set parsing works, and the real failure modes hit building this, the
men/women wording variant, the fillable-form trap, and a false-positive bug.
That context is what makes this script actually usable instead of just code
that runs.

Loads TYPESAFE_API_KEY from .env (never printed, never logged). Builds the
request body per the documented shape (https://docs.typesafe.ai/api.md):
POST https://api.typesafe.ai/v1/systemone, Authorization: Bearer <key>,
body = {state, model, questions}.
"""

import os
import sys
import json
import requests
from pathlib import Path
from dotenv import dotenv_values

ROOT = Path(__file__).parent
API_URL = "https://api.typesafe.ai/v1/systemone"


def get_api_key():
    config = dotenv_values(ROOT / ".env")
    key = config.get("TYPESAFE_API_KEY") or os.environ.get("TYPESAFE_API_KEY")
    if not key:
        raise RuntimeError("TYPESAFE_API_KEY not found in .env or environment")
    return key


def call_jev(state, questions, model="jev-latest"):
    key = get_api_key()
    resp = requests.post(
        API_URL,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        json={"state": state, "model": model, "questions": questions},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python call_jev.py <path-to-request.json>")
        print("  request.json must contain: {\"state\": {...}, \"questions\": {...}}")
        sys.exit(1)

    payload = json.loads(Path(sys.argv[1]).read_text())
    result = call_jev(payload["state"], payload["questions"])
    print(json.dumps(result, indent=2))
