from convert_input_data import *
import re

class StructureWorker:
    def make_pages_array(self, pages_string):

        result = []
        trimmed_string = pages_string.strip()
        if not trimmed_string:
            return result

        blocks = trimmed_string.split(',')
        for block in blocks:
            trimmed_block = block.strip()
            split_block = trimmed_block.split('-')
            if len(split_block) < 2:
                result.append(int(trimmed_block.replace('~', '-')))
            else:
                for i in range(int(split_block[0].replace('~', '-')), int(split_block[1].replace('~', '-')) + 1):
                    result.append(i)

        return result

    def find_min_part_page(self, part):
        array = self.make_pages_array(part.pages)
        return min(array) + shift_modifier

    def find_min_chapter_page(self, chapter):
        array = self.make_pages_array(chapter.pages)

        for part in chapter.parts:
            array += self.make_pages_array(part.pages)

        return min(array) + shift_modifier

    def find_min_book_page(self, book):
        array = self.make_pages_array(book.pages)

        for part in book.parts:
            array += self.make_pages_array(part.pages)

        for chapter in book.chapters:
            array += self.make_pages_array(chapter.pages)
            for part in chapter.parts:
                array += self.make_pages_array(part.pages)

        return min(array) + shift_modifier

    def find_max_book_page(self, book):
        array = self.make_pages_array(book.pages)

        for part in book.parts:
            array += self.make_pages_array(part.pages)

        for chapter in book.chapters:
            array += self.make_pages_array(chapter.pages)
            for part in chapter.parts:
                array += self.make_pages_array(part.pages)

        return max(array) + shift_modifier


def write_chapter(file, chapter):
    file.write('  ' * 2 + '- \n')
    file.write('  ' * 3 + 'name: \'' + chapter.name + '\'\n')
    file.write('  ' * 3 + 'type: ' + '\'chapter\'' + '\n')
    file.write('  ' * 3 + 'page: ' + '\'' + str(StructureWorker().find_min_chapter_page(chapter)) + '\'\n')


def write_part(file, part):
    file.write('  ' * 2 + '- \n')
    file.write('  ' * 3 + 'name: \'' + part.name + '\'\n')
    file.write('  ' * 3 + 'type: ' + '\'part\'' + '\n')
    file.write('  ' * 3 + 'page: ' + '\'' + str(StructureWorker().find_min_part_page(part)) + '\'\n')


def write_page(file, page_num, page_name):

    new_name = re.sub(r'^Страница \d+\. ', '', page_name)

    file.write('  ' * 2 + '- \n')
    file.write('  ' * 3 + 'name: \'' + new_name + '\'\n')
    file.write('  ' * 3 + 'type: ' + '\'page\'' + '\n')
    file.write('  ' * 3 + 'page: ' + '\'' + str(page_num) + '\'\n')


def __main__():
    with open('output.yml', 'w') as f:
        f.write('pdf_regex: \'^' + page_selector + '\\' + pdf_extension + '$\'\n')
        f.write('html_regex: \'^' + page_selector + '\\' + html_extension + '$\'\n')

        f.write('shift_modifier: \'' + str(shift_modifier) + '\'\n')

        f.write('book:\n')
        f.write('  picture_path: \n')
        f.write('  book_file: \n')
        f.write('  name_prefix: \n')
        f.write('  tree_prefix: \n')
        f.write('  name: \n')
        f.write('  name_comment: \n')
        f.write('  page_count: \'' + str(StructureWorker().find_max_book_page(book_structure) + 1 - StructureWorker().find_min_book_page(book_structure)) + '\'\n')
        f.write('  first_page: \'' + str(StructureWorker().find_min_book_page(book_structure)) + '\'\n')
        f.write('  synopsis: \n')
        f.write('  contents: \n')

        for chapter in book_structure.chapters:
            write_chapter(f, chapter)
            for part in chapter.parts:
                write_part(f, part)

        for part in book_structure.parts:
            write_part(f, part)

        for page_num in sorted(pages_dictionary):
            write_page(f, page_num, pages_dictionary[page_num])


if __name__ == '__main__':
    __main__()
