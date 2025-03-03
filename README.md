  | Nama                      | NRP        |
  |:-------------------------:|:----------:|
  | Almira Fidela Soehartanto Putri | 5025221222 |
  | Adelia Putri Kamaski        | 5025221320 |
  | Indhira Ayu Puspita Ningrum | 5025231316 |
  | Imelda Alexis Jovita  | 5025231032 |
  
  # Otomata - E (Ilham Gurat Adillion) Tugas 1

1. [Binary Checker](BinaryChecker.cpp)
   Algoritma:
   1. cek bit dari kiri ke kanan.
   2. lalu cocokkan dengan pattern yang telah disediakan sampai ketemu.
   3. jika ketemu maka testcase valid jika tidak ketemu reverse tescase yang diinputkan.
   4. sek seperti step ke-2.
   5. jika ketemu maka testcase valid, jika tidak maka tescase tidak valid.
  Program tersebut menggunakan konsep backtracking dan brute force yang dioptimalkan dengan rekursi.
2. [Arithmatic Expression Checker](ARITHMETIC.PY)
   Algoritma:
   1. Input operasi aritmatika yang ingin diperiksa. (jangan pakai spasi)
   2. Algoritma akan mencari () terdalam menggunakan fungsi dari regex.
   3. Setelah mencari () terdalam, ia akan mengevaluasi operatornya sesuai aturan yang ada di Buku Cohen Halaman 31 (fungsi check operator ada di dalam kode: menggunakan kombinasi stack dan if statements)
   4. Lalu setelah mengevaluasi, jika masih lanjut dan valid, () terdalam akan di representasikan (re.substitute) menjadi angka 1. Hal ini dikarenakan aturan (2): if x is true, then so are (x) and -(x).
      Jika dilogikakan, maka (x) also has the same value as x in a binary (1 and 0) checker situation. (x) can be presented as x if I want to. 
   6. Setelah dicek () terdalam, ia akan recursively mengecek () yang di luarnya. Aturannya masih sama seperti yang sebelumnya, cuma sekarang pakai operasi yang sudah disubstitusi elemennya.
   7. Operasi akan dicek kembali di main function, karena terkadang akan mengembalikan incomplete expression yang disebabkan oleh unbalanced parantheses.
   8. Hasil valid atau invalid adalah line terakhir yang di print kode.
