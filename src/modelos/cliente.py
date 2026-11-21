import re

from modelos.entidad import Entidad


class Cliente(Entidad):
    """
    Representa un cliente de Software FJ.

    La clase hereda de Entidad y encapsula los datos personales del cliente.
    Las validaciones se ejecutan tanto al crear el objeto como al modificar
    posteriormente sus datos de contacto.
    """

    _PATRON_CORREO = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self, identificador, nombre, correo, telefono):
        # Se inicializa primero la parte heredada de Entidad.
        super().__init__(identificador)

        # Los datos personales se guardan como atributos privados para
        # aplicar encapsulación y controlar cualquier modificación.
        self.__nombre = self._validar_nombre(nombre)
        self.__correo = self._validar_correo(correo)
        self.__telefono = self._validar_telefono(telefono)

    @staticmethod
    def _validar_nombre(nombre):
        """Valida el nombre del cliente."""
        if nombre is None:
            raise ValueError("El nombre no puede ser nulo.")

        nombre = str(nombre).strip()

        if len(nombre) < 2 or len(nombre) > 80:
            raise ValueError(
                "El nombre debe tener entre 2 y 80 caracteres."
            )

        caracteres_validos = all(
            caracter.isalpha()
            or caracter.isspace()
            or caracter in "-'"
            for caracter in nombre
        )

        if not caracteres_validos:
            raise ValueError(
                "El nombre solo puede contener letras, espacios, guiones o apóstrofes."
            )

        return " ".join(nombre.split())

    @classmethod
    def _validar_correo(cls, correo):
        """Valida que el correo tenga una estructura básica válida."""
        if correo is None:
            raise ValueError("El correo no puede ser nulo.")

        correo = str(correo).strip().lower()

        if not correo:
            raise ValueError("El correo no puede estar vacío.")

        if len(correo) > 120:
            raise ValueError("El correo supera la longitud permitida.")

        if not cls._PATRON_CORREO.fullmatch(correo):
            raise ValueError("El formato del correo electrónico no es válido.")

        return correo

    @staticmethod
    def _validar_telefono(telefono):
        """Valida y normaliza el número telefónico."""
        if telefono is None:
            raise ValueError("El teléfono no puede ser nulo.")

        telefono = str(telefono).strip()

        if not telefono:
            raise ValueError("El teléfono no puede estar vacío.")

        telefono_normalizado = "".join(
            caracter for caracter in telefono if caracter.isdigit()
        )

        if len(telefono_normalizado) < 7 or len(telefono_normalizado) > 15:
            raise ValueError(
                "El teléfono debe contener entre 7 y 15 dígitos."
            )

        return telefono_normalizado

    @property
    def nombre(self):
        """Permite consultar el nombre encapsulado del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = self._validar_nombre(nuevo_nombre)

    @property
    def correo(self):
        """Permite consultar el correo encapsulado del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo):
        self.__correo = self._validar_correo(nuevo_correo)

    @property
    def telefono(self):
        """Permite consultar el teléfono encapsulado del cliente."""
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = self._validar_telefono(nuevo_telefono)

    def actualizar_contacto(self, correo=None, telefono=None):
        """
        Actualiza uno o ambos datos de contacto.
        """
        if correo is None and telefono is None:
            raise ValueError(
                "Debe proporcionar al menos un dato de contacto para actualizar."
            )

        if correo is not None:
            self.correo = correo

        if telefono is not None:
            self.telefono = telefono

    def obtener_resumen(self):
        """
        Implementa el método abstracto heredado de Entidad.
        """
        return (
            f"Cliente: {self.__nombre} | "
            f"ID: {self.identificador} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )

    def __str__(self):
        return self.obtener_resumen()
