import partitura
from partitura.score import Part, Note, Measure, TimeSignature, KeySignature, Clef
import os

# Create test_data directory if it doesn't exist
output_dir = "test_data"
os.makedirs(output_dir, exist_ok=True)

# Create a part with proper structure
part = Part(id="P0", part_name="Test Part", quarter_duration=480)

# Add a measure with start and end times
measure = Measure(number=1)
part.add(measure, start=0, end=1920)  # 4 quarter notes = 4*480 = 1920 ticks

# Add time signature, key signature, clef
ts = TimeSignature(4, 4)
ks = KeySignature(0, mode="major")  # C major
clef = Clef(sign="G", line=2, staff=1, octave_change=0)

part.add(ts, start=0)
part.add(ks, start=0)
part.add(clef, start=0)

# Add a note (C4 quarter note)
note = Note(id="n0", step="C", octave=4, alter=0, voice=1)
part.add(note, start=0, end=480)

# Save to file
output_path = os.path.join(output_dir, "test_output.musicxml")
partitura.save_musicxml(part, output_path)
print(f"Wrote {output_path}")

# Also print what's in the part
print("\nPart contents:")
print(f"Number of notes: {len([x for x in part.notes])}")
print(f"Number of measures: {len([x for x in part.measures])}")

