import array
import os

with open('binary.bin', 'rb') as f:
    data = f.read()
print(data)


#array로 가져오자
data = array.array('B')
with open('binary.bin', 'rb') as f:
    f.seek(0, os.SEEK_END)
    filesize = f.tell()
    f.seek(0)
    data.fromfile(f, filesize)

for item in data:
    print(item)