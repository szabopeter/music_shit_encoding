from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array

from pathlib import Path

origin_pdf_file_name = 'more_shit.pdf'

pdf = Pdf.open(origin_pdf_file_name)

xml_file_name = 'music.xml'

filespec = AttachedFileSpec.from_filepath(pdf, Path(xml_file_name))

dest_xml_file = pdf.attachments.pop(xml_file_name, None)

dest_pdf_file_name = 'check_shit.pdf'

pdf.save(dest_pdf_file_name)

dest_xml_file_name = 'check_music.xml'

Path(dest_xml_file_name).write_bytes(dest_xml_file.get_file().read_bytes())