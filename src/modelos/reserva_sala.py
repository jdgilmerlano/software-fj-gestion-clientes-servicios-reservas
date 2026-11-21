# Componente de servicios - Compañero 2
from modelos.servicio import Servicio


class ReservaSala(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        capacidad,
        disponible=True,
        incluye_proyector=False,
    ):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        self.__capacidad = self._validar_capacidad(capacidad)
        self.__incluye_proyector = self._validar_proyector(incluye_proyector)

    @staticmethod
    def _validar_capacidad(capacidad):
        if isinstance(capacidad, bool) or not isinstance(capacidad, int):
            raise ValueError("La capacidad de la sala debe ser un número entero.")
        if capacidad <= 0:
            raise ValueError("La capacidad de la sala debe ser mayor que cero.")
        return capacidad

    @staticmethod
    def _validar_proyector(incluye_proyector):
        if not isinstance(incluye_proyector, bool):
            raise ValueError("El campo 'incluye_proyector' debe ser booleano.")
        return incluye_proyector

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, nueva_capacidad):
        self.__capacidad = self._validar_capacidad(nueva_capacidad)

    @property
    def incluye_proyector(self):
        return self.__incluye_proyector

    @incluye_proyector.setter
    def incluye_proyector(self, valor):
        self.__incluye_proyector = self._validar_proyector(valor)

    def calcular_costo(self, unidades=1, descuento=0.0, recargo=0.0):
        """Calcula el costo total por bloques/horas de sala."""
        unidades_validadas = self._validar_unidades(unidades)
        descuento_validado = self._validar_porcentaje(descuento, "El descuento")
        recargo_validado = self._validar_recargo(recargo)

        extra_proyector = 15000.0 if self.__incluye_proyector else 0.0
        subtotal = (self.tarifa_base * unidades_validadas) + extra_proyector + recargo_validado
        total = subtotal * (1.0 - descuento_validado)
        return round(total, 2)

    def describir(self):
        proyector_texto = "Con proyector" if self.__incluye_proyector else "Sin proyector"
        return (
            f"[Sala] {self.nombre} (ID: {self.identificador}) | "
            f"Capacidad: {self.__capacidad} personas | {proyector_texto} | "
            f"Tarifa base: ${self.tarifa_base:,.2f}"
        )