# Componente de servicios - Compañero 2
from modelos.servicio import Servicio


class AlquilerEquipo(Servicio):

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        tipo_equipo,
        disponible=True,
        dias_garantia=1,
    ):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        self.__tipo_equipo = self._validar_tipo_equipo(tipo_equipo)
        self.__dias_garantia = self._validar_dias_garantia(dias_garantia)

    @staticmethod
    def _validar_tipo_equipo(tipo_equipo):
        if tipo_equipo is None:
            raise ValueError("El tipo de equipo no puede ser nulo.")
        tipo_limpio = " ".join(str(tipo_equipo).strip().split())
        if len(tipo_limpio) < 2 or len(tipo_limpio) > 60:
            raise ValueError("El tipo de equipo debe tener entre 2 y 60 caracteres.")
        return tipo_limpio

    @staticmethod
    def _validar_dias_garantia(dias_garantia):
        if isinstance(dias_garantia, bool) or not isinstance(dias_garantia, int):
            raise ValueError("Los días de garantía deben ser un número entero.")
        if dias_garantia < 0:
            raise ValueError("Los días de garantía no pueden ser negativos.")
        return dias_garantia

    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    @tipo_equipo.setter
    def tipo_equipo(self, nuevo_tipo):
        self.__tipo_equipo = self._validar_tipo_equipo(nuevo_tipo)

    @property
    def dias_garantia(self):
        return self.__dias_garantia

    @dias_garantia.setter
    def dias_garantia(self, nuevos_dias):
        self.__dias_garantia = self._validar_dias_garantia(nuevos_dias)

    def calcular_costo(self, unidades=1, descuento=0.0, recargo=0.0):
        """Calcula el costo total según unidades/períodos de alquiler."""
        unidades_validadas = self._validar_unidades(unidades)
        descuento_validado = self._validar_porcentaje(descuento, "El descuento")
        recargo_validado = self._validar_recargo(recargo)

        subtotal = (self.tarifa_base * unidades_validadas) + recargo_validado
        total = subtotal * (1.0 - descuento_validado)
        return round(total, 2)

    def describir(self):
        return (
            f"[Equipo] {self.nombre} (ID: {self.identificador}) | "
            f"Tipo: {self.__tipo_equipo} | Garantía: {self.__dias_garantia} día(s) | "
            f"Tarifa base: ${self.tarifa_base:,.2f}"
        )