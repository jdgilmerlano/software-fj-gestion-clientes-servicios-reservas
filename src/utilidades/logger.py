# Manejo de excepciones y logs - Compañero 4
import logging


# Configuración del archivo de logs
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    """Registra un evento informativo del sistema."""
    logging.info(mensaje)


def registrar_error(mensaje):
    """Registra un error ocurrido en el sistema."""
    logging.error(mensaje)


def registrar_advertencia(mensaje):
    """Registra una advertencia del sistema."""
    logging.warning(mensaje)
  
