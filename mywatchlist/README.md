# (README) Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku
[HTML](http://lokeswara-pbp-tugas2.herokuapp.com/mywatchlist/html/)
[XML](http://lokeswara-pbp-tugas2.herokuapp.com/mywatchlist/xml/)
[JSON](http://lokeswara-pbp-tugas2.herokuapp.com/mywatchlist/json/)

## Penjelasan dan demonstrasi program
(1) Jelaskan perbedaan antara JSON, XML, dan HTML! <br>
(2) Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? <br>
(3) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>

Langkah - langkah yang dilakukan dalam pengerjaan checklist tugas 3, antara lain: <br>

(a) Pada direktori yang sama dengan tugas sebelumnya, saya masuk kedalam _virtual environment_ kemudian menjalankan perintah ```python manage.py startapp "app_name"``` untuk menambahkan folder app_name (mywatchlist) beserta isinya sesuai dengan template yang telah disediakan. <br>

(b) Pada folder project_django, saya menambahkan app_name kedalam list installed_apps pada file settings.py dan juga menambahkan path'mywatchlist/' pada file urls.py yang juga include seluruh urlpatterns pada urls.py di folder mywatchlist. <br>

(c) Dengan import models dari django.db, saya membuat class object WatchlistItem dengan seluruh attributes yang diminta pada soal. <br>

(d) Lalu saya membuat folder fixtures di dalam folder mywatchlist dan menambahkan file initial_watchlist_data.json yang berisi object class yang baru saja dibuat pada poin (c) sebanyak 10 buah. Serta menjalankan perintah ```python manage.py makemigrations``` dan ```python manage.py migrate``` untuk mempersiapkan dan menerapkan migrasi skema model ke dalam database Django lokal, serta perintah ```python manage.py loaddata initial_watchlist_data.json``` untuk memasukkan data dari folder fixtures ke dalam database Django lokal. <br>

(e) Pada fungsi views.py saya menambahkan function yang mengembalikan data / menyajikan data dalam bentuk HTML, XML, JSON, kemudian menambahkan routingnya ke dalam file urls.py yang ada pada folder mywatchlist <br>

(f) Sebelum melakukan deploy, pada file procfile saya menambahkan loaddata watchlist dan melakukan migrate ulang, kemudian saya melakukan git add, commit, dan push ke repositori tugas pbp yang sama seperti sebelumnya. <br>

(g) Setelah deploy berhasil, saya membuat akun postman dan juga melakukan pengecekan pada link app heroku yang telah di deploy apakah mengembalikan respon HTTP 200 OK <br>

(h) Terakhir, saya menambahkan unit test dari referensi - referensi yang saya baca dan membuat file README.md pada repositori github ini. <br>


#### URL "/mywatchlist/html" berhasil mengembalikan respon HTTP 200 OK
![](postmanHTML.jpg) <br>

#### URL "/mywatchlist/xml" berhasil mengembalikan respon HTTP 200 OK
![](postmanXML.jpg) <br>

#### URL "/mywatchlist/json" berhasil mengembalikan respon HTTP 200 OK
![](postmanJSON.jpg) <br>

#### Referensi:
