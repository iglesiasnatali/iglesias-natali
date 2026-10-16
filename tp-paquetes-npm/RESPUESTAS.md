# Respuestas – TP Administradores de Paquetes y GitHub Actions

## Parte 1 – Administrador de paquetes elegido: NPM / NPX

**1. ¿Para qué sirve?**

NPM (Node Package Manager) es un administrador de paquetes que permite instalar,
actualizar y desinstalar paquetes y bibliotecas para proyectos de JavaScript.
También permite administrar las dependencias de un proyecto y ejecutar scripts
definidos en el archivo `package.json`.

NPX es una herramienta que permite ejecutar paquetes de Node.js sin necesidad de
instalarlos globalmente de forma permanente. Es útil para utilizar herramientas
puntuales o crear proyectos mediante comandos.

Por ejemplo, NPM permite instalar las dependencias de un proyecto, mientras que
NPX permite ejecutar herramientas como los creadores de proyectos.

**2. ¿En qué lenguaje, sistema operativo o ecosistema se utiliza?**

NPM y NPX se utilizan principalmente en el ecosistema de JavaScript y Node.js.
Son compatibles con los sistemas operativos Windows, Linux y macOS.

Se utilizan tanto en proyectos de desarrollo web frontend como backend. Por
ejemplo, pueden emplearse en proyectos creados con React, herramientas de
desarrollo y aplicaciones que utilizan Node.js.

**3. ¿De dónde obtiene los paquetes?**

NPM obtiene los paquetes principalmente del registro público de NPM (npm
Registry), un repositorio en línea que contiene miles de bibliotecas y
herramientas desarrolladas por la comunidad.

Por ejemplo, para instalar React en un proyecto se puede utilizar el siguiente
comando:

```bash
npm install react
```

Este comando descarga el paquete de React y lo agrega a las dependencias del
proyecto. Por otro lado, NPX permite ejecutar herramientas disponibles en el
registro de NPM. Por ejemplo:

```bash
npx create-vite mi-proyecto
```

Este comando permite utilizar la herramienta create-vite para crear un nuevo
proyecto llamado mi-proyecto.

**Conclusión:** NPM y NPX facilitan el desarrollo de software porque permiten
reutilizar herramientas y bibliotecas existentes, administrar las dependencias
de un proyecto y ejecutar utilidades sin tener que desarrollar todas las
funcionalidades desde cero. Además, pueden integrarse con GitHub Actions para
automatizar tareas como la instalación de dependencias, la ejecución de pruebas
y la verificación del código.

---

## Preguntas finales

**1. ¿Qué administrador de paquetes elegiste y por qué?**

Elegí **npm** (junto con npx) porque es el administrador estándar del ecosistema
JavaScript/Node.js, ya viene instalado con Node y lo utilizo habitualmente en
proyectos con React y Next.js.

**2. ¿Qué paquete o librería instalaste?**

Instalé **lodash**, una librería de utilidades para JavaScript. Se usa en
`src/utilidades.js` para manejar textos, números, arrays y objetos.

**3. ¿Qué ventaja tiene utilizar un administrador de paquetes?**

Permite reutilizar librerías ya hechas en lugar de programar todo desde cero,
instalar y actualizar dependencias con un solo comando, mantener las versiones
controladas (`package-lock.json`) y compartir el proyecto de forma reproducible
en cualquier equipo.

**4. ¿Qué función cumple GitHub Actions?**

Es una herramienta de **integración continua (CI)**. Ejecuta tareas automáticas
(un pipeline) cada vez que se hace un push: descargar el código, preparar el
entorno, instalar dependencias y correr las pruebas, para avisar si el proyecto
está en buen estado.

**5. ¿Qué sucede con el pipeline cuando una prueba falla?**

El job se marca como **fallido** (rojo). El proceso se detiene en el paso de las
pruebas y el resultado final queda como "failed", avisando que el cambio rompió
algo.

**6. ¿Qué ventaja tendría este proceso trabajando en un equipo de desarrollo?**

Que cada uno detecta los errores automáticamente antes de mezclar su código con
el de los demás. Todos ven rápido si un cambio rompe las pruebas, se evita subir
código defectuoso y se mantiene una misma forma de instalar y probar el
proyecto para todo el equipo.
