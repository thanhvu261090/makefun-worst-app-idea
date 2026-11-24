"""MoodRouter — the worst app idea ever pitched.

A tiny program with one job: hand the judge a single sentence
pitching a spectacularly useless app, after proving the sentence
is fit to be judged.
"""

import os

PITCH = (
    "MoodRouter is a $10-a-month app that asks your Wi-Fi router how it "
    "feels twice a day and texts you its mood, so you can finally stop "
    "wondering whether your internet is emotionally supported."
)

MAX_CHARS = 240


def sentence_is_sound(text: str) -> bool:
    """Return True only if the pitch clears every gate rule."""
    if not text or text != text.strip():
        return False
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if "\n" in text or "\r" in text:
        return False
    # Exactly one sentence: one full stop, sitting at the very end.
    if text.count(".") != 1 or not text.endswith("."):
        return False
    # A pitch reads as a pitch: it opens with a capital and has no
    # doubled spaces padding it out.
    if not text[0].isupper() or "  " in text:
        return False
    return True


def main() -> None:
    if not sentence_is_sound(PITCH):
        raise SystemExit(
            f"pitch failed the gate: {len(PITCH)} chars, "
            f"{PITCH.count('.')} full stops"
        )

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(PITCH)

    print(PITCH)
    print(f"({len(PITCH)} characters)")


if __name__ == "__main__":
    main()
