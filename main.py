from MuseParse.classes.Output.helpers import setupLilypondClean as setupLilypond
from MuseParse.classes.Input import MxmlParser
from MuseParse.classes.Output import LilypondOutput
import os

default_path_to_lily = '../../../Downloads/lilypond-2.24.4/bin'
setupLilypond(default_path_to_lily)

parser = MxmlParser.MxmlParser()
obj = parser.parse("test.xml")

renderer = LilypondOutput.LilypondRenderer(obj, "output")
renderer.run()
