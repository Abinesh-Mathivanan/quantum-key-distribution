from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.providers.aer import AerSimulator
import numpy as np

def simulate_eavesdropping(circuit, eavesdropper):
    circuit.cx(0, 1)
    eavesdropper.measure([0, 1], [0, 1])
    eavesdropped_circuit = circuit.compose(eavesdropper, inplace=False)
    return eavesdropped_circuit

if __name__ == "__main__":
    original_circuit = create_bb84_circuit()
    eavesdropper = QuantumCircuit(2, 2)
    eavesdropped_circuit = simulate_eavesdropping(original_circuit, eavesdropper)
    print("Eavesdropped Circuit:")
    print(eavesdropped_circuit)
