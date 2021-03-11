import os 
import shutil


if os.path.exists('files'):
    shutil.rmtree('files')

os.mkdir('files')
os.chdir('files')

n = eval(input())
for i in range(1, n+1):
    os.mkdir('f'+str(i))
pt = os.listdir()
pt.sort()
print(pt)

os.rename('f1', 'folder1')
pt = os.listdir()
pt.sort()
print(pt)

os.rmdir('folder1')
pt = os.listdir()
pt.sort()
print(pt)


os.chdir('../')
shutil.rmtree('files')