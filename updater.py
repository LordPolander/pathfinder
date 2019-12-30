
import urllib.request


print('This window will close automatically after the installation is finished')
print('unfortunately i didn\'t implement a progress bar')
print('sry. . .')

url = 'https://github.com/LordPolander/pathfinder/blob/master/pathfinder.exe?raw=true'

f = urllib.request.urlopen(url)
file = f.read()
f.close()
f2 = open('Pathinator.exe', 'wb')
f2.write(file)
f2.close()

url = 'https://github.com/LordPolander/pathfinder/blob/master/excel_path_sheet.ods?raw=true'

f = urllib.request.urlopen(url)
file = f.read()
f.close()
f2 = open('excel_path_sheet.ods', 'wb')
f2.write(file)
f2.close()