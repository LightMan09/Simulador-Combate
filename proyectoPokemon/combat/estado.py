from combat.turno import turno

class Combate:
    def __init__(self, pokemon1, pokemon2, lista_ataques: dict):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.lista_ataques = lista_ataques
        
    def quien_primero(self):
        if self.pokemon1.get_velocidad() < self.pokemon2.get_velocidad():
            self.pokemon1, self.pokemon2 = self.pokemon2, self.pokemon1
    def escojer_ataque(self, pok):
        print(f"el pokemon {pok.get_nombre()} tiene: {pok.get_ataques()}")
        for i, at in enumerate(pok.get_ataques()):
            print(f"{i}; {at}")
        
        ataque = int(input("Ingrese el indice del ataque: "))
        
        if len(pok.get_ataques()) - 1 < ataque:
            raise IndexError(f"No existe el ataque numero {ataque}")
        if ataque < 0:
            raise ValueError(f"No existe el ataque numero {ataque}")
        return (pok.get_ataques())[ataque]
        
        
    def inciar_combate(self):
        
        self.quien_primero()
        
        while self.pokemon1.get_ps_actual() and self.pokemon2.get_ps_actual():
            print(turno(self.escojer_ataque(self.pokemon1), self.pokemon2, self.pokemon1, self.lista_ataques))
            self.pokemon1, self.pokemon2 = self.pokemon2, self.pokemon1
        if not self.pokemon1.get_ps_actual():
            return f"el pokemon {self.pokemon1.get_nombre()} quedo fuera de combate"
        elif not self.pokemon2.get_ps_actual():
            return f"el pokemon {self.pokemon2.get_nombre()} quedo fuera de combate"