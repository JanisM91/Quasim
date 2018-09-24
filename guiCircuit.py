##
# @file guiCircuit.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief File containing several methods to generate widgets to select gates and add them to the circuit and start a simulation.
#
##

import tkinter as tk
import tkinter.ttk as ttk
import time
from simulator import Simulator
from functools import partial
from random import randint

##
# @class GuiCircuit 
# @brief Generating widgets for the gate selection window and allowing to start a simulation
##

class GuiCircuit(object):

    ##
    # init method handling the imported class and instantiating variables and a frame needed for Quasim.
    ##
    def __init__(self, parent):
        self.parent = parent
        ## @variable circuit
        # A list in which the quantum circuit is saved for simulation
        ##
        self.circuit = []
        self.numberOfQubits = " "
        self.simulatorApp =  Simulator()
        
        self.frameCircuit = tk.Frame(self.parent)
        self.frameCircuit.config(bg="white")
        self.frameCircuit.grid(column = 0, row = 1)
        self.simulationCounter = 0
        
    ## Opens a Message box on the screen showing a 
    # @param errorMessage
    # String variable containing an error message that is shown on the screen.
    def showErrorMessage(self, errorMessage):
        tk.messagebox.showinfo('Error', errorMessage)
    
    ##
    # Starting the simulation. Depending on the selected mode either the single lane or whole circuit simulation is started and shows the simulation result.
    ##
    def startSimulation(self):
        self.simulationCounter += 1
        if self.mode == "whole circuit": ##simulate the whole circuit
            start = time.time()
            simulationResult = self.simulatorApp.circuitSimulation(self.simulator, self.numberOfQubits, self.circuit)
            ende = time.time()
            print('{:5.3f}s'.format(ende-start))
        else: ##simulate the circuit lane by lane
            simulationResult = self.simulatorApp.singleLaneSimulation(self.simulator, self.numberOfQubits, self.circuit)
            
        self.showResult(simulationResult)

    ## Prints a new gate in the frame Circuit in the main window.
    # @param imageGate
    # A Tkinter Photo image containing the image that will be printed.
    # @param position
    # An integer variable containing the position the image will be inserted.
    # @param qubit
    # An integer variable containing the number of the qubit lane the image will be inserted.
    ##
    def printNewGate(self, imageGate, position, qubit):
        lblAddGate = tk.Label(self.frameCircuit, image = imageGate, highlightthickness=0, borderwidth=0)
        lblAddGate.image = imageGate
        lblAddGate.grid(column = position+1, row = qubit+1)
    
    ## Checks if a gate already is on a position and qubit lane. If not the gate is added to the circuit list. Otherwise an error message is shown.
    # @return True if gate was inserted, False if not.
    # @param gate
    # A String variable containing the name of the gate. This is inserted into the list.
    # @param position
    # An integer variable containing the position the gate will be inserted.
    # @param qubit
    # An integer variable containing the number of the qubit lane the gate will be inserted.
    ##   
    def insertNewGateIntoCircuit(self, gate, position, qubit):
        if self.circuit[qubit][position] == "0":
            self.circuit[qubit][position] = gate
            return True
        else:
            errorMessage = "There already is a gate on  q" + str(qubit) + "  position " + str(position)
            self.showErrorMessage(errorMessage)
            return False
    
    ## Assigns the parameters to public attributes and builds the list in which the circuit is saved according to the number of Qubits.
    # @param simulator
    # A String variable containing the name of the simulator
    # @param mode
    # A String variable containing the mode of simulation
    # @param numberOfQubits
    # An integer variable containing the number of Qubits
    ##          
    def buildCircuit(self, simulator, mode, numberOfQubits):
        self.simulator = simulator
        self.numberOfQubits = numberOfQubits
        self.mode = mode

        for i in range(numberOfQubits):
            gateList = []
            for j in range(15):
                gateList.append("0")
            self.circuit.append(gateList)

        self.printInitialCircuit()
        self.showGateSelectionWindow(numberOfQubits, mode)
    
    ## Opens a new window to present the result of a simulation if there is not already one opened. The presentation of the results depends on the selected simulator. During runtime the results are counted and placed side-by-side in one window.
    # @param simulationResult
    # A list or tuple containing the results of the latest simulation
    ##  
    def showResult(self, simulationResult):
        try:
            self.ResultWindow.state() == "normal"
        except:
            self.ResultWindow = tk.Toplevel(self.parent)
            self.ResultWindow.title("Simulation Results")
        
        lblNumberOfSimulation = tk.Label(self.ResultWindow, text = "Simulation Number: " + str(self.simulationCounter))
        lblNumberOfSimulation.grid(column = self.simulationCounter, row = 0)
        if self.simulator == "matrix":
            for i in range(len(simulationResult)):
                lblResult = tk.Label(self.ResultWindow, text = simulationResult[i], wraplength = 210)
                lblResult.grid(column = self.simulationCounter, row = i+1)
        else:
            lblResult = tk.Label(self.ResultWindow, text = simulationResult)
            lblResult.grid(column = self.simulationCounter, row = 1)

    ##
    def printInitialCircuit(self):
        self.frameCircuit = tk.Frame(self.parent)
        self.frameCircuit.config(bg="white")
        self.frameCircuit.grid(column = 0, row = 1)
        lblCircuit = tk.Label(self.frameCircuit, text="Circuit: ", bg="white")
        lblCircuit.grid(column = 0, row = 0)
        for i in range(int(self.numberOfQubits)):
            lblQubit = tk.Label(self.frameCircuit, text = "q" + str(i), bg="white", pady=34)
            lblQubit.grid(column = 0, row = i+1)
            for j in range(15):
                if j < 10:
                    lblPosition = tk.Label(self.frameCircuit, text = str(j), bg="white", padx=52)
                else:
                    lblPosition = tk.Label(self.frameCircuit, text = str(j), bg="white", padx=48)
                    
                lblPosition.grid(column = j+1, row = 0)
                
                imageWire = tk.PhotoImage(file="./pics/Wire.gif")
                lblWire = tk.Label(self.frameCircuit, image=imageWire, highlightthickness=0, borderwidth=0)
                lblWire.image = imageWire
                lblWire.grid(column = j+1, row = i+1)
            
    ## Opens a new window to select a gate to add to the quantum circuit or delete it and start a simulation. The selection of gates depends on the number of Qubits and simulation modes are counted and placed side-by-side in one window.
    # @param[in] numberOfQubits
    # A string variable containing the number of Qubits.
    # @param[in] mode
    # A string variable containing the mode of simulation.
    ## 
    def showGateSelectionWindow(self, numberOfQubits, mode):
        try:
            self.gateSelectionWindow.state() == "normal"
        except:
            ## @variable gateSelectionWindow 
            # A Tkinter window that is used to select gates.
            ##
            self.gateSelectionWindow = tk.Toplevel(self.parent)
            self.gateSelectionWindow.title("Gate Selection")
        
        ## @variable selectedGate
        # A IntVar variable from Tkinter making it possible to get the selected Gate from the radio buttons during runtime
        ##
        self.selectedGate = tk.IntVar()

        rbtnXGate = ttk.Radiobutton(self.gateSelectionWindow, text='Pauli X Gate', value=1, variable = self.selectedGate)
        rbtnYGate = ttk.Radiobutton(self.gateSelectionWindow, text='Pauli Y Gate', value=2, variable = self.selectedGate)
        rbtnZGate = ttk.Radiobutton(self.gateSelectionWindow, text='Pauli Z Gate', value=3, variable = self.selectedGate)
        rbtnHGate = ttk.Radiobutton(self.gateSelectionWindow, text='Hadamard Gate', value=4, variable = self.selectedGate)
        rbtnSGate = ttk.Radiobutton(self.gateSelectionWindow, text='S Gate', value=5, variable = self.selectedGate)
        rbtnTGate = ttk.Radiobutton(self.gateSelectionWindow, text='T Gate', value=6, variable = self.selectedGate)
        rbtnIGate = ttk.Radiobutton(self.gateSelectionWindow, text='Identity', value=7, variable = self.selectedGate)
        rbtnMGate = ttk.Radiobutton(self.gateSelectionWindow, text='Measurement', value=8, variable = self.selectedGate)
        rbtnCnotGate = ttk.Radiobutton(self.gateSelectionWindow, text='CNot Gate', value=9, variable = self.selectedGate)
        rbtnSwapGate = ttk.Radiobutton(self.gateSelectionWindow, text='Swap Gate', value=10, variable = self.selectedGate)
        rbtnToffoliGate = ttk.Radiobutton(self.gateSelectionWindow, text='Toffoli Gate', value=11, variable = self.selectedGate)
        rbtnFredkinGate = ttk.Radiobutton(self.gateSelectionWindow, text='Fredkin Gate', value=12, variable = self.selectedGate)
        rbtnDeutschOracleGate = ttk.Radiobutton(self.gateSelectionWindow, text='Deutsch Oracle', value=13, variable = self.selectedGate)

        lblGateSelectionQubit = tk.Label(self.gateSelectionWindow, text = "Qubit: ")
        lblGateSelectionPosition = tk.Label(self.gateSelectionWindow, text = "Position: ")

        self.valueComboGateSelectionQubit = []
        for i in range(int(numberOfQubits)):
            self.valueComboGateSelectionQubit.append(str(i))
        self.comboGateSelectionQubit = ttk.Combobox(self.gateSelectionWindow, value = self.valueComboGateSelectionQubit)
        self.comboGateSelectionQubit.current(0)

        self.comboGateSelectionPosition = ttk.Combobox(self.gateSelectionWindow)
        self.comboGateSelectionPosition['values']= ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
        self.comboGateSelectionPosition.current(0)

        btnAddGate = tk.Button(self.gateSelectionWindow, text="Add", command = self.addGate)
        btnDeleteGate = tk.Button(self.gateSelectionWindow, text="Delete", command = self.deleteGate)
        btnStartSimulation = tk.Button(self.gateSelectionWindow, text="Start Simulation", command = self.startSimulation)


        ## add all radio buttons, buttons and labels to the window
        rbtnXGate.grid(column = 0, row= 0, sticky = 'w')
        rbtnYGate.grid(column = 0, row= 1, sticky = 'w')
        rbtnZGate.grid(column = 0, row= 2, sticky = 'w')
        rbtnHGate.grid(column = 0, row= 3, sticky = 'w')
        rbtnSGate.grid(column = 0, row= 4, sticky = 'w')
        rbtnTGate.grid(column = 0, row= 5, sticky = 'w')
        rbtnIGate.grid(column = 0, row= 6, sticky = 'w')
        rbtnMGate.grid(column = 0, row= 7, sticky = 'w')
        
        ## two qubit gates are selectable
        if numberOfQubits >= 2 and mode == "whole circuit":
            rbtnCnotGate.grid(column = 0, row= 8, sticky = 'w')
            rbtnSwapGate.grid(column = 0, row= 9, sticky = 'w')
            rbtnDeutschOracleGate.grid(column = 0, row= 12, sticky = 'w')
        
        ## three qubit gates are selectable
        if numberOfQubits >= 3 and mode == "whole circuit":
            rbtnToffoliGate.grid(column = 0, row= 10, sticky = 'w')
            rbtnFredkinGate.grid(column = 0, row= 11, sticky = 'w')

        lblGateSelectionQubit.grid(column = 1, row = 0)
        self.comboGateSelectionQubit.grid(column = 2, row = 0)
        lblGateSelectionPosition.grid(column = 1, row = 1)
        self.comboGateSelectionPosition.grid(column = 2, row = 1)

        btnAddGate.grid(column = 2, row = 6)
        btnDeleteGate.grid(column = 2, row = 7)
        btnStartSimulation.grid(column = 2, row = 8)
    
    ## Method is called when the add Gate button is pressed. Gets the currently selected gate, qubit, and position and adds it to the circuit list and prints it.  
    def addGate(self):
        position = int(self.comboGateSelectionPosition.get())
        qubit = int(self.comboGateSelectionQubit.get())
        if self.selectedGate.get() == 0:
            errorMessage = "Please select a gate out of the list first."
            self.showErrorMessage(errorMessage)
        elif self.selectedGate.get() == 1:
            imageGate = tk.PhotoImage(file="./pics/XGate.gif")
            if self.insertNewGateIntoCircuit("Pauli-X-Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)
        elif self.selectedGate.get() == 2:
            imageGate = tk.PhotoImage(file="./pics/YGate.gif")
            if self.insertNewGateIntoCircuit("Pauli-Y-Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 3:
            imageGate = tk.PhotoImage(file="./pics/ZGate.gif")
            if self.insertNewGateIntoCircuit("Pauli-Z-Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 4:
            imageGate = tk.PhotoImage(file="./pics/HGate.gif")
            if self.insertNewGateIntoCircuit("Hadamard Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 5:
            imageGate = tk.PhotoImage(file="./pics/SGate.gif")
            if self.insertNewGateIntoCircuit("S Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 6:
            imageGate = tk.PhotoImage(file="./pics/TGate.gif")
            if self.insertNewGateIntoCircuit("T Gate", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 7:
            imageGate = tk.PhotoImage(file="./pics/Identity.gif")
            if self.insertNewGateIntoCircuit("Identity", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 8:
            imageGate = tk.PhotoImage(file="./pics/Measurement.gif")
            if self.insertNewGateIntoCircuit("Measurement", position, qubit):
                self.printNewGate(imageGate, position, qubit)        
        elif self.selectedGate.get() == 9:
            self.showControlQubitSelection("CNot Gate", position, qubit)
        elif self.selectedGate.get() == 10:
            self.showControlQubitSelection("Swap Gate", position, qubit)
        elif self.selectedGate.get() == 11:
            if qubit <= 1:
                self.showErrorMessage("You have selected qubit: " + str(qubit) + " but two qubits above the selected qubit are required for a Toffoli-Gate.")
            else:
                self.multiQubitGate("Toffoli Gate", position, qubit)
        elif self.selectedGate.get() == 12:
            self.multiQubitGate("Fredkin Gate", position, qubit)
        elif self.selectedGate.get() == 13:
            self.multiQubitGate("Deutsch Oracle", position, qubit)

    ## Method is called when the delete gate button is clicked. Gets the currently selected qubit and position and deletes it out of the circuit list and replaces it in the window with a plain wire.
    def deleteGate(self):
        qubit = int(self.comboGateSelectionQubit.get())
        position = int(self.comboGateSelectionPosition.get())
        imageGate = tk.PhotoImage(file="./pics/Wire.gif")
        if self.circuit[qubit][position] == "CNot Gate":
            self.circuit[qubit][position] = "0"
            self.printNewGate(imageGate, position, qubit)
            try:
                if self.circuit[qubit+1][position] == "Control":
                    self.circuit[qubit+1][position] = "0"
                    self.printNewGate(imageGate, position, qubit+1)
            except IndexError:
                pass
            try:
                if self.circuit[qubit-1][position] == "Control":
                    self.circuit[qubit-1][position] = "0"
                    self.printNewGate(imageGate, position, qubit-1)
            except IndexError:
                pass
        elif self.circuit[qubit][position] == "Swap Gate":
            self.circuit[qubit][position] = "0"
            self.printNewGate(imageGate, position, qubit)
            try:
                if self.circuit[qubit+1][position] == "Swap Gate":
                    self.circuit[qubit+1][position] = "0"
                    self.printNewGate(imageGate, position, qubit+1)
            except IndexError:
                pass
            try:
                if self.circuit[qubit-1][position] == "Swap Gate":
                    self.circuit[qubit-1][position] = "0"
                    self.printNewGate(imageGate, position, qubit-1)
            except IndexError:
                pass
        else: ## single qubit gate
            self.circuit[qubit][position] = "0"
            self.printNewGate(imageGate, position, qubit)

    ## Opens a new window prompting the user to select a control qubit for a two qubit gate.
    # @param[in] gate
    # A String variable containing the name of a gate.
    # @param[in] position
    # An Integer variable containing the position in the circuit.
    # @param[in] qubit
    # An integer variable containing the qubit in the circuit.
    ## 
    def showControlQubitSelection(self, gate, position, qubit):
        self.controlQubitSelectionWindow = tk.Toplevel(self.parent)
        self.controlQubitSelectionWindow.title("Control Qubit Selection")

        lblControlQubitSelection = tk.Label(self.controlQubitSelectionWindow, text = "Which Qubit should be the control qubit for the selected gate?")
        self.valueControlQubit = []
        for i in range(int(self.numberOfQubits)):
            if int(self.comboGateSelectionQubit.get()) == i:
                pass
            else:
                self.valueControlQubit.append(str(i))
        
        self.comboControlQubit = ttk.Combobox(self.controlQubitSelectionWindow, value = self.valueControlQubit)
        self.comboControlQubit.current(0)
        self.btnControlQubit = tk.Button(self.controlQubitSelectionWindow, text = "OK", command = partial(self.multiQubitGate, gate, position, qubit))

        lblControlQubitSelection.grid(column = 0, row = 0)
        self.comboControlQubit.grid(column = 1, row = 0)
        self.btnControlQubit.grid(column = 2, row = 0)
   
    ## Prints and inserts multi qubit gates into the circuit.
    # @param[in] gate
    # A String variable containing the name of a gate.
    # @param[in] position
    # An Integer variable containing the position in the circuit.
    # @param[in] gateQubit
    # An integer variable containing the qubit in the circuit.
    ## 
    def multiQubitGate(self, gate, position, gateQubit):
        if gate == "CNot Gate":
            controlQubit = int(self.comboControlQubit.get())
            self.controlQubitSelectionWindow.destroy()
            if gateQubit > controlQubit:
                imageGate = tk.PhotoImage(file="./pics/CnotGateUp.gif")
                if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                    self.printNewGate(imageGate, position, gateQubit)
                imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
                if self.insertNewGateIntoCircuit("Control", position, controlQubit):
                    self.printNewGate(imageGate, position, controlQubit)
            else:
                imageGate = tk.PhotoImage(file="./pics/CnotGateDown.gif")
                if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                    self.printNewGate(imageGate, position, gateQubit)
                imageGate = tk.PhotoImage(file="./pics/ControlUp.gif")
                if self.insertNewGateIntoCircuit("Control", position, controlQubit):
                    self.printNewGate(imageGate, position, controlQubit)
        elif gate == "Swap Gate":
            controlQubit = int(self.comboControlQubit.get())
            self.controlQubitSelectionWindow.destroy()
            if gateQubit > controlQubit:
                imageGate = tk.PhotoImage(file="./pics/SwapGateUp.gif")
                if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                    self.printNewGate(imageGate, position, gateQubit)
                imageGate = tk.PhotoImage(file="./pics/SwapGateDown.gif")
                if self.insertNewGateIntoCircuit(gate, position, controlQubit):
                    self.printNewGate(imageGate, position, controlQubit)
            else:
                imageGate = tk.PhotoImage(file="./pics/SwapGateDown.gif")
                if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                    self.printNewGate(imageGate, position, gateQubit)
                imageGate = tk.PhotoImage(file="./pics/SwapGateUp.gif")
                if self.insertNewGateIntoCircuit(gate, position, controlQubit):
                    self.printNewGate(imageGate, position, controlQubit)
        elif gate == "Fredkin Gate":
            imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
            if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                self.printNewGate(imageGate, position, gateQubit)
            imageGate = tk.PhotoImage(file="./pics/SwapGateMid.gif")
            if self.insertNewGateIntoCircuit("Fredkin1", position, gateQubit+1):
                self.printNewGate(imageGate, position, gateQubit+1)
            imageGate = tk.PhotoImage(file="./pics/SwapGateUp.gif")
            if self.insertNewGateIntoCircuit("Fredkin2", position, gateQubit+2):
                self.printNewGate(imageGate, position, gateQubit+2)
        elif gate == "Toffoli Gate":
            imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
            if self.insertNewGateIntoCircuit("Toffoli1", position, gateQubit-2):
                self.printNewGate(imageGate, position, gateQubit-2)
            imageGate = tk.PhotoImage(file="./pics/ControlMid.gif")
            if self.insertNewGateIntoCircuit("Toffoli2", position, gateQubit-1):
                self.printNewGate(imageGate, position, gateQubit-1)
            imageGate = tk.PhotoImage(file="./pics/CnotGateUp.gif")
            if self.insertNewGateIntoCircuit(gate, position, gateQubit):
                self.printNewGate(imageGate, position, gateQubit)
        elif gate == "Deutsch Oracle":
            imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
            if self.insertNewGateIntoCircuit("Deutsch OracleC", position, gateQubit-1):
                self.printNewGate(imageGate, position, gateQubit-1)
            imageGate = tk.PhotoImage(file="./pics/OracleUp.gif")
            if self.insertNewGateIntoCircuit("Deutsch Oracle", position, gateQubit):
                self.printNewGate(imageGate, position, gateQubit)
            
    def new(self):
        self.simulator = " "
        self.mode = " "
        self.numberOfQubits = 0
        self.circuit = []
     
    ## Prints and inserts the Algorithm of Deutsch as a quantum circuit.
    # Circuit: <br>
    # q0: ----H---*---H---M <br>
    # q1: X---H---f---H---M <br>
    ##
    def algorithmDeutsch(self):
        self.simulator = "matrix"
        self.mode = "whole circuit"
        self.numberOfQubits = 2
        self.circuit = []
        
        self.buildCircuit(self.simulator, self.mode, self.numberOfQubits)
        
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 0, 1)
        imageGate = tk.PhotoImage(file="./pics/XGate.gif")
        self.printNewGate(imageGate, 0, 1)
        self.insertNewGateIntoCircuit("Hadamard Gate", 1, 0)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 1, 0)
        self.insertNewGateIntoCircuit("Hadamard Gate", 1, 1)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 1, 1)

        imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
        self.insertNewGateIntoCircuit("Deutsch OracleC", 2, 0)
        self.printNewGate(imageGate, 2, 0)
        imageGate = tk.PhotoImage(file="./pics/OracleUp.gif")
        self.insertNewGateIntoCircuit("Deutsch Oracle", 2, 1)
        self.printNewGate(imageGate, 2, 1)

        self.insertNewGateIntoCircuit("Hadamard Gate", 3, 0)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 3, 0)
        self.insertNewGateIntoCircuit("Hadamard Gate", 3, 1)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 3, 1)

        self.insertNewGateIntoCircuit("Measurement", 4, 0)
        imageGate = tk.PhotoImage(file="./pics/Measurement.gif")
        self.printNewGate(imageGate, 4, 0)

        self.insertNewGateIntoCircuit("Measurement", 4, 1)
        imageGate = tk.PhotoImage(file="./pics/Measurement.gif")
        self.printNewGate(imageGate, 4, 1)
        
    ## Prints and inserts the Algorithm of Grover as a quantum circuit. There are four different possible circuit depending on the randomly generated bit sequence. <br>
    # Circuit for [0, 0]: <br>
    # q0: ----H---X---*---X---H---X-------*-------X---H <br>
    # q1: ----H---X---*---X---H---X---H---C---H---X---H <br>
    # q2: X---H-------T-------------------------------- <br>
    # Circuit for [1, 0]: <br>
    # q0: ----H-------*-------H---X-------*-------X---H <br>
    # q1: ----H---X---*---X---H---X---H---C---H---X---H <br>
    # q2: X---H-------T-------------------------------- <br>
    # Circuit for [0, 1]: <br>
    # q0: ----H---X---*---X---H---X-------*-------X---H <br>
    # q1: ----H-------*-------H---X---H---C---H---X---H <br>
    # q2: X---H-------T-------------------------------- <br>
    # Circuit for [1, 1]: <br>
    # q0: ----H------*------H---X-------*-------X---H <br>
    # q1: ----H------*------H---X---H---C---H---X---H <br>
    # q2: X---H------T------------------------------- <br>
    ##        
    def algorithmGrover(self):
        self.simulator = "matrix"
        self.mode = "whole circuit"
        # three qubits are needed q0: x1, q1: x2, q3: q
        self.numberOfQubits = 3
        self.circuit = []
            
        self.buildCircuit(self.simulator, self.mode, self.numberOfQubits)
        
        #randomly generate a bit sequence [x1, x2]
        bitSequence = []
        for _ in range(2):
            bitSequence.append(randint(0,1))
        
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 0, 2)
        imageGate = tk.PhotoImage(file="./pics/XGate.gif")
        self.printNewGate(imageGate, 0, 2)
        self.insertNewGateIntoCircuit("Hadamard Gate", 1, 0)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 1, 0)
        self.insertNewGateIntoCircuit("Hadamard Gate", 1, 1)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 1, 1)
        self.insertNewGateIntoCircuit("Hadamard Gate", 1, 2)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 1, 2)
        
        #generate the oracle with information about the bit sequence
        if bitSequence[0] == 1:
            pass
        elif bitSequence[0] == 0:
            self.insertNewGateIntoCircuit("Pauli-X-Gate", 2, 0)
            imageGate = tk.PhotoImage(file="./pics/XGate.gif")
            self.printNewGate(imageGate, 2, 0)
            self.insertNewGateIntoCircuit("Pauli-X-Gate", 4, 0)
            self.printNewGate(imageGate, 4, 0)
            
        if bitSequence[1] == 1:
             pass
        elif bitSequence[1] == 0:
            self.insertNewGateIntoCircuit("Pauli-X-Gate", 2, 1)
            imageGate = tk.PhotoImage(file="./pics/XGate.gif")
            self.printNewGate(imageGate, 2, 1)
            self.insertNewGateIntoCircuit("Pauli-X-Gate", 4, 1)
            self.printNewGate(imageGate, 4, 1)
        
        #Toffoli
        imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
        if self.insertNewGateIntoCircuit("Toffoli1", 3, 0):
            self.printNewGate(imageGate, 3, 0)
            imageGate = tk.PhotoImage(file="./pics/ControlMid.gif")
        if self.insertNewGateIntoCircuit("Toffoli2", 3, 1):
            self.printNewGate(imageGate, 3, 1)
            imageGate = tk.PhotoImage(file="./pics/CnotGateUp.gif")
        if self.insertNewGateIntoCircuit("Toffoli Gate", 3, 2):
            self.printNewGate(imageGate, 3, 2)
            
            
        self.insertNewGateIntoCircuit("Hadamard Gate", 5, 0)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 5, 0)
        self.insertNewGateIntoCircuit("Hadamard Gate", 5, 1)
        self.printNewGate(imageGate, 5, 1)
        
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 6, 0)
        imageGate = tk.PhotoImage(file="./pics/XGate.gif")
        self.printNewGate(imageGate, 6, 0)
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 6, 1)
        self.printNewGate(imageGate, 6, 1)
            
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.insertNewGateIntoCircuit("Hadamard Gate", 7, 1)
        self.printNewGate(imageGate, 7, 1)
        
        imageGate = tk.PhotoImage(file="./pics/CnotGateUp.gif")
        self.insertNewGateIntoCircuit("CNot Gate", 8, 1)
        self.printNewGate(imageGate, 8, 1)
        imageGate = tk.PhotoImage(file="./pics/ControlDown.gif")
        self.insertNewGateIntoCircuit("Control", 8, 0)
        self.printNewGate(imageGate, 8, 0)
        
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.insertNewGateIntoCircuit("Hadamard Gate", 9, 1)
        self.printNewGate(imageGate, 9, 1)
        
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 10, 0)
        imageGate = tk.PhotoImage(file="./pics/XGate.gif")
        self.printNewGate(imageGate, 10, 0)
        self.insertNewGateIntoCircuit("Pauli-X-Gate", 10, 1)
        self.printNewGate(imageGate, 10, 1)
        
        self.insertNewGateIntoCircuit("Hadamard Gate", 11, 0)
        imageGate = tk.PhotoImage(file="./pics/HGate.gif")
        self.printNewGate(imageGate, 11, 0)
        self.insertNewGateIntoCircuit("Hadamard Gate", 11, 1)
        self.printNewGate(imageGate, 11, 1)
