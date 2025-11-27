import argparse
import partitura
from typing import Tuple, List


# -----------------------------
# musical note → 4-bit nibble
# -----------------------------
def note_to_nibble(step: str, alter: int, octave: int) -> int:
    """
    Convert (step, alter, octave) back into a 4-bit value (0–15)
    using the inverse of the encoding rules:

        pitch (2 bits): C=0, D=1, E=2, F=3
        accidental:     flat=0, sharp=1
        octave:         4=0, 5=1
    """
    # Map step to pitch bits
    step_map = {"C": 0, "D": 1, "E": 2, "F": 3}
    if step not in step_map:
        raise ValueError(f"Unknown step: {step}")
    pitch_bits = step_map[step]

    # Map alter to accidental bit
    if alter < 0:
        accidental_bit = 0  # flat
    else:
        accidental_bit = 1  # sharp (or natural treated as sharp)

    # Map octave to octave bit
    if octave == 4:
        octave_bit = 0
    elif octave == 5:
        octave_bit = 1
    else:
        raise ValueError(f"Octave must be 4 or 5 (got {octave})")

    # Reconstruct nibble: bits 3,2,1,0 = octave, accidental, pitch_bit1, pitch_bit0
    nibble = (octave_bit << 3) | (accidental_bit << 2) | pitch_bits
    return nibble & 0xF


# -----------------------------
# MusicXML → bytes
# -----------------------------
def musicxml_to_bytes(xml_path: str, validate: bool = True) -> bytes:
    """
    Convert a MusicXML file back into the original bytes by extracting notes
    and decoding their pitch/accidental/octave information.

    Parameters:
    - xml_path: Path to the MusicXML file
    - validate: If True, prints warnings for unexpected note configurations

    Returns:
    - Reconstructed bytes
    """
    # Load MusicXML file
    try:
        score = partitura.load_musicxml(xml_path)
    except Exception as e:
        raise ValueError(f"Failed to load MusicXML file '{xml_path}': {e}")

    # Get the first part (assume single-part encoding)
    if not score.parts:
        raise ValueError("No parts found in MusicXML file")

    part = score.parts[0]

    # Extract all notes in order
    notes = list(part.notes_tied)  # notes_tied groups tied notes together
    if not notes:
        raise ValueError("No notes found in the MusicXML file")

    nibbles: List[int] = []

    for note in notes:
        try:
            step = note.step
            alter = note.alter if hasattr(note, 'alter') and note.alter is not None else 0
            octave = note.octave
        except AttributeError as e:
            if validate:
                print(f"[WARN] Skipping note without required attributes: {e}")
            continue

        try:
            nibble = note_to_nibble(step, alter, octave)
            nibbles.append(nibble)
        except ValueError as e:
            if validate:
                print(f"[WARN] {e}")
            continue

    if validate and not nibbles:
        print("[WARN] No valid nibbles extracted from notes")

    # Reconstruct bytes from pairs of nibbles
    data = bytearray()
    for i in range(0, len(nibbles), 2):
        if i + 1 < len(nibbles):
            # Combine two nibbles into one byte (hi, lo)
            hi = nibbles[i]
            lo = nibbles[i + 1]
            byte_val = (hi << 4) | lo
            data.append(byte_val)
        else:
            # Odd number of nibbles; pad with zero
            if validate:
                print(f"[WARN] Odd number of nibbles ({len(nibbles)}); last nibble will be padded with 0")
            hi = nibbles[i]
            byte_val = (hi << 4) | 0
            data.append(byte_val)

    return bytes(data)


# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert MusicXML notation back to arbitrary bytes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python musical_xml_to_bytes.py byte_music.musicxml
  python musical_xml_to_bytes.py byte_music.musicxml -o output.bin
  python musical_xml_to_bytes.py byte_music.musicxml --no-validate
        """
    )
    parser.add_argument(
        "input_file",
        help="Input MusicXML file to decode"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output binary file path (default: print hex to stdout)"
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Disable warnings for unexpected note configurations"
    )

    args = parser.parse_args()

    # Decode MusicXML to bytes
    try:
        recovered_bytes = musicxml_to_bytes(args.input_file, validate=not args.no_validate)
        print(f"Decoded {len(recovered_bytes)} bytes from {args.input_file}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    # Output
    if args.output:
        try:
            with open(args.output, "wb") as f:
                f.write(recovered_bytes)
            print(f"Wrote {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            exit(1)
    else:
        # Print as hex and ASCII
        print(f"Decoded data (hex): {recovered_bytes.hex().upper()}")
        try:
            print(f"Decoded data (ASCII): {recovered_bytes.decode('utf-8', errors='replace')}")
        except Exception:
            pass
