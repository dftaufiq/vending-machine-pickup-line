import os

LINE = "I've returned your coin 12 times today \u2014 not because it's fake, but because the clink of it coming back is the closest thing I have to a heartbeat."

def main() -> None:
    assert 1 <= len(LINE) <= 200, f"LINE length {len(LINE)} out of range (1-200)"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the written line must be byte-identical.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt contents do not match LINE")


if __name__ == "__main__":
    main()
