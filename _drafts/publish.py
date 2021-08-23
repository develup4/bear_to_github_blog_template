import os
import re
import shutil
import hashlib
from os import renames
from datetime import datetime


# Global
current_file_created_date = ""


def remove_old_data():
    remove_dirs = ['../assets/images', '../_posts']
    try:
        for remove_dir in remove_dirs:
            if os.path.isdir(remove_dir):
                shutil.rmtree(remove_dir)
                os.mkdir(remove_dir)
                print('[  SUCCESS  ] Remove old ' + remove_dir)
            else:
                os.mkdir(remove_dir)
                print('[  SUCCESS  ] Make directory ' + remove_dir)
    except:
        print("Occur exception : Cannot remove " + remove_dir)
        quit()


def move_image_directory(directory_name):
    h = hashlib.md5()
    h.update(directory_name.encode('utf-8'))
    hash_value = h.hexdigest()

    try:
        renames(directory_name, '../assets/images/' + hash_value)
        print('[  SUCCESS  ] Move [' + directory_name + '] directory to [assets/images/' + hash_value + ']')
    except:
        print("Occur exception : Cannot move " + directory_name + " directory(hash:" + hash_value + ")")
        quit()


def is_python_file(filename):
    return filename.split('.')[1] == 'py'


def rename_markdown(filename):
    h = hashlib.md5()
    filename_without_ext = filename.split('.')[0]
    h.update(filename_without_ext.encode('utf-8'))
    hash_value = h.hexdigest()

    global current_file_created_date

    new_name = current_file_created_date;
    new_name += "-"
    new_name += hash_value

    try:
        renames(filename, '../_posts/' + new_name + ".md")
        print('[  SUCCESS  ] Rename [' + filename + '] to [' + new_name + ']\n')
    except:
        print("Occur exception : Cannot rename " + filename + "(hash:" + hash_value + ")")
        quit()


def write_meta_info(f, read_lines):
    current_line = 0
    toc_count = 0

    for line in read_lines:
        if line.startswith('## '):
            toc_count += 1

    # Mandantory
    f.write('---\n')
    f.write('title: ' + read_lines[current_line].split('#')[1] + '\n')
    current_line += 1

    # Optional
    if read_lines[current_line].startswith('## '):
        f.write('subtitle: ' + read_lines[current_line].split('##')[1])
        current_line += 1

    # Mandantory
    global current_file_created_date
    current_file_created_date = read_lines[current_line].split('###')[1].split('\n')[0].split(' ')[1]
    current_line += 1

    # Get category and tags
    tags = read_lines[current_line].split('#')
    current_line += 1

    if len(tags) > 0:
        f.write('categories: ' + tags[1] + '\n')

    if len(tags) > 1:
        f.write('tags: ');
        for tag in tags[2:]:
            f.write(tag + " ")
        f.write('\n')

    # TOC
    if toc_count > 2:
        f.write('toc: true\n')
        f.write('toc_sticky: true\n')
    
    f.write('---\n\n')
    f.write('  \n')
    
    print('[  SUCCESS  ] write meta info')
    return current_line


def edit_by_jekyll_format(read_line):
    # Transform enter to double space
    new_line = read_line.split('\n')[0] + '  \n'

    # transform double quotation
    if new_line.find('“') != -1:
        new_line = new_line.replace('“', '"')

    if new_line.find('”') != -1:
        new_line = new_line.replace('”', '"')

    return new_line


def transform_image_path(filename, image_format_line):
    # 이미지 이름이 한글이면 잘안된다. 이런경우 베어에서부터 다른이름으로 저장하던지해서 영어이름으로 바꾸자.
    # ![](IntelliJ%20%E1%84%83%E1%85%A1%E1%86%AB%E1%84%8E%E1%85%AE%E1%86%A8%E1%84%8F%E1%85%B5/34BD35F8-BE30-49F2-873F-5E07A1D86BCF.png)
    # ![]({{ site.url }}{{ site.baseurl }}/assets/images/2021-06-22-IntelliJ 단축키/34BD35F8-BE30-49F2-873F-5E07A1D86BCF.png)

    h = hashlib.md5()
    filename_without_ext = filename.split('.')[0]
    h.update(filename_without_ext.encode('utf-8'))
    hash_value = h.hexdigest()

    return '![]({{ site.url }}{{ site.baseurl }}/assets/images/' + hash_value + '/' + image_format_line.split('/')[1]


def edit_markdown(filename):
    # Read all lines
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        print('[  SUCCESS  ] read file - ' + filename)

    # Write lines by jekyll format
    with open(filename, 'w') as f:
        start_line = write_meta_info(f, lines)

        for line in lines[start_line:]:
            jekyll_format_line = edit_by_jekyll_format(line)

            # Process image expression
            if jekyll_format_line.find('![](') != -1:
                jekyll_format_line = transform_image_path(filename, jekyll_format_line)
                print('[  SUCCESS  ] transform image path to /assets/images')

            f.write(jekyll_format_line)
        

if __name__ == "__main__":

    remove_old_data()
    with os.scandir() as result:
        entries = list(result)

    for entry in entries:
        if entry.is_file() == False:
            move_image_directory(entry.name)
        else:
            if is_python_file(entry.name) == False:
                edit_markdown(entry.name)
                rename_markdown(entry.name)