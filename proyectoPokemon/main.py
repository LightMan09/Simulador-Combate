from src.cargar_data import cargar_tipos, cargar_ataques, cargar_pokemon
from combat.combate import Pokemon
from combat.estado import ciclo_combate, Combate

if __name__ == "__main__":
    tipos = cargar_tipos()
    ataques = cargar_ataques(tipos)
    pokemones = cargar_pokemon(tipos, ataques)

    
    p1 = Pokemon("Charmander", pokemones["Charmander"])
    p2 = Pokemon("Bulbasour", pokemones["Bulbasour"])
    
    #(p1, p2, ataques, tipos, "Llamarada")
    
    #print(ciclo_combate("Placaje", p2, p1, ataques))
    c =Combate(p1,p2,ataques)
    print(c.inciar_combate())
   
    
"""
Siempre pasando tipos
real    0m0,726s
user    0m0,197s
sys     0m0,032s

Cargar tipos hasta que se usa
real    0m0,165s
user    0m0,140s
sys     0m0,025s"""