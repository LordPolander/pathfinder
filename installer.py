import urllib.request
import os

# install install.txt
# txt file containing list of files



def find_files(file):
    with open(file) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return [x.strip() for x in content]



def install():
    for content in contents:
        url = 'https://github.com/imifk/pathfinder/blob/master/{}?raw=true'.format(content)
        print('downloading {}                '.format(content), end="\r")
        f = urllib.request.urlopen(url)
        file = f.read()
        f.close()
        f2 = open(content, 'wb')
        f2.write(file)
        f2.close()
    return

def reinstall():
    try:
        f = open("install.txt")
        contents = find_files('install.txt')
        print('deleting old files . . .')
        print(contents)
        for content in contents:
            print(content)
            os.remove(content)
        f.close()
        os.remove('install.txt')
    except IOError:
        print("File not accessible")
    finally:
        pass

def hide_file():
    os.system(f'attrib +h install.txt')
    for content in contents:
        os.system(f'attrib +h {content}')
    os.system('attrib -h Pathinator.exe')
    return

reinstall()

url = 'https://github.com/imifk/pathfinder/blob/master/install.txt?raw=true'

f = urllib.request.urlopen(url)
file = f.read()
f.close()
f2 = open('install.txt', 'wb')
f2.write(file)
f2.close()

contents = find_files('install.txt')
print(f'downloading {contents}')

install()

hide_file()

print('finished             ')
print('if install.txt is present.')
print('re-run software')
print('. . .')
input("Press Enter to exit...")

