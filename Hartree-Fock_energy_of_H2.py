import numpy as np


S = np.array([[1.0, 0.6593],
              [0.6593, 1.0]])


H = np.array([[-1.256, -0.4759],
              [-0.4759, -1.256]])

# Electron repulsion integrals 
eri = {
    (0, 0, 0, 0): 0.7746,
    (0, 0, 1, 1): 0.5697,
    (1, 1, 0, 0): 0.5697,
    (0, 1, 0, 1): 0.4441,
    (0, 1, 1, 0): 0.4441,
    (1, 0, 0, 1): 0.4441,
    (1, 0, 1, 0): 0.4441
}


def inverse_2x2(m):
    det = m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]
    inv = np.array([[m[1, 1], -m[0, 1]],
                    [-m[1, 0], m[0, 0]]]) / det
    return inv


def diagonalize_2x2(A):
    a, b, d = A[0, 0], A[0, 1], A[1, 1]
    delta = np.sqrt((a - d)**2 + 4*b**2)
    eig1 = 0.5 * (a + d - delta)
    eig2 = 0.5 * (a + d + delta)

    if b == 0:
        vec1 = np.array([1.0, 0.0])
        vec2 = np.array([0.0, 1.0])
    else:
        v1 = np.array([eig1 - d, b])
        v2 = np.array([eig2 - d, b])
        vec1 = v1 / np.linalg.norm(v1)
        vec2 = v2 / np.linalg.norm(v2)

    C = np.column_stack((vec1, vec2))
    return np.array([eig1, eig2]), C

def build_fock(P):
    F = H.copy()
    for i in range(2):
        for j in range(2):
            val = 0.0
            for k in range(2):
                for l in range(2):
                    g = eri.get((i, j, k, l), 0.0)
                    g_ex = eri.get((i, l, k, j), 0.0)
                    val += P[k, l] * (g - 0.5 * g_ex)
            F[i, j] += val
    return F

def scf():
    P = np.zeros((2, 2))
    E_old = 0.0
    for step in range(50):
        F = build_fock(P)
        S_inv = inverse_2x2(S)
        Fp = np.dot(S_inv, F)
        eigvals, C = diagonalize_2x2(Fp)

        C_occ = C[:, :1]
        P_new = 2 * np.dot(C_occ, C_occ.T)

        E_elec = 0.0
        for i in range(2):
            for j in range(2):
                E_elec += P_new[i, j] * (H[i, j] + F[i, j])

        if abs(E_elec - E_old) < 1e-6:
            break
        P = P_new
        E_old = E_elec

    return E_elec + 0.7143  # Add nuclear repulsion energy


hf_energy = scf()
print("Hartree-Fock energy of H2 =", round(hf_energy, 6), "Hartree")
