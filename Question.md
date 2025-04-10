# Quantum-chemistry-Problem-codes

Q1.Write a Python function that takes four values a, b, c, d of the matrix and returns the inverse.
Q2.Write a Python function to diagonalize a 2×2 matrix using basic linear algebra formulas.
Q3. You are given the following data for the H₂ molecule (internuclear distance = 1.4 Bohr):
1. Overlap Matrix 
S = [[1.0000, 0.6593],
     [0.6593, 1.0000]]
2. Core Hamiltonian 
H = [[-1.256, -0.4759],
     [-0.4759, -1.256]]
3. Two-Electron Integrals (in chemist's notation)
These are the electron repulsion integrals:
(0 0 | 0 0) = 0.7746  
(0 0 | 1 1) = 0.5697  
(1 1 | 0 0) = 0.5697  
(0 1 | 0 1) = 0.4441  
(0 1 | 1 0) = 0.4441  
(1 0 | 0 1) = 0.4441  
(1 0 | 1 0) = 0.4441
4. Nuclear Repulsion Energy
E_nuc = 0.7143 Hartree

Write a Python code that:
Initializes a guess for the electron density matrix.
Builds the Fock matrix using the core Hamiltonian and electron repulsion integrals.
Diagonalizes the Fock matrix 
Updates the electron density matrix using the lowest energy orbital.
Iterates until the total electronic energy converges.
Adds the nuclear repulsion energy to get the total Hartree-Fock energy.

