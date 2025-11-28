# Music Shít Encoding

A bidirectional encoding-decoding system that converts arbitrary data to and from music notation formats, enabling data to be represented as printable PDF scores and optional MIDI files.

## Overview

This project provides a novel approach to data serialization by leveraging music notation as an encoding medium. Convert any data into music-xml format, generate beautiful PDF scores and MIDI files, and decode the music back to retrieve the original data.

### Important defaults
```
input.json ==> music.xml ==> shít.pdf (withOUT embedded input.json) == more_shít.pdf (WITH embedded input.json)
```

Check back:
```
more_shít.pdf ==> check_music.xml ==> check_input.json
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
git clone https://github.com/szabopeter/music_shít_encoding.git
cd music_shít_encoding
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- **partitura**: A library for handling music notation in various formats including Music-XML
- **pikepdf**: Required for PDF attachment operations

For detailed information about dependencies, see `requirements.txt`.

## Usage

### Streamlined Workflow

```powershell
# 1) Encode bytes to MusicXML (from repo root)
python bytes_to_musical_xml.py sample.txt -o test_data/sample_music.musicxml -p "Sample Text"

# 2) Convert MusicXML to LilyPond (run from C:\DevTools\lilypond-2.24.4)
cd C:\DevTools\lilypond-2.24.4
bin\musicxml2ly.exe -o output.ly C:\Repos\music_shít_encoding\test_data\sample_music.musicxml

# 3) Render PDF (still in C:\DevTools\lilypond-2.24.4)
bin\lilypond.exe -o shít output.ly  # produces shít.pdf

# 4) Attach MusicXML to PDF (from repo root)
cd C:\Repos\music_shít_encoding
Copy-Item .\test_data\sample_music.musicxml .\music.xml -Force
python add_attachment.py  # -> more_shít.pdf

# 5) Remove attachment and extract MusicXML (from repo root)
python remove_attachment.py  # -> check_shít.pdf and check_music.xml

# 6) Decode MusicXML back to bytes (from repo root)
python musical_xml_to_bytes.py check_music.xml -o decoded_sample.txt
```

### Command-Line Options

Encoder (`bytes_to_musical_xml.py`):
- `input_file`: Path to file to convert (optional, uses "Hello" if not provided)
- `-o, --output`: Output MusicXML file path (default: music.xml)
- `-n, --notes-per-measure`: Number of notes per measure (default: 16)
- `-p, --part-name`: Name of the musical part (default: "Encoded Bytes")

Decoder (`musical_xml_to_bytes.py`):
- `input_file`: Path to MusicXML file to decode (required)
- `-o, --output`: Output file path (optional)

## Project Structure

```
music_shít_encoding/
├── README.md                      # This file
├── LICENSE                        # MIT License
├── requirements.txt               # Python dependencies
├── bytes_to_musical_xml.py        # Encoder: converts arbitrary data to MusicXML
├── musical_xml_to_bytes.py        # Decoder: converts MusicXML back to data
├── add_attachment.py              # Attaches music.xml to shít.pdf -> more_shít.pdf
├── remove_attachment.py           # Extracts from more_shít.pdf -> check_music.xml
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

cd /Users/szaszdominik/programming/py/musicXML/music-shít2
/Users/szaszdominik/Downloads/lilypond-2.24.4/bin/lilypond output.ly



cd /Users/szaszdominik/programming/py/musicXML/music-shít2/Users/szaszdominik/Downloads/lilypond-2.24.4/bin/musicxml2ly \
  -o output.ly \
  test_data/sample_music.musicxml










python3 bytes_to_musical_xml.py input.json -o test_data/sample_music.musicxml -p "Sample Text"                          
python3 main.py
python3 add_attachment.py
python3 remove_attachment.py 
python musical_xml_to_bytes.py output.xml -o decoded_sample.txt