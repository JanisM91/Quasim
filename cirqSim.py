##
# @file cirqSim.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief File containing methods to start whole circuit or single lane simulation with Cirq.
#
##

import cirq
from random import randint

DEBUG = True

##
# @class CirqSim
# @brief Start a simulation with Cirq. Either whole circuit or single lane.
##	
class CirqSim(object):

    ## Create a Cirq circuit out of the quasim circuit
    # @param qubits
    # A list of all qubits
    # @param circuit
    # A list containing the quantum circuit as generated in the gui.
    # @return The cirqCircuit corresponding to the quantum circuit
    ##
    def buildCirqCircuit(self, qubits, circuit):
        cirqCircuit = cirq.Circuit()
        ## Instantiate a CNot Gate
        cNotGate = cirq.CNotGate()
        ## Instantiate a Swap Gate
        swapGate = cirq.SwapGate()
        control = 0
        controlFirst = False

        for j in range(len(circuit[0])):
            for i in range(len(circuit)):
                if circuit[i][j] == "Pauli-X-Gate":
                    cirqCircuit.append(cirq.X(qubits[i]))
                elif circuit[i][j] == "Pauli-Y-Gate":
                    cirqCircuit.append(cirq.Y(qubits[i]))
                elif circuit[i][j] == "Pauli-Z-Gate":
                    cirqCircuit.append(cirq.Z(qubits[i]))
                elif circuit[i][j] == "Hadamard Gate":
                    cirqCircuit.append(cirq.H(qubits[i]))
                elif circuit[i][j] == "S Gate":
                    cirqCircuit.append(cirq.S(qubits[i]))
                elif circuit[i][j] == "T Gate":
                    cirqCircuit.append(cirq.T(qubits[i]))
                elif circuit[i][j] == "Identity":
                    pass
                elif circuit[i][j] == "CNot Gate":
                    if controlFirst:
                        cirqCircuit.append(cNotGate(control, qubits[i]))
                    else:
                        cirqCircuit.append(cNotGate(qubits[i+1], qubits[i]))
                elif circuit[i][j] == "Swap Gate":
                    cirqCircuit.append(cirq.swapGate(control, qubits[i]))
                elif circuit[i][j] == "Deutsch OracleC":
                    pass
                elif circuit[i][j] == "Deutsch Oracle":
                    if randint(0,1) == 1:
                        cirqCircuit.append(cNotGate(qubits[i-1], qubits[i]))
                    else:
                        pass
                elif circuit[i][j] == "Fredkin Gate":
                    cirqCircuit.append(cirq.CSWAP(qubits[i], qubits[i+1], qubits[i+2]))
                elif circuit[i][j] == "Toffoli Gate":
                    cirqCircuit.append(cirq.TOFFOLI(qubits[i-2], qubits[i-1], qubits[i]))
                elif "Control" in circuit[i][j]:
                    if not controlFirst:
                        control = qubits[i]
                        controlFirst = True
                elif "Measurement" in circuit[i][j] :
                    cirqCircuit.append(cirq.measure(qubits[i], key = str(i) + " " + str(j)))

        if DEBUG:
            print("Class: cirqSim Function: buildCirqCircuit Line: 42 Output: cirqCircuit after being completely build")
            print(cirqCircuit)

        return cirqCircuit

    ## Generate the qubits
    # @param numberOfQubits
    # An integer value containing the number of qubits that are to be simulated.
    # @param circuit
    # A list containing the quantum circuit as generated in the gui.
    # @return The result of the simulation.
    ##
    def simulateCircuit(self, numberOfQubits, circuit):
        qubits = []

        for i in range(numberOfQubits):
            qubits.append(cirq.GridQubit(0, i))

        cirqCircuit = self.buildCirqCircuit(qubits, circuit)

        ## Simulate the circuit n times.
        simulator = cirq.google.XmonSimulator()
        result = simulator.run(cirqCircuit, repetitions = 50)

        if DEBUG:
            print("Class: cirqSim Function: simulateCircuit Line: 42 Output: result of simulation")
            print(result)

        return result
