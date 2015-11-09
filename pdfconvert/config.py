# coding=utf-8
__author__ = 'd.yavno'

pdf_files_directory = '/users/schrecknetuser/pdf-ocr/td1'
pdf2htmlex_directory = ''
dest_dir_specifier = '--dest-dir='
converter_name = '/users/schrecknetuser/pdf2htmlex/pdf2htmlEX/pdf2htmlex'
additional_options = [
    '--fallback=1',
    '--zoom=1.5',
    '--heps=5',
    '--data-dir=/usr/local/opt/pdf2htmlex/share/pdf2htmlEX/',
    '--stretch-narrow-glyph=1',
    #'--space-threshold=10',
    '--space-as-offset=1',
    '--optimize-text=1']
use_gs = False
#ghostscript_path = 'c:\\Program Files (x86)\\gs\\gs9.18\\bin\\gswin32c.exe'
ghostscript_path = 'gs'

