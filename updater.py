import urllib.request
import os

# install install.txt
# txt file containing list of files

url = 'https://github.com/imifk/pathfinder/blob/master/install.txt?raw=true'

f = urllib.request.urlopen(url)
file = f.read()
f.close()
f2 = open('install.txt', 'wb')
f2.write(file)
f2.close()


def find_files(file):
    with open(file) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return [x.strip() for x in content]


contents = find_files('install.txt')
print(contents)


def install():
    for content in contents:
        url = 'https://github.com/imifk/pathfinder/blob/master/{}?raw=true'.format(content)
        print('downloading {}           '.format(content), end="\r")
        f = urllib.request.urlopen(url)
        file = f.read()
        f.close()
        f2 = open(content, 'wb')
        f2.write(file)
        f2.close()
    return

def hide_file():
    for content in contents:
        os.system(f'attrib +h {content}')
    os.system('attrib -h Pathinator.exe')
    return

install()
hide_file()


os.remove('install.txt')

print('finished             ')
print('if install.txt is present.')
print('re-run software')
print('. . .')
input("Press Enter to exit...")

