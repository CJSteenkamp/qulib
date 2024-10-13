import pytest
import numpy as np
from qulib import QRegister
from qulib.Gates import H, CNOT

A_TOL=1e-1
R_TOL=1e-1


def test_cnot_2():
    qr = QRegister(2)
    qr.apply_gate(H(), 0)
    qr.apply_two_qubit_gate(CNOT(), 0, 1)

    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_cnot_3():
    qr = QRegister(3)
    qr.apply_gate(H(), 0)
    qr.apply_two_qubit_gate(CNOT(), 0, 1)
    qr.apply_two_qubit_gate(CNOT(), 1, 2)

    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 1/np.sqrt(2)])
    
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_cnot_3_2():
    qr = QRegister(3)
    qr.apply_gate(H(), 0)
    qr.apply_two_qubit_gate(CNOT(), 0, 2)
    qr.apply_two_qubit_gate(CNOT(), 0, 1)

    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 0, 0, 0, 0, 0, 0, 1/np.sqrt(2)])
    
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)
