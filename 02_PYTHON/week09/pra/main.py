import os
from shutil import move
from tkinter import image_types

user = os.getlogin()

root_dir = 'C:/Users/{}/Downloads/'.format(user)
images_dir = 'C:/Users/{}/Downloads/images/'.format(user)
documents_dir = 'C:/Users/{}/Downloads/documents/'.format(user)
others_dir = 'C:/Users/{}/Downloads/others/'.format(user)
softwares_dir = 'C:/Users/{}/Downloads/softwares/'.format(user)

doc_types = ['.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx']
img_types = ['.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff']
software_types = ['.exe', '.pkg', '.dmg']

files = os.listdir(root_dir)

for i in files:
    f = i.split('.')
    
    if len(f) == 2:
        if f'.{f[1]}' in doc_types:
            move(root_dir + f'{i}', documents_dir)
        elif f'.{f[1]}' in img_types:
            move(root_dir + f'{i}', images_dir)
        elif f'.{f[1]}' in software_types:
            move(root_dir + f'{i}', softwares_dir)
        else:
            move(root_dir + f'{i}', others_dir)