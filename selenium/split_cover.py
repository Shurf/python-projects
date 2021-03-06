import yaml
import os
import subprocess
import shutil
import re

class PdfConverter:
    def __init__(self, pdf_files_path, additional_options):
        self.pdf_files_path = pdf_files_path
        self.converter_name = 'pdf2htmlex'
        self.additional_options = additional_options
        self.tmp_file_name = 'tmp.tmp'

    def convert(self):
        # command_line = os.path.join(self.pdf_converter_path, self.converter_name) + ' '
        #command_line += self.dest_dir_specifier + self.pdf_files_path + ' '
        for file_name in os.listdir(self.pdf_files_path):
            full_path = os.path.join(self.pdf_files_path, file_name)
            if not os.path.isfile(full_path):
                continue
            match = re.search('(.+)\.pdf', file_name)
            if not match:
                continue

            args = [self.converter_name]
            for option in self.additional_options:
                args.append(option)
            args.append('--dest-dir=' + self.pdf_files_path)
            args.append(full_path)

            print("Converting %s" % full_path)
            subprocess.call(args)

def process_folder(folder):

    split_directory = os.path.join(folder, 'split')
    if os.path.exists(split_directory):
        print("already exists")
        return
    os.mkdir(split_directory)
    subprocess.call(["pdftk", os.path.join(folder, "0002.pdf"), "burst", "output", os.path.join(split_directory, "%04d.pdf")])

    new_count = len([name for name in os.listdir(split_directory) if os.path.isfile(os.path.join(split_directory, name)) and name.endswith('.pdf')])

    #call pdf2htmlex here
    PdfConverter(split_directory, ['--fallback=1', '--zoom=1.5',
                 '--data-dir=/usr/local/opt/pdf2htmlex/share/pdf2htmlEX/',
                 '--stretch-narrow-glyph=1',
                 '--process-outline=0']).convert()

    for file in sorted(os.listdir(folder), key=str.lower, reverse=True):
        if file.startswith('._'):
            continue
        file_name, file_extension = os.path.splitext(file)
        if file_extension not in ['.pdf', '.html']:
            continue
        file_number = int(file_name)
        if file_number == 2:
            os.unlink(os.path.join(folder, file))
            continue
        if file_number == 1:
            continue
        shutil.move(os.path.join(folder, file),
                    os.path.join(folder, str(file_number + new_count - 1).zfill(4) + file_extension))

    for file in os.listdir(split_directory):
        if file.startswith('._'):
            continue
        file_name, file_extension = os.path.splitext(file)
        if file_extension not in ['.pdf', '.html']:
            continue
        file_number = int(file_name)
        shutil.move(os.path.join(split_directory, file),
                    os.path.join(folder, str(file_number + 1).zfill(4) + file_extension))

    config = None
    with open(os.path.join(folder, 'config.yml'), encoding='utf-8') as f:
        config = yaml.load(f)

    os.unlink(os.path.join(folder, 'config.yml'))

    with open(os.path.join(folder, 'config.yml'), 'w', encoding='utf-8') as f:
        f.write('pdf_regex: \'%s\'\n' % config['pdf_regex'])
        f.write('html_regex: \'%s\'\n' % config['html_regex'])
        f.write('book:\n')
        f.write('  picture_path: \'%s\'\n' % config['book']['picture_path'])
        f.write('  book_file: \n')
        f.write('  name_prefix: \n')
        f.write('  tree_prefix: \n')
        f.write('  name: \'%s\'\n' % config['book']['name'])
        f.write('  name_comment: \n')
        f.write('  page_count: \'%d\'\n' % (int(config['book']['page_count']) + new_count - 1))
        f.write('  first_page: \'%s\'\n' % config['book']['first_page'])
        f.write('  synopsis: \n')
        f.write('  contents: \n')

        for content_element in config['book']['contents']:

            page_number = int(content_element['page'])
            if page_number > 0:
                page_number += new_count - 1

            f.write('  ' * 2 + '- \n')
            f.write('  ' * 3 + 'name: \'' + content_element['name'] + '\'\n')
            f.write('  ' * 3 + 'page: \'' + str(page_number) + '\'\n')
            f.write('  ' * 3 + 'type: \'' + content_element['type'] + '\'\n')

    #os.unlink(split_directory)

def __main__():
    process_folder('/Users/schrecknetuser/pdf-ocr/documents2/Сергий')
    """directory = r'/Users/schrecknetuser/pdf-ocr/documents2/Мысль'
    for child in os.listdir(directory):
        full_path = os.path.join(directory, child)
        if not os.path.isdir(full_path):
            continue
        print(full_path)
        process_folder(full_path)"""

if __name__ == '__main__':
    #__main__()
    PdfConverter('/users/schrecknetuser', ['--fallback=1', '--zoom=0.7',
                 '--data-dir=/usr/local/opt/pdf2htmlex/share/pdf2htmlEX/',
                 '--stretch-narrow-glyph=1',
                 '--process-outline=0']).convert()