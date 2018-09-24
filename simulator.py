##
# @file simulator.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief File containing two methods to start whole circuit or single lane simulation.
#
##

from tableSim import TableSim
from matSim import MatSim
from cirqSim import CirqSim

##
# @class Simulator
# @brief Start a simulation. Either whole circuit or single lane.
##	
class Simulator(object):
	
	##
    # init method handling the imports and a variable to save the simulation result.
    ##
	def __init__(self):
		## list to save the result of simulation in.
		self.result = []
		self.tableSim = TableSim()
		self.matSim = MatSim()
		self.cirqSim = CirqSim()
		
	##
	# Method to simulate a whole circuit and returning the result of simulation.
	# @param [in] simulation 
	# A String variable containing the simulator. Can only be "matrix" or "cirq" because truth table simulation does not support whole circuit simulation.
	# @param [in] numberOfQubits
	# The number of Qubits the circuit has.
	# @param circuit
	# A list containing the quantum circuit itself.
	# @return the result of the simulation.
	##
	def circuitSimulation(self, simulation, numberOfQubits, circuit):
		if simulation == "matrix":
		    self.result = self.matSim.simulateCircuit(numberOfQubits, circuit)
		elif simulation == "cirq":
			self.result = self.cirqSim.simulateCircuit(numberOfQubits, circuit)
			
		return self.result			
	
	##
	# Method to simulate all single lanes in a circuit independently and returning the result of simulation.
	# @param [in] simulation 
	# A String variable containing the simulator. Can only be "matrix" or "truth table" simulation because "cirq" does not support single lane simulation.
	# @param [in] numberOfQubits
	# The number of Qubits the circuit has.
	# @param circuit
	# A list containing the quantum circuit itself.
	# @return the result of the simulation.
	##		
	def singleLaneSimulation(self, simulation, numberOfQubits, circuit):
		#reduce the circuit to its minimum size to reduce the required time for calculation.
		circuit = self.matSim.fillGapsInCircuit(circuit)
		
		qubitLanes = len(circuit)
		self.result = [[] for _ in range(qubitLanes)]
		lane = []

		while qubitLanes > 0:

			numberOfGates = len(circuit[qubitLanes-1])
			counter = 0

			while numberOfGates > 0:
				lane.append(circuit[qubitLanes-1][counter])
				counter += 1
				numberOfGates -= 1
			
			if simulation == "truth table":
				self.result[qubitLanes-1].append(self.tableSim.simulateLane(lane))
			elif simulation == "matrix":
				self.result[qubitLanes-1].append(self.matSim.simulateLane(lane))
			
			qubitLanes -= 1
		
		return self.result
