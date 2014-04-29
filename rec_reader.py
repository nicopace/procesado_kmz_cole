from zipfile import ZipFile
import codecs
from pykml import parser

def recuperar_recorrido(coche):
  return coche.Placemark.LineString.coordinates.text

def rec_read(filename):

    kmz = ZipFile(filename, 'r')
    files = kmz.namelist()
    # there must be just one file

    kmltext = kmz.open(files[0], 'r').read().decode('iso-8859-1')
    kmltext = kmltext.replace(' encoding="UTF-8"', '')

    k = parser.fromstring(kmltext)

    compania = k.Document.Folder[0]
    compania_nombre = compania.name

    coche = compania.Folder[0]
    coche_nombre = coche.name

    puntos = recuperar_corrido(coche)

    resultado = {
        'compania': compania_nombre,
        'coche': coche_nombre,
        'puntos': puntos
    }

    return resultado

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print rec_read(filename)
