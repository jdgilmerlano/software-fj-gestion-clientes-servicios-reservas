"""
Punto de entrada e integración general del sistema Software FJ.

Este módulo integra los componentes desarrollados por el equipo.
No utiliza base de datos: toda la información se conserva en listas
internas durante la ejecución del programa.
"""

import os
from datetime import datetime
from pathlib import Path

# ------------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ------------------------------------------------------------
# Se fija como directorio de trabajo la raíz del proyecto.
# Esto garantiza que logs/sistema.log se utilice siempre en la
# ubicación correcta, independientemente de dónde se ejecute Python.
RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
os.chdir(RAIZ_PROYECTO)
(RAIZ_PROYECTO / "logs").mkdir(parents=True, exist_ok=True)

# Importación de los módulos desarrollados por los compañeros.
from modelos.cliente import Cliente
from modelos.reserva import Reserva, OperacionReservaError

from excepciones.excepciones_personalizadas import (
    DatoInvalidoError,
    OperacionNoPermitidaError,
    ParametroFaltanteError,
    ReservaInvalidaError,
    ServicioNoDisponibleError,
)

from utilidades.logger import (
    registrar_evento,
    registrar_excepcion,
)


class SistemaSoftwareFJ:
    """
    Clase de integración general del sistema.

    Coordina clientes, servicios y reservas mediante listas internas.
    También transforma errores de validación en las excepciones
    personalizadas definidas para el proyecto.
    """

    def __init__(self):
        # Estas listas almacenan los objetos durante la ejecución.
        # Se utilizan en lugar de una base de datos, tal como solicita
        # el enunciado de la actividad.
        self.clientes = []
        self.servicios = []
        self.reservas = []

        registrar_evento("Sistema Software FJ iniciado.")

    # ========================================================
    # GESTIÓN DE CLIENTES
    # ========================================================
    def crear_cliente(self, identificador, nombre, correo, telefono):
        """
        Crea y registra un cliente.

        Si Cliente detecta un dato inválido, el ValueError original
        se encadena dentro de DatoInvalidoError para conservar la
        causa real del error.
        """
        if self.buscar_cliente(identificador) is not None:
            raise DatoInvalidoError(
                f"Ya existe un cliente con identificador {identificador}."
            )

        try:
            cliente = Cliente(
                identificador,
                nombre,
                correo,
                telefono,
            )

        except ValueError as error:
            registrar_excepcion(
                f"No fue posible crear el cliente "
                f"{identificador}: {error}"
            )

            # Encadenamiento de excepciones.
            raise DatoInvalidoError(
                f"Datos inválidos para el cliente {identificador}."
            ) from error

        else:
            self.clientes.append(cliente)

            registrar_evento(
                f"Cliente {identificador} registrado correctamente."
            )

            return cliente

        finally:
            registrar_evento(
                f"Finalizó el intento de registro del cliente "
                f"{identificador}."
            )

    def buscar_cliente(self, identificador):
        """Busca un cliente por su identificador."""
        return next(
            (
                cliente
                for cliente in self.clientes
                if cliente.identificador == identificador
            ),
            None,
        )

    # ========================================================
    # GESTIÓN DE SERVICIOS
    # ========================================================
    def crear_servicio(self, clase_servicio, *args, **kwargs):
        """
        Crea y registra cualquier servicio especializado.

        El mismo método funciona con ReservaSala, AlquilerEquipo y
        Asesoria, aprovechando herencia y polimorfismo.
        """
        if clase_servicio is None:
            raise ParametroFaltanteError(
                "Debe indicarse la clase del servicio que se desea crear."
            )

        try:
            servicio = clase_servicio(*args, **kwargs)

        except (TypeError, ValueError) as error:
            registrar_excepcion(
                f"No fue posible crear un servicio: {error}"
            )

            raise DatoInvalidoError(
                "Los datos suministrados para el servicio "
                "no son válidos."
            ) from error

        else:
            if self.buscar_servicio(
                servicio.identificador
            ) is not None:
                raise DatoInvalidoError(
                    f"Ya existe un servicio con identificador "
                    f"{servicio.identificador}."
                )

            self.servicios.append(servicio)

            registrar_evento(
                f"Servicio {servicio.identificador} "
                "registrado correctamente."
            )

            return servicio

        finally:
            registrar_evento(
                "Finalizó un intento de creación de servicio."
            )

    def registrar_servicio(self, servicio):
        """Registra un servicio previamente construido."""
        if servicio is None:
            raise ParametroFaltanteError(
                "No se recibió un servicio para registrar."
            )

        if self.buscar_servicio(
            servicio.identificador
        ) is not None:
            raise DatoInvalidoError(
                f"Ya existe un servicio con identificador "
                f"{servicio.identificador}."
            )

        self.servicios.append(servicio)

        registrar_evento(
            f"Servicio {servicio.identificador} "
            "registrado correctamente."
        )

        return servicio

    def buscar_servicio(self, identificador):
        """Busca un servicio por su identificador."""
        return next(
            (
                servicio
                for servicio in self.servicios
                if servicio.identificador == identificador
            ),
            None,
        )

    def calcular_costo_servicio(
        self,
        servicio,
        unidades=1,
        descuento=0.0,
        recargo=0.0,
    ):
        """
        Ejecuta calcular_costo() sobre cualquier servicio.

        Los argumentos opcionales descuento y recargo permiten usar
        el mismo método con diferentes combinaciones de parámetros,
        simulando la sobrecarga solicitada en el ejercicio.
        """
        if servicio is None:
            raise ParametroFaltanteError(
                "Debe suministrarse un servicio para calcular el costo."
            )

        if not servicio.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {servicio.identificador} "
                "no está disponible."
            )

        try:
            return servicio.calcular_costo(
                unidades,
                descuento,
                recargo,
            )

        except ValueError as error:
            registrar_excepcion(
                f"Error calculando el costo del servicio "
                f"{servicio.identificador}: {error}"
            )

            raise DatoInvalidoError(
                "No fue posible calcular el costo con "
                "los valores recibidos."
            ) from error

    # ========================================================
    # GESTIÓN DE RESERVAS
    # ========================================================
    def crear_reserva(
        self,
        codigo,
        cliente,
        servicio,
        horas_reservadas,
    ):
        """Crea una reserva después de validar sus componentes."""
        if cliente is None:
            raise ParametroFaltanteError(
                "La reserva requiere un cliente."
            )

        if servicio is None:
            raise ParametroFaltanteError(
                "La reserva requiere un servicio."
            )

        if not servicio.disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {servicio.identificador} "
                "no está disponible."
            )

        if self.buscar_reserva(codigo) is not None:
            raise ReservaInvalidaError(
                f"Ya existe una reserva con código {codigo}."
            )

        try:
            reserva = Reserva(
                codigo,
                cliente,
                servicio,
                horas_reservadas,
            )

        except ValueError as error:
            registrar_excepcion(
                f"No fue posible crear la reserva "
                f"{codigo}: {error}"
            )

            raise ReservaInvalidaError(
                f"La reserva {codigo} contiene datos inválidos."
            ) from error

        else:
            self.reservas.append(reserva)

            registrar_evento(
                f"Reserva {codigo} creada correctamente."
            )

            return reserva

        finally:
            registrar_evento(
                f"Finalizó el intento de creación de la "
                f"reserva {codigo}."
            )

    def buscar_reserva(self, codigo):
        """Busca una reserva por su código."""
        return next(
            (
                reserva
                for reserva in self.reservas
                if reserva.codigo == codigo
            ),
            None,
        )

    def ejecutar_operacion_reserva(
        self,
        reserva,
        operacion,
    ):
        """
        Ejecuta confirmar, cancelar o procesar una reserva.

        La excepción propia del módulo Reserva se transforma en
        OperacionNoPermitidaError mediante encadenamiento.
        """
        if reserva is None:
            raise ParametroFaltanteError(
                "Debe suministrarse una reserva."
            )

        operaciones = {
            "confirmar": reserva.confirmar,
            "cancelar": reserva.cancelar,
            "procesar": reserva.procesar,
        }

        accion = str(operacion).strip().lower()

        if accion not in operaciones:
            raise OperacionNoPermitidaError(
                f"La operación '{operacion}' no está permitida."
            )

        try:
            resultado = operaciones[accion]()

        except OperacionReservaError as error:
            registrar_excepcion(
                f"Operación no permitida sobre la reserva "
                f"{reserva.codigo}: {error}"
            )

            raise OperacionNoPermitidaError(
                str(error)
            ) from error

        except ValueError as error:
            registrar_excepcion(
                f"Datos inválidos en la reserva "
                f"{reserva.codigo}: {error}"
            )

            raise ReservaInvalidaError(
                str(error)
            ) from error

        else:
            registrar_evento(
                f"Operación '{accion}' realizada sobre la "
                f"reserva {reserva.codigo}."
            )

            return resultado

        finally:
            registrar_evento(
                f"Finalizó la operación '{accion}' sobre la "
                f"reserva {reserva.codigo}."
            )

    # ========================================================
    # INFORMACIÓN GENERAL
    # ========================================================
    def obtener_totales(self):
        """Retorna la cantidad de objetos almacenados en memoria."""
        return {
            "clientes": len(self.clientes),
            "servicios": len(self.servicios),
            "reservas": len(self.reservas),
        }


def main():
    """Punto de inicio único del proyecto."""
    print("=" * 72)
    print("SOFTWARE FJ - SISTEMA INTEGRAL DE GESTIÓN")
    print("=" * 72)
    print(
        "Fecha y hora de ejecución:",
        datetime.now().strftime("%d/%m/%Y - %H:%M:%S"),
    )

    sistema = SistemaSoftwareFJ()

    # Se importa aquí para evitar dependencias circulares.
    from pruebas.simulacion_operaciones import ejecutar_simulacion

    ejecutar_simulacion(sistema)

    totales = sistema.obtener_totales()

    print("\n" + "=" * 72)
    print("RESUMEN FINAL")
    print("=" * 72)
    print(f"Clientes almacenados: {totales['clientes']}")
    print(f"Servicios almacenados: {totales['servicios']}")
    print(f"Reservas almacenadas: {totales['reservas']}")
    print(
        "Consulte logs/sistema.log para verificar "
        "los eventos y errores."
    )

    registrar_evento(
        "Sistema Software FJ finalizado correctamente."
    )


if __name__ == "__main__":
    main()
