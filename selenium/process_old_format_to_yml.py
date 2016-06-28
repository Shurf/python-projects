import configparser
import os
import shutil
import re

folder = r'c:\work\other\_docx\books\agni_yoga\01_Zov'
prefix = 'AY_Zov_'
page_selector = '(\d+)'
html_extension = '.html'
config_file_name = 'description.ini'

description_file_name = 'description.ini'
contents_file_name = 'cont.prs'


def __main__():
    destination_folder = folder + '_ready'
    converted_folder = folder + '_converted'
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder)

    config = configparser.ConfigParser()
    file = open(os.path.join(folder, description_file_name))
    config.read_string('[dummy_section]\n' + file.read())
    file.close()

    shift = 1 - int(config['dummy_section']['firstfile'])
    shutil.copyfile(os.path.join(folder, config['dummy_section']['oblojka']),
                    os.path.join(destination_folder, config['dummy_section']['oblojka']))

    for html_file in os.listdir(converted_folder):
        regex = re.match("([^-\d]+)(-?\d+).html", html_file)
        if not regex:
            continue
        new_name = regex.group(1) + str(int(regex.group(2)) + shift).zfill(4) + '.html'
        shutil.copyfile(os.path.join(converted_folder, html_file),
                        os.path.join(destination_folder, new_name))

    with open(os.path.join(destination_folder, 'config.yml'), 'w', encoding='utf-8') as f:
        f.write('html_regex: \'^' + prefix + page_selector + '\\' + html_extension + '$\'\n')
        f.write('has_pdf: \'false\'\n')
        f.write('book:\n')
        f.write('  picture_path: \'%s\'\n' % config['dummy_section']['oblojka'])
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

        with open(os.path.join(folder, contents_file_name)) as contents:
            for line in contents:
                line_regex = re.match('<(.+)><(\d+)>(.+)', line)
                if not line_regex:
                    continue
                page_number = int(line_regex.group(2))
                tag = line_regex.group(1)
                f.write('  ' * 2 + '- \n')
                f.write('  ' * 3 + 'name: \'' + line_regex.group(3) + '\'\n')
                f.write('  ' * 3 + 'page: ' + '\'' + str(page_number) + '\'\n')
                if tag == 'li':
                    f.write('  ' * 3 + 'type: ' + '\'page\'' + '\n')
                else:
                    raise Exception(tag)


if __name__ == '__main__':
    __main__()
