# from MuseParse.classes.Output.helpers import setupLilypondClean as setupLilypond
# from MuseParse.classes.Input import MxmlParser
# from MuseParse.classes.Output import LilypondOutput
# import os

# # default_path_to_lily = '../../../../Downloads/lilypond-2.24.4/bin'
# # setupLilypond(default_path_to_lily)

# parser = MxmlParser.MxmlParser()
# obj = parser.parse("./test_data/sample_music.musicxml")

# renderer = LilypondOutput.LilypondRenderer(obj, "output")
# renderer.run()
# # import subprocess

# # PYTHON = "/usr/bin/python3"  # or the exact python3 that works for you
# # LILYPOND_DIR = "/Users/szaszdominik/Downloads/lilypond-2.24.4/bin"

# # musicxml_path = "test_data/sample_music.musicxml"
# # ly_path = "/Users/szaszdominik/programming/py/musicXML/music-shit2/output.ly"

# # subprocess.run(
# #     [PYTHON, f"{LILYPOND_DIR}/musicxml2ly", "-o", ly_path, musicxml_path],
# #     check=True,
# # )

# # subprocess.run(
# #     [f"{LILYPOND_DIR}/lilypond", ly_path],
# #     check=True,
# # )
from pathlib import Path
import subprocess

LILYPOND_DIR = "/Users/szaszdominik/Downloads/lilypond-2.24.4/bin"
musicxml_path = "test_data/sample_music.musicxml"
ly_path = Path("output.ly")

# 1) MusicXML -> .ly
subprocess.run(
    [f"{LILYPOND_DIR}/musicxml2ly", "-o", str(ly_path), musicxml_path],
    check=True,
)

# 2) Read and patch score block
text = ly_path.read_text(encoding="utf-8")

from pathlib import Path

ly_path = Path("output.ly").resolve()
text = ly_path.read_text(encoding="utf-8")

# Abort if an active \midi already exists (not commented)
if "\\midi" in text and "%  \\midi" not in text:
    print("MIDI block already present")
else:
    # Replace the commented midi hint block that musicxml2ly creates
    text = text.replace(
        "    % To create MIDI output, uncomment the following line:\n"
        "    %  \\midi {\\tempo 4 = 100 }\n"
        "    }\n",
        "    \\midi { }\n"
        "}\n"
    )
    ly_path.write_text(text, encoding="utf-8")
    print("Patched output.ly, now contains \\midi { }")

# 3) Run lilypond
subprocess.run(
    [f"{LILYPOND_DIR}/lilypond", str(ly_path)],
    check=True,
)


