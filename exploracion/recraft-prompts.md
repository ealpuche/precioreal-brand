# Exploración de símbolo en Recraft

Ronda 1 (2026-10-21). Cinco conceptos, un prompt por concepto. Se corren en Recraft tal cual; los resultados se guardan en esta carpeta como `ronda-1/<concepto>-<n>.png` (o SVG si Recraft lo exporta) y se anota aquí cuál avanza y por qué.

## Qué tiene que comunicar el símbolo

PrecioReal.mx muestra el historial de precios del e-commerce mexicano para que el "descuento" se compare contra lo que el producto costaba de verdad. El símbolo tiene que decir **"este es el precio verdadero"**, no "ofertas" ni "ahorro". Ideas que descartamos de entrada: carrito, bolsa de compras, moneda, porcentaje, signo de pesos solo. Son de cualquier tienda.

Restricciones comunes a todos los prompts (van al final de cada uno):

> Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Concepto A — Etiqueta con serie de tiempo

La etiqueta de precio clásica, pero dentro no hay cifra: hay una línea de historial.

> A price tag shape with a small hole at the top, containing a simple line chart of price history inside it, the line ends with a single highlighted dot marking the current real price. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Concepto B — El punto real

Una línea de precio y un solo punto marcado. El punto es la marca: lo que de verdad costó.

> A minimal line chart made of a single smooth stroke rising and falling, with one bold filled circle sitting exactly on the line marking a point, the circle is the focal element and larger than the stroke. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Concepto C — Tachado y verdadero

Dos barras horizontales: la de arriba cruzada en diagonal (el precio inflado), la de abajo entera (el real). Es el gesto visual del "precio anterior tachado" que toda tienda usa, invertido a nuestro favor.

> Two horizontal bars stacked vertically, the top bar is thin and crossed out by a short diagonal slash, the bottom bar is thicker and solid and slightly wider, composition reads as a struck-through old price above a true price. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Concepto D — Sello de verificación

Una etiqueta de precio con una marca de verificación integrada en la forma, como un sello: "precio comprobado".

> A price tag silhouette where the lower corner is cut into the shape of a checkmark, the checkmark is part of the tag outline itself rather than an overlay, one continuous shape. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Concepto E — Lupa sobre la serie

La inspección: una lupa cuyo lente contiene un fragmento de gráfica de línea.

> A magnifying glass, the circular lens contains a small zigzag line chart, the handle is short and thick at 45 degrees to the lower right. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Cómo evaluar los resultados

Para cada imagen, tres preguntas, sí o no:

1. ¿Se entiende a 16 px (favicon) sin saber qué es?
2. ¿Se puede redibujar con menos de 10 primitivas SVG (rect, circle, path simple)? Si no, no entra en `build.py`.
3. ¿Podría ser el logo de cualquier tienda o fintech? Si sí, se descarta.

## Resultados

*Pendiente.* Se llena al cerrar la ronda.
