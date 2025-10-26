"""
detector_simulator.py
A defensive example that scans a log of running processes (simulated) and flags suspicious indicators.
Purpose: learn detection patterns; does NOT interact with OS or processes.
"""

import json

# Example simulated processes log file (processes.jsonl)
# Each line example: {"pid": 1234, "exe": "python.exe", "cmdline": "python simulate.py", "user": "user1"}

SUSPICIOUS_KEYWORDS = ["keylog", "logger", "persistence", "autorun", "startup", "hidden"]

def scan_process_log(path="processes.jsonl"):
    flagged = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            entry = json.loads(line)
            cmd = entry.get("cmdline", "").lower()
            exe = entry.get("exe", "").lower()
            if any(k in cmd for k in SUSPICIOUS_KEYWORDS) or any(k in exe for k in SUSPICIOUS_KEYWORDS):
                flagged.append(entry)
    return flagged

if __name__ == "__main__":
    print("This is a detector simulator. Create a simulated 'processes.jsonl' and run the script.")
    flagged = scan_process_log()
    if flagged:
        print("Flagged entries:")
        for e in flagged:
            print(json.dumps(e, indent=2))
    else:
        print("No suspicious simulated processes found.")
