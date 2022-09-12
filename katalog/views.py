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
