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
        btnSGate = tk.Button(self.tabQuantumComputingGeneral, text="S Gate", command = self.showSGateEntry)
        btnTGate = tk.Button(self.tabQuantumComputingGeneral, text="T Gate", command = self.showTGateEntry)
        btnIGate = tk.Button(self.tabQuantumComputingGeneral, text="I Gate", command = self.showIGateEntry)
        btnMGate = tk.Button(self.tabQuantumComputingGeneral, text="M Gate", command = self.showMGateEntry)
        btnCnotGate = tk.Button(self.tabQuantumComputingGeneral, text="CNOT Gate", command = self.showCnotGateEntry)
        btnSwapGate = tk.Button(self.tabQuantumComputingGeneral, text="Swap Gate", command = self.showSwapGateEntry)
        btnToffoliGate = tk.Button(self.tabQuantumComputingGeneral, text="Toffoli Gate", command = self.showToffoliGateEntry)
        btnFredkinGate = tk.Button(self.tabQuantumComputingGeneral, text="Fredkin Gate", command = self.showFredkinGateEntry)

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
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/Quickstart.GIF")
        lblQ = tk.Label(QuickstartWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()

    ## Shows the number of Qubits entry
    def showNumberOfQubitsEntry(self):
        NumberOfQubitsWindow = tk.Toplevel(self.manualWindow)
        NumberOfQubitsWindow.title("Number of Qubits")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/NumberOfQubits.GIF")
        lblQ = tk.Label(NumberOfQubitsWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()

    ## Shows the simulator entry
    def showSimulatorEntry(self):
        SimulatorWindow = tk.Toplevel(self.manualWindow)
        SimulatorWindow.title("Simulator")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/Simulator.GIF")
        lblQ = tk.Label(SimulatorWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()

    ## Shows the qubit entry
    def showQubitEntry(self):
        qubitEntryWindow = tk.Toplevel(self.manualWindow)
        qubitEntryWindow.title("Qubits")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/Qubits.GIF")
        lblQ = tk.Label(qubitEntryWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()


    ## Shows the entanglement entry
    def showEntanglementEntry(self):
        entanglementEntryWindow = tk.Toplevel(self.manualWindow)
        entanglementEntryWindow.title("Entanglement")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/Entanglement.GIF")
        lblQ = tk.Label(entanglementEntryWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()

    ## Shows the quantum registry entry
    def showQuantumRegisterEntry(self):
        quantumRegisterEntryWindow = tk.Toplevel(self.manualWindow)
        quantumRegisterEntryWindow.title("Quantum register")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/QuantumRegister.GIF")
        lblQ = tk.Label(quantumRegisterEntryWindow, image = imageGate)
        lblQ.image = imageGate
        lblQ.pack()
        
    def showXGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Pauli-X-Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/XGate.GIF")
        lblXGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblXGate.image = imageGate
        lblXGate.pack()
        
    def showYGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Pauli-Y-Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/YGate.GIF")
        lblYGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblYGate.image = imageGate
        lblYGate.pack()
        
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
        
    def showSGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("S Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/SGate.GIF")
        lblSGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblSGate.image = imageGate
        lblSGate.pack()
        
    def showTGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("T Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/TGate.GIF")
        lblTGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblTGate.image = imageGate
        lblTGate.pack()
        
    def showIGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("I Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/IGate.GIF")
        lblIGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblIGate.image = imageGate
        lblIGate.pack()
        
    def showMGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Measurement")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/TGate.GIF")
        lblTGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblTGate.image = imageGate
        lblTGate.pack()
        
    def showCnotGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("CNOT Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/CNOTGate.GIF")
        lblCnotGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblCnotGate.image = imageGate
        lblCnotGate.pack()
        
    def showSwapGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Swap Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/SwapGate.GIF")
        lblSwapGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblSwapGate.image = imageGate
        lblSwapGate.pack()
        
    def showToffoliGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Toffoli Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/ToffoliGate.GIF")
        lblToffoliGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblToffoliGate.image = imageGate
        lblToffoliGate.pack()
        
    def showFredkinGateEntry(self):
        hGateEntryWindow = tk.Toplevel(self.manualWindow)
        hGateEntryWindow.title("Fredkin Gate")
        imageGate = tk.PhotoImage(file="./pics/QuasimManual/FredkinGate.GIF")
        lblFredkinGate = tk.Label(hGateEntryWindow, image = imageGate)
        lblFredkinGate.image = imageGate
        lblFredkinGate.pack()

    def openAbout(self):
        aboutWindow = tk.Toplevel(self.parent)
        aboutWindow.title("About Quasim")
        lblAbout = tk.Label(aboutWindow, text="Quasim was developed by Janis Mohr as part of his master thesis focused on quantum circuits and their simulation at Bochum University of Applied Sciences. This software is licensed under Apache 2.0.", wraplength=200)
        lblAbout.pack()
