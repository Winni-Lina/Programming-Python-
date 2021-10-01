import os
data = os.listdir('.')
data = os.listdir('..')
data = os.listdir('my_directory')
data = os.listdir('E:\\School\\PycharmProjects\\file handler')
data = os.listdir('E:/School/PycharmProjects/file handler')

# print(data)

for d in data:
    print(d)
    print(f"is directory? : {os.path.isdir(d)}")
    print(f"is file? : {os.path.isfile(d)}")
