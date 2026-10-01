from medicamentos.paracetamol import Paracetamol
from medicamentos.antibiotico import Antibiotico

def main ():

  paracetamol = Paracetamol()
  antibiotico = Antibiotico()

  paracetamol.administrar()
  antibiotico.administrar()

if __name__ == "__main__":
    main()
