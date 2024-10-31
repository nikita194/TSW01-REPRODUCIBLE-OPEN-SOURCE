from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

class BellPair():

    def __init__(self,n_qubits:int = 2,n_bits:int = 2):
        """
        Create a new Bell Pair quantum circuit
        
        Args:
            n_qubits (int, optional): Number of qubits in the circuit. Defaults to 2.
        """
        # Create a new circuit with two qubits
        qc = QuantumCircuit(n_qubits, n_bits)

        # Add a Hadamard gate to qubit 0
        qc.h(0)

        # Perform a CNOT gate on qubit 1, controlled by qubit 0
        qc.cx(0, 1)

        qc.measure([0, 1], [0, 1])

        self.qc = qc

    def draw(self)->None:
        # Return a drawing of the circuit using MatPlotLib ("mpl"). This is the
        # last line of the cell, so the drawing appears in the cell output.
        self.qc.draw("mpl")

    def print(self)->None:
        """
        Print the quantum circuit
        """
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
    bp = BellPair()
    bp.print()

        