""" Arquivo para correr. """

from app import Shop
from app import AppDefaults

if __name__ == "__main__":
    #AppDefaults().app_size
    AppDefaults(True).app_bordeless
    Shop().run()