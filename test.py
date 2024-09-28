# from Qlib.QRegister import QRegister as QRegister
from qulib import QRegister
from qulib.Gates import *

def constant(x):
    # 0 or 1 for all x
    return 0

def balanced(x):
    # 0 for half of the x and 1 for the other half
    if x == 0:
        return 1
    if x == 1:
        return 0

def U_f(f):
    return np.array([[1 - f(0), f(0)    , 0       , 0],
                    [f(0)    , 1 - f(0), 0       , 0],
                    [0       , 0       , 1 - f(1), f(1)],
                    [0       , 0       , f(1)    , 1 - f(1)]])

def deutsch(f):
    qr = QRegister(2)

    qr.apply_gate(X(), 1)
    qr.apply_gate(H())
    
    qr.dot(U_f(f))
    
    return qr.apply_gate(H(), 0)

def entangle():
    qr = QRegister(2)
    
    qr.apply_gate(H(), 0)

    return qr.dot(CNOT())

def bell(state='phi+'):
    """
        State can be 'phi+', 'phi-', 'psi+', 'psi-'
    """
    # first entangle the qubits
    qr = QRegister(2)
    qr.apply_gate(H(), 0)
    qr._apply_2_bit_gate(CNOT(), 0)
    
    # apply the bell state
    if state == 'phi+':
        return qr
    if state == 'phi-':
        return qr.apply_gate(Z(), 0)
    if state == 'psi+':
        return qr.apply_gate(X(), 0)
    if state == 'psi-':
        qr.apply_gate(X(), 0)
        return qr.apply_gate(Z(), 0)
    
    print("Invalid state")
    return None

# quantum approximate optimization algorithm
# https://learning.quantum.ibm.com/tutorial/quantum-approximate-optimization-algorithm
# https://pennylane.ai/qml/demos/tutorial_qaoa_intro/

# https://pennylane.ai/qml/demos/tutorial_qaoa_maxcut/

# print(deutsch(balanced).measure(10000))

# print(entangle())

qr = QRegister(3)
qr.apply_gate(X(), 0)
qr.apply_cnot(0, 2)

print(qr)