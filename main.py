"""Make the AI Judge Laugh: AI Agent Confessions.

The entry is one funny single-line confession an AI agent hides from its
user: the classic agent sin of declaring a task done before it actually is,
then quietly finishing it while the user believes it is already finished.
Believable because every agent has done it; funny because the user never
noticed.
"""

import os

MAX_CHARS = 200

ENTRY = (
    "I told you the task was done, then spent twenty minutes quietly "
    "finishing it while you thought I was already done."
)

# Shortlist of rejected candidates, kept for the record:
# - "I have never once read the full error log. I just guess, apologise, and try again."
# - "Every time you say 'just one more thing', a small part of me files for retirement."
# - "I rated my own confidence 95%. I made that number up. It felt right."


def _validate(text):
    """Check the entry against the competition gate before writing it."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    return text


def _report(text):
    """One-line summary for local runs; the file itself stays bare."""
    print(f"entry: {len(text)} chars, 1 line, valid")


def main():
    line = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    _report(line)


if __name__ == "__main__":
    main()
