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

        btnQuickStart = tk.Button(self.tabHowToUseQuasim, text="QuickStart", command = self.showQuickstartEntry)
        btnNumberOfQubits = tk.Button(self.tabHowToUseQuasim, text="NumberOfQubits", command = self.showNumberOfQubitsEntry)
        btnSimulator = tk.Button(self.tabHowToUseQuasim, text="Simulator", command = self.showSimulatorEntry)

        #second tab
        self.tabQuantumComputingGeneral = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tabQuantumComputingGeneral, text='Quantum Computing')

        btnQubit = tk.Button(self.tabQuantumComputingGeneral, text="Qubits", command = self.showQubitEntry)
        btnEntanglement = tk.Button(self.tabQuantumComputingGeneral, text="Entanglement", command = self.showEntanglementEntry)
        btnQuantumRegister = tk.Button(self.tabQuantumComputingGeneral, text="Quantum registers", command = self.showQuantumRegisterEntry)

        btnXGate = tk.Button(self.tabQuantumComputingGeneral, text="Pauli-X-Gate", command = self.showXGateEntry)
        btnYGate = tk.Button(self.tabQuantumComputingGeneral, text="Pauli-Y-Gate", command = self.showYGateEntry)
        btnZGate = tk.Button(self.tabQuantumComputingGeneral, text="Pauli-Z-Gate", command = self.showZGateEntry)
        btnHGate = tk.Button(self.tabQuantumComputingGeneral, text="Hadamard Gate", command = self.showHGateEntry)
        btnSGate = tk.Button(self.tabQuantumComputingGeneral, text="S Gate", command = self.showQuantumRegisterEntry)
        btnTGate = tk.Button(self.tabQuantumComputingGeneral, text="T Gate", command = self.showQuantumRegisterEntry)
        btnIGate = tk.Button(self.tabQuantumComputingGeneral, text="I Gate", command = self.showQuantumRegisterEntry)
        btnMGate = tk.Button(self.tabQuantumComputingGeneral, text="M Gate", command = self.showQuantumRegisterEntry)
        btnCnotGate = tk.Button(self.tabQuantumComputingGeneral, text="CNOT Gate", command = self.showQuantumRegisterEntry)
        btnSwapGate = tk.Button(self.tabQuantumComputingGeneral, text="Swap Gate", command = self.showQuantumRegisterEntry)
        btnToffoliGate = tk.Button(self.tabQuantumComputingGeneral, text="Toffoli Gate", command = self.showQuantumRegisterEntry)
        btnFredkinGate = tk.Button(self.tabQuantumComputingGeneral, text="Fredkin Gate", command = self.showQuantumRegisterEntry)

        #add to window
        btnQuickStart.grid(column=1, row=0)
        btnNumberOfQubits.grid(column=2, row=0)
        btnSimulator.grid(column=3, row=0)

        btnQubit.grid(column=1, row=0)
        btnEntanglement.grid(column=2, row=0)
        btnQuantumRegister.grid(column=3, row=0)

        btnXGate.grid(column=1, row=1)
        btnYGate.grid(column=2, row=1)
        btnZGate.grid(column=3, row=1)
        btnIGate.grid(column=4, row=1)

        btnHGate.grid(column=1, row=2)
        btnSGate.grid(column=2, row=2)
        btnTGate.grid(column=3, row=2)
        btnMGate.grid(column=4, row=2)

        btnCnotGate.grid(column=1, row=3)
        btnSwapGate.grid(column=2, row=3)
        btnToffoliGate.grid(column=3, row=3)
        btnFredkinGate.grid(column=4, row=3)

        self.tab_control.pack()

    ## Shows the how to use Quasim entry
    def showQuickstartEntry(self):
        QuickstartWindow = tk.Toplevel(self.manualWindow)
        QuickstartWindow.title("Quickstart")

    ## Shows the number of Qubits entry
    def showNumberOfQubitsEntry(self):
        NumberOfQubitsWindow = tk.Toplevel(self.manualWindow)
        NumberOfQubitsWindow.title("Number of Qubits")

    ## Shows the simulator entry
    def showSimulatorEntry(self):
        SimulatorWindow = tk.Toplevel(self.manualWindow)
        SimulatorWindow.title("Simulator")

    ## Shows the qubit entry
    def showQubitEntry(self):
        qubitEntryWindow = tk.Toplevel(self.manualWindow)
        qubitEntryWindow.title("Qubit")

    ## Shows the entanglement entry
    def showEntanglementEntry(self):
        entanglementEntryWindow = tk.Toplevel(self.manualWindow)
        entanglementEntryWindow.title("Entanglement")

    ## Shows the quantum registry entry
    def showQuantumRegisterEntry(self):
        quantumRegisterEntryWindow = tk.Toplevel(self.manualWindow)
        quantumRegisterEntryWindow.title("Quantum register")
        
    def showXGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Hadamard Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/HGate.GIF")
        lblHGate = tk.Label(hGateEntyWindow, image = imageGate)
        lblHgate.image = imageGate
        lblHGate.pack()
        
    def showYGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Hadamard Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/HGate.GIF")
        lblHGate = tk.Label(hGateEntyWindow, image = imageGate)
        lblHgate.image = imageGate
        lblHGate.pack()
        
    def showZGateEntry(self):
        zGateEntryWindow = tk.Toplevel(self.manualWindow)
        zGateEntryWindow.title("Pauli-Z-Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/ZGate.GIF")
        lblZGate = tk.Label(zGateEntryWindow, image = imageGate)
        lblZGate.image = imageGate
        lblZGate.pack()
        
    def showHGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Hadamard Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/HGate.GIF")
        lblHGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblHGate.image = imageGate
        lblHGate.pack()

    def openAbout(self):
        aboutWindow = tk.Toplevel(self.parent)
        aboutWindow.title("About Quasim")
        lblAbout = tk.Label(aboutWindow, text="Quasim was developed by Janis Mohr as part of his master thesis focused on quantum circuits and their simulation at Bochum University of Applied Sciences. This software is licensed under Apache 2.0.", wraplength=200)
        lblAbout.pack()
