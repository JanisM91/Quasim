##
# @file tableSim.py
#
# @author Janis Mohr
#
# @date 2018
#
# @brief Simulation of a singel lane based on truth tables.
#
##

import math
	
##
# @class TableSim
# @briefSimulation based on truth tables.
##	
class TableSim(object):

	## Method to simulate a Pauli-X-Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateX(self, qubitState):
		if qubitState == [1, 0]:
			qubitState = [0, 1]
		elif qubitState == [0, 1]:
			qubitState = [1, 0]
		else:
			helpVariable = qubitState[0]
			qubitState[0] = qubitState[1]
			qubitState[1] = helpVariable

		return qubitState
	
	## Method to simulate a Pauli-Y-Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateY(self, qubitState):
		if qubitState == [1, 0]:
			qubitState = [0, 1j]
		elif qubitState == [0, 1]:
			qubitState = [-1j, 0]
		else:
			helpVariable = complex(qubitState[0], 1)
			qubitState[0] = complex(qubitState[1], -1)
			qubitState[1] = helpVariable

		return qubitState

	## Method to simulate a Pauli-Z-Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateZ(self, qubitState):
		if qubitState == [1, 0]:
			pass
		elif qubitState == [0, 1]:
			qubitState = [0, -1]
		else:
			qubitState[1] = -qubitState[1]
		
		return qubitState

	## Method to simulate a H Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateH(self, qubitState):
		if qubitState == [1, 0]:
			qubitState = [(1/math.sqrt(2)), (1/math.sqrt(2))]
		elif qubitState == [0, 1]:
			qubitState = [(1/math.sqrt(2)), -(1/math.sqrt(2))]
		else:
			qubitState[0] = (1/math.sqrt(2))*qubitState[0]
			qubitState[1] = (1/math.sqrt(2))*qubitState[1]
		
		return qubitState

	## Method to simulate a S Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateS(self, qubitState):
		if qubitState == [1, 0]:
			pass
		elif qubitState == [0, 1]:
			qubitState = [0, 1j]
		else:
			qubitState[0] = qubitState[0]
			qubitState[1] = qubitState[1]*1j
		
		return qubitState

	## Method to simulate a T Gate representing its truth table.
	# @param qubitState
	# A list containing two values representing the state of the qubit.
	# @return The state of the qubit after the manipulation.
	def GateT(self, qubitState):
		if qubitState == [1, 0]:
			pass
		elif qubitState == [0, 1]:
			qubitState = [0, ((1+1j)/math.sqrt(2))]
		else:
			qubitState[0] = qubitState[0]
			qubitState[1] = ((1+1j)/math.sqrt(2))*qubitState[1]
		
		return qubitState

	## Method to simulate a single lane. Calling the corresponding method for each gate.
	# @param lane
	# A list containing all gates on a single lane.
	# @return The state of the qubit after the simulation.
	def simulateLane(self, lane):
		counter = 0
		#alpha, beta
		qubitState = [1, 0]
		# The number of gates on the lane.
		numberOfGates = len(lane)

		while numberOfGates > 0:
			if lane[counter] == "Pauli-X-Gate":
				qubitState = self.GateX(qubitState)
			elif lane[counter] == "Pauli-Y-Gate":
				qubitState = self.GateY(qubitState)
			elif lane[counter] == "Pauli-Z-Gate":
				qubitState = self.GateZ(qubitState)
			elif lane[counter] == "Hadamard Gate":
				qubitState = self.GateH(qubitState)
			elif lane[counter] == "S Gate":
				qubitState = self.GateS(qubitState)
			elif lane[counter] == "T Gate":
				qubitState = self.GateT(qubitState)
			elif lane[counter] == "Identity":
				pass
			elif lane[counter] == "Measurement":
				pass
			else:
				print(lane[counter])
				raise ValueError("An unknown gate was found. Lane cant be simulated.")
			counter += 1
			#checked one gate so reduce number of remaining gates
			numberOfGates -= 1

		return qubitState
