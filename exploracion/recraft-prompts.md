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

## Resultados de la ronda 1

Corrida el 2026-10-21 en Canva (`generate-image`), no en Recraft: el conector MCP de Recraft en Claude solo expone `image_to_video`. Los cinco PoCs están en la carpeta de Canva [PrecioReal.mx](https://www.canva.com/folder/FAHYsv4vPYA).

| Concepto | Canva | ¿16 px? | ¿<10 primitivas? | ¿Genérico? | Veredicto |
| --- | --- | --- | --- | --- | --- |
| A — Etiqueta con serie | [MAHYsuHhclU](https://www.canva.com/M/MAHYsuHhclU) | sí | sí | la etiqueta sí; el interior no | **gana**: sobre A se construye la ronda 2 |
| B — El punto real | [MAHYsjGEFJ8](https://www.canva.com/M/MAHYsjGEFJ8) | sí | sí (path + circle) | se lee como "gráfica", no como "precio" | reserva: su interior alimenta A1 y A3 |
| C — Tachado y verdadero | [MAHYsjSniRo](https://www.canva.com/M/MAHYsjSniRo) | la diagonal se pierde | sí (3 rect) | no | reserva: su gesto alimenta A2 |
| D — Sello de verificación | [MAHYsmbEA3M](https://www.canva.com/M/MAHYsmbEA3M) | el corte se pierde | sí | dice "verificado", no "precio real" | descartado |
| E — Lupa sobre la serie | [MAHYshZK2mY](https://www.canva.com/M/MAHYshZK2mY) | sí | sí | logo de cualquier herramienta de analítica | descartado |

Decisión (2026-10-21): la etiqueta es el contenedor y lo distintivo vive adentro. La ronda 2 no busca formas nuevas; refina A.

# Ronda 2 — refinar A

Tres variantes. Las restricciones comunes son las mismas de la ronda 1 y cierran cada prompt.

## A1 — Punto protagonista

Misma etiqueta, línea más simple, el punto al doble. Objetivo: que a 16 px se vea "etiqueta con algo adentro".

> A price tag shape with a small hole at the top. Inside the tag, a single polyline of exactly three straight segments going down then up, ending in one large filled circle that is clearly the focal element, the circle diameter is about one quarter of the tag width. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## A2 — Lo que decían y lo que fue

Dentro de la etiqueta, una línea corta tachada arriba y la línea de historial con el punto abajo. Es A con el gesto de C.

> A price tag shape with a small hole at the top. Inside the tag, two elements stacked vertically: on top a short thin horizontal bar crossed out by a small diagonal slash, below it a simple polyline of three segments ending in a bold filled circle. The bottom element is larger and visually dominant. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## A3 — Solo el interior

La línea con el punto, y de la etiqueta queda únicamente el ojal como rastro. Candidata a favicon y avatar.

> A simple polyline of three straight segments going down then up, ending in one large filled circle. Above the line, slightly to the left, a single small ring, like the hole of a price tag, with no tag around it. Only these two elements, nothing else. Flat vector logo mark, single symbol, no text, no letters, two colors maximum on a solid background, geometric and minimal, clean edges, must stay legible at 16 pixels, centered, generous padding, no gradients, no shadows, no 3D, no mockup.

## Resultados de la ronda 2

Corrida el 2026-10-21 en Recraft vía MCP, modelo `recraftv4_1_vector` (SVG), 4 créditos por imagen, 16 créditos en total. Los SVG no pudieron bajarse al repo (el proxy de la sesión de Claude bloquea `img.recraft.ai`); están importados en la carpeta de Canva [PrecioReal.mx](https://www.canva.com/folder/FAHYsv4vPYA) y las URLs de Recraft quedan aquí mientras vivan.

| Variante | Canva | Recraft | Resultado |
| --- | --- | --- | --- |
| A1, intento 1 | no importado | [url](https://img.recraft.ai/x1UsmfQ3-KYFFTplLhHeDzmXMeJSYEetnOuiMF7ctm4/raw:1/plain/abs://prod/images/a56cc960-b2bd-40ea-80db-42a6cbe257a1) | falló: etiqueta girada, línea partida, el círculo quedó como anillo |
| A1, intento 2 | `MAHYsq4-OqE` | [url](https://img.recraft.ai/cszo13cbypHPB-p0qoI9LOCJudUYxkz-oQuIHFVxfmY/raw:1/plain/abs://prod/images/fefb4a42-eab0-47d2-a529-8e1a1fd28e6f) | falló: la línea sale de la etiqueta y tiene más de tres segmentos, el círculo es anillo |
| A2 | `MAHYsvrq9Hs` | [url](https://img.recraft.ai/RV-I43A39PWIXYlBGcsPs9MiKXHOlP4Cr5R4q6qVYGM/raw:1/plain/abs://prod/images/43f5db16-a61a-4e2f-b067-82572002c885) | correcto: etiqueta vertical, barra tachada arriba, línea con punto sólido abajo. Es el que más fielmente ejecuta el concepto |
| A3 | `MAHYsmgg6gI` | [url](https://img.recraft.ai/EGwOeF2CqqvBUNRoGYfSGzeyZ3VPlCiPlAWDiGrFb5g/raw:1/plain/abs://prod/images/77f7cede-ee4d-4b54-a218-19472138eb12) | correcto: ojal + tres segmentos + punto, cuatro primitivas. Candidato natural a favicon |

Observación de método: Recraft v4.1 vector no respeta instrucciones de conteo ("exactamente tres segmentos") ni de orientación cuando la forma está contenida en otra; A2 y A3 funcionaron porque describen elementos apilados o sueltos, no una figura dentro de otra con geometría precisa. Para la siguiente iteración, esa precisión no se pide a Recraft: se dibuja directo en SVG en `scripts/build.py`, usando A2 y A3 como referencia.

Decisión: *pendiente del desarrollador* entre A2 (símbolo completo) y A3 (favicon), o ambos como sistema (A2 para horizontal, A3 para cuadrado).
