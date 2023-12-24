#
# Envoltorio para cargar imágenes como listas
#

try:
	from PIL import Image
	import matplotlib.pyplot as plt
	from typing import List, Tuple

except ModuleNotFoundError:
	print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n'
	      '┃ El paquete Matplotlib no está disponible. Escribe el ┃\n'
	      '┃   comando !pip install matplotlib para instalarlo.   ┃\n'
	      '┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
	raise


Color = Tuple[int, int, int]
Imagen = List[List[Color]]


def read(ruta: str) -> Imagen:
    """Lee una imagen desde un archivo"""

    img = Image.open(ruta).convert('RGB')
    ancho, alto = img.size
    pixels = img.load()
    return [[pixels[j, i] for j in range(ancho)] for i in range(alto)]


def show(img: Imagen):
    """Muestra una imagen"""

    plt.imshow(img)

    if _not_notebook():
       plt.show()


def save(nombre: str, img: Imagen, lossless=False):
    """Guarda una imagen en un archivo"""
    alto, ancho = len(img), len(img[0])
    out = Image.new('RGB', (ancho, alto), color=None)
    pixels = out.load()
    for i in range(alto):
        for j in range(ancho):
            pixels[j, i] = img[i][j]
    out.save(nombre, lossless=lossless)


def _not_notebook() -> bool:
    """Comprueba si no se está ejecutando en Jupyter"""
    try:
        return get_ipython().__class__.__name__ != 'ZMQInteractiveShell'
    except NameError:
        return True  # most probably

