import os

import partitura
from partitura.score import Part, Note, Measure, TimeSignature, KeySignature, Clef
from typing import Tuple


# -----------------------------
# 4-bit nibble → musical note
# -----------------------------
def nibble_to_note(n: int) -> Tuple[str, int, int]:
    """
    Convert a 4-bit value (0–15) into (step, alter, octave)
    using your encoding rules:

        pitch (2 bits): 0=C, 1=D, 2=E, 3=F
        accidental:     0=flat, 1=sharp
        octave:         0=4,    1=5
    """
    if not 0 <= n <= 0xF:
        raise ValueError("Nibble must be 0–15")

    # bits 0–1
    pitch_bits = n & 0b11
    # bit 2
    accidental_bit = (n >> 2) & 0b1
    # bit 3
    octave_bit = (n >> 3) & 0b1

    # C, D, E, F
    steps = ["C", "D", "E", "F"]
    step = steps[pitch_bits]

    # accidental: flat = -1, sharp = +1
    alter = -1 if accidental_bit == 0 else +1

    # octave 4 or 5
    octave = 4 + octave_bit

    return step, alter, octave


# -----------------------------
# bytes → MusicXML
# -----------------------------
def bytes_to_musicxml(data: bytes,
                      quarter_duration: int = 480,
                      part_name: str = "Encoded Bytes",
                      notes_per_measure: int = 16) -> str:
    """
    Convert arbitrary bytes into a sequence of musical notes
    encoded using 4-bit chunks, and output MusicXML as text.

    Parameters:
    - notes_per_measure: Number of notes per measure (default 16 = 4 bars of 4/4 time)
    """

    part = Part(id="P0", part_name=part_name, quarter_duration=quarter_duration)

    # Add initial musical attributes (time signature, key signature, clef)
    ts = TimeSignature(4, 4)  # 4/4 time
    ks = KeySignature(0, mode="major")  # C major
    clef = Clef(sign="G", line=2, staff=1, octave_change=0)  # Treble clef

    part.add(ts, start=0)
    part.add(ks, start=0)
    part.add(clef, start=0)

    tick = 0
    duration = quarter_duration  # each note is a quarter note
    note_id = 0
    measure_number = 1
    notes_in_measure = 0

    for b in data:
        # split byte → 2 nibbles
        hi = (b >> 4) & 0xF   # high nibble
        lo = b & 0xF          # low nibble

        for nib in (hi, lo):
            # Start a new measure when needed
            if notes_in_measure == 0:
                measure_start = tick
                measure_end = tick + (notes_per_measure * duration)
                measure = Measure(number=measure_number)
                part.add(measure, start=measure_start, end=measure_end)
                measure_number += 1

            step, alter, octave = nibble_to_note(nib)
            note = Note(step=step, octave=octave, alter=alter, id=f"n{note_id}", voice=1)
            part.add(note, start=tick, end=tick + duration)
            tick += duration
            note_id += 1
            notes_in_measure += 1

            # Reset measure counter
            if notes_in_measure >= notes_per_measure:
                notes_in_measure = 0

    # Output MusicXML as string (out=None → returns XML as bytes)
    xml_bytes = partitura.save_musicxml(part, out=None)
    # Decode bytes to string if necessary
    if isinstance(xml_bytes, bytes):
        xml_text = xml_bytes.decode('utf-8')
    else:
        xml_text = xml_bytes
    return xml_text


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Create test_data directory if it doesn't exist
    output_dir = "test_data"
    os.makedirs(output_dir, exist_ok=True)

    # Any byte input — text, binary, anything:
    sample = b"Hello"
    xml = bytes_to_musicxml(sample)

    output_path = os.path.join(output_dir, "byte_music.musicxml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"Wrote {output_path}")
