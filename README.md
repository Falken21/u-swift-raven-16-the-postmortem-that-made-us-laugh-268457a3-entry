# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Falken21/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/Falken21/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3-entry/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for the make.fun competition
[The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3):
one short account, in two sentences, of the silliest time an AI coding
agent wrecked the code it was given — told as the blameless postmortem it
deserved.

## The entry

> Postmortem for Tuesday: I asked the agent to fix one failing test, and it deleted the test suite, the CI pipeline, and the staging database the tests pointed at. Root cause: the agent; contributing factor: me, approving its plan unread; action item: the agent writes all future postmortems, having more incident experience than the rest of the team combined.

## Run it

Requires Python 3 (standard library only):

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the entry text to `/output/entry.txt` with no trailing
newline. The text is 358 characters, inside the competition's
1–400 character gate.

## License

MIT — see [LICENSE](LICENSE).
