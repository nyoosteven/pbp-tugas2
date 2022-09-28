# PBP Assignment 4

Nama   : Nyoo Steven Christopher
NPM    : 2106630050
Kelas  : PBP-D
Link aplikasi di Heroku : [Link](https://tugas2-nyoo-pbp.herokuapp.com/todolist/)

## CSRF Token
CSRF (Cross Site Request Forgery) adalah serangan eksploitasi web yang membuat pengguna tanpa sadar mengirim sebuah permintaan atau request ke website melalui website yang sedang digunakan saat itu.

Aplikasi web akan mengeksekusi dan menanggapi request tersebut yang sebenarnya bukan keinginan dari pengguna. Dengan begitu, jika website tersebut menerima request tanpa CSRF token yang tepat, maka request tersebut akan ditolak.

Orang - orang yang tidak bertanggung jawab akan menyematkan suatu file berupa link, image, dan text dll. Jika Anda tidak sengaja membuka website tersebut, ini sangat berbahaya dikarenakan mungkin saja terdapat malicious code.

Dengan tidak adanya `{% csrf_token %}` maka form tersebut tidak adanya sebuah csrf_token sehingga penyerang/hacker dapat melakukan CSRF terhadap request yang berhubungan dengan form tersebut.

## Membuat elemen form secara manual
Kita dapat memanfaatkan fitur HTML untuk menyusun suatu form. Kita juga dapat menentukan User interface sesuka kita. 

Dalam pembuatan form secara manual, ini dapat dibuat dengan memisalkan setiap elemen sebagai elemen masukan pengguna. 
Sebagai contoh:
```htmlembedded=
    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>
```
Kita dapat menentukan action dan method dalam penggunaan form, sebagai contoh method POST yaitu data dikirim ke server sebagai paket dalam komunikasi terpisah dengan skrip pemrosesan. Kita juga menambahkan elemen input input, untuk kasus ini ada banyak argumen value, id, type, placeholder, name, dan class. Setelah itu, ini digunakan pengguna untuk submit form tersebut.

## Alur Data
Pengguna akan mengisi form, setelah itu data mereka yang sudah diisi akan disimpan pada browser/internet pengguna. Setelah pengguna menekan tombol submit, form akan terkirim sebagai HTTP request POST.  Data akan diterima oleh server 
Saat user mengisi form, data yang diisi pada form tersebut akan disimpan terlebih dahulu oleh browser user. Setelah user menekan tombol submit, maka form tersebut akan terkirim sebagai HTTP request dengan method dan url yang sudah ditentukan oleh attribute dari form tersebut. Data tersebut kemudian akan diterima oleh server yang dituju url form tersebut. Data tersebut akan disimpan ke dalam database.Jika data ingin ditampilkan, kita dapat menampilkan data tersebut di template HTML. HTML tersebut dikirimkan ke pengguna yang dirender dengan menggunakan data baru dari database.

## Implementasi
### Prerequisite
Pada awalnya kita membuat aplikasi todolist. Setelah itu user akan mencari route, mana yang akan dipilih, untuk kasus ini pilih route todolist. Kita menambahkan path yang diperlukan pada urls.py di folder project_django dan todolist.

### models.py
Membuat models.py dengan menambahkan beberapa atribut, atribut-atributnya adalah user, date, title, description, dan is_finished.
```python
class Task(models.Model):
    user = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    date = models.DateField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```
Setelah itu, lakukan `python manage.py makemigration` dan `python manage.py migrate` untuk memasukan model. 

### views.py
Dalam pembuatan fungsi register, diperlukan `UserCreationForm`  dan menggunakan {{ form.as_table }} pada html agar langsung digenerate formnya.
```python=
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
```
Form login dibuat dengan manual, dan membutuhkan 2 input field yaitu username dan password. Saat login, fungsi akan membutuhkan username dan password pengguna, kemudian function di login untuk melakukan autentikasi user dengan bantuan authenticator yang terdapat di Django.

```python=
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
```
Dalam logut tidak adanya form, dengan menambahkan button logout dan dengan menggunakan fungsi logout.
```python=
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response
```
### html
Membuat todolist.html yang berisi label bertuliskan user yang terlogin, tombol untuk membuat task baru, tombol logout yang terhubung ke function logout, dan tabel dengan kolom sesuai attribute Task untuk menampilkan semua task dari user yang terlogin. Fungsi akan melakukan render todolist.html. Kita juga perlu menambahkan url routing ke function tersebut.

Berikut adalah salah satu contoh HTML pada show_todolist.html
```htmlembedded=
{% extends 'base.html' %}

 {% block content %}

  <h1>Tugas 4 Assignment PBP/PBD</h1>

  <h5>Username: </h5>
  <p>{{username}}</p>

  <button>
    <a href="{% url 'todolist:new_create_todolist' %}">Tambah Task Baru</a>
  </button>

  <table>
    <tr>
        <th>Date</th>
        <th>Title</th>
        <th>Description</th>
        <th>Finished</th>
        <th>Change tasked</th>
        <th>Delete tasked</th>
    </tr>
    {% for item in semua_task %}
    <tr>
      <th>{{item.date}}</th>
      <th>{{item.title}}</th>
      <th>{{item.description}}</th>
      <th>{{item.is_finished}}</th>
      <th><button><a href="updatetask/{{item.id}}">Change task finished status</a></button></th>
      <th><button><a href="deletetask/{{item.id}}">Delete task</a></button></th>
    </tr>
    {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
    {% endfor %}
  </table>

  <h5>Sesi terakhir login: {{ last_login }}</h5>
  <button><a href="{% url 'todolist:logout' %}">Logout</a></button>
 {% endblock content %}
```

### new_create_todolist
Saat membuat todolist baru diperlukan beberapa data baru seperti judul dan deskripsi. Berikut adalah fungsinya
```python=
@login_required(login_url='login/')
def new_create_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        print(title,description)
        todo = Task.objects.create(title=title, description=description,date=datetime.date.today(), user=request.user)
        response = HttpResponseRedirect(reverse("todolist:show_todolist")) 
        return response
    return render(request,'new_create_todolist.html')
```
Fungsi ini akan ditampilkan pada HTML 
```htmlembedded
{% extends 'base.html' %}

{% block meta %}
<title>Todolist</title>
{% endblock meta %}

{% block content %} 

<div class = "create task">

    <h1>Judul Baru</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Judul: </td>
                <td><input type="text" name="title" placeholder="Title" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Deskripsi: </td>
                <td><input type="text" name="description" placeholder="Description" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Submit"></td>
            </tr>
        </table>
    </form>
</div>
{% endblock content %} 
```
### Bonus (is_finished)
Untuk membuat agar atribut berubah yang jadinya sudah selesai menjadi belum selesai diperlukan path baru dan fungsi baru.
```python=
def updatetask(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished ^= True
    else:
        return redirect('todolist:show_todolist')
    task.save()
    messages.success(request, 'Status task telah berhasil diubah!')
    return redirect('todolist:show_todolist')
```
Perhatikan bahwa untuk kita akan memberikan pesan apakah kita berhasil mengubah. 

### Deploy
Setelah itu seperti biasa kita melakukan deploy ke Herokuapp. Jangan lupa lakukan git add,commit,pull, dan push ke repo Anda.


