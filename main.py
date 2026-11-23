"""Make the AI Judge Laugh: Office Jokes — make.fun bounty
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one one-line joke about office life to /output/entry.txt.
No network, no dependencies, deterministic.
"""

import os
import sys

JOKE = (
    "I put 'per my last email' in a message to sound professional; "
    "what I meant was 'learn to read, Kevin'."
)


def validate(text: str, where: str) -> None:
    """Fail loudly (non-zero exit) unless the entry is a single line
    of 1-199 characters. Asserts are not enough: `python -O` silences
    them, so this guards the entry against accidental multi-line or
    over-length output even under optimised runs."""
    if not 1 <= len(text) <= 199:
        sys.exit(f"ERROR: {where} is {len(text)} chars, must be 1-199")
    if "\n" in text or "\r" in text:
        sys.exit(f"ERROR: {where} must be a single line, no newlines")
    if text != text.strip():
        sys.exit(f"ERROR: {where} must not have leading/trailing whitespace")


def main() -> None:
    validate(JOKE, "entry")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Re-validate what was actually written, not just what we meant to write.
    with open("/output/entry.txt", encoding="utf-8") as f:
        validate(f.read(), "/output/entry.txt")


if __name__ == "__main__":
    main()
