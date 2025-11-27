import partitura
from partitura.score import Part, Note, Measure, TimeSignature, KeySignature, Clef
import os

# Create test_data directory if it doesn't exist
output_dir = "test_data"
os.makedirs(output_dir, exist_ok=True)

# Create a part
part = Part(id="P0", part_name="Test", quarter_duration=480)

# Add time signature, key signature, clef
ts = TimeSignature(4, 4)
ks = KeySignature(0, mode="major")
clef = Clef(sign="G", line=2, staff=1, octave_change=0)

part.add(ts, start=0)
part.add(ks, start=0)
part.add(clef, start=0)

# Add measure
measure = Measure(number=1)
part.add(measure, start=0, end=1920)

# Add a few notes for "Hello" (H=72, e=101, l=108, l=108, o=111)
# H = 0x48 = 0100 1000 = nibbles 4, 8
# e = 0x65 = 0110 0101 = nibbles 6, 5
# First nibble 4 = 0100 = pitch 0 (C), accidental 1 (sharp), octave 0 (4)
note1 = Note(step="C", octave=4, alter=1, id="n0", voice=1)
part.add(note1, start=0, end=480)

# Second nibble 8 = 1000 = pitch 0 (C), accidental 0 (flat), octave 1 (5)
note2 = Note(step="C", octave=5, alter=-1, id="n1", voice=1)
part.add(note2, start=480, end=960)

print("Notes in part:", len(list(part.notes)))
print("Measures in part:", len(list(part.measures)))

# Save
xml_bytes = partitura.save_musicxml(part, out=None)
xml_text = xml_bytes.decode('utf-8') if isinstance(xml_bytes, bytes) else xml_bytes

output_path = os.path.join(output_dir, "debug_output.musicxml")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(xml_text)

print(f"Wrote {output_path}")
print("\nFirst 1000 chars of XML:")
print(xml_text[:1000])

