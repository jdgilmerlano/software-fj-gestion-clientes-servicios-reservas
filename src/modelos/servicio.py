# Componente de servicios - Compañero 2
from abc import abstractmethod

from modelos.entidad import Entidad


class Servicio(Entidad):

    def __init__(self, identificador, nombre, tarifa_base, disponible=True):
        super().__init__(identificador)
        self.__nombre = self._validar_nombre(nombre)
        self.__tarifa_base = self._validar_tarifa_base(tarifa_base)
        self.__disponible = self._validar_disponible(disponible)

    @staticmethod
    def _validar_nombre(nombre):
        if nombre is None:
            raise ValueError("El nombre del servicio no puede ser nulo.")

        nombre_limpio = " ".join(str(nombre).strip().split())
        if len(nombre_limpio) < 3 or len(nombre_limpio) > 100:
            raise ValueError("El nombre del servicio debe tener entre 3 y 100 caracteres.")

        return nombre_limpio

    @staticmethod
    def _validar_tarifa_base(tarifa_base):
        if isinstance(tarifa_base, bool) or not isinstance(tarifa_base, (int, float)):
            raise ValueError("La tarifa base debe ser un valor numérico.")

        tarifa = float(tarifa_base)
        if tarifa <= 0:
            raise ValueError("La tarifa base debe ser mayor que cero.")

        return round(tarifa, 2)

    @staticmethod
    def _validar_disponible(disponible):
        if not isinstance(disponible, bool):
            raise ValueError("La disponibilidad debe ser un valor booleano (True o False).")

        return disponible

    @staticmethod
    def _validar_unidades(unidades):
        if isinstance(unidades, bool) or not isinstance(unidades, int):
            raise ValueError("Las unidades/duración deben ser un número entero.")
        if unidades <= 0:
            raise ValueError("Las unidades/duración deben ser mayores que cero.")
        return unidades

    @staticmethod
    def _validar_porcentaje(valor, nombre_parametro):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ValueError(f"{nombre_parametro} debe ser un valor numérico.")
        porcentaje = float(valor)
        if porcentaje < 0.0 or porcentaje >= 1.0:
            raise ValueError(f"{nombre_parametro} debe estar entre 0.0 (inclusive) y 1.0 (exclusive).")
        return porcentaje

    @staticmethod
    def _validar_recargo(recargo):
        if isinstance(recargo, bool) or not isinstance(recargo, (int, float)):
            raise ValueError("El recargo adicional debe ser un valor numérico.")
        monto = float(recargo)
        if monto < 0:
            raise ValueError("El recargo adicional no puede ser negativo.")
        return round(monto, 2)

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = self._validar_nombre(nuevo_nombre)

    @property
    def tarifa_base(self):
        return self.__tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, nueva_tarifa):
        self.__tarifa_base = self._validar_tarifa_base(nueva_tarifa)

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, estado):
        self.__disponible = self._validar_disponible(estado)

    @abstractmethod
    def calcular_costo(self, unidades=1, descuento=0.0, recargo=0.0):
        """
        Calcula el costo total de un servicio.
        Permite simular sobrecarga mediante parámetros opcionales.
        """
        pass

    @abstractmethod
    def describir(self):
        """Retorna una descripción detallada del servicio especializado."""
        pass

    def obtener_resumen(self):
        """Implementa el método abstracto heredado de Entidad."""
        estado = "Disponible" if self.__disponible else "No disponible"
        return (
            f"Servicio: {self.__nombre} | "
            f"ID: {self.identificador} | "
            f"Tarifa base: ${self.__tarifa_base:,.2f} | "
            f"Estado: {estado}"
        )

    def __str__(self):
        return self.describir()