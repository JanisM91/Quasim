##
# @file guiManual.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief File containing several methods to generate widgets for the manual window
#
##

import tkinter as tk
import tkinter.ttk as ttk

##
# @class GuiManual
# @brief Open windows and generate widgets to show informations for the user.
##

class GuiManual(object):

    ##
    # init method
    ##
    def __init__(self, parent):
        self.parent = parent

    ##Opens a new window and adds several buttons to it and structures them with tabs.
    def openManual(self):
        self.manualWindow = tk.Toplevel(self.parent)
        self.manualWindow.title("Quasim Manual")
        self.tab_control = ttk.Notebook(self.manualWindow)

        #first tab
        self.tabHowToUseQuasim = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tabHowToUseQuasim, text='How to use Quasim')

        btnQuickStart = tk.Button(self.tabHowToUseQuasim, text="QickStart", command = self.showQuickstartEntry)
        btnNumberOfQubits = tk.Button(self.tabHowToUseQuasim, text="NumberOfQubits", command = self.showNumberOfQubitsEntry)
        btnSimulator = tk.Button(self.tabHowToUseQuasim, text="Simulator", command = self.showSimulatorEntry)

        #second tab
        self.tabQuantumComputingGeneral = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tabQuantumComputingGeneral, text='Quantum Computing')

        btnQubit = tk.Button(self.tabQuantumComputingGeneral, text="What is a qubit?", command = self.showQubitEntry)
        btnEntanglement = tk.Button(self.tabQuantumComputingGeneral, text="Entanglement", command = self.showEntanglementEntry)
        btnQuantumRegister = tk.Button(self.tabQuantumComputingGeneral, text="Quantum registers", command = self.showQuantumRegisterEntry)

        #add to window
        btnQuickStart.grid(column=1, row=0)
        btnNumberOfQubits.grid(column=2, row=0)
        btnSimulator.grid(column=3, row=0)

        btnQubit.grid(column=1, row=0)
        btnEntanglement.grid(column=2, row=0)
        btnQuantumRegister.grid(column=3, row=0)

        self.tab_control.pack()

    ## Shows the how to use Quasim entry
    def showQuickstartEntry(self):
        self.QuickstartWindow = tk.Toplevel(self.manualWindow)
        self.QuickstartWindow.title("Quickstart")

    ## Shows the number of Qubits entry
    def showNumberOfQubitsEntry(self):
        self.NumberOfQubitsWindow = tk.Toplevel(self.manualWindow)
        self.NumberOfQubitsWindow.title("Number of Qubits")

    ## Shows the simulator entry
    def showSimulatorEntry(self):
        self.SimulatorWindow = tk.Toplevel(self.manualWindow)
        self.SimulatorWindow.title("Simulator")

    ## Shows the qubit entry
    def showQubitEntry(self):
        self.qubitEntryWindow = tk.Toplevel(self.manualWindow)
        self.qubitEntryWindow.title("Qubit")

    ## Shows the entanglement entry
    def showEntanglementEntry(self):
        self.entanglementEntryWindow = tk.Toplevel(self.manualWindow)
        self.entanglementEntryWindow.title("Entanglement")

    ## Shows the quantum registry entry
    def showQuantumRegisterEntry(self):
        self.quantumRegisterEntryWindow = tk.Toplevel(self.manualWindow)
        self.quantumRegisterEntryWindow.title("Quantum register")
