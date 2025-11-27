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
    print(f"DEBUG: Converting {len(data)} bytes to MusicXML...")

    part = Part(id="P0", part_name=part_name, quarter_duration=quarter_duration)

    # Add initial musical attributes (time signature, key signature, clef)
    ts = TimeSignature(4, 4)  # 4/4 time
    ks = KeySignature(0, mode="major")  # C major
    clef = Clef(sign="G", line=2, staff=1, octave_change=0)  # Treble clef

    part.add(ts, start=0)
    part.add(ks, start=0)
    part.add(clef, start=0)
    print(f"DEBUG: Added time sig, key sig, clef")

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
                print(f"DEBUG: Added measure {measure_number} from {measure_start} to {measure_end}")
                measure_number += 1

            step, alter, octave = nibble_to_note(nib)
            note = Note(step=step, octave=octave, alter=alter, id=f"n{note_id}", voice=1)
            part.add(note, start=tick, end=tick + duration)
            print(f"DEBUG: Added note {note_id}: {step}{alter:+d} octave {octave} at tick {tick}")
            tick += duration
            note_id += 1
            notes_in_measure += 1

            # Reset measure counter
            if notes_in_measure >= notes_per_measure:
                notes_in_measure = 0

    print(f"DEBUG: Total notes added: {note_id}")
    print(f"DEBUG: Notes in part: {len(list(part.notes))}")
    print(f"DEBUG: Measures in part: {len(list(part.measures))}")

    # Output MusicXML as string (out=None → returns XML as bytes)
    print("DEBUG: Calling save_musicxml...")
    xml_bytes = partitura.save_musicxml(part, out=None)
    # Decode bytes to string if necessary
    if isinstance(xml_bytes, bytes):
        xml_text = xml_bytes.decode('utf-8')
    else:
        xml_text = xml_bytes
    print(f"DEBUG: Generated XML, length: {len(xml_text)} chars")
    return xml_text


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    # Any byte input — text, binary, anything:
    sample = b"Hello"
    print(f"Input: {sample}")
    xml = bytes_to_musicxml(sample)

    with open("byte_music.musicxml", "w", encoding="utf-8") as f:
        f.write(xml)

    print("Wrote byte_music.musicxml")

