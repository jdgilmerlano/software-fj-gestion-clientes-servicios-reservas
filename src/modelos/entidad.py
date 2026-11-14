from abc import ABC, abstractmethod


class Entidad(ABC):
    """
    Clase abstracta base para las entidades principales del sistema.

    Su propósito es definir características y comportamientos comunes que
    pueden ser reutilizados por otras clases, aplicando abstracción y
    favoreciendo una estructura modular orientada a objetos.
    """

    def __init__(self, identificador):
        # El identificador se almacena de forma encapsulada para evitar que
        # sea modificado directamente desde otras partes del programa.
        self.__identificador = self._validar_identificador(identificador)

    @staticmethod
    def _validar_identificador(identificador):
        """
        Valida que el identificador sea una cadena no vacía y que contenga
        únicamente letras, números o guiones.

        Retorna el identificador normalizado cuando es válido.
        """
        if identificador is None:
            raise ValueError("El identificador no puede ser nulo.")

        identificador = str(identificador).strip()

        if not identificador:
            raise ValueError("El identificador no puede estar vacío.")

        if len(identificador) < 3 or len(identificador) > 20:
            raise ValueError(
                "El identificador debe tener entre 3 y 20 caracteres."
            )

        if not all(
            caracter.isalnum() or caracter == "-"
            for caracter in identificador
        ):
            raise ValueError(
                "El identificador solo puede contener letras, números o guiones."
            )

        return identificador

    @property
    def identificador(self):
        """Permite consultar el identificador sin exponer el atributo privado."""
        return self.__identificador

    def obtener_identificador(self):
        """Retorna el identificador de la entidad."""
        return self.__identificador

    @abstractmethod
    def obtener_resumen(self):
        """
        Método abstracto que obliga a las clases derivadas a proporcionar
        una representación resumida de sus datos principales.
        """
        pass
