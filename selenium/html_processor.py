__author__ = 'schrecknetuser'

import bs4
import os
import re
import base64
import shutil

def process_folder(folder_name):
    destination_folder = folder_name + '_processed'
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    os.makedirs(destination_folder)
    for html_file in os.listdir(folder_name):
        regex = re.match(".+\.html", html_file)
        if not regex:
            continue
        with open(os.path.join(folder_name, html_file), 'r', encoding='cp1251') as f:
            soup = bs4.BeautifulSoup(f.read(), 'html.parser')
            for img_tag in soup.findAll('img'):
                if os.path.exists(os.path.join(folder_name, img_tag['src'])):
                    extension = os.path.splitext(os.path.join(folder_name, img_tag['src']))[1]
                    type = 'image/png'
                    if extension in ['.jpg', '.jpeg']:
                        type = 'image/jpeg'
                    data = base64.b64encode(open(os.path.join(folder_name, img_tag['src']), 'rb').read()).decode('utf-8').replace('\n', '')
                    img_tag['src'] = "data:%s;base64,%s" % (type, data)
            with open(os.path.join(destination_folder, html_file), 'wb') as out_file:
                out_file.write(soup.prettify('utf-8'))


def __main__():
    process_folder(r'/Users/schrecknetuser/_docx/books/roerich/let_eir2')


if __name__ == '__main__':
    __main__()
