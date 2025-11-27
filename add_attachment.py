from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array

from pathlib import Path

origin_pdf_file_name = 'output.pdf'

pdf = Pdf.open(origin_pdf_file_name)

xml_file_name = 'test_data/sample_music.musicxml'

filespec = AttachedFileSpec.from_filepath(pdf, Path(xml_file_name))

pdf.attachments[xml_file_name] = filespec

dest_pdf_file_name = 'output2.pdf'

pdf.save(dest_pdf_file_name)