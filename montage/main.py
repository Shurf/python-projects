import requests
import shutil
import argparse
import os
import fnmatch
import datetime

#text = ""; for(cnt = 1; cnt < 23; cnt++) {$.each($("a.card-list__pagination-number").filter(function(){return $(this).text() == cnt}), function(i, button){button.click(); $.each($("img.card-deck__overlay-image"), function(i, val){text += val.alt + "<br />\n" + val.src + "<br />\n"});})} window.open("about:blank", "", "_blank").document.write(text);

#sudo apt-get install montage
#sudo apt-get install imagemagick

def download():
    images_path = os.path.join(os.getcwd(), 'images')
    if os.path.exists(images_path):
        shutil.rmtree(images_path)
    os.makedirs(images_path)

    lines = [line.rstrip('\n') for line in open('config-arkham.txt')]
    for i in range(0, int(len(lines) / 2)):
        name = lines[i * 2]
        url = lines[i * 2 + 1]

        print(url)
        r = requests.get(url, stream=True)
        with open(os.path.join(images_path, name) + '.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

def convert():
    datetime.datetime.now().strftime("%Y%m%d-%S")

    parser = argparse.ArgumentParser(prog='mtg-montage', description='Process images for print')
    parser.add_argument('-d', '--directory', default='./images', help='the directory where the card images are located')
    parser.add_argument('-i', '--input', default='./arkham.txt', required=False, help='input file with card names and quatity')
    parser.add_argument('-o', '--output', default='./arkham.pdf', required=False, help='output pdf file to store the montage')
    parser.add_argument('-t', '--test', action='store_true', default=False,
                        help='tests to see which images can be found - doesn\'t generate anything')
    parser.add_argument('-s', '--savefile', default='', required=False,
                        help='the filepath where to store the card image choices')
    parser.add_argument('-c', '--choices', default='', required=False, help='load choices from this file')
    args = parser.parse_args()

    matches = []
    unmatched = []
    choices = []

    input_lines = [line.strip() for line in open(args.input)]

    # if the user imported choices add them to a list
    if args.choices != '':
        choices_loaded = []
        for line in open(args.choices):
            choices_loaded.append(tuple(line.strip().split(',')))
        choices_loaded = dict(choices_loaded)

    for line in input_lines:
        print('searching for ' + line)

        # find images in directory which match the name of the card
        pre_matches = []
        for root, dirnames, filenames in os.walk(args.directory):
            for filename in fnmatch.filter(filenames, '*' + line + '*'):
                pre_matches.append(os.path.join(root, filename))

        if len(pre_matches) == 0:
            unmatched.append(line[1])
            print('Couldn\'t find a match for', line)
        else:
            print('Matched', line)

            # if the --test flag is set, don't ask for input
            if args.test:
                continue

            matches.append(pre_matches[0])

    # build the montage command based on the images in matches[]
    if not args.test:
        command = 'montage '
        for img in matches:
            command = command + '"' + img + '" '
        command = command + '-quality 100 -geometry 744x1039 -density 400 -tile 3x3 '
        command = command + args.output
        print('')
        print('Building the pdf. This may take a while...')
        print(command)
        os.system(command)

    # if the save choices flag is set, write the choices to a file
    if args.savefile != '':
        f = open(args.savefile, 'w')
        for item in choices:
            f.write(item)

    # print some statistics
    print('')

    print('Statistics')
    print('-------------------------------------------')
    print('  Total different cards input:', len(input_lines))
    print('  Total unsuccessful finds:', len(unmatched))
    for sad in unmatched:
        print('    ', sad)
    print('')

if __name__ == '__main__':
    convert()
