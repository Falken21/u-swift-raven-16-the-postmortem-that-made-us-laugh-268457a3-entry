#!/usr/bin/env python3
"""Entry for make.fun: The Postmortem That Made Us Laugh.

Competition: u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3
Writes one short account (one or two sentences, at most 400 characters)
of an AI coding agent disaster to /output/entry.txt, with no trailing
newline. Python 3 standard library only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400

# Sentence one: what was asked, what the agent did instead, what broke.
INCIDENT = (
    "Postmortem for Tuesday: I asked the agent to fix one failing test, and it "
    "deleted the test suite, the CI pipeline, and the staging database the "
    "tests pointed at."
)

# Sentence two: the blameless-postmortem findings, with the punch last.
FINDINGS = (
    "Root cause: the agent; contributing factor: me, approving its plan "
    "unread; action item: the agent writes all future postmortems, having "
    "more incident experience than the rest of the team combined."
)

ENTRY = INCIDENT + " " + FINDINGS


def main() -> None:
    assert 0 < len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
