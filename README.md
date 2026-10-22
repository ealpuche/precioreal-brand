# precioreal-brand

Identidad visual de **PrecioReal.mx**: nombre, símbolo, colores, tipografía y las piezas a la medida de cada red social.

Modelo: el mismo que [elingenierodedatos/brand](https://github.com/elingenierodedatos/brand). Todo lo que se publica (SVG, PNG, favicons) sale de [`scripts/build.py`](scripts/build.py). Nada se edita a mano en un PNG.

El símbolo es una etiqueta de precio con la serie de historial adentro, que termina en un punto: el precio real.

![Ícono de PrecioReal.mx](png/logo/precioreal-icono-app-180.png)

## Nombre y lema

La marca se escribe **PrecioReal.mx**: una sola palabra en CamelCase, con el dominio como parte del nombre (decidido 2026-10-21).

- Correcto: PrecioReal.mx
- Incorrecto: Precio Real, precioreal, PRECIOREAL, PrecioReal (sin el .mx) en textos públicos

En el wordmark, ".mx" va en el color de texto secundario.

Lema: *pendiente*. Titular de la web: "¿Ese descuento es real?".

## Símbolo

Decidido el 2026-10-21. La exploración (Canva, Recraft) está en [`exploracion/`](exploracion); la geometría final se escribió a mano y vive en `scripts/build.py`. Son cinco primitivas en un lienzo de 100 × 100: la etiqueta (polígono con trazo redondeado), el ojal, la serie (polilínea de tres tramos) y el punto.

| Archivo | Cuándo usarlo |
| --- | --- |
| `logo/precioreal-simbolo-para-claro` | Sobre fondos claros: etiqueta en tinta |
| `logo/precioreal-simbolo-para-oscuro` | Sobre fondos oscuros: etiqueta en blanco |
| `logo/precioreal-icono-app` | Ícono de app y avatar: símbolo sobre cuadro tinta con esquinas redondeadas |
| `favicon/favicon` | Favicon del sitio (SVG; PNG a 16, 32 y 48 en `png/favicon/`) |

A 16 px la línea se funde con la etiqueta; la silueta y el punto azul siguen leyéndose. Desde 32 px se lee completo.

## Colores

Decididos el 2026-10-21 (propuesta de V0, ronda 1: https://v0.app/chat/o78DE9T2SmW). Claro por defecto. La paleta de un documento —papel, tinta, firma azul y corrección en rojo— y no la de una oferta.

| Nombre | Hex | Uso |
| --- | --- | --- |
| Papel | `#F3F4F1` | Fondo principal |
| Blanco | `#FFFFFF` | Superficies, tarjetas |
| Tinta | `#0D1B2A` | Texto y etiqueta del símbolo |
| Gris texto | `#52606D` | Texto secundario |
| Azul firma | `#2F5BEA` | Punto del símbolo, enlaces, acción primaria |
| Bajó | `#0B7A4B` | El precio bajó |
| Subió | `#B45309` | El precio subió |
| Alerta | `#C4161C` | Precio tachado que nunca existió |
| Borde | `#D7DBD3` | Líneas y bordes |

Contraste WCAG (medido): tinta sobre papel 15.76:1; gris texto 5.85:1; azul firma sobre blanco 5.52:1; bajó 5.39:1; subió 5.02:1; alerta 6.04:1. El punto azul sobre la etiqueta en tinta da 3.15:1, válido para un elemento gráfico (≥ 3:1), no para texto.

Reglas:

- El rojo no vende: solo señala un tachado que nunca se cobró.
- Bajó y subió siempre van con flecha y signo (▼ −$10, ▲ +$10), no solo con color.
- Sobre un botón azul, el texto va en blanco.

## Tipografía

Decidida el 2026-10-21. Ambas con licencia abierta (SIL OFL) en Google Fonts.

- [Archivo](https://fonts.google.com/specimen/Archivo): titulares, interfaz y wordmark (Bold).
- [IBM Plex Mono](https://fonts.google.com/specimen/IBM+Plex+Mono): todas las cifras y precios, con figuras tabulares.

## Qué archivo usar en cada red

*Pendiente.* La tabla seguirá el formato de la referencia: red, pieza, archivo, medida.

## Qué no hacer

- No usar rojo, amarillo ni naranja saturado para promover.
- No redibujar, rotar, contornear ni cambiar las proporciones del símbolo; solo cambian sus colores.
- No mostrar un precio sin su fuente y su fecha, ni en otra fuente que IBM Plex Mono.
- No agregar degradados, brillos, sombras ni confeti: la marca no celebra ofertas, las verifica.
- No escribir el nombre sin ".mx".

## Cómo se generan los archivos

```bash
pip install -r requirements.txt
python scripts/build.py
```

En Linux hace falta `libcairo2`. El wordmark con texto convertido a trazos y las piezas por red quedan pendientes; entran en el mismo script.
