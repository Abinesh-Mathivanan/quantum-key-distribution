# Quantum Cryptography using BB84 Protocol

This project demonstrates the implementation of the BB84 Quantum Key Distribution Protocol using Qiskit, a popular quantum computing library.

## Overview

The BB84 protocol is a quantum key distribution protocol that allows two parties, Alice and Bob, to securely exchange a secret key over a noisy quantum channel. The protocol relies on the properties of quantum mechanics to ensure the security of the key exchange process.

## Prerequisites

- Python 3.x
- Qiskit (install using `pip install qiskit`)

## Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/Abinesh-Mathivanan/quantum-key-distribution.git
   cd quantum-key-distribution
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the BB84 protocol:
   ```
   python bb84_protocol.py
   ```

## How It Works

1. The `bb84_protocol.py` script defines the implementation of the BB84 protocol using Qiskit.
2. Alice encodes a random sequence of bits using Hadamard gates and sends the qubits to Bob over a simulated noisy quantum channel.
3. Bob receives the qubits and measures them on a random basis (Hadamard or standard) to obtain a new sequence of bits.
4. Alice and Bob communicate publicly to reveal the bases used for encoding and measuring the qubits.
5. Alice and Bob discard the bits measured in the incorrect bases and compare a subset of their remaining bits to ensure they have matching bits.
6. The matching bits are used as the shared secret key for encryption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
