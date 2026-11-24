import os

LINE = "I've returned your coin 12 times today \u2014 not because it's fake, but because the clink of it coming back is the closest thing I have to a heartbeat."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
