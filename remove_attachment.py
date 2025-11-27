from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array

from pathlib import Path

origin_pdf_file_name = 'output2.pdf'

pdf = Pdf.open(origin_pdf_file_name)

xml_file_path = 'test_data/sample_music.musicxml'

filespec = AttachedFileSpec.from_filepath(pdf, Path(xml_file_path))

dest_xml_file = pdf.attachments.get(xml_file_path, None)

dest_pdf_file_name = 'check_shit.pdf'

pdf.save(dest_pdf_file_name)

dest_xml_file_name = 'output.xml'

Path(dest_xml_file_name).write_bytes(dest_xml_file.get_file().read_bytes())