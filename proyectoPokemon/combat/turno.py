from src.daño import multiplicador_daño
import random

def turno(ataque_nombre:str,
          pokemon_defensor,
          pokemon_atacante,
          lista_ataques:dict
          ):
    
    ataque = lista_ataques[ataque_nombre]
    
    acierta = ataque["Precision"]
    
    if acertar(acierta):
        daño_final = multiplicador_daño(ataque_nombre, pokemon_defensor, pokemon_atacante, lista_ataques)

        pokemon_defensor.daño_recibido(daño_final)
        return f"Se hizo {daño_final}, al pokemon {pokemon_defensor.get_nombre()}, su ps restante es {pokemon_defensor.get_ps_actual()}"
    else:
        return f"el pokemon {pokemon_atacante.get_nombre()} fallo su ataque, los ps de {pokemon_defensor.get_nombre()} son {pokemon_defensor.get_ps_actual()} "
   
        
def acertar(precision: int):
    return random.randint(1, 100) <= precision
         