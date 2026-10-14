# Historial de cambios

Todas las modificaciones importantes del proyecto se registran en este archivo,
aplicando **Versionado Semantico** (MAYOR.MENOR.PARCHE).

## [1.0.1] - 2026-10-14

### Corregido
- Error crítico en `dividir()`: el programa se caía con `ZeroDivisionError`
  al dividir por cero. Ahora lanza un mensaje claro (`ValueError`).

## [1.0.0] - 2026-10-14

### Agregado
- Función `sumar()` para sumar dos números.
- Función `restar()` para restar dos números.
- Función `dividir()` para dividir dos números.
- Función `multiplicar()` para multiplicar dos números.
- Interfaz básica por línea de comandos.
- Archivo `VERSION` con el número de versión.

