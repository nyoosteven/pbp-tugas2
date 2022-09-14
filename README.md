# PBP Assignment 2 

Nama    : Nyoo Steven Christopher
NPM     : 2106630050
Kelas   : PBP-D
Link aplikasi di Heroku : [Link](https://tugas2-nyoo-pbp.herokuapp.com/katalog/)

## Bagan Request User dan korelasi antara urls.py, models.py, views.py, dan html.
![](./render/Django.png?raw=true)

Penjelasan:
1. Pada awalnya, user melakukan request terhadap server Django.
2. URL akan memproses request tersebut dan melakukan routing ke views yang terpilih.
3. `views.py` memproses request tersebut dan melakukan query ke `models.py` jika diperlukan.
4. Di `models.py` mengambil data yang ada di database `katalog.html` sesuai permintaan `views.py`.
5. `views.py` akan memilih template html yang diperlukan dan menggunakan data dari models.py untuk memproses template tersebut lalu mengirim ke `html`
6. User menampilkan `html`.



## Virtual Environment
Virtual Environment sangat berguna ketika kita membutuhkan dependencies yang berbeda-beda antara project satu dengan lainnya yang berjalan pada satu system operasi yang sama.

Virtual Environment biasa digunakan untuk project berbasis Python. Karena Project tersebut mempunyai kebutuhan / dependent yang berbeda-beda antara satu dengan lainnya, maka dibutuhkanlah sebuah virtual environment untuk menjalankannya, tanpa merubah configurations pada system operasi yang kita pakai.

### Tidak adanya Virtual Environment
Dengan tidak adanya virtual environment pada web Django, jika Anda mengupdate libary/package akan berdampak untuk project lain juga. 

## Penjelasan Implementasi
### Prerequiste
Sebelumnya Anda harus memiliki sbuah aplikasi bernama `katalog app`. Setelah itu user akan mencari route, mana yang akan dipilih, untuk kasus ini pilih route `katalog`. 

Di langkah selanjutnya, Anda akan masuk ke folder `katalog` . 

### Fixtures
Masukan database yang akan ditampilkan di display. Jangan lupa load database tersebut.
```jsonld=
[
    {
        "model": "katalog.catalogitem",
        "pk": 1,
        "fields": {
            "item_name": "iPhone 12 Pro Max",
            "item_price": 17999999,
            "description": "Original from iBox",
            "item_stock": 3,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/ptpratamasemesta/iphone-12-pro-max-garansi-resmi-ibox-silver-256-gb"
        }
    },
    {
        "model": "katalog.catalogitem",
        "pk": 2,
        "fields": {
            "item_name": "MG Nu Gundam Ver.Ka",
            "item_price": 1060000,
            "description": "Bandai Original Ver.Ka Series",
            "item_stock": 100,
            "rating": 4,
            "item_url": "https://www.tokopedia.com/hobbyjapan/mg-nu-gundam-verka"
        }
    },
    {
        "model": "katalog.catalogitem",
        "pk": 3,
        "fields": {
            "item_name": "Samsung Galaxy S22",
            "item_price": 12249000,
            "description": "Specification: Snapdragon 8",
            "item_stock": 1,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/mhi-samsung/samsung-galaxy-s22-8-256gb-black"
        }
    },
    {
        "model": "katalog.catalogitem",
        "pk": 4,
        "fields": {
            "item_name": "Nike Air Jordan Fasilkom",
            "item_price": 3799000,
            "description": "Nike Original Made In China",
            "item_stock": 20,
            "rating": 5,
            "item_url": "https://www.tokopedia.com/807garage/air-jordan-1-mid-multicolour"
        }
    },
    {
        "model": "katalog.catalogitem",
        "pk": 5,
        "fields": {
            "item_name": "Airpods Pro 3 Official Guarantee from iBox",
            "item_price": 2999000,
            "description": "Authorized Reseller",
            "item_stock": 3,
            "rating": 4,
            "item_url": "https://www.tokopedia.com/tokobaruofficial/apple-airpods-3-mme73id-a-garansi-resmi-ibox"
        }
    }
]
```
### 1. urls.py
Buat path tambahan di `urlpatterns`. Ini bertujuan untuk melakukan routing ke selanjutnya. 
```python=
urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]
```
### 2. views.py
Buat fungsi `show_catalog` yang mereturn template html pada `views.py`.
```python=
from django.shortcuts import render
from katalog.models import CatalogItem
data_barang_katalog = CatalogItem.objects.all()
context = {
    'list_barang': data_barang_katalog,
    'nama': 'Nyoo Steven',
    'npm': '2106630050',
}
# TODO: Create your views here.
def show_katalog(request):
    return render(request, "katalog.html",context)
```
### 3. models.py
Buat class `CatalogItem` , sesuaikan dengan yang ada di render `html`.
```python=
class CatalogItem(models.Model):
    item_name = models.CharField(max_length=255)
    item_price = models.BigIntegerField()
    item_stock = models.IntegerField()
    description = models.TextField()
    rating = models.IntegerField()
    item_url = models.URLField()
```

### 4. html
Dari data yang kita berikan dalam bentuk context ke template (HTML), kita bisa tampilkan data yang diberikan tersebut

```html
{% extends 'base.html' %}

 {% block content %}

  <h1>Lab 1 Assignment PBP/PBD</h1>

  <h5>Name: </h5>
  <p>{{nama}}</p>

  <h5>Student ID: </h5>
  <p>{{npm}}</p>

  <table>
    <tr>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Item Stock</th>
      <th>Rating</th>
      <th>Description</th>
      <th>Item URL</th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% for items in list_barang %}
    <tr>
        <th>{{items.item_name}}</th>
        <th>{{items.item_price}}</th>
        <th>{{items.item_stock}}</th>
        <th>{{items.description}}</th>
        <th>{{items.rating}}</th>
        <th>{{items.item_url}}</th>
    </tr>
    {% endfor %}
  </table>

 {% endblock content %}
 ```

### Deploy
Setelah semua selesai, jangan lupa untuk git add,commit,pull, dan push di github Anda. Setelah itu repo yang Anda gunakan akan dihubungkan dengan aplikasi yang Anda buat di Herokuapp. Setelah itu lakukan deploy di Herokuapp. 

