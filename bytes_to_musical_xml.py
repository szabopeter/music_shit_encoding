import os
import argparse

import partitura
from partitura.score import Part, Note, Measure, TimeSignature, KeySignature, Clef
from typing import Tuple, List


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
                      notes_per_measure: int = 16,
                      validate: bool = True) -> str:
    """
    Convert arbitrary bytes into a sequence of musical notes encoded using 4-bit chunks.

    Parameters:
    - quarter_duration: Tick length of one quarter note (must be > 0)
    - part_name: Name for the part
    - notes_per_measure: Positive number of notes per measure
    - validate: If True, prints warnings for any zero-length notes/measures
    """
    if quarter_duration <= 0:
        raise ValueError(f"quarter_duration must be > 0 (got {quarter_duration})")
    if notes_per_measure <= 0:
        raise ValueError(f"notes_per_measure must be > 0 (got {notes_per_measure})")

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

    if validate:
        # Avoid arithmetic on partitura's internal time objects; only compare if numeric.
        zero_note_ids: List[str] = []
        for n in part.notes:
            start = getattr(n, 'start', None)
            end = getattr(n, 'end', None)
            if isinstance(start, (int, float)) and isinstance(end, (int, float)):
                if end <= start:
                    zero_note_ids.append(getattr(n, 'id', 'unknown'))
        zero_measures = []
        for m in part.measures:
            m_start = getattr(m, 'start', None)
            m_end = getattr(m, 'end', None)
            if isinstance(m_start, (int, float)) and isinstance(m_end, (int, float)):
                if m_end <= m_start:
                    zero_measures.append(m)
        if zero_note_ids:
            print(f"[WARN] Zero or negative duration notes detected: {zero_note_ids}")
        if zero_measures:
            print(f"[WARN] Zero-length measures detected: {[getattr(m,'number','?') for m in zero_measures]}")

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
    parser = argparse.ArgumentParser(
        description="Convert arbitrary bytes to MusicXML notation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python bytes_to_musical_xml.py input.json
  python bytes_to_musical_xml.py input.json -o music.xml
  python bytes_to_musical_xml.py input.json --notes-per-measure 8 -o music.xml
        """
    )
    parser.add_argument(
        "input_file",
        nargs="?",
        help="Input file to convert (if not provided, uses 'Hello' as sample)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output MusicXML file path (default: music.xml)"
    )
    parser.add_argument(
        "-n", "--notes-per-measure",
        type=int,
        default=16,
        help="Number of notes per measure (default: 16)"
    )
    parser.add_argument(
        "-p", "--part-name",
        default="Encoded Bytes",
        help="Name of the musical part (default: 'Encoded Bytes')"
    )
    parser.add_argument("--no-validate", action="store_true", help="Disable zero-duration sanity checks")

    args = parser.parse_args()

    # Create test_data directory if it doesn't exist (retained for backward compatibility)
    output_dir = "test_data"
    os.makedirs(output_dir, exist_ok=True)

    # Read input data
    if args.input_file:
        try:
            with open(args.input_file, "rb") as f:
                data = f.read()
            print(f"Read {len(data)} bytes from {args.input_file}")
        except FileNotFoundError:
            print(f"Error: File '{args.input_file}' not found")
            exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            exit(1)
    else:
        # Default sample
        data = b"Hello"
        print("No input file provided, using sample: 'Hello'")

    # Convert to MusicXML
    xml = bytes_to_musicxml(
        data,
        part_name=args.part_name,
        notes_per_measure=args.notes_per_measure,
        validate=not args.no_validate
    )

    # Determine output path
    if args.output:
        output_path = args.output
    else:
        output_path = "music.xml"

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"Wrote {output_path}")
