# Componente de servicios - Compañero 2
from modelos.servicio import Servicio


class Asesoria(Servicio):
    """Servicio especializado para asesorías técnicas o profesionales."""

    _MODALIDADES_VALIDAS = ("PRESENCIAL", "VIRTUAL", "HIBRIDA")

    def __init__(
        self,
        identificador,
        nombre,
        tarifa_base,
        especialidad,
        disponible=True,
        modalidad="VIRTUAL",
    ):
        super().__init__(identificador, nombre, tarifa_base, disponible)
        self.__especialidad = self._validar_especialidad(especialidad)
        self.__modalidad = self._validar_modalidad(modalidad)

    @staticmethod
    def _validar_especialidad(especialidad):
        if especialidad is None:
            raise ValueError("La especialidad no puede ser nula.")
        especialidad_limpia = " ".join(str(especialidad).strip().split())
        if len(especialidad_limpia) < 3 or len(especialidad_limpia) > 80:
            raise ValueError("La especialidad debe tener entre 3 y 80 caracteres.")
        return especialidad_limpia

    @classmethod
    def _validar_modalidad(cls, modalidad):
        if modalidad is None:
            raise ValueError("La modalidad no puede ser nula.")
        modalidad_norm = str(modalidad).strip().upper()
        if modalidad_norm not in cls._MODALIDADES_VALIDAS:
            raise ValueError(
                f"Modalidad inválida. Use una de: {', '.join(cls._MODALIDADES_VALIDAS)}."
            )
        return modalidad_norm

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, nueva_especialidad):
        self.__especialidad = self._validar_especialidad(nueva_especialidad)

    @property
    def modalidad(self):
        return self.__modalidad

    @modalidad.setter
    def modalidad(self, nueva_modalidad):
        self.__modalidad = self._validar_modalidad(nueva_modalidad)

    def calcular_costo(self, unidades=1, descuento=0.0, recargo=0.0):
        """Calcula el costo total según horas/sesiones de asesoría."""
        unidades_validadas = self._validar_unidades(unidades)
        descuento_validado = self._validar_porcentaje(descuento, "El descuento")
        recargo_validado = self._validar_recargo(recargo)

        recargo_presencial = 20000.0 if self.__modalidad == "PRESENCIAL" else 0.0
        subtotal = (self.tarifa_base * unidades_validadas) + recargo_presencial + recargo_validado
        total = subtotal * (1.0 - descuento_validado)
        return round(total, 2)

    def describir(self):
        return (
            f"[Asesoría] {self.nombre} (ID: {self.identificador}) | "
            f"Especialidad: {self.__especialidad} | Modalidad: {self.__modalidad} | "
            f"Tarifa base: ${self.tarifa_base:,.2f}"
        )