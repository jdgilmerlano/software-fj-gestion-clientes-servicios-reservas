"""
Simulación integral de operaciones del sistema Software FJ.

Se ejecutan casos válidos e inválidos para comprobar que el programa
continúa funcionando después de los errores y que las excepciones
son manejadas de forma controlada.
"""

from modelos.alquiler_equipo import AlquilerEquipo
from modelos.asesoria import Asesoria
from modelos.reserva_sala import ReservaSala

from excepciones.excepciones_personalizadas import ErrorSistema

from utilidades.logger import (
    registrar_error,
    registrar_evento,
)


def _mostrar_operacion(numero, titulo):
    """Muestra el encabezado de cada caso de prueba."""
    print(f"\n[{numero:02d}] {titulo}")
    print("-" * 72)


def _ejecutar_controlado(
    numero,
    titulo,
    funcion,
):
    """
    Ejecuta una prueba evitando que un error detenga el sistema.

    Este bloque demuestra:
    - try/except
    - try/except/else
    - try/except/finally
    """
    _mostrar_operacion(numero, titulo)

    try:
        resultado = funcion()

    except ErrorSistema as error:
        print(f"ERROR CONTROLADO: {error}")

        registrar_error(
            f"Operación {numero} controlada con error: {error}"
        )

        return None

    except Exception as error:
        # La captura general mantiene activo el programa incluso
        # ante un error inesperado.
        print(f"ERROR INESPERADO CONTROLADO: {error}")

        registrar_error(
            f"Operación {numero} produjo un error "
            f"inesperado: {error}"
        )

        return None

    else:
        if resultado is not None:
            # Cuando el objeto posee obtener_resumen(), se presenta
            # una salida legible en lugar de su dirección de memoria.
            if hasattr(resultado, "obtener_resumen"):
                print(resultado.obtener_resumen())
            else:
                print(resultado)

        registrar_evento(
            f"Operación {numero} completada correctamente: "
            f"{titulo}"
        )

        return resultado

    finally:
        print(
            "Estado: operación finalizada; "
            "el sistema continúa activo."
        )


def ejecutar_simulacion(sistema):
    """
    Ejecuta quince operaciones.

    El enunciado exige al menos diez. Se incluyen casos adicionales
    para demostrar confirmación, procesamiento, cancelación,
    polimorfismo, sobrecarga simulada y errores de cálculo.
    """

    print("\nINICIO DE LA SIMULACIÓN DE OPERACIONES")

    # ========================================================
    # 1. REGISTRO VÁLIDO DE CLIENTE
    # ========================================================
    cliente_1 = _ejecutar_controlado(
        1,
        "Registro válido de cliente",
        lambda: sistema.crear_cliente(
            "CLI-001",
            "Ana Torres",
            "ana.torres@email.com",
            "3001234567",
        ),
    )

    # ========================================================
    # 2. REGISTRO INVÁLIDO DE CLIENTE
    # ========================================================
    _ejecutar_controlado(
        2,
        "Registro inválido de cliente",
        lambda: sistema.crear_cliente(
            "X",
            "",
            "correo-invalido",
            "12",
        ),
    )

    # ========================================================
    # 3. SERVICIO DE SALA VÁLIDO
    # ========================================================
    sala = _ejecutar_controlado(
        3,
        "Creación correcta de servicio de reserva de sala",
        lambda: sistema.crear_servicio(
            ReservaSala,
            "SAL-001",
            "Sala Ejecutiva",
            80000,
            12,
            True,
            True,
        ),
    )

    # ========================================================
    # 4. SERVICIO INVÁLIDO
    # ========================================================
    _ejecutar_controlado(
        4,
        "Creación incorrecta de servicio",
        lambda: sistema.crear_servicio(
            ReservaSala,
            "SAL-ERR",
            "Sala inválida",
            -5000,
            0,
            True,
            False,
        ),
    )

    # ========================================================
    # 5. ALQUILER DE EQUIPO VÁLIDO
    # ========================================================
    equipo = _ejecutar_controlado(
        5,
        "Creación correcta de alquiler de equipo",
        lambda: sistema.crear_servicio(
            AlquilerEquipo,
            "EQ-001",
            "Portátil profesional",
            120000,
            "Computador portátil",
            True,
            2,
        ),
    )

    # ========================================================
    # 6. ASESORÍA VÁLIDA
    # ========================================================
    asesoria = _ejecutar_controlado(
        6,
        "Creación correcta de asesoría especializada",
        lambda: sistema.crear_servicio(
            Asesoria,
            "ASE-001",
            "Asesoría de arquitectura",
            150000,
            "Arquitectura de software",
            True,
            "VIRTUAL",
        ),
    )

    # ========================================================
    # 7. RESERVA VÁLIDA
    # ========================================================
    reserva_1 = _ejecutar_controlado(
        7,
        "Creación de reserva válida",
        lambda: sistema.crear_reserva(
            "RES-001",
            cliente_1,
            sala,
            3,
        ),
    )

    # ========================================================
    # 8. SERVICIO NO DISPONIBLE
    # ========================================================
    servicio_no_disponible = sistema.crear_servicio(
        ReservaSala,
        "SAL-002",
        "Sala de contingencia",
        60000,
        8,
        False,
        False,
    )

    _ejecutar_controlado(
        8,
        "Intento de reserva sobre servicio no disponible",
        lambda: sistema.crear_reserva(
            "RES-002",
            cliente_1,
            servicio_no_disponible,
            2,
        ),
    )

    # ========================================================
    # 9. CONFIRMACIÓN DE RESERVA
    # ========================================================
    _ejecutar_controlado(
        9,
        "Confirmación de una reserva pendiente",
        lambda: sistema.ejecutar_operacion_reserva(
            reserva_1,
            "confirmar",
        ),
    )

    # ========================================================
    # 10. PROCESAMIENTO DE RESERVA
    # ========================================================
    _ejecutar_controlado(
        10,
        "Procesamiento de una reserva confirmada",
        lambda: sistema.ejecutar_operacion_reserva(
            reserva_1,
            "procesar",
        ),
    )

    # ========================================================
    # 11. OPERACIÓN NO PERMITIDA
    # ========================================================
    _ejecutar_controlado(
        11,
        "Intento de cancelar una reserva ya procesada",
        lambda: sistema.ejecutar_operacion_reserva(
            reserva_1,
            "cancelar",
        ),
    )

    # ========================================================
    # 12. CANCELACIÓN VÁLIDA
    # ========================================================
    def crear_y_cancelar_reserva():
        reserva_2 = sistema.crear_reserva(
            "RES-003",
            cliente_1,
            equipo,
            1,
        )

        return sistema.ejecutar_operacion_reserva(
            reserva_2,
            "cancelar",
        )

    _ejecutar_controlado(
        12,
        "Creación y cancelación válida de una reserva",
        crear_y_cancelar_reserva,
    )

    # ========================================================
    # 13. POLIMORFISMO SOBRE LISTA DE SERVICIOS
    # ========================================================
    def demostrar_polimorfismo():
        descripciones = []

        # Cada objeto pertenece a una clase diferente, pero todos
        # responden al mismo método describir().
        for servicio in sistema.servicios:
            descripciones.append(servicio.describir())

        return "\n".join(descripciones)

    _ejecutar_controlado(
        13,
        "Recorrido polimórfico de servicios mezclados",
        demostrar_polimorfismo,
    )

    # ========================================================
    # 14. SOBRECARGA SIMULADA
    # ========================================================
    def demostrar_sobrecarga():
        # Primera variante: únicamente unidades.
        costo_normal = sistema.calcular_costo_servicio(
            asesoria,
            2,
        )

        # Segunda variante: unidades, descuento y recargo.
        costo_ajustado = sistema.calcular_costo_servicio(
            asesoria,
            2,
            descuento=0.10,
            recargo=5000,
        )

        return (
            "Mismo método calcular_costo() con diferentes parámetros:\n"
            f"  Costo normal: ${costo_normal:,.2f}\n"
            f"  Costo con descuento y recargo: "
            f"${costo_ajustado:,.2f}"
        )

    _ejecutar_controlado(
        14,
        "Cálculo con parámetros opcionales",
        demostrar_sobrecarga,
    )

    # ========================================================
    # 15. CÁLCULO INVÁLIDO
    # ========================================================
    _ejecutar_controlado(
        15,
        "Intento de cálculo con duración inválida",
        lambda: sistema.calcular_costo_servicio(
            asesoria,
            0,
        ),
    )

    print(
        "\nFIN DE LA SIMULACIÓN: "
        "el programa permaneció activo."
    )
