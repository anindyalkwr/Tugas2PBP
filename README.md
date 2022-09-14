# (README) Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku
[Lab 1 Assignment PBP/PBD](http://lokeswara-pbp-tugas2.herokuapp.com/katalog/)


## Penjelasan dan demonstrasi program
(1) Bagan _request client_ dan responnya pada aplikasi web berbasis Django 

![](baganPBP-rev.png)

  Program berjalan dengan memproses HTTP Request user pada file ```urls.py``` yang akan men-_extract_ URL dari request dan mencocokkan url tersebut dengan url yang telah terdefinisi. Apabila dikenali, maka program akan memanggil fungsi view pada file ```views.py``` yang bersesuaian (menggunakan parameter request) untuk membuat pemodelan dari data berdasarkan file ```models.py```. Terakhir pada file tersebut (models.py) terjadi transaksi data, yaitu pengambilan atau pembuatan data dari database (apabila tersedia) ke dalam fungsi view dan menerapkannya ke .html template yang sesuai.
 
 (2) Mengapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
 
