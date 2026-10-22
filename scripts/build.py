"""Genera los archivos de marca de PrecioReal.mx a partir de la geometría y la paleta.

Todo lo publicado en logo/, png/ y favicon/ sale de aquí; nada se edita a mano.
Uso: pip install -r requirements.txt && python scripts/build.py
"""

from pathlib import Path

import cairosvg

ROOT = Path(__file__).resolve().parent.parent

# Paleta decidida el 2026-10-21 (README → Colores). Mismos valores que tokens.css de la web.
PAPEL = "#F3F4F1"
BLANCO = "#FFFFFF"
TINTA = "#0D1B2A"
AZUL = "#2F5BEA"

# Geometría del símbolo en un lienzo de 100 x 100. No se cambia: solo cambian los colores.
TAG = "12,50 34,24 88,24 88,76 34,76"
LINE = "44,64 55,50 65,60 78,43"


def symbol(tag: str, ink: str, hole: str, dot: str = AZUL, line_w: float = 6) -> str:
    return (
        '<g stroke-linejoin="round" stroke-linecap="round">'
        f'<polygon points="{TAG}" fill="{tag}" stroke="{tag}" stroke-width="8"/>'
        f'<circle cx="30" cy="50" r="5" fill="{hole}"/>'
        f'<polyline points="{LINE}" fill="none" stroke="{ink}" stroke-width="{line_w}"/>'
        f'<circle cx="78" cy="43" r="7.5" fill="{dot}"/>'
        "</g>"
    )


def svg(body: str, view_box: str = "0 0 100 100", bg: str | None = None, rx: int = 0) -> str:
    rect = ""
    if bg:
        rect = f'<rect x="0" y="0" width="100" height="100" rx="{rx}" fill="{bg}"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}">{rect}{body}</svg>\n'


# Recorte ajustado a la etiqueta (con el grosor del trazo), para usar junto al nombre.
CROP = "6 18 88 64"

FILES: dict[str, tuple[str, list[int]]] = {
    # nombre: (svg, tamaños png)
    "logo/precioreal-simbolo-para-claro": (svg(symbol(TINTA, BLANCO, PAPEL), CROP), [512]),
    "logo/precioreal-simbolo-para-oscuro": (svg(symbol(BLANCO, TINTA, TINTA), CROP), [512]),
    "logo/precioreal-icono-app": (
        svg(f'<g transform="translate(9 9) scale(0.82)">{symbol(BLANCO, TINTA, TINTA, line_w=7)}</g>', bg=TINTA, rx=22),
        [1024, 512, 180],
    ),
    "favicon/favicon": (
        svg(f'<g transform="translate(9 9) scale(0.82)">{symbol(BLANCO, TINTA, TINTA, line_w=7)}</g>', bg=TINTA, rx=22),
        [16, 32, 48],
    ),
}


def main() -> None:
    for name, (markup, sizes) in FILES.items():
        target = ROOT / f"{name}.svg"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(markup)
        for size in sizes:
            png = ROOT / "png" / f"{name}-{size}.png"
            png.parent.mkdir(parents=True, exist_ok=True)
            cairosvg.svg2png(bytestring=markup.encode(), write_to=str(png), output_width=size)
        print(f"{name}: svg + {sizes}")


if __name__ == "__main__":
    main()
