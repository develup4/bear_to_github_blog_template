import os
import shutil
from os import renames
from datetime import datetime


def remove_old_data():
    remove_dirs = ['../assets/images', '../_posts']
    for remove_dir in remove_dirs:
        if os.path.isdir(remove_dir):
            shutil.rmtree(remove_dir)
            os.mkdir(remove_dir)
            print('[  SUCCESS  ] Remove old ' + remove_dir)
        else:
            os.mkdir(remove_dir)
            print('[  SUCCESS  ] Make directory ' + remove_dir)


def move_image_directory(directory_name):
    print('[  SUCCESS  ] Move [' + directory_name + '] directory to [assets/images]')
    renames(directory_name, '../assets/images/' + datetime.today().strftime('%Y-%m-%d-') + directory_name)


def is_python_file(filename):
    return filename.split('.')[1] == 'py'


def rename_markdown(filename):
    chunks = filename.split(' ');
    new_name = datetime.today().strftime('%Y-%m-%d');
    for chunk in chunks:
        new_name = new_name + '-' + chunk
    print('[  SUCCESS  ] Rename [' + filename + '] to [' + new_name + ']')
    renames(filename, '../_posts/' + new_name)


def write_meta_info(f, read_lines):
    toc_count = 0
    for line in read_lines:
        if line.startswith('#'):
            toc_count += 1

    f.write('---\n')
    f.write('title: ' + read_lines[0].split('#')[1] + '\n')
    tags = read_lines[1].split('#')
    if len(tags) > 0:
        f.write('categories: ' + tags[1] + '\n')
    if len(tags) > 1:
        f.write('tags: ');
        for tag in read_lines[1].split('#')[2:]:
            f.write(tag + " ")
    f.write('\n')
    f.write('classes: wide\n')
    if toc_count > 3:
        f.write('toc: true\n')
    f.write('---\n\n')
    f.write('  \n')
    print('[  SUCCESS  ] write meta info')


def edit_by_jekyll_format(read_line):
    new_line = read_line.split('\n')[0] + '  \n'

    # transform double quotation
    if new_line.find('“') != -1:
        new_line = new_line.replace('“', '"')
        print('[  SUCCESS  ] transform “ mark to double quotation')

    if new_line.find('”') != -1:
        new_line = new_line.replace('”', '"')
        print('[  SUCCESS  ] transform ” mark to double quotation')

    return new_line


def transform_image_path(filename, read_line):
    # ![]({{ site.url }}{{ site.baseurl }}/assets/images/2021-06-22-IntelliJ 단축키/34BD35F8-BE30-49F2-873F-5E07A1D86BCF.png)
    # ![](IntelliJ%20%E1%84%83%E1%85%A1%E1%86%AB%E1%84%8E%E1%85%AE%E1%86%A8%E1%84%8F%E1%85%B5/34BD35F8-BE30-49F2-873F-5E07A1D86BCF.png)
    print('[  SUCCESS  ] transform image path to /assets/images')
    return '![]({{ site.url }}{{ site.baseurl }}/assets/images/' + datetime.today().strftime('%Y-%m-%d-') + filename.split('.')[0] + '/' + read_line.split('/')[1]


def edit_markdown(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        print('[  SUCCESS  ] read file - ' + filename)

    with open(filename, 'w') as f:
        write_meta_info(f, lines)

        for line in lines[2:]:
            edited_line = edit_by_jekyll_format(line)

            if edited_line.find('![](') != -1:
                edited_line = transform_image_path(filename, edited_line)

            f.write(edited_line)
        
     
if __name__ == "__main__":
    remove_old_data()
    with os.scandir() as entries:
        for entry in entries:
            if entry.is_file() == False:
                move_image_directory(entry.name)
            else:
                if is_python_file(entry.name) == False:
                    edit_markdown(entry.name)
                    rename_markdown(entry.name)