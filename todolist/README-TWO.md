# Tugas 6: Javascript dan AJAX

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

## Link Aplikasi Heroku
[App To Do List](https://lokeswara-pbp-tugas2.herokuapp.com/todolist/)

## Penjelasan dan demonstrasi program
(1) Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. <br>
Sederhananya, pada synchronous programming satu operasi dijalankan di satu waktu dan akan menunggu hingga operasi tersebut selesai untuk dapat lanjut ke operasi selanjutnya, sedangkan pada asynchronous programming operasi dapat terus dilaksanakan tanpa menunggu (dependen) terhadap operasi sebelumnya. <br>
Sehingga pada asychronous programming memperbolehkan untuk menghadapi request banyak sekaligus secara lebih cepat. <br>

(2) Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. <br>
Paradigma Event Driven Programming bermaksud bahwa alur dari suatu program ditentukan oleh suatu "Event" yang dapat berupa user actions dan lain lain. Salah satu contoh yang diterapkan pada tugas ini adalah ketika menggunakan tombol "Add a new task" / "Delete" / "Change Progression", yaitu menunggu user action (menekan tombol) sebelum melakukan fungsi yang bersesuaian. <br>

(3) Jelaskan penerapan asynchronous programming pada AJAX. <br>
Asynchronus programming diterapkan pada AJAX, pada operasi - operasi penambahan, penghapusan, dan perubahan status card objek TaskItem. Dimana untuk melakukan operasi tersebut tidak terjadi proses men-refresh halaman keselurhan sehingga dapat tetap melanjutkan operasi lainnya. <br>

(4) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. <br>
Langkah - langkah yang dilakukan dalam pengerjaan checklist tugas 6, antara lain: <br>
Setelah menambahkan fungsi show_json dan urlnya pada folder todolist, saya menambahkan script ajax dan operasi get dan post untuk melakukan operasinya. Dimana terdapat fungsi Get yaitu createTask(), deleteTask(), toggleTaskStatus(), dan getTaskList() yang akan mengambil data dari json berdasarkan url yang telah di map. Serta fungsi Post putTaskList yang akan mengiterasi data for each berisikan kartu berisi TaskItem. Saya juga merubah form menjadi di dalam tag form yang sebelumnya merupakan template (UserCreationForm() untuk form createTask()) untuk memudahkan memasukannya ke dalam modal untuk ditampilkan <br>

#### Referensi: <br>
https://www.outsystems.com/blog/posts/asynchronous-vs-synchronous-programming/
