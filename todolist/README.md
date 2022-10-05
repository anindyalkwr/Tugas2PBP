
# (README) Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku
[App To Do List](https://lokeswara-pbp-tugas2.herokuapp.com/todolist/)

## Penjelasan dan demonstrasi program
(1) Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form? <br>

Cross-Site Request Forgery (CSRF) token adalah sebuah _secure random token (e.g., synchronizer token or challenge token)_ yang digunakan untuk menentukan apabila HTTP request yang diterima benar dihasilkan melalui _user interface_ dari aplikasi tersebut. Singkatnya, CRSF token bekerja dengan cara melakukan verifikasi terhadap _end-user request_ dnmana request yang di-_generate_ dari browser tersebut harus mengandung CRSF token yang bersangkutan dan server aplikasi akan menolak _request_ apabila CRSF token gagal memenuhi verifikasi tersebut. <br>

Apabila CSRF token tidak digunakan di dalam potongan kode yang dibutuhkan, seharusnya aplikasi tetap dapat berjalan sesuai dengan maksudnya, tetapi aplikasi menjadi sangat rentan untuk terkena _CSRF attack_ (Seseorang selain user dapat mengakses halaman yang seharusnya tidak dapat diakses / memerlukan kondisi khusus untuk diakses) sehingga dampaknya adalah mengalami kerugian data yang seharusnya bisa dihindari dengan mudah. <br>

(2) Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual. <br>

Kita tetap dapat membuat elemen form secara manual tanpa melalui generator tersebut, yaitu dengan menambahkan block form dari file html yang diinginkan dan dihubungkan dengan sebuah Action Trigger (atau url yang bersesuaian dengan fungsi views.py) yang akan memulai actionnya menggunakan method POST. Kemudian di dalam block form tersebut dapat diisi dengan block table yang akan meminta input dari user sesuai yang dibutuhkan formnya dan divalidasi sesuai pada file views.py. Apabila memenuhi maka, data dari form akan tersimpan dan dapat ditampilkan

(3) Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML. <br>

Setelah memberi input yang dibutuhkan oleh Form, data akan mempunyai value berupa Post yang divalidasi pada fungsi di dalam views.py (Data dapat diambil menggunakan fungsi request.POST.get()) . Setelah data berhasil divalidasi maka akan membuat objek TaskItem baru dengan attribut yang telah diberikan oleh user dan sekarang data sudah tersedia dalam database (data difilter sesuai usernya) serta akan menjadi response yang akan dimasukkan ke dalam url html yang akan disajikan kembali kepada user.
  
(4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>

Langkah - langkah yang dilakukan dalam pengerjaan checklist tugas 4, antara lain: <br>

(a) Pada direktori yang sama dengan tugas sebelumnya, saya masuk kedalam _virtual environment_ kemudian menjalankan perintah ```python manage.py startapp "app_name"``` untuk menambahkan folder app_name (todolist) beserta isinya sesuai dengan template yang telah disediakan. <br>

(b) Pada folder project_django, saya menambahkan app_name kedalam list installed_apps pada file settings.py dan juga menambahkan path 'todolist/' pada file urls.py yang juga include seluruh urlpatterns pada urls.py di folder todolist. <br>

(c) Dengan import models dari django.db, saya membuat class object TaskItem dengan seluruh attributes yang diminta pada soal. <br>

(d) Implementasi form registrasi, login, dan logout dilakukan beracuan pada materi yang diberikan pada lab3, dengan menyesuaikan data pada views.py yang diperlukan <br>

(e) Membuat file baru yaitu forms.py yang akan berfungsi meminta dan menerima input untuk data objek TaskItem, Serta menyiapkan semua html file yang diperlukan (Data dan fungsi untuk verifikasi dibuat ke dalam views.py) <br>
  
(f) Melengkapi file views.py dan menyiapkan seluruh routing yang diperlukan dari fungsi views.py , serta menghubungkan kode tersebut dengan file html. <br>

(g) Untuk melakukan deploy,  saya melakukan git add, commit, dan push ke repositori tugas pbp yang sama seperti sebelumnya. <br>

(h) Setelah deploy berhasil, saya melakukan pengecekan pada link app heroku yang telah di deploy apakah berjalan dengan lancar <br>

(i) Terakhir, saya menambahkan dari referensi yang saya baca dan membuat file README.md pada repositori github ini. <br>


#### Account Dummy Pertama
![](penggunaSatu.jpg) <br>

#### Account Dummy Kedua
![](penggunaDua.jpg) <br>


#### Referensi:
https://www.synopsys.com/glossary/what-is-csrf.html#:~:text=A%20CSRF%20token%20is%20a,token%20for%20every%20user%20session.
 
# (README) Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku
[App To Do List](https://lokeswara-pbp-tugas2.herokuapp.com/todolist/)

## Penjelasan dan demonstrasi program
(1) Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style? <br>

a. Inline CSS <br>
Inline CSS digunakan untuk memberi gaya (_style_) elemen HTML yang spesifik dengan menambahkan atribut _style_ di dalam tag HTML-nya. Hal ini menyebabkan Inline CSS dapat memiliki kelebihan dan kekurangan sebagai berikut: <br>

Kelebihan: <br>
Dapat digunakan untuk melakukan pengecekan apakah style yang akan diterapkan benar atau melakukan pembenaran skala kecil <br>
Tidak perlu membuat atau men-_upload_ dokumen terpisah atau ketika tidak mendapatkan akses kepada CSS Files <br>
Sangat efektif untuk menerapkan style pada elemen tunggal <br>

Kekurangan: <br>
Apabila digunakan untuk seluruh tag HTML atau sebagian besar, akan sangat tidak efektif baik dalam waktu pembuatannya maupun ruang dan waktu yang program butuhkan serta tidak terstruktur dengan rapih <br>

b. Internal CSS <br>
Internal CSS digunakan untuk memberi gaya kepada elemen HTML tunggal maupun lebih dalam file html yang sama atau file CSS pada direktori yang sama. Hal ini dilakukan dengan menambahkan tag style di dalam head section file HTML. Adapun kelebihan dan kekurangan dari Internal CSS, antara lain: <br>

Kelebihan: <br>
Efektif untuk menerapkan style pada halaman tunggal HTML <br>
Dapat menggunakan class dan Id Selectors di dalam style sheetnya <br>

Kekurangan: <br>
Apabila digunakan untuk banyak halaman HTML, tidak efektif baik dalam waktu pembuatannya maupun ruang dan waktu yang program butuhkan (Ukuran halaman dan lama aplikasi load) <br>

c. External CSS <br>
External CSS digunakan untuk memberi gaya kepada elemen HTML tunggal maupun lebih pada file CSS yang telah dihubungkan dengan webpagesnya. Adapun kelebihan dan kekurangan dari External CSS, antara lain: <br>

Kelebihan: <br>
Efektif digunakan untuk aplikasi yang memiliki lebih dari 1 html page dan terhubung <br>
HTML page menjadi lebih mudah dibaca dan lebih rapih <br>
File CSS dapat digunakan untuk memberi gaya pada beberapa macam page HTML <br>

Kekurangan: <br>
Tidak efektif digunakan dalam skala kecil <br>
Apabila external CSS File belum selesai di load, maka ada kemungkinan page tidak di render secara sempurna<br>
Apabila menggunakan banyak atau menghubungkan banyak external CSS files akan menambah waktu unduh site <br>

(2) Jelaskan tag HTML5 yang kamu ketahui. <br>
HTML menyediakan banyak tag untuk digunakan, tetapi beberapa tag yang paling umum dan sudah sering saya jumpai beserta kegunaannya, antara lain :

```<!DOCTYPE>	Tag untuk menentukan tipe dokumen
<html>	Tag untuk membuat sebuah dokumen HTML
<title>	Tag untuk membuat judul dari sebuah halaman
<body>	Tag untuk membuat tubuh dari sebuah halaman
<h1> to <h6>	Tag untuk membuat heading
<p>	Tag untuk membuat paragraf
<br>	Memasukan satu baris putus
<hr>	Tag untuk membuat perubahan dasar kata didalam isi
<!--...-->	Tag untuk membuat komentar
<table>	Tag untuk membuat tabel
<caption>	Tag untuk membuat sebuah caption tabel
<th>	Tag untuk membuat sebuah sel header tabel
<tr>	Tag untuk membuat baris dalam sebuah tabel
<td>	Tag untuk membuat sel dalam sebuah tabel
style>	Tag untuk membuat informasi style untuk dokumen
<div>	Tag untuk membuat sebuah bagian dalam dokumen
<span>	Tag untuk membuat sebuah bagian dalam dokumen
```
<br>

(3)  Jelaskan tipe-tipe CSS selector yang kamu ketahui. <br>
CSS selector yang saya ketahui dan beberapa sudah pernah saya gunakan, antara lain :

```Selektor Tag - tagName {}
Selektor Class - .className {}
Selektor ID - #id {}
Selektor Atribut - elemen[filter] {}
Selektor Universal - * {}
Selektor Pseudo - :hover {} atau :active {} dan masih banyak lagi
```
<br> 

(4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>
Saya menerapkan inline CSS dan juga internal CSS. <br>
a. Karena pada tugas 4 saya telah menerapkan internal CSS untuk memberi gaya pada file html, pada tugas 5 saya hanya menambahkan kode untuk membuat page saya menjadi lebih responsive. <br>
b. Selain itu, pada html file login, register. add_task saya sudah menggunakan konsep yang sama yaitu dengan adanya tabel dengan isi informasi dan juga button untuk melakukan operasi. Saya menambahkan :pseudo-class seperti hover agar page menjadi responsive; <br>
c. Pada file todolist sendiri, saya menghapus tabel yang ada dan membuat komponen cards berdasarkan website https://mdbootstrap.com/docs/standard/components/cards/. <br>
d. Setelah itu saya mulai menambahkan komponen yang diperlukan di dalam cards, dan menambahkan style agar cards dan page tersebut menjadi responsive. Salah satunya adalah kode bonus yaitu agar cards dapat di hover. <br>
e. Penyesuaian style saya lakukan dengan melihat perubahan pada localhost. <br>
f. Kemudian saya melakukan deploy dengan melakukan git add, git commit, dan git push. <br>
g. Setelah memastikan app heroku berjalan lancar, saya membaca beberapa referensi yang dibutuhkan untuk menjawab pertanyaan readme.md <br>

#### Referensi: <br>
https://www.hostinger.com/tutorials/difference-between-inline-external-and-internal-css <br>
https://gilacoding.com/read/tag-tag-pada-html-beserta-fungsinya
