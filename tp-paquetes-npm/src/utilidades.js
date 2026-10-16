// Utilidades del proyecto. Usan la librería lodash (instalada con npm).
import _ from "lodash";

/**
 * Convierte un texto a "Formato Título".
 * Ej: "agro market" -> "Agro Market"
 */
export function capitalizar(texto) {
  return _.startCase(_.toLower(texto));
}

/**
 * Devuelve el promedio de una lista de números.
 * Ej: [10, 20, 30] -> 20
 */
export function promedio(numeros) {
  return _.mean(numeros);
}

/**
 * Quita los elementos repetidos de una lista.
 * Ej: [1, 1, 2, 3, 3] -> [1, 2, 3]
 */
export function unicos(lista) {
  return _.uniq(lista);
}

/**
 * Agrupa una lista de objetos por el valor de una clave.
 * Ej: agruparPor([{tipo:"a"},{tipo:"b"},{tipo:"a"}], "tipo")
 *     -> { a: [...], b: [...] }
 */
export function agruparPor(lista, clave) {
  return _.groupBy(lista, clave);
}

/**
 * Ordena una lista de objetos por una clave, de menor a mayor.
 */
export function ordenarPor(lista, clave) {
  return _.orderBy(lista, [clave], ["asc"]);
}
