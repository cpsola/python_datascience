import hashlib

seed = 'Programacion Python para Data Science'

if __name__ == "__main__":
    try:
        dni = raw_input('Introduce tu DNI o NIE (sin letra):')
    except ValueError:
        raise SystemExit('Error al introducir el DNI')

    digest = hashlib.sha224('.'.join(seed.split())+dni).hexdigest()
    with open('prog_datasci_1.txt', 'w') as output:
        output.write("%s %s\n" % (dni, digest))
        print 'Archivo prog_datasci_1.txt generado'
