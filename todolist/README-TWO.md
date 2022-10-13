# PBP Assignment 6
Nama : Nyoo Steven Christopher 
NPM : 2106630050 
Kelas : PBP-D 
Link : [Link](https://tugas2-nyoo-pbp.herokuapp.com/todolist/)

## Asynchronous Programming dan Synchronous Programming
Synchronous Programming adalah proses jalannya program secara sequential , disini yang dimaksud sequential ada berdasarkan antrian ekseskusi program. Pada dasarnya semua Bahasa pemrograman menggunakan Asynchronouse terutama PHP.

Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous . Asynchronouse hampir disemua Bahasa pemrograman ada namun untuk PHP masih belum ada. PHP sebagai server side hanya menyediakan synchronous namun bisanya di WEB Developers tetap digunakan namun menggunakan AJAX (Asynchronous Javascript And XML) untuk proses Asynchronouse.

## Event-Driven Programming
Event-Driven Programming adalah salah satu teknik pemogramman, yang konsep kerjanya tergantung dari kejadian atau event tertentu. misalnya ketika tombol A diklik maka nilai label 2 di tambah nilai label 3 dibagi nilai label 4.  tapi jika tombol A diklik dan ternyata label satu berisikan penjumlahan. maka program yang dijalankan label 2 ditambah label 3.

Konsep Event-Driven Programming sama seperti konsep pemogramman menggunakan Procedure.  pemograman yang memiliki input, proses dan output. Namun, ada satu penambahan yang berbeda, yaitu konsep pemilihan untuk mengeksekusi proses programnya. Event-Driven programming juga bisa dibilang suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna atau bisa berupa pesan dari program lainnya. 

## Asynchronous Programming pada AJAX
Pengunaan AJAX, websit dapat mengirimkan request dan menerima response secara asynchronous. Ketika response dari server sampai ke browser, AJAX akan mengupdate website dari background. Karena response diterima secara asynchronous, website masih bisa digunakan oleh user meskipun AJAX sedang menunggu response server untuk interaksi user terakhir. User dapat melakukan  dan menggunakan website, terus menerus setiap kali tanpa menunggu.

## Implementasi
- Buat fungsi addtask yang digunakan untuk menambahkan data dari json.
- Menggunakan url addtask
- Implementasi penggunaan Ajax pada todolist.html
- Membuat beberapa function card, modal, open modal, close modal
