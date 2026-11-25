"""The Tired Dark Lord: a 100-word villain monologue (make.fun entry)."""

MONOLOGUE = """Ah. You again. The throne room, the torches, the whole performance. Sit down. Not there. There. Good.

Three hundred years I have ruled these valleys, and every hero arrives with the same speech. I know it by heart. I mouthed along just now.

The plan, since you will ask: the eclipse, the bell, the old bargain. It worked on your grandfather. It will work on you. Probably.

Look. The sword is polished, the monologue rehearsed, the trapdoor oiled. I have done my part. So. Shall we get on with it? The kettle is on, and honestly, I would like this over before it boils."""

if __name__ == "__main__":
    import os

    print(MONOLOGUE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)
