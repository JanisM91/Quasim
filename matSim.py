##
# @file matSim.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief Implementation of the naive Simulation mode based on matrix multiplication.
#
##

import math
import numpy as np
from random import randint
from itertools import cycle

DEBUG = True

## base representation of quantum gates as matrix
#one quibt gates
## base matrix representation of a Pauli-X-Gate as a python list.
gateX = [[0, 1], [1, 0]]
## base matrix representation of a Pauli-Y-Gate as a python list.
gateY = [[0, -1j], [1j, 0]]
## base matrix representation of a Pauli-Z-Gate as a python list.
gateZ = [[1, 0], [0, -1]]
## base matrix representation of a H Gate as a python list.
gateH = [[1 / math.sqrt(2), 1 / math.sqrt(2)], [1 / math.sqrt(2), -(1 / math.sqrt(2))]]
## base matrix representation of a S Gate as a python list.
gateS = [[1, 0],    [0, 1j]]
## base matrix representation of a T Gate as a python list.
gateT = [[1, 0], [0, ((1+1j) / (math.sqrt(2)))]]
#two qubit gates
gateCnotCFirst = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
gateCnotCSecond = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]
gateSwap = [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]
#three qubit gates
gateFredkin = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
gateToffoli = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1, 0]]

## identity Matrices
identityMatrixOne = [[1]]
identityMatrixTwo = [[1, 0], [0, 1]]
identityMatrixFour = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

##
# @class MatSim
# @brief Simulate a circuit with matrix representation. Either whole circuit or single lane.
##	
class MatSim(object):
    
    ## Build a vector to represent the state of all qubits in one circuit depending on the number of qubits selected in the GUI.
    # @param numberOfQubits
    # Integer value representing the number of Qubits selected by the user in the GUI.
    # @return Returns the State vector as a list of lists. For example for one qubit: [[1], [0]]
    def buildQubitStateVector(self, numberOfQubits):
        qubitStateVector = []
        if numberOfQubits == 1:
            qubitStateVector = [[1], [0]]
        elif numberOfQubits == 2:
            qubitStateVector = [[1], [0], [0], [0]]
        elif numberOfQubits == 3:
            qubitStateVector = [[1], [0], [0], [0], [0], [0], [0], [0]]
        elif numberOfQubits == 4:
            qubitStateVector = [[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
        elif numberOfQubits == 5:
            qubitStateVector = [[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
        elif numberOfQubits == 6:
            qubitStateVector = [[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]
        elif numberOfQubits == 7:
            qubitStateVector = [[1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]
                                , [0], [0], [0], [0], [0], [0], [0]]
        else:
            raise ValueError("Number of Qubits must be between 1 and 7 (inclusive).")
            
        return qubitStateVector
    
    ## Reduces the list representing the quantum circuit to the minimal size to reduce the reuqired computing power for the simulation. 
    # Furthermore possible gaps in the circuit are substituted with an identity matrix to make the circuit square which is needed to simulate it.
    # @param circuit
    # A list representing the quantum circuit as generated from the GUI.
    # @return The enhanced list representing the quantum circuit.
    def fillGapsInCircuit(self, circuit):
        
        newCircuit = [[] for _ in range(len(circuit))]
        lastGate = 0
        
        if DEBUG:
            print("Class: matSim Func: fillGapsInCircuit Variable: circuit")
            print(circuit)        
        
        #reduce size of circuit with deleting or replacing all zeros
        for k in range(len(circuit)):
            for l in range(len(circuit[k])):
                if circuit[k][l] != "0":
                    if l > lastGate:
                        lastGate = l
                        
        for m in range(len(circuit)):
            for n in range(lastGate+1):
                if circuit[m][n] == "0":
                    newCircuit[m].append("Identity")
                else:
                    newCircuit[m].append(circuit[m][n])
        
        if DEBUG:
            print("Class: matSim Func: fillGapsInCircuit Variable: newCircuit (return)")
            print(newCircuit)
        
        return newCircuit
    
    ## Generates a single manipulation matrix corresponding to the gates of one cycle using the tensor product.
    # @param gateMatrix
    # A list containing all the gates in one position/cycle.
    # @return Returns the manipulation matrix for one cycle.
    def buildOneCycleManipulationMatrix(self, gateMatrix):
        print("Gate Matrix: ")
        print(gateMatrix)
        
        firstMatrix = []
        secondMatrix = []
        thirdMatrix = []
        fourthMatrix = []
        fifthMatrix = []
        sixthMatrix = []
        seventhMatrix = []
        eigthMatrix = []
        i = 0
        
        numberOfGates = len(gateMatrix)
        print(len(gateMatrix))
            
        while numberOfGates > 0:
            j = 0
            k = len(gateMatrix[i])
                
            while k > 0:
                print(gateMatrix[i][j])
                    
                if i == 0:
                    firstMatrix.append(gateMatrix[i][j])
                elif i == 1:
                    secondMatrix.append(gateMatrix[i][j])          
                elif i == 2:
                    thirdMatrix.append(gateMatrix[i][j])   
                elif i == 3:
                    fourthMatrix.append(gateMatrix[i][j])   
                elif i == 4:
                    fifthMatrix.append(gateMatrix[i][j])
                elif i == 5:
                    sixthMatrix.append(gateMatrix[i][j]) 
                elif i == 6:
                    seventhMatrix.append(gateMatrix[i][j])
                elif i == 7:
                    eigthMatrix.append(gateMatrix[i][j])
                    
                j += 1
                k -= 1
                
            i += 1
            numberOfGates -= 1
        
        if secondMatrix == []:
            oneCycleManipulationMatrix = firstMatrix        
        elif thirdMatrix == []:
            oneCycleManipulationMatrix = np.kron(firstMatrix, secondMatrix)
        elif fourthMatrix == []:
            firstKronMatrix = []
            firstKronMatrix = np.kron(firstMatrix, secondMatrix)
            oneCycleManipulationMatrix = np.kron(firstKronMatrix, thirdMatrix)
        elif fifthMatrix == []:
            firstKronMatrix = []
            secondKronMatrix = []
            firstKronMatrix = np.kron(firstMatrix, secondMatrix)
            secondKronMatrix = np.kron(firstKronMatrix, thirdMatrix)
            oneCycleManipulationMatrix = np.kron(secondKronMatrix, fourthMatrix)
        elif sixthMatrix == []:
            firstKronMatrix = []
            secondKronMatrix = []
            thirdKronMatrix = []
            firstKronMatrix = np.kron(firstMatrix, secondMatrix)
            secondKronMatrix = np.kron(firstKronMatrix, thirdMatrix)
            thirdKronMatrix = np.kron(secondKronMatrix, fourthMatrix)
            oneCycleManipulationMatrix = np.kron(thirdKronMatrix, fifthMatrix)
        elif seventhMatrix == []:
            firstKronMatrix = []
            secondKronMatrix = []
            thirdKronMatrix = []
            fourthKronMatrix = []
            firstKronMatrix = np.kron(firstMatrix, secondMatrix)
            secondKronMatrix = np.kron(firstKronMatrix, thirdMatrix)
            thirdKronMatrix = np.kron(secondKronMatrix, fourthMatrix)
            fourthKronMatrix = np.kron(thirdKronMatrix, fifthMatrix)
            oneCycleManipulationMatrix = np.kron(fourthKronMatrix, sixthMatrix)
        elif eigthMatrix == []:
            firstKronMatrix = []
            secondKronMatrix = []
            thirdKronMatrix = []
            fourthKronMatrix = []
            fifthKronmatrix = []
            firstKronMatrix = np.kron(firstMatrix, secondMatrix)
            secondKronMatrix = np.kron(firstKronMatrix, thirdMatrix)
            thirdKronMatrix = np.kron(secondKronMatrix, fourthMatrix)
            fourthKronMatrix = np.kron(thirdKronMatrix, fifthMatrix)
            fifthKronMatrix = np.kron(fourthKronMatrix, sixthMatrix)
            oneCycleManipulationMatrix = np.kron(fifthKronMatrix, seventhMatrix)
            
        if DEBUG:
            print("oneCycleManipulationMatrix:")
            print(oneCycleManipulationMatrix)        
        
        return oneCycleManipulationMatrix
        
    ## Multiplies all one cycle manipulation matrices to calculate the manipulation matrix of the whole quantum circut.
    # @param allOneCycleManipulationMatrices
    # A list representing all matrices for ever single cycle in the circuit.
    # @return Returns the manipulation matrix of the whole circuit.
    ##    
    def multiplyOneCycleManipulationMatrices(self, allOneCycleManipulationMatrices):
        manipulationMatrix = []
        helpMatrix = []
        a = []
        i = 0
        
        if DEBUG:
            print("Func: multiplyOneCycleManipulationMatrices Variable: len(allOneCycleManipulationMatrices): ")
            print(len(allOneCycleManipulationMatrices))
            
        if len(allOneCycleManipulationMatrices) == 1:
            helpMatrix = allOneCycleManipulationMatrices
        else:
            while i < len(allOneCycleManipulationMatrices)-1:
                if len(helpMatrix) > 0:
                    helpMatrix = np.matmul(helpMatrix, allOneCycleManipulationMatrices[i+1])
                else:
                    helpMatrix = np.matmul(allOneCycleManipulationMatrices[i], allOneCycleManipulationMatrices[i+1])
                                       
                print(helpMatrix)
                i += 1
            
        manipulationMatrix = helpMatrix
        print("Func: multiplyOneCycleManipulationMatrices Variable: manipulationMatrix: ")
        print(manipulationMatrix)
        return manipulationMatrix        
            
    ## Go through the quantum circuit and generate the manipulation matrix for the whole circuit.
    # @param circuit
    # A list representing the circuit as generated from the GUI.
    # @return Returns the manipulation matrix.
    ##
    def buildManipulationMatrix(self, circuit):
        manipulationMatrix = []
        allOneCycleManipulationMatrices = []
        controlQubitFirst = False
        multiQubitGateFirst = False
        firstSwap = True
        
        numberOfGates = 0        
        numberOfLanes = len(circuit)
        numberOfQubits = numberOfLanes
        
        #calculate how many gates the whole circuit has
        i = numberOfLanes-1
        
        while i >= 0:
            numberOfGates += len(circuit[i])
            i -= 1
            print(numberOfGates)
         
        numberOfGatesOnLane = len(circuit[0])
        
        #if only one lane we need the number of gates on this lane for l
        l = numberOfGatesOnLane
        
        #crawl through circuit, scale gate matrix up and build manipulation matrix
        while l > 0:
            print("Func: buildManipulationMatrix Variable: l: ")
            print(l)
            j = numberOfLanes
            k = 0
            
            oneCycleGateMatrix = []
            
            while j > 0:
                
                print("Func: buildManipulationMatrix Variable: j:")
                print(j)
                print("Func: buildManipulationMatrix Variable: k:")
                print(k)
                print("Func: buildManipulationMatrix Variable: numberOfGatesOnLane: ")
                print(numberOfGatesOnLane)
                print("Func: buildManipulationMatrix Variable: circuit[k][numberOfGatesOnLane-1] ")
                print(circuit[k][numberOfGatesOnLane-1])
                #check wich gate is in the circuit and append the corresponding matrix to the matrix for one cycle
                if circuit[k][numberOfGatesOnLane-1] == "Pauli-X-Gate":
                   oneCycleGateMatrix.append(gateX)
                elif circuit[k][numberOfGatesOnLane-1] == "Pauli-Y-Gate":
                   oneCycleGateMatrix.append(gateY)
                elif circuit[k][numberOfGatesOnLane-1] == "Pauli-Z-Gate":
                   oneCycleGateMatrix.append(gateZ)
                elif circuit[k][numberOfGatesOnLane-1] == "Hadamard Gate":
                   oneCycleGateMatrix.append(gateH)
                elif circuit[k][numberOfGatesOnLane-1] == "S Gate":
                   oneCycleGateMatrix.append(gateS)
                elif circuit[k][numberOfGatesOnLane-1] == "T Gate":
                   oneCycleGateMatrix.append(gateT)
                elif circuit[k][numberOfGatesOnLane-1] == "Measurement":
                   oneCycleGateMatrix.append(identityMatrixTwo)
                elif circuit[k][numberOfGatesOnLane-1] == "Identity":
                    oneCycleGateMatrix.append(identityMatrixTwo)
                elif "Control" in circuit[k][numberOfGatesOnLane-1]:
                    if multiQubitGateFirst:
                        controlQubitFirst = False
                    else:
                        controlQubitFirst = True
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "CNot Gate":
                    if controlQubitFirst:
                        multiQubitGateFirstmultiQubitGateFirst = False
                        oneCycleGateMatrix.append(gateCnotCFirst)
                    else:
                        multiQubitGateFirst = True
                        oneCycleGateMatrix.append(gateCnotCSecond)
                elif circuit[k][numberOfGatesOnLane-1] == "Swap Gate":
                    if firstSwap:
                        oneCycleGateMatrix.append(gateSwap)
                        firstSwap = False
                    else:
                        oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Toffoli Gate":
                    oneCycleGateMatrix.append(gateToffoli)
                elif circuit[k][numberOfGatesOnLane-1] == "Toffoli1":
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Toffoli2":
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Fredkin Gate":
                    oneCycleGateMatrix.append(gateFredkin)
                elif circuit[k][numberOfGatesOnLane-1] == "Fredkin1":
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Fredkin2":
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Deutsch OracleC":
                    oneCycleGateMatrix.append(identityMatrixOne)
                elif circuit[k][numberOfGatesOnLane-1] == "Deutsch Oracle":
                    if randint(0,1) == 1:
                        oneCycleGateMatrix.append(gateCnotCFirst)
                    else:
                        oneCycleGateMatrix.append(identityMatrixFour)
                    
                    
                print("Func: buildManipulationMatrix Variable: oneCycleGateMatrix:")
                print(oneCycleGateMatrix)
                
                #update auxiliary variables   
                j -= 1
                k += 1
            
            controlQubitFirst = False
            multiQubitGateFirst = False
            l -= 1
            numberOfGatesOnLane -= 1
            allOneCycleManipulationMatrices.append(self.buildOneCycleManipulationMatrix(oneCycleGateMatrix))
            if DEBUG:
                print("Func: buildManipulationMatrix Variable: oneCycleManipulationMatrix:")
                print(allOneCycleManipulationMatrices)
        
        #build manipulation matrix and return it
        manipulationMatrix = self.multiplyOneCycleManipulationMatrices(allOneCycleManipulationMatrices)
        
        if DEBUG:
            print("Manipulation Matrix:")
            print(manipulationMatrix)
            
        return manipulationMatrix
       
    ## Simulates a whole circuit based on the matrix representation of quantum gates and qubits.
    # @param numberOFQubits
    # The number of Qubits of the circuit that is going to be simulated.
    # @param circuit
    # The circuit that will be simulated.
    # @return Returns the result of the simulation.
    ##
    def simulateCircuit(self, numberOfQubits, circuit):
        result = []
        if DEBUG:
            print("Class: matSim Func: simulateCircuit Variable: numberOfQubits:")
            print(numberOfQubits)
        
        qubitStateVector = self.buildQubitStateVector(numberOfQubits)
        
        if DEBUG:
            print("Class: matSim Func: simulateCircuit Variable: qubitStateVector:")
            print(qubitStateVector)
        
        circuit = self.fillGapsInCircuit(circuit)
        if DEBUG:
            print("Class: matSim Func: simulateCircuit Variable: circuit:")
            print(circuit)
        
        manipulationMatrix = self.buildManipulationMatrix(circuit)
        
        #multiply manipulation matrix and qubit state vector to calculate a result
        resultVector= np.matmul(manipulationMatrix, qubitStateVector)
        
        if DEBUG:
            print("Class: matSim Func: simulateCircuit Variable: resultVector:")
            print(resultVector)
        
        cycleOneQubit = cycle([" |0> :  ", " |1> :  "])
        cycleTwoQubits = cycle([" |00> :  ", " |01> :  ", " |10> :  ", " |11> :  "])
        cycleThreeQubits = cycle([" |000> :  ", " |001> :  ", " |010> :  ", " |011> :  ", " |100> :  ", " |101> :  ", " |110> :  ", " |111> :  "])
        cycleFourQubits = cycle([" |0000> :  ", " |0001> :  ", " |0010> :  ", " |0011> :  ", " |0100> :  ", " |0101> :  ", " |0110> :  ", " |0111> :  ", " |1000> :  ",
                                " |1001> :  ", " |1010> :  ", " |1011> :  ", " |1100> :  ", " |1101> :  ", " |1110> :  ", " |1111> :  "])
        cycleFiveQubits = cycle([" |000> :  ", " |001> :  ", " |010> :  ", " |011> :  ", " |100> :  ", " |101> :  ", " |110> :  ", " |111> :  "])
        cycleSixQubits = cycle([" |000> :  ", " |001> :  ", " |010> :  ", " |011> :  ", " |100> :  ", " |101> :  ", " |110> :  ", " |111> :  "])
        
        if len(resultVector[0]) == 1:
            for i in range(2**numberOfQubits):
                if(numberOfQubits == 1):
                    result += ("Probability of" + next(cycleOneQubit) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 2):
                    result += ("Probability of" + next(cycleTwoQubits) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 3):
                    result += ("Probability of |" + next(cycleThreeQubits) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 4):
                    result += ("Probability of |" + next(cycleFourQubits) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 5):
                    result += ("Probability of |" + next(cycleThreeQubits) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 6):
                    result += ("Probability of |" + next(cycleThreeQubits) + str(round(((resultVector[i][0])**2), 2)), )
                elif(numberOfQubits == 7):
                    result += ("Probability of |" + next(cycleThreeQubits) + str(round(((resultVector[i][0])**2), 2)), )
        else:
            for i in range(2**numberOfQubits):
                if(numberOfQubits == 1):
                    result += ("Probability of" + next(cycleOneQubit) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 2):
                    result += ("Probability of" + next(cycleTwoQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 3):
                    result += ("Probability of" + next(cycleThreeQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 4):
                    result += ("Probability of" + next(cycleFourQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 5):
                    result += ("Probability of" + next(cycleThreeQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 6):
                    result += ("Probability of" + next(cycleThreeQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
                elif(numberOfQubits == 7):
                    result += ("Probability of" + next(cycleThreeQubits) + str(round(((resultVector[0][i][0])**2), 2)), )
            
        if DEBUG:
            print("Class: matSim Func: simulateCircuit Variable: result:")
            print(result)
            
        return result
     
    ## Simulate a single gate. Multiplies a Matrix with the state of the qubit.
    # @param gate
    # The matrix representation of a quantum gate
    # @param qubitState
    # The vector representation of the state of a qubit.
    # @return Returns the state of a qubit after manipulation with the operator(gate).
    ##
    def simulateSingleGate(self, gate, qubitState):
        qubitState = self.matrixMult(gate, qubitState)
        
        return qubitState
    
    ## Simulate one single qubit(lane) indepently from other qubits.
    # @param lane
    # A list of strings representing every gate on a single lane.
    # @return Returns the state of the qubit after the simulation.
    ##
    def simulateLane(self, lane):
        qubitState = []
        counter = 0
        #alpha, beta
        qubitState = [[1], [0]]
        numberOfGates = len(lane)

        while numberOfGates > 0:
            if lane[counter] == "Pauli-X-Gate":
                qubitState = np.matmul(gateX, qubitState)
            elif lane[counter] == "Pauli-Y-Gate":
                qubitState = np.matmul(gateY, qubitState)
            elif lane[counter] == "Pauli-Z-Gate":
                qubitState = np.matmul(gateZ, qubitState)
            elif lane[counter] == "Hadamard Gate":
                qubitState = np.matmul(gateH, qubitState)
            elif lane[counter] == "S Gate":
                qubitState = np.matmul(gateS, qubitState)
            elif lane[counter] == "T Gate":
                qubitState = np.matmul(gateT, qubitState)
            elif lane[counter] == "Identity":
                qubitState = np.matmul(identityMatrixTwo, qubitState)
            elif lane[counter] == "Measurement":
                qubitState = np.matmul(identityMatrixTwo, qubitState)
            else:
                print(lane[counter])
                raise ValueError("An unknown gate was found. Lane cant be simulated.")
            counter += 1
            numberOfGates -= 1

        return qubitState
