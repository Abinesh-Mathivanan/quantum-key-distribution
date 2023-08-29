from qiskit import QuantumCircuit, assemble, transpile
from sympy import assemble_partfrac_list

from bb84_protocol import create_bb84_circuit


def visualize_quantum_state(state_vector):
    backend = AerSimulator()
    qc = QuantumCircuit(1)
    qc.initialize(state_vector, 0)
    qc.measure(0, 0)
    job = assemble_partfrac_list(transpile(qc, backend=backend), backend=backend)
    result = backend.run(job).result()
    counts = result.get_counts()
    print("State Visualization:", counts)

if __name__ == "__main__":
    circuit = create_bb84_circuit()
    backend = AerSimulator()
    job = assemble(transpile(circuit, backend=backend), backend=backend)
    result = backend.run(job).result()
    final_state_vector = result.get_statevector()
    visualize_quantum_state(final_state_vector)
