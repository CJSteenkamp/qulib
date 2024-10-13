# qulib

qulib is a Python library designed for working with quantum computing gates and registers. It provides basic operations to create, manipulate, and work with quantum states and gates using Python.

## Features

- Simple interface built using NumPy.
- Handles application of gates.
- Two qbit gates include: SWAP, CNOT.

## Installation

You can install qulib using pip:

```bash
pip install qulib
```

Usage

Here’s a simple example of how to create a quantum register and apply a gate:

```python

from qulib import QRegister
from qulib.Gates import X

# Create a quantum register with 2 qubits
qreg = QRegister(2)

# Apply an X gate (NOT gate) to all the qubits
qreg.apply_gate(X())

# Display the basis states of the quantum register
print(qreg)

# Mesure the sates by firing shots
print(qreg.mesure(shots=1000))
```

Requirements
- Python 3.6+
- NumPy

## Running Tests

qulib uses pytest for testing. To run tests, install pytest and run:

```bash

pytest
```

## Contributing

Feel free to submit issues, fork the repository, and make pull requests. Contributions are welcome!
