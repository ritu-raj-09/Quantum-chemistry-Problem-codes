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
A=S = np.array([[1.0, 0.44],
              [0.44, 1.0]])
print(diagonalize_2x2(A))
