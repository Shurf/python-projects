# coding=utf-8
__author__ = 'd.yavno'

import config
import os
import re
import subprocess


class PdfConverter:
    def __init__(self, pdf_files_path, pdf_converter_path, dest_dir_specifier, converter_name, additional_options, ghostscript_path):
        self.pdf_files_path = pdf_files_path
        self.pdf_converter_path = pdf_converter_path
        self.dest_dir_specifier = dest_dir_specifier
        self.converter_name = converter_name
        self.additional_options = additional_options
        self.ghostscript_path = ghostscript_path
        self.tmp_file_name = 'tmp.tmp'

    def ghostcript_process(self, file_path):
        tmp_file = os.path.join(os.path.dirname(file_path), self.tmp_file_name)
        #os.system('"%s"' % self.ghostscript_path + '-sDEVICE=pdfwrite' + ' ' + '-sOutputFile="%s"' % tmp_file + '-dNOPAUSE' + '-dBATCH' + ' ' + file_path)
        subprocess.call([self.ghostscript_path, '-sDEVICE=pdfwrite', '-sOutputFile=%s' % tmp_file, '-dNOPAUSE', '-dBATCH', file_path])
        os.unlink(file_path)
        os.rename(tmp_file, file_path)

    def convert(self):
        # command_line = os.path.join(self.pdf_converter_path, self.converter_name) + ' '
        #command_line += self.dest_dir_specifier + self.pdf_files_path + ' '
        for file_name in os.listdir(self.pdf_files_path):
            full_path = os.path.join(self.pdf_files_path, file_name)
            if not os.path.isfile(full_path):
                continue
            if not re.match('.+\.pdf', file_name):
                continue

            #print("ghostscripting %s" % full_path)
            #self.ghostcript_process(full_path)
            args = [os.path.join(self.pdf_converter_path, self.converter_name)]
            for option in self.additional_options:
                args.append(option)
            args.append(self.dest_dir_specifier + self.pdf_files_path)
            args.append(full_path)

            print("Converting %s" % full_path)
            subprocess.call(args)


def __main__():
    converter = PdfConverter(config.pdf_files_directory,
                             config.pdf2htmlex_directory,
                             config.dest_dir_specifier,
                             config.converter_name,
                             config.additional_options,
                             config.ghostscript_path)
    converter.convert()


if __name__ == '__main__':
    __main__()