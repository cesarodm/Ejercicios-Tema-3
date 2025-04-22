def determinante_sarrus(m):
    return (
        m[0][0]*m[1][1]*m[2][2] +
        m[0][1]*m[1][2]*m[2][0] +
        m[0][2]*m[1][0]*m[2][1]
        - m[0][2]*m[1][1]*m[2][0]
        - m[0][0]*m[1][2]*m[2][1]
        - m[0][1]*m[1][0]*m[2][2]
    )

def determinante_recursivo(m):
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]

    det = 0
    for col in range(len(m)):
        submatriz = [
            [m[i][j] for j in range(len(m)) if j != col]
            for i in range(1, len(m))
        ]
        signo = (-1) ** col
        det += signo * m[0][col] * determinante_recursivo(submatriz)
    return det
