from inicializar import *

if __name__ == "__main__":
    maquina = crearMaquina()
    tape = leerCinta()
    maquina.setCinta(tape)
    
    maquina.simular()
    print("Cinta final: ", tape.celdas)
    celdas = tape.celdas
    cont = 0
    for celda in celdas:
        if celda == '0':
            cont += 1
    maquina.simular()
    print("El enésimo número en la secuencia de Fibonacci:", tape.enesimo_fibonacci)
    print("El siguiente número en la secuencia de Fibonacci:", cont)