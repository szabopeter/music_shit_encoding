# Music Shit Encoding

A bidirectional encoding-decoding system that converts arbitrary data to and from music notation formats, enabling data to be represented as printable PDF scores and optional MIDI files.

## Overview

This project provides a novel approach to data serialization by leveraging music notation as an encoding medium. Convert any data into music-xml format, generate beautiful PDF scores and MIDI files, and decode the music back to retrieve the original data.

### Important defaults
```
input.json ==> music.xml ==> shit.pdf (withOUT embedded input.json) == more_shit.pdf (WITH embedded input.json)
```

Check back:
```
more_shit.pdf ==> check_shit.pdf + check_music.xml ==> check_input.json
```


### Core Workflow

```
Arbitrary Data ↔ Music-XML ↔ PDF Scores / MIDI
```

**Encoding**: Transform arbitrary data into music-xml notation
**Generation**: Convert music-xml to printable PDF scores and optionally MIDI files
**Decoding**: Extract the original data from the music-xml representation

### Full data flow (ASCII diagram)

Below is a complete ASCII diagram of the encoding and decoding pipeline, showing the round-trip from arbitrary data to printable/audio outputs and back.

```
   +--------+       +-----------+       +-----------+       +----------------+
   |  Data  | <---> | MusicXML  | <---> | LilyPond  | <---> | PDF  +  MIDI   |
   +--------+       +-----------+       +-----------+       +----------------+
```

Notes:
- "LilyPond" is used here as the layout/engraving step that renders MusicXML into printable PDF (via LilyPond or converted formats) and can also be used to produce MIDI output.
- The pipeline is bidirectional: once the score is rendered or exported, tools can re-extract or re-serialize the MusicXML representation and decode it back to the original data.

### Alternative transmission channels (state-of-the-art / enterprise-grade)

Below are two state-of-the-art / enterprise-grade alternative transmission channels illustrating how generated artifacts might be transmitted and recovered in non-standard channels.

```
PDF (printed score)                      __
    |                                   __(.)<
    v                                   \___)
    Pigeon (physical courier)             \ /
    |                                      \/
    v
 Receiver (human) -> scan -> score-recognition (OMR) -> MusicXML -> Data


MIDI file -> FM transmitter -> radio waves (analog) -> FM receiver -> audio capture -> audio2midi/audio2score -> MusicXML -> Data

```

Notes:
- These alternative channels are presented as high-level, enterprise-oriented transmission scenarios. They demonstrate that once artifacts exist in human-readable (PDF) or audio (MIDI) forms, non-standard delivery mechanisms are possible and may be integrated into workflows.
- Practical recovery from these channels requires robust tooling and engineering: scanned PDFs need production-grade optical music recognition (OMR) and image preprocessing pipelines, while audio capture requires high-fidelity audio capture, noise resilience, and reliable audio-to-score or audio-to-MIDI conversion to approach the fidelity of the native MusicXML path.


## Features

- 🔄 **Bidirectional Conversion**: Seamlessly encode data to music and decode music back to data
- 📄 **PDF Generation**: Create printable music scores from encoded data
- 🎵 **MIDI Support**: Optional MIDI file generation for audio playback
- 🎼 **Music-XML Format**: Industry-standard notation format for maximum compatibility
- 🔐 **Data Integrity**: Ensure perfect reconstruction of original data through encode-decode cycles

## Installation

### Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

### Setup

1. Clone the repository:
```bash
git clone https://github.com/szabopeter/music_shit_encoding.git
cd music_shit_encoding
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- **partitura**: A library for handling music notation in various formats including Music-XML

For detailed information about dependencies, see `requirements.txt`.

## Usage

### Converting Bytes to MusicXML

The `bytes_to_musical_xml.py` script converts arbitrary byte data into MusicXML notation using a 4-bit encoding scheme.

#### Basic Usage

```bash
# Convert a file to MusicXML (outputs to test_data/byte_music.musicxml)
python bytes_to_musical_xml.py input.txt

# Use default "Hello" sample if no file is provided
python bytes_to_musical_xml.py

# Specify custom output path
python bytes_to_musical_xml.py input.bin -o output.musicxml

# Customize notes per measure (default: 16)
python bytes_to_musical_xml.py input.txt --notes-per-measure 8

# Set custom part name
python bytes_to_musical_xml.py input.txt --part-name "My Data"

# Combine all options
python bytes_to_musical_xml.py data.bin -o music.xml -n 8 -p "Secret Message"

# Example using the provided sample.txt test file
python bytes_to_musical_xml.py sample.txt -o test_data/sample_music.musicxml -p "Sample Text"
```

#### Command-Line Options

- `input_file`: Path to file to convert (optional, uses "Hello" if not provided)
- `-o, --output`: Output MusicXML file path (default: test_data/byte_music.musicxml)
- `-n, --notes-per-measure`: Number of notes per measure (default: 16)
- `-p, --part-name`: Name of the musical part (default: "Encoded Bytes")

#### Encoding Scheme

Each byte is split into two 4-bit nibbles, where each nibble encodes:
- **Bits 0-1**: Pitch (C, D, E, or F)
- **Bit 2**: Accidental (flat or sharp)
- **Bit 3**: Octave (4 or 5)

### Converting MusicXML back to Bytes

The `musical_xml_to_bytes.py` script decodes a MusicXML file back to the original bytes, completing the round-trip encoding/decoding cycle.

#### Basic Usage

```bash
# Decode a MusicXML file and print the result
python musical_xml_to_bytes.py encoded.musicxml

# Decode and save to a binary file
python musical_xml_to_bytes.py encoded.musicxml -o decoded.bin

# Suppress validation warnings
python musical_xml_to_bytes.py encoded.musicxml --no-validate
```

#### Command-Line Options

- `input_file`: Path to MusicXML file to decode (required)
- `-o, --output`: Output binary file path (optional, prints hex/ASCII to stdout if not specified)
- `--no-validate`: Disable warnings for unexpected note configurations

### Round-Trip Example

```bash
# Encode a file
python bytes_to_musical_xml.py input.txt -o encoded.musicxml

# Decode it back
python musical_xml_to_bytes.py encoded.musicxml -o decoded.txt

# Verify they match
diff input.txt decoded.txt
```

### Basic Example

## Project Structure

```
music_shit_encoding/
├── README.md                      # This file
├── LICENSE                        # MIT License
├── requirements.txt               # Python dependencies
├── bytes_to_musical_xml.py        # Encoder: converts arbitrary data to MusicXML
├── musical_xml_to_bytes.py        # Decoder: converts MusicXML back to data
├── sample.txt                     # Example test file
└── test_data/                     # Output directory for generated MusicXML files
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Contributors

- **Farmasi Bulcsú**
- **Szabó Péter**
- **Szász Dominik**
- **Tóth András**

---

**Note**: This project explores research-driven and enterprise-grade approaches to data encoding through music notation.




python3 bytes_to_musical_xml.py sample.txt -o test_data/sample_music.musicxml -p "Sample Text"

cd /Users/szaszdominik/programming/py/musicXML/music-shit2
/Users/szaszdominik/Downloads/lilypond-2.24.4/bin/lilypond output.ly



cd /Users/szaszdominik/programming/py/musicXML/music-shit2/Users/szaszdominik/Downloads/lilypond-2.24.4/bin/musicxml2ly \
  -o output.ly \
  test_data/sample_music.musicxml