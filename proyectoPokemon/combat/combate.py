class Pokemon:
    def __init__(self, nombre:str, datos:dict):
        self.nombre = nombre
        self.tipos = datos["Tipo"]
        self.ps_max = datos["Ps"]
        self.ps_actual = datos["Ps"]
        self.daño_fs = datos["Ataque-Fs"]
        self.defensa_fs = datos["Defensa-Fs"]
        self.ataques = datos["Ataques"]
        self.vivo = True
    def daño_recibido(self, daño:float):
        self.ps_actual -= int(daño)
        if self.ps_actual < 0:
            self.ps_actual = 0
    def esta_vivo(self) -> bool:
        if self.ps_actual <= 0:
            return False
        return True
    def get_nombre(self)-> str:
        return self.nombre
    def get_tipos(self)-> list:
        return self.tipos
    def get_ps_max(self)-> int:
        return self.ps_max
    def get_ps_actual(self)->int:
        return self.ps_actual
    def get_daño_fs(self)-> int:
        return self.daño_fs
    def get_defensa_fs(self)-> int:
        return self.defensa_fs
    def get_ataques(self)->list:
        return self.ataques
    def get_ataques(self)-> list:
        return self.ataques
