import random

def generate_chart(
    song_length_seconds,
    bpm,
    lanes = 4,
    note_density = 0.5
):
    beats_total = (bpm / 60) * song_length_seconds
    current_beat = 1

    print("Length:", song_length_seconds, "seconds")
    print("BPM:", bpm)

    notes = []

    while current_beat < beats_total:
        subdivision = random.choice([1, 0.5, 0.25])
        if random.random() < note_density:
            lane = random.randint(0, lanes - 1)
            notes.append({
                "lane": lane,
                "beat": round(current_beat, 3)
            })
        current_beat += subdivision

    chart = {
        "data": {
            "title": "Auto Generated",
            "bpm": bpm,
            "offset": 0
        },
        "notes": notes
    }

    return chart
