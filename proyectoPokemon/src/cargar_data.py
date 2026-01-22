import json
from pathlib import Path


#Cargar las direcciones
Ruta_Tipos = Path(__file__).parent.parent /"data"/"tipos.json"
Ruta_Ataques = Path(__file__).parent.parent /"data"/"ataques.json"
Ruta_Pokemon = Path(__file__).parent.parent /"data"/"pokemon.json"

contiene_el_tipo = {"debilidades", "fortalezas", "inmunidades"}
contiene_los_ataques = {"Tipo", "Precision", "Potencia"}
contienen_los_pokemon = {"Tipo","Ps","Ataques","Defensa-Fs","Ataque-Fs"}


def cargar_tipos():
    with open(Ruta_Tipos, "r", encoding="utf-8") as f:
        datos = json.load(f)
    validar_tipos(datos) 
    return datos

def cargar_ataques(tipos:dict):
    with open(Ruta_Ataques, "r", encoding = "utf-8") as f:
        datos_ataques = json.load(f)
    validar_ataques(datos_ataques,tipos)
    return datos_ataques

def cargar_pokemon(tipos:dict, ataques:dict):
    with open(Ruta_Pokemon, "r", encoding = "utf-8") as f:
        datos_pkm = json.load(f)
    validar_pokemon(datos_pkm, tipos, ataques)
    return datos_pkm


def validar_tipos(tipos:dict): #tipos:dict solo marca que se quiere recibir un diccionario
    
    if not isinstance(tipos, dict):
        raise ValueError("error, no es dic")#validamos que sea un diccionario
    for nombre_tipo, info in tipos.items():
        if not isinstance(info, dict):
            raise ValueError(f"el {nombre_tipo} debe de ser un diccionario")#validamos que tenga otro dict dentro
    
        fort_debil = set(info.keys()) #Conjunto con las keys que hay dentro del tipo 
        validacion = contiene_el_tipo - fort_debil
        validacion2 = fort_debil - contiene_el_tipo
        if validacion2:
            raise ValueError(f"le sobran a {nombre_tipo}: {validacion2}")
        if validacion:
            raise ValueError(f"le faltan a {nombre_tipo}: {validacion}")

        for clave in contiene_el_tipo:
            if not isinstance(info[clave], list):
                raise ValueError(f"{clave} en {nombre_tipo} no es una lista")
        
def validar_ataques(ataque:dict, tipos:dict):
    if not isinstance(ataque, dict):
        raise ValueError("No es un diccionario")
    for nombre_ataque, datos in ataque.items():
        if not isinstance(datos, dict):
            raise ValueError(f"El {nombre_ataque} debe ser un dict")
        dentro_dict = set(datos.keys())
        
        validacion1 = dentro_dict - contiene_los_ataques
        validacion2 = contiene_los_ataques - dentro_dict
        
        if validacion1:
            raise ValueError(f"El ataque {nombre_ataque} le sobran {validacion1}")
        if validacion2:
            raise ValueError(f"El ataque {nombre_ataque} le faltan {validacion2}")
        if not(0 < datos["Precision"] < 101):
            raise ValueError(f"El ataque {nombre_ataque} tiene precision erronea {datos['Precision']}")
        if 0 > datos["Potencia"]:
            raise ValueError(f"El ataque {nombre_ataque} tiene potencia negativa {datos['Potencia']}")
        if datos["Tipo"] not in tipos:
            raise ValueError(f"El ataque {nombre_ataque} tiene un tipo inexistente {datos['Tipo']}")


def validar_pokemon(pokemones:dict, tipos:dict, ataques:dict):
    
    if not isinstance(pokemones, dict):
        raise ValueError(f"{pokemones} debe ser un dict")
    
    for nombre_pokemon, datos in pokemones.items():
        if not isinstance(datos, dict):
            raise ValueError(f"El pokemon {nombre_pokemon}, su dict esta mal :)") 
        
        stats_atk = set(datos.keys())
        validacion1 = stats_atk - contienen_los_pokemon
        validacion2 = contienen_los_pokemon - stats_atk
        
        if validacion1:
            raise ValueError(f"Al pokemon {nombre_pokemon} le sobran {validacion1}")
        if validacion2:
            raise ValueError(f"Al pokemon {nombre_pokemon} le faltan {validacion2}")
        
        if not isinstance(datos["Ps"], int):
            raise ValueError(f"El pokemon {nombre_pokemon} sus ps no son enteros")
        if 0 > datos["Ps"]:
            raise ValueError(f"Los ps del pokemon {nombre_pokemon} son negativos o nulos {datos['Ps']}")
        
        for tipos_del_pokemon in datos["Tipo"]:
            if tipos_del_pokemon not in tipos:
                raise ValueError(f"El {tipos_del_pokemon} no existe")
        
        if not isinstance(datos["Tipo"],list):
            raise ValueError(f"Los tipos del pokemon {nombre_pokemon} no son una lista")
        
        if not (0 < len(datos["Tipo"]) < 3): #Validar pokemon tenga 1 o 2 tipos
            raise ValueError(f"El pokemon {nombre_pokemon} no cumple con los tipos {datos['Tipo']}")
        
        if not isinstance(datos["Ataques"], list):
            raise ValueError(f"El pokemon {nombre_pokemon} no tiene una lista como ataques")    
        
        for atks in datos["Ataques"]: #Ataques existan
            if atks not in ataques:
                raise ValueError(f"El ataque {atks} no existe")
        
                
