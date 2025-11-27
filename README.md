# Music Shit Encoding

A bidirectional encoding-decoding system that converts arbitrary data to and from music notation formats, enabling data to be represented as printable PDF scores and optional MIDI files.

## Overview

This project provides a novel approach to data serialization by leveraging music notation as an encoding medium. Convert any data into music-xml format, generate beautiful PDF scores and MIDI files, and decode the music back to retrieve the original data.

### Core Workflow

```
Arbitrary Data ↔ Music-XML ↔ PDF Scores / MIDI
```

**Encoding**: Transform arbitrary data into music-xml notation
**Generation**: Convert music-xml to printable PDF scores and optionally MIDI files
**Decoding**: Extract the original data from the music-xml representation

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

*(Documentation to be added as project develops)*

### Basic Example

```python
# Encoding: Convert data to music-xml
# from music_encoding import encode_to_musicxml
# data = b"Hello, World!"
# musicxml = encode_to_musicxml(data)

# Generation: Convert music-xml to PDF and MIDI
# from music_encoding import generate_score
# generate_score(musicxml, output_pdf="score.pdf", output_midi="score.mid")

# Decoding: Extract original data from music-xml
# from music_encoding import decode_from_musicxml
# recovered_data = decode_from_musicxml(musicxml)
# assert data == recovered_data
```

## Project Structure

```
music_shit_encoding/
├── README.md              # This file
├── LICENSE                # MIT License
├── requirements.txt       # Python dependencies
└── ...                    # Source code (to be added)
```

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Author

**Peter Szabo** (szabopeter)

---

**Note**: This is an experimental project exploring creative approaches to data encoding through music notation.
