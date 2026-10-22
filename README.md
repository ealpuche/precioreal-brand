# precioreal-brand

Identidad visual de **PrecioReal.mx**: nombre, lema, logo, colores, tipografía y las piezas a la medida de cada red social.

Modelo: el mismo que [elingenierodedatos/brand](https://github.com/elingenierodedatos/brand). Todo lo que se publica (SVG, PNG, favicons, piezas por red) sale de `scripts/build.py` y un workflow lo regenera en cada cambio. Nada se edita a mano en un PNG.

Estado: **en construcción**. Las secciones marcadas *pendiente* no tienen decisión tomada; lo que sí está decidido lleva fecha.

## Nombre y lema

La marca se escribe **PrecioReal.mx**: una sola palabra en CamelCase, con el dominio como parte del nombre (decidido 2026-10-21).

- Correcto: PrecioReal.mx
- Incorrecto: Precio Real, precioreal, PRECIOREAL, PrecioReal (sin el .mx) en textos públicos

Lema: *pendiente*.

Titular descriptivo para el sitio y las bios: *pendiente*.

## Qué archivo usar en cada red

*Pendiente.* Se llena cuando exista el logo. La tabla seguirá el formato de la referencia: red, pieza, archivo, medida.

## Logo

*Pendiente.* La exploración de conceptos vive en [`exploracion/`](exploracion): los prompts que se corren en Recraft y, cuando existan, los resultados y la decisión. El símbolo elegido se codifica como SVG en `scripts/build.py`; el archivo de Recraft es referencia, no fuente.

## Colores

*Pendiente.* Cada color entra con su hex, su uso y su contraste WCAG medido contra los fondos donde se va a usar.

Lo que hoy usa `precioreal-web` (fondo `#0b0e14`, verde `#22ff88`, ámbar `#ffb454`) **no es una decisión de marca**: salió de un prototipo y se reemplaza con lo que se decida aquí.

## Tipografía

*Pendiente.* Solo fuentes de licencia abierta (SIL OFL) disponibles en Google Fonts, para que el script pueda descargarlas y convertir el texto a trazos.

## Qué no hacer

*Pendiente hasta que exista el logo.*

## Cómo se generan los archivos

*Pendiente.* `scripts/build.py` nace con el primer SVG decidido. Hasta entonces este repo contiene solo decisiones y exploración.
