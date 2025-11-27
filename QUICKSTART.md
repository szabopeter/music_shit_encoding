# Quickstart (Streamlined)

Follow these exact steps in order.

Prerequisites:
- Python 3.7+
- LilyPond 2.24.4 installed at C:\DevTools\lilypond-2.24.4
- Dependencies installed: `pip install -r requirements.txt`

1) Encode bytes to MusicXML (from repo root):

```powershell
python bytes_to_musical_xml.py sample.txt -o test_data/sample_music.musicxml -p "Sample Text"
```

2) Convert MusicXML to LilyPond (run from C:\DevTools\lilypond-2.24.4):

```powershell
cd C:\DevTools\lilypond-2.24.4
bin\musicxml2ly.exe -o output.ly C:\Repos\music_shit_encoding\test_data\sample_music.musicxml
```

3) Render PDF (still in C:\DevTools\lilypond-2.24.4):

```powershell
bin\lilypond.exe -o shit output.ly  # produces shit.pdf
```

4) Attach MusicXML to PDF (from repo root):

```powershell
cd C:\Repos\music_shit_encoding
# Ensure the expected filename for attachment exists
Copy-Item .\test_data\sample_music.musicxml .\music.xml -Force
python add_attachment.py  # attaches music.xml to shit.pdf -> more_shit.pdf
```

5) Remove attachment and extract MusicXML (from repo root):

```powershell
python remove_attachment.py  # extracts to check_music.xml and writes check_shit.pdf
```

6) Decode MusicXML back to bytes (from repo root):

```powershell
python musical_xml_to_bytes.py check_music.xml -o decoded_sample.txt
```

Notes:
- The attachment scripts expect files named `shit.pdf` and `music.xml` in the repo root.
- Adjust paths if your LilyPond install directory differs.
