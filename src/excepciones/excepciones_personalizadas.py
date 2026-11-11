# Manejo de excepciones y logs - Compañero 4
class ErrorSistema(Exception):
    """Excepción base para los errores del sistema."""
    pass


class DatoInvalidoError(ErrorSistema):
    """Se genera cuando un dato no cumple las validaciones."""
    pass


class ParametroFaltanteError(ErrorSistema):
    """Se genera cuando falta un parámetro obligatorio."""
    pass


class OperacionNoPermitidaError(ErrorSistema):
    """Se genera cuando se intenta realizar una operación no permitida."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class ReservaInvalidaError(ErrorSistema):
    """Se genera cuando una reserva no cumple las condiciones requeridas."""
    pass
