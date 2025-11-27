from pikepdf import Pdf, AttachedFileSpec, Name, Dictionary, Array

from pathlib import Path

pdf = Pdf.open('../tests/resources/fourpages.pdf')

filespec = AttachedFileSpec.from_filepath(pdf, Path('../README.md'))

pdf.attachments['README.md'] = filespec