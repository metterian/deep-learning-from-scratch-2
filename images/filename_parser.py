import os,sys


file_path = os.path.dirname(os.path.abspath(__file__))
file_names = os.listdir(file_path)

for name in file_names:
    src = os.path.join(file_path, name)
    dst = name.replace(' ', '')
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
