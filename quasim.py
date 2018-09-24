##
# @mainpage Quasim - A Simulator for Quantum circuits
#
# Quasim (short for Quantum Simulation) is a project aiming on researchers, teachers and students interested in Quantum Computer Science and the simulation of quantum circuits.
# It features a Graphical User Interface and allows the user to build quantum circuits with single and multi qubit gates.
# These quantum circuit can then be simulated with three different simulators. A version based on truth tables, another one based on the matrix representation of quantum circuits and the third one is Googles Xmon Simulator included in the Framework Cirq
# This software is part of a master thesis focused on quantum circuits and their simulation.
#
# @author Janis Mohr
# @date 2018
##

##
# @file quasim.py
#
# @brief File containing the main method and therefore acting as a starting point for Quasim
#
##

import tkinter as tk

from gui import Gui

##
#
# @brief main method instancing the main window and starting the main loop
#
##
def main(args):
	#Create a main window and give it a title
    root = tk.Tk()
    root.title("Quasim")
    app = Gui(root)
    #set the size of the main window and open it
    root.geometry('1000x400')
    root.mainloop()

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
