
# Nicolas Rico
# Gestion de reservas - Software FJ

class Reserva:
    """
    Representa una reserva realizada por un cliente
    para utilizar un servicio de Software FJ.
    """

    def __init__(self, codigo, cliente, servicio, horas_reservadas):

# Antes de crear la reserva, revisamos que los datos estén completos.
        if not codigo or not str(codigo).strip():raise ValueError("El código de la reserva no puede estar vacío.")

        if cliente is None:raise ValueError("La reserva debe tener un cliente asignado.")

        if servicio is None:raise ValueError("La reserva debe tener un servicio asignado.")

# Las horas deben ser un número mayor que cero.
        if isinstance(horas_reservadas, bool) or not isinstance(horas_reservadas, (int, float)) or horas_reservadas <= 0:raise ValueError("Las horas reservadas deben ser un número mayor que cero.")
        
# Guardamos el codigo unico de la reserva.
        self.__codigo = codigo

# Guardamos el cliente asociado.
        self.__cliente = cliente

# Guardamos el servicio solicitado.
        self.__servicio = servicio

# Guardamos la cantidad de horas reservadas.
        self.__horas_reservadas = horas_reservadas

# Toda reserva comienza pendiente de confirmacion.
        self.__estado = "Pendiente"

# Guardamos observaciones adicionales.
        self.__observaciones = ""

# Consultamos el codigo de la reserva.
    @property
    def codigo(self):return self.__codigo

# Consultamos el cliente asociado.
    @property
    def cliente_asignado(self):return self.__cliente

# Consultamos el servicio solicitado.
    @property
    def servicio_solicitado(self):return self.__servicio

# Consultamos las horas reservadas.
    @property
    def horas_reservadas(self):return self.__horas_reservadas

 # Consultamos el estado de la reserva.
    @property
    def estado_actual(self): return self.__estado

# Consultamos las observaciones.
    @property
    def observaciones(self):return self.__observaciones

# Confirmamos una reserva pendiente.
    def confirmar(self):
        if self.__estado == "Pendiente":
            self.__estado = "Confirmada"
            return "Reserva confirmada correctamente."
        else:return "No se puede confirmar esta reserva."

# Cancelamos una reserva pendiente.
    def cancelar(self):
        if self.__estado == "Pendiente":
            self.__estado = "Cancelada"
            return "Reserva cancelada correctamente."
        else:return "No se puede cancelar esta reserva."
# Procesamos la reserva cuando ya ha sido confirmada.
    def procesar(self):
        if self.__estado == "Confirmada":
            self.__estado = "Procesada"
            return "Reserva procesada correctamente."
        else:return "Solo se pueden procesar reservas confirmadas."
# Agregamos una observación para dejar constancia de algún detalle.
    def agregar_observacion(self, observacion):

        if not observacion or not observacion.strip():return "La observación no puede estar vacía."

        if self.__observaciones:self.__observaciones += " | " + observacion
        else:self.__observaciones = observacion
        return "Observación agregada correctamente."