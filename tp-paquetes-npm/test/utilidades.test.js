// Pruebas automáticas con el runner integrado de Node (node:test).
// Se ejecutan con: npm test
import test from "node:test";
import assert from "node:assert/strict";

import { capitalizar, promedio, unicos, agruparPor, ordenarPor } from "../src/utilidades.js";

test("capitalizar devuelve el texto en Formato Título", () => {
  assert.equal(capitalizar("agro market"), "Agro Market");
});

test("promedio calcula el promedio de una lista de números", () => {
  assert.equal(promedio([10, 20, 30]), 21);
});

test("unicos elimina los elementos repetidos", () => {
  assert.deepEqual(unicos([1, 1, 2, 3, 3]), [1, 2, 3]);
});

test("agruparPor agrupa los objetos según una clave", () => {
  const datos = [
    { tipo: "animal" },
    { tipo: "maquinaria" },
    { tipo: "animal" },
  ];
  const resultado = agruparPor(datos, "tipo");
  assert.equal(resultado.animal.length, 2);
  assert.equal(resultado.maquinaria.length, 1);
});

test("ordenarPor ordena de menor a mayor por una clave", () => {
  const datos = [{ precio: 30 }, { precio: 10 }, { precio: 20 }];
  assert.deepEqual(ordenarPor(datos, "precio"), [
    { precio: 10 },
    { precio: 20 },
    { precio: 30 },
  ]);
});
