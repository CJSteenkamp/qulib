import numpy as np
from .Gates import SWAP

class QRegister:
    def __init__(self, num_qubits=2, initial_state_matrix=None):
        """
        Initialize a quantum register.
        
        Args:
            num_qubits (int): Number of qubits in the register.
            initial_state_matrix (numpy.ndarray): Initial state matrix, if provided.
        """

        if initial_state_matrix is not None:
            self.matrix = initial_state_matrix
            if num_qubits != int(np.log2(len(initial_state_matrix))):
                raise ValueError("Number of qubits does not match the state matrix")
            self.num_qubits = num_qubits
        else:
            # Initialize to |0...0> state
            self.matrix = np.zeros(2 ** num_qubits, dtype=complex)
            self.matrix[0] = 1
            self.num_qubits = num_qubits

    def __str__(self):
        # return self.matrix.__str__()
        basis = [np.binary_repr(i, width=self.num_qubits) for i in range(2 ** self.num_qubits)]
        return "\n".join(f"|{b}>: {self.matrix[i]:+.3f}" for i, b in enumerate(basis))
    
    def __repr__(self):
        return self.__str__()

# -------------------------------Math-------------------------------
    def dot(self, operand):
        """Apply a matrix operation to the quantum state."""
        self.matrix = np.dot(self.matrix, operand)
        return self

    def tensor(self, operand):
        """Compute the tensor product with another quantum state."""
        return np.kron(self.matrix, operand)
# ------------------------------------------------------------------

# -------------------------------Gates------------------------------
    def _apply_1_bit_gate_all(self, gate):
        operation = gate.matrix

        for _ in range(self.num_qubits-1):
            operation = np.kron(operation, gate.matrix)

        return self.dot(operation)
    
    def _apply_1_bit_gate_targets(self, gate, targets):
        # sort the targets
        targets = sorted(targets)

        operation = np.eye(2) if 0 not in targets else gate.matrix

        for i in range(self.num_qubits-1):
            # plus one as frist line is already initialized
            if i+1 in targets:
                operation = np.kron(operation, gate.matrix)
            else:
                operation = np.kron(operation, np.eye(2))

        return self.dot(operation)

    def _apply_2_bit_gate(self, gate, control):
        """
        Assumes that qbits are next to each other and that the control is the provided qbit
        """
        if control == 0:
            operation = np.kron(gate.matrix, np.eye(2 ** (self.num_qubits-2)))
            return self.dot(operation)

        # check if control is the last qbit
        if control == self.num_qubits-1:
            operation = np.kron(np.eye(2 ** (self.num_qubits-2)), gate.matrix)
            return self.dot(operation)

        # know that the first it not the control
        operation = np.eye(2 ** (control))
        
        operation = np.kron(operation, gate.matrix)

        # add the rest of the qbits, if any after target
        if control != self.num_qubits-1:
            operation = np.kron(operation, np.eye(2 ** (self.num_qubits-2-control)))

        return self.dot(operation)

    def apply_gate(self, gate, target_qubits=None):
        """
        Apply a quantum gate to the register.
        
        Args:
            gate: The quantum gate to apply.
            target_qubits (Optional): The qubit(s) to apply the gate to. If None, apply to all qubits.
        """    
        if isinstance(target_qubits, int):
            target_qubits = [target_qubits]

        if target_qubits is not None:
            if (max(target_qubits) >= self.num_qubits) or (min(target_qubits) < 0):
                raise ValueError("Target qubit is out of range")
        else:
            # If no target qubits are provided, apply to all qubits
            return self._apply_1_bit_gate_all(gate)

        return self._apply_1_bit_gate_targets(gate, target_qubits)

    def apply_two_qubit_gate(self, gate, control, target):
        """
        Apply a two qubit gate to the register.
        
        Args:
            gate: The quantum gate to apply.
            control (int): The control qubit.
            target (int): The target qubit.
        """
        if control == target:
            raise ValueError("Qbits cannot be the same")
        if control >= self.num_qubits or target >= self.num_qubits:
            raise ValueError("Qbit is out of range")
        if gate.matrix.shape != (4, 4):
            raise ValueError("Gate is not a two qubit gate")
        
        if (abs(control - target) == 1):
            # qbits are next to each other
            if control < target:
                return self._apply_2_bit_gate(gate, control)
            else:
                # means control is greater than target, so need swap them
                print("one opp", control, target)
                control, target = target, control

                self._apply_2_bit_gate(SWAP(), control)
                self._apply_2_bit_gate(gate, control)
                self._apply_2_bit_gate(SWAP(), control)

                return self

        # check if control is smaller than target
        if control < target:
            # means that the qbits are not next to each other
            # we need to move the control qbit to the target qbit
            for i in range(control, target-1):
                self._apply_2_bit_gate(SWAP(), i)

            # apply the gate
            self._apply_2_bit_gate(gate, target-1)

            # move the control back to its original position
            for i in range(target-2, control-1, -1):
                self._apply_2_bit_gate(SWAP(), i)
        else:
            print("control > target", control, target)
            control, target = target, control

            # do one more swap to get the control to the target
            for i in range(control, target-1):
                self._apply_2_bit_gate(SWAP(), i)

            self._apply_2_bit_gate(SWAP(), target-1)
            self._apply_2_bit_gate(gate, target-1)
            self._apply_2_bit_gate(SWAP(), target-1)

            for i in range(target-2, control-1, -1):
                self._apply_2_bit_gate(SWAP(), i)


        return self
# ------------------------------------------------------------------

# ----------------------------Mesurements---------------------------
    def measure(self, shots=1000):
        """Measures the qubits
        
        Args:
            shots (int): The number of shots to take"""
        mesurement = [self._measure() for _ in range(shots)]
        # group by basis states
        basis = [np.binary_repr(i, width=self.num_qubits) for i in range(2 ** self.num_qubits)]
        
        string =""
        for i, b in enumerate(basis):
            # string += f"|{b}>: {(mesurement.count(i) / shots)* 100:.2f} %\n"
            string += f"|{b}>: {(mesurement.count(i) / shots):.4f}\n"
        
        return string
    
    def _measure(self):
        probs = np.abs(self.matrix) ** 2
        return np.random.choice(range(2 ** self.num_qubits), p=probs)
# ------------------------------------------------------------------
