from combat.turno import turno
def ciclo_combate(ataque_nombre:str,
                  pokemon_defensor,
                  pokemon_atacante,
                  lista_ataques:dict
                  ):
    
    pokemon_1 = pokemon_atacante
    pokemon_2 = pokemon_defensor
    
    while True:
        print(turno(ataque_nombre, pokemon_2, pokemon_1, lista_ataques))
        
        #print(turno(ataque_nombre, pokemon_2, pokemon_1, lista_pokemon, lista_ataques, tipos))
        pokemon_1, pokemon_2 = pokemon_2, pokemon_1
        if not pokemon_1.esta_vivo() or not pokemon_2.esta_vivo():
            break
    if not pokemon_1.esta_vivo():
        return f"El pokemon {pokemon_1.get_nombre()} ha caido en combate, gano {pokemon_2.get_nombre()}"
    elif not pokemon_2.esta_vivo():
        return f"El pokemon {pokemon_2.get_nombre()} ha caido en combate, gano {pokemon_1.get_nombre()}"

class Combate:
    def __init__(self, pokemon1, pokemon2, lista_ataques: dict):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.lista_ataques = lista_ataques
    def escojer_ataque(self, pok):
        print(f"el pokemon {pok.get_nombre()} tiene: {pok.get_ataques()}")
        for i, at in enumerate(pok.get_ataques()):
            print(f"{i}; {at}")
        ataque = int(input("Ingrese el indice del ataque: "))
        return (pok.get_ataques())[ataque]
        
        
    def inciar_combate(self):
        while self.pokemon1.get_ps_actual() and self.pokemon2.get_ps_actual():
            self.pokemon1, self.pokemon2 = self.pokemon2, self.pokemon1
            print(turno(self.escojer_ataque(self.pokemon1), self.pokemon2, self.pokemon1, self.lista_ataques))
        if not self.pokemon1.get_ps_actual():
            return f"el pokemon {self.pokemon1.get_nombre()} quedo fuera de combate"
        elif not self.pokemon2.get_ps_actual():
            return f"el pokemon {self.pokemon2.get_nombre()} quedo fuera de combate"