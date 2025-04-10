Program ini mendefinisikan sebuah kelas bernama `OBEMatrix` yang bertujuan untuk merepresentasikan matriks dan operasi baris elementer (Elementary Row Operations - EROs) yang dapat diterapkan padanya. Mari kita breakdown setiap bagian dari kelas ini:

**1. Import `sympy`:**
   - `import sympy as sp`: Mengimpor library SymPy dan memberikannya alias `sp`. SymPy adalah library Python untuk matematika simbolik, yang memungkinkan kita untuk bekerja dengan simbol-simbol matematika dan melakukan operasi aljabar secara simbolik.

**2. Definisi Kelas `OBEMatrix`:**
   - `class OBEMatrix:`: Mendefinisikan sebuah kelas bernama `OBEMatrix`. Kelas ini akan memiliki atribut dan metode yang berkaitan dengan matriks dan operasi baris elementer.

**3. Metode `__init__(self, size)` (Konstruktor):**
   - `def __init__(self, size):`: Ini adalah konstruktor kelas. Metode ini dipanggil ketika sebuah objek dari kelas `OBEMatrix` dibuat.
   - `if size <= 0:`: Memeriksa apakah ukuran matriks (didefinisikan oleh `size`) kurang dari atau sama dengan nol. Jika ya, maka:
     - `raise ValueError("Ukuran matriks harus lebih dari nol.")`: Akan memunculkan error `ValueError` dengan pesan yang sesuai, karena ukuran matriks harus positif.
   - `self.n = size`: Menyimpan ukuran matriks (`size`) sebagai atribut `n` dari objek `OBEMatrix`.
   - `self.A = sp.Matrix(size, size, lambda i, j: sp.Symbol(f"a_{{{i+1},{j+1}}}"))`: Ini adalah bagian penting.
     - `sp.Matrix(size, size, ...)`: Membuat sebuah matriks SymPy berukuran `size x size`.
     - `lambda i, j: sp.Symbol(f"a_{{{i+1},{j+1}}}")`: Ini adalah fungsi lambda yang mendefinisikan elemen-elemen dari matriks. Untuk setiap indeks baris `i` dan indeks kolom `j` (keduanya dimulai dari 0), elemen matriks akan menjadi simbol SymPy dengan format `a_{baris,kolom}` (misalnya, `a_{1,1}`, `a_{2,3}`, dll.). Ini memungkinkan kita untuk bekerja dengan matriks secara simbolik, di mana elemen-elemennya tidak harus berupa angka spesifik. Matriks simbolik ini disimpan sebagai atribut `A` dari objek `OBEMatrix`.

**4. Metode `swap_rows(self, i, j)`:**
   - `def swap_rows(self, i, j):`: Metode ini menghasilkan matriks elementer yang sesuai dengan operasi pertukaran baris `i` dan baris `j`.
   - `if not (0 <= i < self.n and 0 <= j < self.n and i != j):`: Memeriksa apakah indeks baris `i` dan `j` valid (berada dalam batas ukuran matriks) dan apakah `i` tidak sama dengan `j` (kita tidak menukar baris dengan dirinya sendiri). Jika tidak valid:
     - `raise IndexError("Indeks tidak valid untuk tukar baris.")`: Akan memunculkan error `IndexError` dengan pesan yang sesuai.
   - `E = sp.eye(self.n)`: Membuat matriks identitas SymPy berukuran `n x n`. Matriks identitas adalah matriks persegi dengan angka 1 di diagonal utama dan 0 di tempat lain.
   - `E[i, i], E[j, j] = 0, 0`: Mengubah elemen diagonal pada baris `i` dan `j` menjadi 0.
   - `E[i, j], E[j, i] = 1, 1`: Mengubah elemen pada posisi (`i`, `j`) dan (`j`, `i`) menjadi 1. Matriks `E` yang dihasilkan adalah matriks elementer untuk pertukaran baris. Ketika matriks ini dikalikan dari kiri dengan matriks lain, baris `i` dan `j` dari matriks tersebut akan tertukar.
   - `return E, "E_1"`: Mengembalikan matriks elementer `E` dan string `"E_1"` sebagai label (konvensi untuk matriks elementer tipe pertama - pertukaran baris).

**5. Metode `scale_row(self, i, factor)`:**
   - `def scale_row(self, i, factor):`: Metode ini menghasilkan matriks elementer yang sesuai dengan operasi mengalikan baris `i` dengan suatu `factor`.
   - `if not (0 <= i < self.n) or factor == 0:`: Memeriksa apakah indeks baris `i` valid dan apakah faktor pengali tidak nol. Jika tidak valid:
     - `raise ValueError("Indeks tidak valid atau faktor nol.")`: Akan memunculkan error `ValueError` dengan pesan yang sesuai (mengalikan baris dengan 0 biasanya tidak dianggap sebagai operasi baris elementer dalam konteks reduksi baris untuk menyelesaikan sistem persamaan linear).
   - `E = sp.eye(self.n)`: Membuat matriks identitas SymPy berukuran `n x n`.
   - `E[i, i] = factor`: Mengubah elemen diagonal pada baris `i` menjadi `factor`. Matriks `E` yang dihasilkan adalah matriks elementer untuk penskalaan baris. Ketika matriks ini dikalikan dari kiri dengan matriks lain, baris `i` dari matriks tersebut akan dikalikan dengan `factor`.
   - `return E, "E_2"`: Mengembalikan matriks elementer `E` dan string `"E_2"` sebagai label (konvensi untuk matriks elementer tipe kedua - penskalaan baris).

**6. Metode `add_rows(self, i, j, factor)`:**
   - `def add_rows(self, i, j, factor):`: Metode ini menghasilkan matriks elementer yang sesuai dengan operasi menambahkan `factor` kali baris `i` ke baris `j`.
   - `if not (0 <= i < self.n and 0 <= j < self.n and i != j):`: Memeriksa apakah indeks baris `i` dan `j` valid dan apakah `i` tidak sama dengan `j`. Jika tidak valid:
     - `raise IndexError("Indeks tidak valid untuk penjumlahan baris.")`: Akan memunculkan error `IndexError` dengan pesan yang sesuai.
   - `E = sp.eye(self.n)`: Membuat matriks identitas SymPy berukuran `n x n`.
   - `E[j, i] = factor`: Mengubah elemen pada posisi (`j`, `i`) menjadi `factor`. Perhatikan urutan indeksnya: kita menambahkan kelipatan baris `i` ke baris `j`, sehingga elemen di baris `j` dan kolom `i` dari matriks elementer menjadi `factor`. Ketika matriks ini dikalikan dari kiri dengan matriks lain, `factor` kali baris `i` akan ditambahkan ke baris `j` dari matriks tersebut.
   - `return E, "E_3"`: Mengembalikan matriks elementer `E` dan string `"E_3"` sebagai label (konvensi untuk matriks elementer tipe ketiga - penambahan kelipatan satu baris ke baris lain).

**7. Metode `apply_operation(self, E)`:**
   - `def apply_operation(self, E):`: Metode ini menerapkan operasi baris elementer yang direpresentasikan oleh matriks `E` ke matriks `self.A`.
   - `return E * self.A`: Melakukan perkalian matriks antara `E` (matriks elementer) dan `self.A` (matriks utama). Karena perkalian matriks dari kiri dengan matriks elementer sesuai dengan penerapan operasi baris elementer, metode ini mengembalikan matriks hasil setelah operasi diterapkan.

**8. Metode `latex(self, matrix, label="A")`:**
   - `def latex(self, matrix, label="A"):`: Metode ini menghasilkan representasi LaTeX dari suatu matriks SymPy.
   - `return f"${label} = {sp.latex(matrix)}$"`: Menggunakan f-string untuk membuat string LaTeX.
     - `${label} = `: Menampilkan label matriks (defaultnya "A") diikuti dengan tanda sama dengan.
     - `{sp.latex(matrix)}`: Menggunakan fungsi `sp.latex()` dari SymPy untuk mengonversi matriks `matrix` menjadi representasi LaTeX-nya.
     - Tanda `$` di awal dan akhir string menandakan bahwa ini adalah ekspresi matematika dalam LaTeX.

**Kegunaan Program:**

Kelas `OBEMatrix` ini sangat berguna untuk:

- **Memvisualisasikan Operasi Baris Elementer:** Kita dapat membuat matriks elementer yang sesuai dengan setiap operasi dan melihat bentuknya secara simbolik.
- **Melakukan Reduksi Baris Secara Simbolik:** Meskipun program ini tidak secara otomatis melakukan reduksi baris (seperti Gaussian elimination), kita dapat menggunakan metode-metodenya untuk menerapkan operasi baris satu per satu dan melihat hasilnya pada matriks simbolik `self.A`.
- **Memahami Konsep Matriks Elementer:** Program ini membantu dalam memahami bagaimana setiap operasi baris elementer dapat direpresentasikan oleh perkalian dengan matriks elementer yang spesifik.
- **Pendidikan dan Demonstrasi:** Program ini dapat digunakan sebagai alat bantu dalam pengajaran aljabar linear untuk mendemonstrasikan konsep operasi baris elementer dan matriks elementer.

**Contoh Penggunaan:**

```python
# Membuat matriks simbolik 3x3
matrix_op = OBEMatrix(3)
print("Matriks Awal:")
print(matrix_op.latex(matrix_op.A))

# Operasi tukar baris 0 dan 1
E1, label1 = matrix_op.swap_rows(0, 1)
matrix_op.A = matrix_op.apply_operation(E1)
print(f"\nMatriks Elementer {label1} (tukar baris 1 dan 2):")
print(matrix_op.latex(E1, label=label1))
print("\nMatriks A setelah operasi:")
print(matrix_op.latex(matrix_op.A))

# Operasi skala baris 1 dengan faktor k
k = sp.Symbol('k')
E2, label2 = matrix_op.scale_row(1, k)
matrix_op.A = matrix_op.apply_operation(E2)
print(f"\nMatriks Elementer {label2} (skala baris 2 dengan k):")
print(matrix_op.latex(E2, label=label2))
print("\nMatriks A setelah operasi:")
print(matrix_op.latex(matrix_op.A))

# Operasi tambah 2 kali baris 0 ke baris 2
E3, label3 = matrix_op.add_rows(0, 2, 2)
matrix_op.A = matrix_op.apply_operation(E3)
print(f"\nMatriks Elementer {label3} (tambah 2 * baris 1 ke baris 3):")
print(matrix_op.latex(E3, label=label3))
print("\nMatriks A setelah operasi:")
print(matrix_op.latex(matrix_op.A))
```

Output dari contoh di atas akan menampilkan representasi LaTeX dari matriks awal dan matriks setelah setiap operasi baris elementer diterapkan, beserta matriks elementer yang bersesuaian. Ini akan membantu dalam memahami bagaimana operasi-operasi ini memengaruhi matriks secara simbolik.
