```markdown
# 📦 OBE Matrix Module

Modul Python untuk melakukan **Operasi Baris Elementer (OBE)** pada matriks simbolik menggunakan `sympy`.

## 🔧 Instalasi (di Google Colab)

Unduh modul langsung:

```python
!wget -O obe_module.py https://raw.githubusercontent.com/Subiono2021/obe-matrix-module/main/obe_module.py
```

## 🚀 Contoh Penggunaan

```python
from obe_module import OBEMatrix

# Buat matriks simbolik 3x3
mat = OBEMatrix(3)

# Operasi E₁: Tukar baris 1 dan 2
E, lbl = mat.swap_rows(0, 1)
print(mat.latex(E, lbl))          # Matriks elementer E₁
print(mat.latex(mat.apply_operation(E), f"{lbl}A"))  # Hasil perkalian E₁A

# Operasi E₂: Skala baris 1 dengan 2
E2, lbl2 = mat.scale_row(0, 2)
print(mat.latex(E2, lbl2))
print(mat.latex(mat.apply_operation(E2), f"{lbl2}A"))

# Operasi E₃: Tambah -3×baris 1 ke baris 3
E3, lbl3 = mat.add_rows(0, 2, -3)
print(mat.latex(E3, lbl3))
print(mat.latex(mat.apply_operation(E3), f"{lbl3}A"))
```

### 🧾 Contoh Output (LaTeX string)

```
E_1 = \left[\begin{matrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{matrix}\right]
E_1A = \left[\begin{matrix}a_{2,1} & a_{2,2} & a_{2,3}\\a_{1,1} & a_{1,2} & a_{1,3}\\a_{3,1} & a_{3,2} & a_{3,3}\end{matrix}\right]

E_2 = \left[\begin{matrix}2 & 0 & 0\\0 & 1 & 0\\0 & 0 & 1\end{matrix}\right]
E_2A = \left[\begin{matrix}2 a_{1,1} & 2 a_{1,2} & 2 a_{1,3}\\a_{2,1} & a_{2,2} & a_{2,3}\\a_{3,1} & a_{3,2} & a_{3,3}\end{matrix}\right]

E_3 = \left[\begin{matrix}1 & 0 & 0\\0 & 1 & 0\\-3 & 0 & 1\end{matrix}\right]
E_3A = \left[\begin{matrix}a_{1,1} & a_{1,2} & a_{1,3}\\a_{2,1} & a_{2,2} & a_{2,3}\\-3 a_{1,1} + a_{3,1} & -3 a_{1,2} + a_{3,2} & -3 a_{1,3} + a_{3,3}\end{matrix}\right]
```

## ▶️ Coba Langsung di Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Subiono2021/obe-matrix-module/blob/main/example.ipynb)

## 📄 API

- `OBEMatrix(n)` → Buat matriks simbolik ukuran n × n
- `.swap_rows(i, j)` → Tukar baris ke-i dan ke-j
- `.scale_row(i, k)` → Skala baris ke-i dengan faktor k
- `.add_rows(i, j, k)` → Tambah k × baris i ke baris j
- `.apply(E)` → Kalikan E dengan A (E · A)
- `.latex(M, label)` → Tampilkan matriks dalam format string LaTeX

## 📚 Lisensi

MIT License.
```
