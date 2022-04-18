import os
import shutil


# Obtengo el path raiz
path = os.path.expanduser("~")
print(path)
# Obtengo el path de la carpeta a ordenar
carpeta_ordenar= path + '/Downloads'
print(carpeta_ordenar)
# Creo las nuevas subcarpetas
nombres_subcarpetas=['imagenes', 'documentos', 'softwares', 'otros', 'scripts']
try:
    for i in nombres_subcarpetas:
        new_subfolder = carpeta_ordenar + '/{}'.format(i)
        os.makedirs(new_subfolder)
except Exception as e:
    print(e)
    pass

# Clasifico extensiones
doc_types=('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')
img_types=('.jpg','.jpeg','.png','.svg','.gif','.tif','.tiff')
software_types=('.exe','.pkg','.dmg')
scripts_types=('.ipynb', '.py')

# Escaneo todos los ficheros y los muevo a su carpeta correspondiente

dir_list=[file for file in os.scandir(carpeta_ordenar)]

for entry in dir_list:
    root, extension = os.path.splitext(entry)
    if entry.is_file():
        if extension in doc_types:
            carpeta = carpeta_ordenar +'/documentos'
            shutil.move(entry, carpeta)
        elif extension in img_types:
            carpeta = carpeta_ordenar +'/imagenes'
            shutil.move(entry, carpeta)
        elif extension in software_types:
            carpeta = carpeta_ordenar +'/software'
            shutil.move(entry, carpeta)
        elif extension in scripts_types:
            carpeta = carpeta_ordenar +'/scripts'
            shutil.move(entry, carpeta)
        else:
            carpeta =  carpeta_ordenar +'/otros'
            shutil.move(entry, carpeta) 