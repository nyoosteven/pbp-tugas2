# PBP Assignment 5
Nama : Nyoo Steven Christopher 
NPM : 2106630050 
Kelas : PBP-D 
Link : [Link](https://tugas2-nyoo-pbp.herokuapp.com/todolist/)

## Inline, Internal, dan External CSS
### Inline CSS
Inline CSS adalah memasukan kode CSS yang ditulis secara langsung pada setiap atribut HTML. Jadi setiap atribut memiliki style CSS yang berbeda tergantung kebutuhan. Inline CSS ini tergolong kurang efisien jika dibandingkan jenis CSS untuk website lainnya. Karena dalam satu atribut memiliki style tersendiri.
```css
<h1 style="color:orange; font-family: arial;">Qwords.com</h1>
```
### Internal CSS
Internal CSS adalah kode CSS yang ditulis dalam tag `<style>` dan lokasinya berada pada bagian atas header file HTML. Internal CSS digunakan untuk membuat custom khusus dalam satu halaman website sehingga halaman lain tidak terpengaruh.

Custom halaman dengan internal CSS ini cocok dipakai untuk Anda yang memiliki website dengan tampilan yang berbeda-beda. Jadi untuk Anda yang ingin membuat website unik dengan berbagai tampilan halaman website yang berbeda, maka inline CSS ini pilihan yang paling benar.
```css
<!DOCTYPE html>
<html>
<head>
  <title>Internal CSS dalam Website</title>
  <!-- contoh internal css dalam tag head -->
  <style type="text/css">
                h1 {
               text-align: center;
               font-family: arial;
               color: orange;
             }
             h2 {
               text-align: left;
               font-family: calibri;
               color: black;
             }
  </style>
</head>
<body>
             <!-- contoh internal css dalam tag body -->
  <style type="text/css">
   h1 {
  text-align: center;
  font-family: arial;
  color: orange;
             }
             h2 {
  text-align: left;
  font-family: calibri;
  color: black;
             }
  </style>
  <h1>Qwords.com</h1>
  <h2>Contoh Internal CSS</h2>
</body>
</html>
```

### External CSS
External CSS adalah kode CSS yang penulisannya dipisah dengan file HTML. Jadi file CSS ditulis pada file sendiri dengan ekstensi .css. File External CSS biasa dituliskan pada bagian `<head>`, jadi setiap halaman website dilakukan pemanggilan file .css. Penggunaan External CSS lebih simple dan sederhana karena tidak perlu menuliskan CSS dalam setiap file HTML.
```css
h1 {
   text-align: center;
   font-family: arial;
   color: orange;
 }
 h2 {
   text-align: left;
   font-family: calibri;
   color: orange;
 }
 h1 {
   text-align: center;
   font-family: arial;
   color: orange;
 }
 h2 {
   text-align: left;
   font-family: calibri;
   color: orange;
 }
```

## Tag HTML5
1. `<a>` untuk menampilkan link
2. `<b>` untuk membuat text menjadi bold
3. `<form>` untuk mendefinisikan suatu form
4. `<body>` main HTML part
5. `<br>` untuk break
6. `<div>` suatu bagian pada dokumen HTML
7. `<h1>` untuk judul
8. `<i>` untuk membuat teks menjadi italik to 
9. `<img>` untuk gambar pada suatu dokumen
10. `<ol>` adalah suatu ordered list
11. `<ul>` untuk suatu unordered list
12. `<li>` tag element untuk item dari list `<ul>` ataupun`<ol>`
13. `<p>` untuk paragraf
14. `<span>` untuk style pada suatu teks
15. `<head>` tag element yang berisi metadata dari html.

## CSS Selector
1. `.class` yang menunjuk ke semua element dengan attribut class="class".
2. `#id` mengarah pada penggunaan property id pada html tag.
3. `*` menselect semua element.
4. `.class1` `.class2` yang digunakan untuk semua element dengan attribut class="class2" yang berada dalam element dengan attribut class="class1"


## Implementasi
### Prerequisites
Pada awalanya implementasi pada tugas ini menggunakan tailwind css. Import tailwindcss menggunakan script 
```css=
<script src="https://cdn.tailwindcss.com"></script>
```
Setelah itu edit sesuka anda menggunakan tailwind.

### todolist
Membuat background yang akan ditampilkan di html
```css=
<div class=" bg-slate-200 h-screen">
    <div class = "h-screen login flex justify-center items-center">
```
Membuat card untuk setiap adanya task baru.
```css
<div class="block bg-white shadow-lg rounded-lg p-6">
```
Melakukan hover pada setiap card di task dengan menggunakan 
```css=
class = "transition ease-in-out hover:scale-105 hover:bg-gray-200" 
```
Implementasi juga pada websites sehingga menjadi responsive websites.
```css
 <div class="max-w-[80%] mx-auto">
    <div class="flex flex-wrap gap-5 justify-center">
```
Pada bagian register, login, dan create task penggunaan implementasi sama persis yaitu dengan melakukan card, button, dan lain lain.

Setelah itu seperti biasa kita melakukan deploy ke Herokuapp. Jangan lupa lakukan git add,commit,pull, dan push ke repo Anda.
