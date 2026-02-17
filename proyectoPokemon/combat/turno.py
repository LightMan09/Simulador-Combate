from src.daño import multiplicador_daño
from combat.efectos import *
import random

def turno(ataque_nombre:str,
          pokemon_defensor,
          pokemon_atacante,
          lista_ataques:dict
          ):
    
        
    ataque = lista_ataques[ataque_nombre]
    
    acierta = ataque["Precision"]
    
    
    if isinstance(ataque["Efecto-Secundario"], dict):
        efecto(ataque["Efecto-Secundario"], pokemon_defensor)  
    
    aplicar_preturno(pokemon_defensor.get_estado(), pokemon_defensor.get_nombre())
    
    
    if acertar(acierta):
        critic = critico()
        daño_final = int(multiplicador_daño(ataque_nombre, pokemon_defensor, pokemon_atacante, lista_ataques)*critic)
        if critic > 1:
            print(f"El pokemon {pokemon_atacante.get_nombre()} hizo critico")
        pokemon_defensor.daño_recibido(daño_final)
        return f"Se uso {ataque_nombre} y se hizo {daño_final}, al pokemon {pokemon_defensor.get_nombre()}, su ps restante es {pokemon_defensor.get_ps_actual()}"
    else:
        return f"el se uso {ataque_nombre} y el pokemon {pokemon_atacante.get_nombre()} fallo su ataque, los ps de {pokemon_defensor.get_nombre()} son {pokemon_defensor.get_ps_actual()} "
   
        
def acertar(precision: int) -> bool:
    return random.randint(1, 100) <= precision

def critico() -> float: 
    return 1.5 if random.randint(0,100) <= 4 else 1.0

def efecto(tipoDeEfecto, pokemon_defen):
    
    if random.randint(0, 100) < tipoDeEfecto["Probabilidad"] + 1:
        if tipoDeEfecto["Estado"] == "Quemar":
            quemar(pokemon_defen)