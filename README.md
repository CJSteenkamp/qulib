# Qulib

Qlib is a Python library designed for working with quantum computing gates and registers. It provides basic operations to create, manipulate, and work with quantum states and gates using Python.

## Features

- Create quantum registers of any size.
- Apply quantum gates to registers (e.g., X, Y, Z, H gates).
- Simulate quantum circuits.
- Simple interface built using NumPy.

## Installation

You can install Qlib using pip:

```bash
pip install qulib
```

Usage

Here’s a simple example of how to create a quantum register and apply a gate:

```python

from Qlib.QRegister import QRegister
from Qlib.Gates import XGate

# Create a quantum register with 1 qubit
qreg = QRegister(1)

# Apply an X gate (NOT gate)
qreg.apply_gate(X())

# Display the state of the quantum register
print(qreg)
```

Requirements
- Python 3.6+
- NumPy

Running Tests

Qlib uses pytest for testing. To run tests, install pytest and run:

```bash

pytest
```

Contributing

Feel free to submit issues, fork the repository, and make pull requests. Contributions are welcome!