# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del proyecto

Este proyecto corresponde al desarrollo de un sistema integral orientado a objetos para la empresa **Software FJ**, encargada de ofrecer diferentes tipos de servicios, entre ellos reservas de salas, alquiler de equipos y asesorías especializadas.

El sistema será desarrollado sin utilizar bases de datos. La información será gestionada mediante objetos, listas internas y archivos destinados exclusivamente al registro de eventos y errores.

El proyecto debe aplicar los principios fundamentales de la Programación Orientada a Objetos, incluyendo:

- Abstracción.
- Herencia.
- Polimorfismo.
- Encapsulación.
- Sobrescritura de métodos.
- Simulación de sobrecarga mediante parámetros opcionales.
- Manejo avanzado de excepciones.
- Registro de eventos y errores mediante archivos de logs.

## Objetivo

Construir una aplicación estable, modular y extensible que permita gestionar clientes, servicios y reservas, garantizando que el sistema continúe funcionando incluso cuando se presenten errores durante su ejecución.

## Integrantes y responsabilidades

| Integrante | Responsabilidad |
|---|---|
| Compañero 1 | Entidades generales, clase Cliente, encapsulación y validaciones |
| Compañero 2 | Clase abstracta Servicio y servicios especializados |
| Compañero 3 | Gestión de reservas, estados, confirmación, cancelación y procesamiento |
| Compañero 4 | Excepciones personalizadas, manejo de errores y sistema de logs |
| Compañero 5 | Integración general, archivo principal y simulación de operaciones |

## Organización del trabajo y ramas

Cada integrante trabajará en una rama independiente del repositorio. La rama `main` se mantendrá como la versión estable e integrada del proyecto.

| Integrante | Rama | Responsabilidad |
|---|---|---|
| Compañero 1 | `companero-1-clientes` | Entidades generales, Cliente y validaciones |
| Compañero 2 | `companero-2-servicios` | Servicio y servicios especializados |
| Compañero 3 | `companero-3-reservas` | Gestión de reservas |
| Compañero 4 | `companero-4-excepciones-logs` | Excepciones personalizadas y logs |
| Compañero 5 | `companero-5-integracion-pruebas` | Integración, main y pruebas |

### Flujo de ramas

```text
main
│
├── companero-1-clientes
├── companero-2-servicios
├── companero-3-reservas
├── companero-4-excepciones-logs
└── companero-5-integracion-pruebas
```

Cada integrante debe realizar sus cambios en su rama asignada. Una vez terminado y revisado su trabajo, los cambios serán integrados mediante un **Pull Request** hacia la rama `main`.

## Estructura del proyecto

```text
software-fj-gestion-clientes-servicios-reservas/
│
├── README.md
├── .gitignore
│
├── src/
│   ├── main.py
│   │
│   ├── modelos/
│   │   ├── entidad.py
│   │   ├── cliente.py
│   │   ├── servicio.py
│   │   ├── reserva_sala.py
│   │   ├── alquiler_equipo.py
│   │   ├── asesoria.py
│   │   └── reserva.py
│   │
│   ├── excepciones/
│   │   └── excepciones_personalizadas.py
│   │
│   ├── utilidades/
│   │   └── logger.py
│   │
│   └── pruebas/
│       └── simulacion_operaciones.py
│
├── logs/
│   └── sistema.log
│
└── docs/
    ├── evidencias/
    │   └── README.md
    ├── diagrama_clases/
    │   └── README.md
    └── documentacion/
        └── README.md
```

## Distribución de archivos por integrante

### Compañero 1

Archivos principales:

```text
src/modelos/entidad.py
src/modelos/cliente.py
```

Responsabilidades:

- Clase abstracta general.
- Clase Cliente.
- Encapsulación de datos personales.
- Validaciones de información.
- Manejo de datos inválidos.

### Compañero 2

Archivos principales:

```text
src/modelos/servicio.py
src/modelos/reserva_sala.py
src/modelos/alquiler_equipo.py
src/modelos/asesoria.py
```

Responsabilidades:

- Clase abstracta Servicio.
- Herencia.
- Polimorfismo.
- Sobrescritura de métodos.
- Cálculo de costos.
- Validación de parámetros.
- Descripción de servicios.

### Compañero 3

Archivo principal:

```text
src/modelos/reserva.py
```

Responsabilidades:

- Integración entre Cliente y Servicio.
- Manejo de duración.
- Manejo de estado.
- Confirmación de reservas.
- Cancelación de reservas.
- Procesamiento de reservas.
- Validación de operaciones permitidas.

### Compañero 4

Archivos principales:

```text
src/excepciones/excepciones_personalizadas.py
src/utilidades/logger.py
logs/sistema.log
```

Responsabilidades:

- Excepciones personalizadas.
- Bloques `try/except`.
- Bloques `try/except/else`.
- Bloques `try/except/finally`.
- Encadenamiento de excepciones.
- Registro de eventos.
- Registro de errores.
- Mantenimiento de la estabilidad del sistema.

### Compañero 5

Archivos principales:

```text
src/main.py
src/pruebas/simulacion_operaciones.py
```

Responsabilidades:

- Integración de todos los módulos.
- Ejecución principal del sistema.
- Lista interna de objetos.
- Simulación de operaciones.
- Validación general.
- Pruebas finales.

## Operaciones mínimas de prueba

El sistema debe simular al menos 10 operaciones completas que incluyan casos exitosos y fallidos.

Ejemplos:

1. Registro válido de un cliente.
2. Registro inválido de un cliente.
3. Creación correcta de un servicio.
4. Creación incorrecta de un servicio.
5. Reserva válida.
6. Reserva con servicio no disponible.
7. Reserva con duración inválida.
8. Cancelación válida.
9. Operación no permitida.
10. Error controlado registrado en el archivo de logs.

El objetivo es demostrar que el sistema puede continuar funcionando aun cuando se presenten errores durante la ejecución.

## Manejo de excepciones

El sistema deberá utilizar manejo robusto de excepciones mediante:

```text
try / except
try / except / else
try / except / finally
encadenamiento de excepciones
```

Los errores podrán estar relacionados con:

- Datos inválidos.
- Parámetros faltantes.
- Operaciones no permitidas.
- Reservas incorrectas.
- Servicios no disponibles.
- Cálculos inconsistentes.
- Cualquier situación que pueda afectar la operación normal del sistema.

## Registro de logs

Todos los errores y eventos relevantes deberán registrarse en:

```text
logs/sistema.log
```

## Flujo de trabajo colaborativo

1. Cada integrante trabaja únicamente en su rama asignada.
2. Cada cambio importante debe registrarse mediante commits claros.
3. No se recomienda trabajar directamente sobre `main`.
4. Cuando una parte esté terminada, se debe crear un Pull Request.
5. Los cambios deben revisarse antes de integrarse a `main`.
6. La rama `main` debe mantenerse como la versión funcional y estable del proyecto.

## Estado del proyecto

Proyecto en desarrollo.
