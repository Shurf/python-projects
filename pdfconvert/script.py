# coding=utf-8
__author__ = 'd.yavno'

import config
import os
import re
import subprocess


class PdfConverter:
    def __init__(self, pdf_files_path, pdf_converter_path, dest_dir_specifier, converter_name):
        self.pdf_files_path = pdf_files_path
        self.pdf_converter_path = pdf_converter_path
        self.dest_dir_specifier = dest_dir_specifier
        self.converter_name = converter_name

    def convert(self):
        #command_line = os.path.join(self.pdf_converter_path, self.converter_name) + ' '
        #command_line += self.dest_dir_specifier + self.pdf_files_path + ' '
        for file_name in os.listdir(self.pdf_files_path):
            full_path = os.path.join(self.pdf_files_path, file_name)
            if not os.path.isfile(full_path):
                continue
            if not re.match('.+\.pdf', file_name):
                continue

            print("Converting %s" % full_path)
            subprocess.call([os.path.join(self.pdf_converter_path, self.converter_name),
                             self.dest_dir_specifier + self.pdf_files_path,
                             full_path])


def __main__():
    converter = PdfConverter(config.pdf_files_directory,
                 config.pdf2htmlex_directory,
                 config.dest_dir_specifier,
                 config.converter_name)
    converter.convert()


if __name__ == '__main__':
    __main__()