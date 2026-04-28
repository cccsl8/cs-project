from timing import Timing
from notes import Note
import json

def load_chart(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data

def load_notes(map_path):
    map = load_chart(map_path)
    meta = map.get("data")
    bpm = meta.get("bpm", 150)
    offset = meta.get("offset", 0)

    timing = Timing(bpm)
    notes = []
    for n in map["notes"]:
        spawn_time = timing.beat_to_time(n["beat"]) + offset
        notes.append(Note(n["lane"], spawn_time))
    return notes
