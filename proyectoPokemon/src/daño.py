from src.cargar_data import cargar_tipos
def cargar_daño(ataque_tipo:str, pokemon_defensor_tipo, tipos:dict)-> float:
    
    
    if ataque_tipo not in tipos:
        raise ValueError(f"No existe el tipo {ataque_tipo}")
    if pokemon_defensor_tipo not in tipos:
        raise ValueError(f"El tipo {pokemon_defensor_tipo} no existe")
    caract_defensor = tipos[pokemon_defensor_tipo]
    if ataque_tipo in caract_defensor["debilidad"]:
        print("El ataque es super efectivo")
        return 2.0
    if ataque_tipo in caract_defensor["resistencias"]:
        print("El ataque es poco efectivo")
        return 0.5
    if ataque_tipo in caract_defensor["inmunidades"]:
        print("El ataque no hace daño")
        return 0
    else:
        return 1
    
    
        
def multiplicador_daño(nombre_ataque:str, pokemon_defensor, pokemon_atacante, lista_ataques:dict)->float:
    tipos = cargar_tipos()
    atk = lista_ataques[nombre_ataque]
    
    
    atk_cat = atk["Categoria"]
    daño = 1
    
    for t in pokemon_defensor.get_tipos():
        daño *= cargar_daño(atk["Tipo"], t, tipos)#tipo ataque, tipo defensa, tipos
    
    
    match atk_cat:
        case "Fisico":
            daño *= 42*atk["Potencia"]*pokemon_atacante.get_daño_fs()/pokemon_defensor.get_defensa_fs()
        case "Especial":
            daño *= 42*atk["Potencia"]*pokemon_atacante.get_daño_ep()/pokemon_defensor.get_defensa_ep()
        
            
    
    return (daño/50) + 2



       
