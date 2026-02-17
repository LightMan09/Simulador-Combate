def quemar(pokemon):
    menos = int(pokemon.get_daño_fs()/2)
    pokemon.set_daño_fs(menos)
    pokemon.set_estado(
        {
        "Quemado": {"PostTurno": pokemon.get_ps_max()/8,
                    "PreTurno": False},
        }
    )

def aplicar_preturno(pokemon_estado, nombre):
    pass
    for estado in pokemon_estado:
        preturno(estado)

def preturno(estado):
    pass