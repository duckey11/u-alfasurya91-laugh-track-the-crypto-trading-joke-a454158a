"""Entry: Laugh Track, the crypto trading joke contest.

The joke text is kept byte-identical to the builder's line. Reviser
judgement: it already satisfies the judge brief on all five criteria,
so no word was changed; only this guard and note were added.

Why it is kept as-is (3 beats, stakes rising each beat):
  1. "refreshed his portfolio 214 times today" - one name (Budi),
     one number (214), compulsive checking every trader recognises.
  2. "finally saw green after three months" - the long-awaited
     payoff, plus the middle beat "screenshot it to the group chat"
     raises the stakes to public embarrassment before the reveal.
  3. "the green was just his phone battery icon at 100%" - the twist
     lands at the very end as a FACT that reverses the whole line:
     the green was never his portfolio. "phone" earns its place
     (the screenshot is of his phone); "finally" carries the relief
     while "after three months" carries the duration.
Candidate edits considered and rejected: "screenshot" -> "screenshotted"
(lateral, no gain); dropping "phone" (loses the scene's grounding);
"before noticing" -> "before realising" (longer, no gain).
186 characters, inside the 1-200 gate.
"""

import os

JOKE = "Budi refreshed his portfolio 214 times today, finally saw green after three months, and screenshot it to the group chat before noticing the green was just his phone battery icon at 100%."

# Gate mirror: the sealed scorer requires UTF-8 text of 1-200 chars,
# not only whitespace, one line. Fail loudly here rather than shipping
# an entry that scores Valid 0.
assert 1 <= len(JOKE) <= 200, f"joke length {len(JOKE)} outside 1-200"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "joke must be a single line"

def main():
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
