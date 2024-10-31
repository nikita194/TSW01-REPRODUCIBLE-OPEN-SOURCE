# A class implementing a Z-H-Z quantum circuit

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

class ZHZ():

    def __init__(self,n_qubits:int = 1):
        # Create a new circuit with two qubits
        qc = QuantumCircuit(n_qubits)

        # Add a Hadamard gate to qubit 0
        qc.h(0)
        qc.z(0)
        qc.h(0)


        self.qc = qc

    def draw(self):
        # Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
        # last line of the cell, so the drawing appears in the cell output.
        self.qc.draw("mpl")

    def print(self):
        print(self.qc)

    def simulate(self)->dict:
        """
        Simulate the quantum circuit and return the counts of the results
        
        Returns:
            dict: A dictionary containing the counts of the results
        """

        # Use Aer's qasm_simulator to simulate the circuits
        # Transpile for simulator
        simulator = AerSimulator()
        circ = transpile(self.qc, simulator)

        # Run and get counts
        result = simulator.run(circ).result()
        counts = result.get_counts(circ)
        return counts 
    
    

if __name__ == "__main__":
    zhz = ZHZ()
    zhz.print()

        