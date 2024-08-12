import json

from venntas import registro_ventas
from compras import registro_compras


def cargar_datos(filename):
    with open(filename, "r")as file:
        return json.load(file)
    
def guardar_datos(filename, data):
    with open(filename, "w")as file:
        json.dump(data, file, indent=4)

medicametos = cargar_datos()