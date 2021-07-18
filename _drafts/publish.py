import os
import shutil
from os import renames
from datetime import datetime
import re


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


def remove_emoji(text):
    emoji_pattern = re.compile("["
        u"\U00010000-\U0010FFFF"  #BMP characters 이외
                           "]+", flags=re.UNICODE)
    emoji_removed = emoji_pattern.sub(r'', text)
    print('[  SUCCESS  ] Remove emoji [' + text + '] to [' + emoji_removed + ']')
    return emoji_removed


def move_image_directory(directory_name):
    print('[  SUCCESS  ] Move [' + directory_name + '] directory to [assets/images]')
    emoji_removed_directory = remove_emoji(directory_name)
    renames(directory_name, '../assets/images/' + datetime.today().strftime('%Y-%m-%d-') + emoji_removed_directory)


def is_python_file(filename):
    return filename.split('.')[1] == 'py'


def rename_markdown(filename):
    emoji_removed_filename = remove_emoji(filename)
    chunks = emoji_removed_filename.split(' ');
    new_name = datetime.today().strftime('%Y-%m-%d');
    for chunk in chunks:
        new_name = new_name + '-' + chunk
    print('[  SUCCESS  ] Rename [' + filename + '] to [' + new_name + ']')
    renames(filename, '../_posts/' + new_name)


def write_meta_info(f, read_lines):
    current_line = 0
    toc_count = 0
    for line in read_lines:
        if line.startswith('## '):
            toc_count += 1

    f.write('---\n')
    f.write('title: ' + read_lines[current_line].split('#')[1] + '\n')
    current_line += 1

    if read_lines[current_line].startswith('##'):
        f.write('subtitle: ' + read_lines[current_line].split('##')[1])
        current_line += 1

    tags = read_lines[current_line].split('#')
    print('<Tags>')
    print(tags)
    current_line += 1

    if len(tags) > 0:
        f.write('categories: ' + tags[1] + '\n')
    if len(tags) > 1:
        f.write('tags: ');
        for tag in tags[2:]:
            f.write(tag + " ")
        f.write('\n')

    if toc_count > 2:
        f.write('toc: true\n')
        f.write('toc_sticky: true\n')
    
    f.write('---\n\n')
    f.write('  \n')
    print('[  SUCCESS  ] write meta info')

    return current_line


def edit_by_jekyll_format(read_line):
    new_line = read_line.split('\n')[0] + '  \n'

    # transform double quotation
    if new_line.find('“') != -1:
        new_line = new_line.replace('“', '"')
        #print('[  SUCCESS  ] transform “ mark to double quotation')

    if new_line.find('”') != -1:
        new_line = new_line.replace('”', '"')
        #print('[  SUCCESS  ] transform ” mark to double quotation')

    return new_line


def transform_image_path(filename, read_line):
    filename = remove_emoji(filename)
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
        start_line = write_meta_info(f, lines)

        for line in lines[start_line:]:
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