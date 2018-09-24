##
# @file gui.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief File containing several methods to generate widgets for the main window
#
##

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from guiManual import GuiManual
from guiCircuit import GuiCircuit

##
# @class Gui 
# @brief generating widgets for the main window
##
class Gui(object):

    ##
    # init method handling the imported classes and instantiating variables needed for Quasim.
    ##
    def __init__(self, parent):
        self.parent = parent
        self.guiManual = GuiManual(self.parent)
        self.guiCircuit = GuiCircuit(self.parent)
        
        ## @variable circuit
        self.circuit = []
        
        self.errorMessage = ""
        
        self.generateWidgets()
    
    ##
    # Generates a frame for the widgets that allow the user to select the Number of Qubits and Simulator and calls the method generating the specific widgets.
    ##
    def generateWidgets(self):
        ## @param frameOptions
        # A frame for all boxes and buttons to select the initial options and start building a circuit
        ## 
        self.frameOptions = tk.Frame(self.parent)
        self.frameOptions.grid(column = 0, row = 0)

        self.taskBar()
        self.chooseSimulator()
        self.chooseMode()
        self.chooseNumberOfQubits()
        self.circuitBtn()
        
    ##
    # Adds a combo box to the options frame to select the simulator
    ##
    def chooseSimulator(self):
        lblSimulator = tk.Label(self.frameOptions, text="Simulator: ")
        self.valueSimulator = tk.StringVar()
        self.valueSimulator.trace('w', self.callbackFunc)
        self.comboSimulator = ttk.Combobox(self.frameOptions, textvar = self.valueSimulator)
        self.comboSimulator['values']= ("truth table", "matrix", "cirq")
        self.comboSimulator.current(1)
        lblSimulator.grid(column=0, row=0)
        self.comboSimulator.grid(column=1, row=0)
    
    ##
    # Adds a combo box to the options frame to select the mode of simulation
    ##    
    def chooseMode(self):
        lblMode = tk.Label(self.frameOptions, text="Mode: ")
        lblMode.grid(column=2, row=0)

        self.comboMode = ttk.Combobox(self.frameOptions)
        if self.comboSimulator.get() == "truth table":
            self.comboMode['values']= ("single lane",)
        elif self.comboSimulator.get() == "matrix":
            self.comboMode['values']= ("single lane", "whole circuit")
        elif self.comboSimulator.get() == "cirq":
            self.comboMode['values']= ("whole circuit",)
        self.comboMode.current(0)
        self.comboMode.grid(column=3, row=0)
     
    ##
    # Adds a spin box to the options frame to select the number of Qubits. the available number of Qubits is influenced by the selected Simulator.
    ##
    def chooseNumberOfQubits(self):
        #label and spinbox for number of Qubits
        lblNumberOfQubits = tk.Label(self.frameOptions, text="Number of Qubits: ")
        lblNumberOfQubits.grid(column=4, row=0)
        if self.comboSimulator.get() == "cirq":
            self.spinNumberOfQubits = tk.Spinbox(self.frameOptions, from_=1, to=50, width=5)
        else:
            self.spinNumberOfQubits = tk.Spinbox(self.frameOptions, from_=1, to=7, width=5)
        self.spinNumberOfQubits.grid(column=5,row=0)
    ##
    # Generationg a button to start the simulation.
    ##
    def circuitBtn(self):
        btnBuildCircuit = tk.Button(self.frameOptions, text="Start building circuit")
        btnBuildCircuit.config(command = self.startBuildingCircuit)
        btnBuildCircuit.grid(column=6, row=0)
    
    ##
    # Method called when button in options frame is clicked. Invokes the buildCircuit method and destroys the options frame.
    ##    
    def startBuildingCircuit(self):
        self.guiCircuit.buildCircuit(self.comboSimulator.get(), self.comboMode.get(), int(self.spinNumberOfQubits.get()))
        self.frameOptions.destroy()

    ##
    # Called when the option New is selected in the menuBar. Resets all attributes to a blank state and closes all widgets. Afterwards reopen the main window and regenerate all the widgets.
    ##
    def new(self):
        self.simulator = " "
        self.mode = " "
        self.numberOfQubits = 0
        self.circuit = []
        
        self.guiCircuit.new()

        for widget in self.parent.winfo_children():
            widget.destroy()

        self.generateWidgets()

    def callbackFunc(self, *args):
        self.chooseMode()
        self.chooseNumberOfQubits()

    ##
    # Places a menu bar on the top of the main window with three selectable points allowing the user to insert algorithms into the circuit, regenerate the main window and show a help window.
    ##
    def taskBar(self):
        ##
        # @param menu
        # A menu object from Tkinter adding a menu bar to the main window.
        ##
        menu = tk.Menu(self.parent)
        
        ##
        # @param fileMenu
        # add two entries to the menu bar to regenerate the main window and close Quasim.
        ##
        fileMenu = tk.Menu(menu)
        fileMenu.add_command(label='New', command = self.new)
        fileMenu.add_command(label='Exit', command = self.parent.destroy)

        menu.add_cascade(label='File', menu = fileMenu)
        
        ##
        # @param algorithmMenu
        # add two entries to the menu bar to insert a Deutsch or Grover algorithm into the main window.
        ##
        algorithmMenu = tk.Menu(menu)
        algorithmMenu.add_command(label = 'Deutsch', command = self.guiCircuit.algorithmDeutsch)
        algorithmMenu.add_command(label = 'Grover', command = self.guiCircuit.algorithmGrover)

        menu.add_cascade(label='Algorithms', menu = algorithmMenu)
        
        ##
        # @param helpMenu
        # add two entries to the menu bar allowing to call a help window and an about window.
        ##
        helpMenu = tk.Menu(menu)
        helpMenu.add_command(label='Manual', command = self.guiManual.openManual)
        helpMenu.add_separator()
        helpMenu.add_command(label='About')

        menu.add_cascade(label='Help', menu = helpMenu)

        self.parent.config(menu = menu)
