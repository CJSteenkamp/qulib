import pytest
import numpy as np
from qulib import QRegister
from qulib.Gates import H, X, Z, Y

A_TOL=1e-1
R_TOL=1e-1

def test_x_gate():
    qr = QRegister(1)
    qr.apply_gate(X())
    result = qr.matrix
    expected = np.array([0, 1])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_y_gate():
    qr = QRegister(1)
    qr.apply_gate(Y())
    result = qr.matrix
    expected = np.array([0, -1j])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_z_gate():
    qr = QRegister(1)
    qr.apply_gate(Z())
    result = qr.matrix
    expected = np.array([1, 0])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_h_gate():
    qr = QRegister(1)
    qr.apply_gate(H())
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_hz_gate():
    qr = QRegister(1)
    qr.apply_gate(H())
    qr.apply_gate(Z())
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_zh_gate():
    qr = QRegister(1)
    qr.apply_gate(Z())
    qr.apply_gate(H())
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_xh_gate():
    qr = QRegister(1)
    qr.apply_gate(X())
    qr.apply_gate(H())
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_hx_gate():
    qr = QRegister(1)
    qr.apply_gate(H())
    qr.apply_gate(X())
    result = qr.matrix
    expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_yh_gate():
    qr = QRegister(1)
    qr.apply_gate(Y())
    qr.apply_gate(H())
    result = qr.matrix
    expected = np.array([-1j/np.sqrt(2), 1j/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)

def test_hy_gate():
    qr = QRegister(1)
    qr.apply_gate(H())
    qr.apply_gate(Y())
    result = qr.matrix
    expected = np.array([1j/np.sqrt(2), -1j/np.sqrt(2)])
    assert np.allclose(result, expected, atol=A_TOL, rtol=R_TOL)
