#importing necessary libraries
import math
import stdio


# Entry point.
def main():

    #constant values
    ETA = 9.135e-4
    RHO = 5e-7
    T = 297.0
    R = 8.31457
    MPP = 1.75e-7

    #Reads from the standard Input 
    displacements = stdio.readAllFloats()
    n = len(displacements)

    #Calculates var using the converted value
    var = sum(map(lambda r: ( MPP * r) ** 2, displacements)) / (2 * n)

    #Estimates Boltzmann's constant
    K = 6 * math.pi * var * ETA * (RHO/T)

    #calculates Avogadro's constant
    avogadro = R/K
    stdio.writeln(avogadro)

if __name__ == "__main__":
    main()
