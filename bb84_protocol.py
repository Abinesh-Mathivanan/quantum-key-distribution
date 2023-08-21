import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit_textbook.tools import random_state, vector2latex
from qiskit.providers.aer import AerSimulator

def encode_message(bits):
    message = []
    for bit in bits:
        qc = QuantumCircuit(1, 1)
        if bit == 1:
            qc.x(0)
        qc.barrier()
        message.append(qc)
    return message

def measure_message(message):
    measurements = []
    for qc in message:
        qc.measure(0, 0)
        measurements.append(qc)
    return measurements

def main():
    np.random.seed(0)
    bits_sent = np.random.randint(2, size=10)  # Alice generates random bits
    
    message_alice = encode_message(bits_sent)
    message_bob = measure_message(message_alice)
    
    backend = AerSimulator()
    shots = 1024
    
    results_alice = execute(message_alice, backend=backend, shots=shots).result()
    counts_alice = results_alice.get_counts()
    
    results_bob = execute(message_bob, backend=backend, shots=shots).result()
    counts_bob = results_bob.get_counts()
    
    print("Alice's Message:")
    print(counts_alice)
    
    print("\nBob's Message:")
    print(counts_bob)
    
if __name__ == "__main__":
    main()
