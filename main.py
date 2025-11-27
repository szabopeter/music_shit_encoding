# from MuseParse.classes.Output.helpers import setupLilypondClean as setupLilypond
# from MuseParse.classes.Input import MxmlParser
# from MuseParse.classes.Output import LilypondOutput
# import os

# default_path_to_lily = '../../../../Downloads/lilypond-2.24.4/bin'
# setupLilypond(default_path_to_lily)

# parser = MxmlParser.MxmlParser()
# obj = parser.parse("./test_data/sample_music.musicxml")

# renderer = LilypondOutput.LilypondRenderer(obj, "output")
# renderer.run()
import subprocess

PYTHON = "/usr/bin/python3"  # or the exact python3 that works for you
LILYPOND_DIR = "/Users/szaszdominik/Downloads/lilypond-2.24.4/bin"

musicxml_path = "test_data/sample_music.musicxml"
ly_path = "/Users/szaszdominik/programming/py/musicXML/music-shit2/output.ly"

subprocess.run(
    [PYTHON, f"{LILYPOND_DIR}/musicxml2ly", "-o", ly_path, musicxml_path],
    check=True,
)

subprocess.run(
    [f"{LILYPOND_DIR}/lilypond", ly_path],
    check=True,
)