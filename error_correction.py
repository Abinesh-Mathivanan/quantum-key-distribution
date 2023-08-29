from qiskit import QuantumCircuit
from bb84_protocol import create_bb84_circuit, key_generation


def apply_error_correction(circuit, key):
    corrected_circuit = QuantumCircuit(2, 2)
    corrected_circuit.h(0)
    corrected_circuit.cx(0, 1)
    corrected_circuit.measure([0, 1], [0, 1])
    return corrected_circuit

if __name__ == "__main__":
    original_circuit = create_bb84_circuit()
    key = key_generation(original_circuit)
    corrected_circuit = apply_error_correction(original_circuit, key)
    print("Corrected Circuit:")
    print(corrected_circuit)
