def inverse_2x2(m):
    det = m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]
    inv = np.array([[m[1, 1], -m[0, 1]],
                    [-m[1, 0], m[0, 0]]]) / det
    return inv

S = np.array([[1.0, 0.35],
              [0.35, 1.0]])

print(inverse_2x2(S))
