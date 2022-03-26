class MobilePhone():
    '''
    Docstring de una clase
    '''
    def __init__(self, phone):
        self.phone = phone # convertimos el parámetro de entrada como variable global a nivel de clase
        print("La clase MobilePhone ha inicializado")

    def encender_telefono(self, boton_power="OFF"):
        if boton_power == 'ON':
            print("Telefono encendido")

    def install_app(self, appname):
        self.phone['apps'].append(appname)
        print(self.phone['apps'])
    
    def remove_app(self, appname):
        for pos,i in enumerate(self.phone['apps']):
            if i['name'] == appname:
                self.phone['apps'].pop(pos)
        print(self.phone['apps'])

def nombrefuncion():
    pass

class OtraClass(object):
    pass