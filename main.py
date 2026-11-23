"""Make the AI Judge Laugh: Office Jokes — make.fun bounty
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes one one-line joke about office life to /output/entry.txt.
No network, no dependencies, deterministic.
"""

import os

JOKE = (
    "I put 'per my last email' in a message to sound professional; "
    "what I meant was 'learn to read, Kevin'."
)


def main() -> None:
    # The entry must be 1-199 Unicode code points, one line, not blank.
    assert 1 <= len(JOKE) <= 199
    assert "\n" not in JOKE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
