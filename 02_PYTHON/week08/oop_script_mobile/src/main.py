# importamos las librerías
from setup import config
from utility import utils

# importamos la estructura del telefono
estructura_samsung = config.samsung
print(estructura_samsung)

yt_app = config.youtube
print(yt_app)

# Instanciamos a un objeto la clase MobilePhone
samsung_a22_1 = utils.MobilePhone(estructura_samsung)
samsung_a22_2 = utils.MobilePhone(estructura_samsung)

# iphone13 = utils.MobilePhone(estructura_iphone)
# 
samsung_a22_1.install_app(yt_app)
samsung_a22_2.install_app(config.gmail_app)