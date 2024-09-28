import pytest
import numpy as np
from qulib import QRegister
from qulib.Gates import X, H, CNOT, Z

A_TOL=1e-1
R_TOL=1e-1

def constant(x):
    return 0

def balanced(x):
    return 1 if x == 0 else 0

def U_f(f):
    return np.array([[1 - f(0), f(0), 0, 0],
                     [f(0), 1 - f(0), 0, 0],
                     [0, 0, 1 - f(1), f(1)],
                     [0, 0, f(1), 1 - f(1)]])

def deutsch(f):
    qr = QRegister(2)
    qr.apply_gate(X(), 1)
    qr.apply_gate(H(), 0)
    qr.dot(U_f(f))
    return qr.apply_gate(H(), 0)

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

def test_bell_state_phi_plus():
    qr = bell('phi+')
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_bell_state_phi_minus():
    qr = bell('phi-')
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_bell_state_psi_plus():
    qr = bell('psi+')
    result = qr.matrix
    expected = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_bell_state_psi_minus():
    qr = bell('psi-')
    result = qr.matrix
    expected = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)
