# Keylogger — Ethics, Simulation & Defensive Demos

**Repository purpose (educational & defensive only)**

This repository contains **safe**, non-malicious materials for learning about:
- How keystroke-related attacks are *conceptually* designed (high-level).
- How encryption (Fernet/AES) is used to protect data in transit or storage.
- Defensive techniques to detect and mitigate keylogging and exfiltration.
- Legal & ethical considerations for security research.

> IMPORTANT: This repository does **not** contain any working keylogger or code that captures real keystrokes, implements persistence, or exfiltrates real user data. It contains simulated demos and defensive tools only.

## Structure

- `SAFE_DEMO/` — simulated keystroke generator and encryption examples (safe).
- `DEFENSIVE/` — scripts that demonstrate detection techniques and logging analysis.
- `DOCS/` — ethics, methodology, and references for safe research.
- `CONTRIBUTING.md` — how to contribute responsibly.

## How to use

1. Read `DOCS/ethics_and_law.md` before running any demo.
2. Run the simulation in `SAFE_DEMO/` to learn encryption and logging data flow.
3. Explore `DEFENSIVE/` to learn detection patterns and log analysis.
4. Use the repository for educational talks, defensive tooling, or secure lab setup only.

## Example commit message
`chore: add safe simulated keystroke demo, encryption examples, and defensive detector`

## License
See `LICENSE`.
