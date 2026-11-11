#  Nicolas Rico 
# Importamos las clases que representan al cliente y al servicio
from src.modelos.cliente import Cliente 
from src.modelos.servicio import Servicio
class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

def __init__(self, codigo, cliente, servicio, horas_reservadas):
# Guardamos el código único de la reserva.
    self.__codigo = codigo

# Guardamos el cliente asociado a la reserva.
    self.__cliente = cliente

# Guardamos el servicio que se va a utilizar.
    self.__servicio = servicio

# Guardamos la cantidad de horas reservadas.
    self.__horas_reservadas = horas_reservadas

# Toda reserva comienza pendiente de confirmación.
    self.__estado = "Pendiente"

# Guardamos observaciones adicionales.
    self.__observaciones = ""
# consulta el código de la reserva.
    @property
    def codigo(self):
        return self.__codigo

# consulta el cliente asociado.
    @property
    def cliente_asignado(self):
        return self.__cliente

# consulta el servicio solicitado.
    @property
    def servicio_solicitado(self):
        return self.__servicio

# consulta las horas reservadas.
    @property
    def horas_reservadas(self):
        return self.__horas_reservadas

# consulta el estado de la reserva.
    @property
    def estado_actual(self):
        return self.__estado

# consulta las observaciones.
    @property
    def observaciones(self):
        return self.__observaciones