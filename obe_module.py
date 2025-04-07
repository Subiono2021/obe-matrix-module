
import sympy as sp

class OBEMatrix:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Ukuran matriks harus lebih dari nol.")
        self.n = size
        self.A = sp.Matrix(size, size, lambda i, j: sp.Symbol(f"a_{{{i+1},{j+1}}}"))

    def swap_rows(self, i, j):
        if not (0 <= i < self.n and 0 <= j < self.n and i != j):
            raise IndexError("Indeks tidak valid untuk tukar baris.")
        E = sp.eye(self.n)
        E[i, i], E[j, j] = 0, 0
        E[i, j], E[j, i] = 1, 1
        return E, "E_1"

    def scale_row(self, i, factor):
        if not (0 <= i < self.n) or factor == 0:
            raise ValueError("Indeks tidak valid atau faktor nol.")
        E = sp.eye(self.n)
        E[i, i] = factor
        return E, "E_2"

    def add_rows(self, i, j, factor):
        if not (0 <= i < self.n and 0 <= j < self.n and i != j):
            raise IndexError("Indeks tidak valid untuk penjumlahan baris.")
        E = sp.eye(self.n)
        E[j, i] = factor
        return E, "E_3"

    def apply_operation(self, E):
        return E * self.A

    def latex(self, matrix, label="A"):
        return f"${label} = {sp.latex(matrix)}$"
