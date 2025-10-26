"""
simulated_keystrokes.py
A safe demo that generates synthetic keystroke events and writes them to a file.
Purpose: learn timestamping, logging format, and encryption pipeline WITHOUT capturing real input.
"""

import time
import json
import random
import string
from datetime import datetime

def generate_random_keystroke():
    # generate a random printable character to simulate a keystroke
    ch = random.choice(string.ascii_letters + string.digits + " ,.;'[]")
    return ch

def simulate_session(num_events=50, out_file="simulated_session.jsonl"):
    with open(out_file, "w", encoding="utf-8") as f:
        for i in range(num_events):
            event = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "event_id": i+1,
                "simulated_key": generate_random_keystroke()
            }
            f.write(json.dumps(event) + "\n")
            time.sleep(0.03)  # small delay to simulate typing speed

if __name__ == "__main__":
    print("Running simulated keystroke generator (safe demo).")
    simulate_session()
    print("Simulation complete. Output: simulated_session.jsonl")
