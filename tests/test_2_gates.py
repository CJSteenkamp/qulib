import pytest
import numpy as np
from qulib import QRegister
from qulib.Gates import SWAP, CNOT, X


A_TOL=1e-1
R_TOL=1e-1

def test_swap():
    qr = QRegister(3)
    qr.apply_gate(X(), 0)
    qr._apply_2_bit_gate(SWAP(), 0)
    qr._apply_2_bit_gate(SWAP(), 1)
    result = qr.matrix
    expected = np.array([0, 1, 0, 0, 0, 0, 0, 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_cnot():
    qr = QRegister(3)
    qr.apply_gate(X(), 0)
    qr._apply_2_bit_gate(CNOT(), 0)
    result = qr.matrix
    expected = np.array([0, 0, 0, 0, 0, 0, 1, 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_cnot_last():
    qr = QRegister(3)
    qr.apply_gate(X(), 0)
    qr.apply_two_qubit_gate(CNOT(), 0, 2)
    result = qr.matrix
    expected = np.array([0, 0, 0, 0, 0, 1, 0, 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)