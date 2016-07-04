import configparser
import os
import shutil
import re

#folder = r'/Users/schrecknetuser/_docx/books/agni_yoga/01_Zov'
prefix = 'AY_Zov_'
page_selector = '(\d+)'
html_extension = '.html'
config_file_name = 'description.ini'

description_file_name = 'description.ini'
contents_file_name = 'cont.prs'


def process_folder(folder_to_process):
    destination_folder = folder_to_process + '_ready'
    converted_folder = folder_to_process + '_converted'
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder)

    config = configparser.ConfigParser()
    file = open(os.path.join(folder_to_process, description_file_name), encoding='cp1251')
    config.read_string('[dummy_section]\n' + file.read())
    file.close()

    shift = 1 - int(config['dummy_section']['firstfile'])

    if 'oblojka' in config['dummy_section']:
        cover = config['dummy_section']['oblojka']
        shutil.copyfile(os.path.join(folder_to_process, cover),
                        os.path.join(destination_folder, cover))

    for html_file in os.listdir(converted_folder):
        regex = re.match("([^-\d]+)(-?\d+).html", html_file)
        if not regex:
            continue
        new_name = regex.group(1) + str(int(regex.group(2)) + shift).zfill(4) + '.html'
        shutil.copyfile(os.path.join(converted_folder, html_file),
                        os.path.join(destination_folder, new_name))

    with open(os.path.join(destination_folder, 'config.yml'), 'w', encoding='utf-8') as f:
        f.write('pdf_regex: \n')
        f.write('html_regex: \'^' + prefix + page_selector + '\\' + html_extension + '$\'\n')
        f.write('book:\n')
        f.write('  has_pdf: \'false\'\n')
        if 'oblojka' in config['dummy_section']:
            f.write('  picture_path: \'%s\'\n' % config['dummy_section']['oblojka'])
        else:
            f.write('  picture_path: \n')
        f.write('  book_file: \n')
        f.write('  name_prefix: \n')
        f.write('  tree_prefix: \n')
        f.write('  name: %s\n' % config['dummy_section']['title'])
        f.write('  name_comment: \n')
        f.write('  page_count: \'%d\'\n' % (
        int(config['dummy_section']['lastfile']) - int(config['dummy_section']['firstfile']) + 1))
        f.write('  first_page: \'%d\'\n' % int(config['dummy_section']['firstfile']))
        f.write('  synopsis: %s\n' % config['dummy_section']['description'])
        f.write('  contents: \n')

        with open(os.path.join(folder_to_process, contents_file_name), encoding='cp1251') as contents:
            for line in contents:
                line_regex = re.match('<(.+)><(\d+)>(.+)', line)
                if not line_regex:
                    continue
                page_number = int(line_regex.group(2))
                tag = line_regex.group(1)
                f.write('  ' * 2 + '- \n')
                f.write('  ' * 3 + 'name: \'' + line_regex.group(3) + '\'\n')
                f.write('  ' * 3 + 'page: ' + '\'' + str(page_number) + '\'\n')
                if tag.lower() == 'li':
                    f.write('  ' * 3 + 'type: ' + '\'page\'' + '\n')
                elif tag.lower() == 'h2':
                    f.write('  ' * 3 + 'type: ' + '\'part\'' + '\n')
                elif tag.lower() == 'h4':
                    f.write('  ' * 3 + 'type: ' + '\'chapter\'' + '\n')
                else:
                    raise Exception(tag)

def __main__():
    process_folder(r'/Users/schrecknetuser/_docx/books/pisma_mahatm')
    #directory = r'/Users/schrecknetuser/_docx/books/uh/'
    #for child in os.listdir(directory):
    #    full_path = os.path.join(directory, child)
    #    if not os.path.isdir(full_path):
    #        continue
    #    if re.match('.+_ready', full_path):
    #        continue
    #    if re.match('.+_converted', full_path):
    #        continue
    #    print(full_path)
    #    process_folder(full_path)


if __name__ == '__main__':
    __main__()
