from turingMachine import *

def crearMaquina():
    with open("maquina.txt", "r") as f:
        nEstados, nTransiciones = map(int, f.readline().strip().split())
        maquina = TuringMachine()

        for _ in range(nEstados):
            line = f.readline().strip().split()
            value = line[0]
            state = Estado(value)
            maquina.agregarEstado(state)

        for _ in range(nTransiciones):
            line = f.readline().strip().split()
            source = line[0]
            read = line[1]
            destination = line[2]
            write = line[3]
            direction = Transicion.Direccion.DERECHA if line[4] == 'R' else Transicion.Direccion.IZQUIERDA if line[4] == 'L' else Transicion.Direccion.NONE
            transition = Transicion(read, write, maquina.getEstado(destination), direction)
            maquina.agregarTransicion(source, transition)

        initialState = f.readline().strip()
        maquina.setEstadoInicial(initialState)

    return maquina

def leerCinta():
    with open("Fn.txt", "r") as f:
        string = f.readline().strip()
        tape = Cinta(string)
        print("Cadena ingresada: ", string)

    return tape