
### WRITE YOUR CODE BETWEEN THESE LINES - START
    
# import libraries that are used in the function below.
from qiskit import QuantumCircuit
import numpy as np
    
### WRITE YOUR CODE BETWEEN THESE LINES - END

def build_state():
    
    # create a quantum circuit on one qubit
    circuit = QuantumCircuit(1)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - START
    
    # apply necessary gates
    circuit.initialize([np.sqrt(0.5), -1j*np.sqrt(0.5)], 0)
    circuit.sdg(0)
    circuit.h(0)
    
    ### WRITE YOUR CODE BETWEEN THESE LINES - END
    return circuit
