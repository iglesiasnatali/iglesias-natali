# TP – Administradores de Paquetes y GitHub Actions

Proyecto de ejemplo en **Node.js** que usa el administrador de paquetes **npm**,
la librería **lodash** y un **pipeline de GitHub Actions** que instala las
dependencias y ejecuta las pruebas automáticas en cada push.

## Administrador de paquetes elegido: npm (con npx)

**npm (Node Package Manager)** es el administrador de paquetes oficial de
Node.js. Permite instalar, actualizar y desinstalar librerías, administrar las
dependencias del proyecto y ejecutar scripts definidos en `package.json`.
**npx** permite ejecutar paquetes sin instalarlos de forma global y permanente.

- **Ecosistema:** JavaScript / Node.js (Windows, Linux y macOS).
- **Registro:** NPM Registry (https://www.npmjs.com).

## Librería instalada: lodash

**lodash** es una librería de utilidades para JavaScript (manejo de arrays,
objetos, textos, etc.). Se usa en el archivo `src/utilidades.js`.

### Comando utilizado para instalarla

```bash
npm install lodash
```

Ese comando descarga la librería, la agrega a `dependencies` en `package.json`
y registra la versión exacta en `package-lock.json`.

## Archivo de configuración de dependencias

- **`package.json`** → declara las dependencias y los scripts del proyecto.
- **`package-lock.json`** → fija las versiones exactas instaladas (lo genera npm).

## Estructura del proyecto

```
tp-paquetes-npm/
├── package.json          # dependencias y scripts
├── package-lock.json     # versiones exactas
├── src/
│   ├── utilidades.js     # funciones que usan lodash
│   └── index.js          # programa principal (demo)
└── test/
    └── utilidades.test.js # pruebas automáticas
```

## Cómo ejecutar el proyecto

```bash
cd tp-paquetes-npm
npm install     # instala las dependencias (primera vez)
npm start       # ejecuta src/index.js
```

## Cómo ejecutar las pruebas

```bash
cd tp-paquetes-npm
npm test        # ejecuta las pruebas con el runner integrado de Node (node --test)
```

Salida esperada: **5 pruebas, 5 correctas, 0 fallidas**.

## Pipeline de GitHub Actions

El workflow está en **`.github/workflows/tp-paquetes-npm.yml`** (en la raíz del
repositorio) y se ejecuta automáticamente en cada **push** que modifique el
proyecto.

Pasos que realiza:

1. Descarga el código del repositorio (`actions/checkout`).
2. Prepara el entorno con Node.js 20 (`actions/setup-node`).
3. Instala las dependencias (`npm ci`).
4. Ejecuta las pruebas automáticas (`npm test`).
5. Informa si la ejecución fue exitosa o falló.

> **Nota:** GitHub Actions solo lee los workflows que están en `.github/workflows/`
> en la **raíz del repositorio**. Como este proyecto convive con otros trabajos
> dentro del mismo repo, el workflow vive en la raíz y usa `defaults.run.working-directory`
> para ejecutarse dentro de la carpeta `tp-paquetes-npm/`.

### Probar que el pipeline detecta errores

Para ver una ejecución **fallida**: cambiar a propósito un valor esperado en
`test/utilidades.test.js` (por ejemplo `"Agro Market"` por `"Agro market"`),
hacer push y ver cómo GitHub Actions marca el job en rojo. Luego se corrige y el
pipeline vuelve a pasar.
