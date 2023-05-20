from os import listdir, system
from base64 import b64decode

def extract(bText):
    bText=bText.replace(b' ', b'').replace(b'\n', b'')
    return [b64decode(i.split(b'"}')[0]) for i in bText.split(b'"encoding":"base64","text":"')[1:]]

c1=0
images=[]
for i in listdir():
    if i.endswith('.har'):
        c1+=1
        with open(i, 'rb') as f:
            images+=extract(f.read())

for i in listdir('images'):
    system('del images\\'+str(i))

c2=0
for i in range(len(images)):
    c2+=1
    with open('images/'+('000'+str(i))[-4:]+'.jpg', 'wb') as f:
        f.write(images[i])

print(c2, 'image(s) from', c1, 'file(s)')
input('any key to exit...')