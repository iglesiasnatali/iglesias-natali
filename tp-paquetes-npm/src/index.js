// Punto de entrada del proyecto: muestra el uso de lodash desde la terminal.
import { capitalizar, promedio, unicos, agruparPor, ordenarPor } from "./utilidades.js";

console.log("capitalizar:", capitalizar("agro market"));
console.log("promedio:", promedio([10, 20, 30]));
console.log("unicos:", unicos([1, 1, 2, 3, 3]));

const publicaciones = [
  { titulo: "Tractor", tipo: "maquinaria", precio: 300 },
  { titulo: "Vaca", tipo: "animal", precio: 100 },
  { titulo: "Arado", tipo: "maquinaria", precio: 200 },
];

console.log("agruparPor tipo:", agruparPor(publicaciones, "tipo"));
console.log("ordenarPor precio:", ordenarPor(publicaciones, "precio").map((p) => p.titulo));
