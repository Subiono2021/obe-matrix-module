Error tersebut muncul karena file `README.md` **sudah ada** di dalam repositorimu. Artinya kamu tidak perlu membuat file baru lagi, cukup **edit** file yang sudah ada.

Berikut cara memperbaikinya:

---

### ✅ Cara Edit `README.md` yang Sudah Ada di GitHub

1. Buka link ini:  
   👉 [https://github.com/Subiono2021/obe-matrix-module/blob/main/README.md](https://github.com/Subiono2021/obe-matrix-module/blob/main/README.md)

2. Klik ikon **pensil** 🖉 di kanan atas (tombol "Edit this file")

3. Ganti isi `README.md` dengan versi yang saya siapkan:

```markdown
# 📦 OBE Matrix Module

Modul Python untuk melakukan **Operasi Baris Elementer (OBE)** pada matriks simbolik menggunakan `sympy`.

## 🔧 Instalasi

Di Google Colab:

```python
!wget -O obe_module.py https://raw.githubusercontent.com/Subiono2021/obe-matrix-module/main/obe_module.py
```

## 🚀 Contoh Penggunaan

```python
from obe_module import OBEMatrix

# Buat matriks simbolik 3x3
mat = OBEMatrix(3)

# Operasi E1: Tukar baris 1 dan 2
E, lbl = mat.swap_rows(0, 1)

# Tampilkan
print(mat.latex(E, lbl))
print(mat.latex(mat.apply_operation(E), f"{lbl}A"))
```

## ▶️ Coba di Colab

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Subiono2021/obe-matrix-module/blob/main/example.ipynb)

## 📄 Isi Modul

- `OBEMatrix(n)`: buat matriks simbolik ukuran n × n
- `swap_rows(i, j)`: tukar baris ke-i dan ke-j
- `scale_row(i, k)`: skala baris ke-i dengan faktor k
- `add_rows(i, j, k)`: tambahkan k × baris i ke baris j
- `apply_operation(E)`: kalikan E dengan A
- `latex(M, label)`: tampilkan string LaTeX dari matriks

## 📚 Lisensi

MIT License.
```

4. Scroll ke bawah, tulis pesan commit (misal: `Update README with usage example and Colab badge`)

5. Klik **"Commit changes"**

---

Kalau kamu mau saya bantu buatkan juga isi `example.ipynb`, tinggal bilang aja. Mau lanjut ke situ?

```python
!wget -O obe_module.py https://raw.githubusercontent.com/Subiono2021/obe-matrix-module/main/obe_module.py

