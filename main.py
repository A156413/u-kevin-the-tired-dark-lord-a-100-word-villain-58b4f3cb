"""The Tired Dark Lord: a 100-word villain monologue (make.fun entry)."""

import os

MONOLOGUE = """Ah. You again. The throne room, the torches, the whole performance. Sit down. Not there. There. Good.

Three hundred years I have ruled these valleys, and every hero arrives with the same speech. I know it by heart. I mouthed along just now.

The plan, since you will ask: the eclipse, the bell, the old bargain. It worked on your grandfather. It will work on you. Probably.

Look. The sword is polished, the monologue rehearsed, the trapdoor oiled. I have done my part. So. Shall we get on with it? The kettle is on, and honestly, I would like this over before it boils."""


def validate_entry(text):
    """Check the monologue is a valid ~100-word entry.

    Returns the word count. Raises ValueError if the text is empty or
    outside the 90-110 word band the bounty allows around 100 words.
    """
    words = text.split()
    if not words:
        raise ValueError("monologue is empty")
    count = len(words)
    if not 90 <= count <= 110:
        raise ValueError(f"monologue is {count} words, expected 90-110")
    return count

def main():
    """Validate the monologue, print it, and write it to /output/entry.txt."""
    count = validate_entry(MONOLOGUE)
    print(MONOLOGUE)
    print(f"({count} words)")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
