
# Nicolas Rico
# Gestion de reservas - Software FJ


# Importamos las herramientas que necesitamos para guardar los eventos y errores.
import logging
from pathlib import Path


# Buscamos la carpeta logs del proyecto y la creamos si todavía no existe.
RUTA_LOGS = Path(__file__).resolve().parents[2] / "logs"
RUTA_LOGS.mkdir(parents=True, exist_ok=True)


# Preparamos el registro para guardar lo que sucede con las reservas.
logger = logging.getLogger("reservas")

if not logger.handlers:
    archivo_log = logging.FileHandler(RUTA_LOGS / "sistema.log",encoding="utf-8")

    # Organizamos los registros para que muestren la fecha, el tipo y el mensaje.
    formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    archivo_log.setFormatter(formato)
    logger.addHandler(archivo_log)
    logger.setLevel(logging.INFO)

# Creamos un error propio para identificar operaciones no permitidas.
class OperacionReservaError(Exception):
    """Se utiliza cuando una operación de reserva no está permitida."""
    pass


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

# Comprobamos que las horas sean un número mayor que cero.
        if (isinstance(horas_reservadas, bool)or not isinstance(horas_reservadas, (int, float))or horas_reservadas <= 0):
            raise ValueError("Las horas reservadas deben ser un número mayor que cero.")

# Guardamos los datos principales de la reserva.
        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__horas_reservadas = horas_reservadas

 # Toda reserva comienza pendiente de confirmación.
        self.__estado = "Pendiente"
# Dejamos este espacio para guardar las observaciones del cliente.
        self.__observaciones = ""
 # Consultamos el código de la reserva.
    @property
    def codigo(self):
        return self.__codigo

# Consultamos el cliente que tiene asignada la reserva.
    @property
    def cliente_asignado(self):
        return self.__cliente

# Consultamos el servicio que se ha solicitado.
    @property
    def servicio_solicitado(self):
        return self.__servicio

# Consultamos la cantidad de horas reservadas.
    @property
    def horas_reservadas(self):
        return self.__horas_reservadas

 # Consultamos el estado actual de la reserva.
    @property
    def estado_actual(self):
        return self.__estado

# Consultamos las observaciones que se han registrado.
    @property
    def observaciones(self):
        return self.__observaciones
 
#   Confirmamos la reserva cuando todavía está pendiente.
    def confirmar(self):
        if self.__estado != "Pendiente":raise OperacionReservaError(
                "No se puede confirmar una reserva que no esté pendiente.")

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

#  Permitimos cancelar únicamente las reservas pendientes.
    def cancelar(self):
        if self.__estado != "Pendiente":raise OperacionReservaError("Solo se pueden cancelar reservas pendientes.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

  # Procesamos la reserva cuando ya ha sido confirmada.
    def procesar(self):
        if self.__estado != "Confirmada":raise OperacionReservaError("Solo se pueden procesar reservas confirmadas.")

        self.__estado = "Procesada"
        return "Reserva procesada correctamente."

# Agregamos una observación para dejar constancia de algún detalle.
    def agregar_observacion(self, observacion):

        if not isinstance(observacion, str) or not observacion.strip():return "La observación no puede estar vacía."

# Si ya existe una observación, añadimos la nueva sin borrar la anterior.
        if self.__observaciones:
            self.__observaciones += " | " + observacion.strip()
        else:
            self.__observaciones = observacion.strip()

        return "Observación agregada correctamente."

# Permitimos cambiar las horas mientras la reserva siga pendiente.
    def modificar_horas(self, nuevas_horas):

        if self.__estado != "Pendiente":raise OperacionReservaError("Solo se pueden modificar reservas pendientes.")

# Revisamos que las nuevas horas sean válidas.
        if (isinstance(nuevas_horas, bool)or not isinstance(nuevas_horas, (int, float))or nuevas_horas <= 0):
            raise ValueError("Las horas deben ser un número mayor que cero.")

        self.__horas_reservadas = nuevas_horas
        return "Las horas de la reserva se actualizaron correctamente."

# Mostramos en un solo resultado los datos principales de la reserva.
    def obtener_resumen(self):
        return (
            f"Código: {self.__codigo}\n"
            f"Cliente: {self.__cliente}\n"
            f"Servicio: {self.__servicio}\n"
            f"Horas reservadas: {self.__horas_reservadas}\n"
            f"Estado: {self.__estado}\n"
            f"Observaciones: {self.__observaciones}" )

 # Ejecutamos una operación y guardamos lo que suceda durante el proceso.
    def ejecutar_operacion(self, operacion):

        try:
            resultado = operacion()

        except OperacionReservaError as error:
# Guardamos el intento de realizar una operación no permitida.
            logger.exception(f"Operación no permitida en la reserva {self.__codigo}: {error}")
            return f"Operación no permitida: {error}"

        except ValueError as error:
# Dejamos registrado cuando se presentan datos incorrectos.
            logger.exception(
                f"Datos incorrectos en la reserva {self.__codigo}: {error}")
            return f"Datos incorrectos: {error}"

        except Exception as error:
            # Registramos cualquier otro error que no hayamos previsto.
            logger.exception(
                f"Error inesperado en la reserva {self.__codigo}: {error}")
            return "Ocurrió un error inesperado al gestionar la reserva."

        else:
# Cuando todo sale bien, también dejamos constancia de la operación.
            logger.info(
                f"Operación realizada correctamente en la reserva {self.__codigo}.")
            return resultado

        finally:
             # Registramos que el intento de operación ha finalizado.
            logger.info(
                f"Finalizó el intento de operación para la reserva {self.__codigo}.")
