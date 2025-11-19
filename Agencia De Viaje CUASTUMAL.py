# Subject
class AgenciaDeViajes:
    def __init__(self):
        self.observadores = []
        self.promocion = None

    def agregar_observador(self, obs):
        self.observadores.append(obs)

    def eliminar_observador(self, obs):
        self.observadores.remove(obs)

    def notificar(self):
        for obs in self.observadores:
            obs.actualizar(self.promocion)

    def nueva_promocion(self, promo):
        self.promocion = promo
        print(f"\n[AGENCIA] Nueva promoción disponible: {promo}")
        self.notificar()


# Observer
class Cliente:
    def actualizar(self, promo):
        pass


# Observers concretos
class ClienteRegular(Cliente):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, promo):
        print(f"{self.nombre} recibió la promo: {promo}")


class ClienteVIP(Cliente):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, promo):
        print(f" VIP {self.nombre} recibe notificación PRIORITARIA: {promo}")


# Uso
agencia = AgenciaDeViajes()

cliente1 = ClienteRegular("cristian cuastumal")
cliente2 = ClienteVIP("María coral")

agencia.agregar_observador(cliente1)
agencia.agregar_observador(cliente2)

agencia.nueva_promocion("2x1 en Cartajena por tiempo limitado")
