from zipfile import ZipFile
import codecs
from pykml import parser

def extraer_info_punto(punto):
  datos = {
    'coordinates': punto.Point.coordinates.text
  }
  for dato in punto.ExtendedData.Data:
    name = dato.values()[0]
    
    try:
      value = dato.value
    except AttributeError:
      value = None

    datos[name] = value
  
  return datos

def recuperar_paradas(coche): 
  datos = map(extraer_info_punto, coche.Placemark)
 
  return datos
  
def stop_read(filename):

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

    puntos = recuperar_paradas(coche)


    resultado = {
        'compania': compania_nombre,
        'coche': coche_nombre,
        'puntos': puntos
    }

    return resultado

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print stop_read(filename)
