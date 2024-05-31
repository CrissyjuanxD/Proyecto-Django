from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from core.models import Product , Category, Supplier, Brand
from core.forms import ProductForm , CategoryForm , SupplierForm, BrandForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout, authenticate
from django.db import IntegrityError

def home(request):
   data = {
        "title1":"Bienvenidos a la App de Ventas",
        "title2":"Super Mercado Economico"
   }
   return render(request,'core/home.html',data)

def signup(request):
    if request.method == "GET":
        return render(request, "signup.html",{
            'form' : UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request,user)
                return redirect("home")
            except IntegrityError: 
                return render(request, "signup.html",{
                    'form':UserCreationForm,
                    'error':'El usuario ya existe'
                    })
        return render(request, "signup.html",{
            'form':UserCreationForm,
            'error':'Las contraseñas no coinciden'
        }) 
def singuot(request):
    logout(request)
    return redirect("home")
def singin(request):
    if request.method == "GET":
        return render(request, "singin.html",{
            'form' : AuthenticationForm()
        })
    else:
        user = authenticate(request,username=request.POST["username"],password=request.POST["password"])
    if user is None:
        return render(request, "singin.html",{
            'form':AuthenticationForm,
            'error':'El usuario o la contraseña no son correctos'
        })
    else:
        login(request,user)
        return redirect("home")

def listas(request):
    data = {
        "title1": "Productos del almaces",
        "title2": "Listas de Productos"
    }
    products=Product.objects.all()
    data["products"]=products
    return render(request,"core/products/listas.html",data)
#Vista de productos :listar,crear,editar,eliminar
def product_List(request):
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos"
    }
    products = Product.objects.all() # SELECT * FROM Product
    data["products"]=products
    return render(request,"core/products/list.html",data)
#Crear un producto
def product_create(request):
    data = {"title1": "Productos","title2": "Ingreso De Productos"}
   
    if request.method == "POST":
        print(request.POST)
        form = ProductForm(request.POST,request.FILES)
        
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect("core:product_list")

    else:
        data["form"] = ProductForm() # controles formulario sin datos

    return render(request, "core/products/form.html", data)
#Editar un producto
def product_update(request,id):
    data = {
        "title1": "Productos",
        "title2": "Editar Producto"
    }
    product=Product.objects.get(pk=id)
    if request.method== 'POST':
        form=ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect("core:product_list")
    else:
        form=ProductForm(instance=product)
        data["form"]=form

    return render(request,"core/products/form.html",data)
#Eliminar un producto
def product_delete(request,id):
    data = {
        "title1": "Productos",
        "title2": "Eliminar Producto"
    }
    product=Product.objects.get(pk=id)
    if request.method== 'POST':
        product.delete()
        return redirect("core:product_list")
    return render(request,"core/products/delete.html",data)
#Vista de marcas :listar,crear,editar,eliminar
def brand_List(request):
    data = {
        "title1": "Marcas",
        "title2": "Consulta De Marcas De Productos"
    }
    brands = Brand.objects.all() # SELECT * FROM Brand
    data["brands"]=brands
    return render(request,"core/brands/list.html",data)
def brand_create(request):
    data = {"title1": "Marcas","title2": "Ingreso De Marcas De Productos"}
   
    if request.method == "POST":
        print(request.POST)
        form = BrandForm(request.POST)
        
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect("core:brand_list")

    else:
        data["form"] = BrandForm() # controles formulario sin datos

    return render(request, "core/brands/form.html", data)
def brand_update(request,id):
    data = {
        "title1": "Marcas",
        "title2": "Editar Marca"
    }
    brand=Brand.objects.get(pk=id)
    if request.method== 'POST':
        form=BrandForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect("core:brand_list")
    else:
        form=BrandForm(instance=brand)
        data["form"]=form

    return render(request,"core/brands/form.html",data)
def brand_delete(request,id):
    data = {
        "title1": "Marcas",
        "title2": "Eliminar Marca"
    }
    brand=Brand.objects.get(pk=id)
    if request.method== 'POST':
        brand.delete()
        return redirect("core:brand_list")
    return render(request,"core/brands/delete.html",data)
#Vista de proveedores :listar,crear,editar,eliminar
def supplier_list(request):
    data = {
        "title1": "Proveedores",
        "title2": "Consulta De Proveedores",
    }
    suppliers = Supplier.objects.all()
    data["suppliers"] = suppliers
    return render(request, 'core/suppliers/list.html', data)
#Crear un Proovedor
def supplier_create(request):
    data = {"title1": "Proveedores", "title2": "Ingreso De Proveedores"}
   
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user
            supplier.save()
            return redirect('core:supplier_list')
    else:
        form = SupplierForm()
    data["form"] = form
    return render(request, 'core/suppliers/form.html', data)
#Modificar un Proovedor
def supplier_update(request, id):
    data = {"title1": "Proveedores", "title2": "Editar Proveedor"}
    supplier = Supplier.objects.get(pk=id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('core:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    data["form"] = form
    return render(request, 'core/suppliers/form.html', data)
#Eliminar un Proovedor
def supplier_delete(request, id):
    data = {
        "title1": "Proovedores",
        "title2": "Eliminar Proovedor"
    }
    supplier = Supplier.objects.get(pk=id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('core:supplier_list')
    return render(request, 'core/suppliers/delete.html', data)
#
def category_List(request):
    data = {
        "title1": "Categorias",
        "title2": "Consulta De Categorias"
    }
    categories = Category.objects.all() # SELECT * FROM Category
    data["categories"]=categories
    return render(request,"core/category/list.html",data)
def category_create(request):
    data = {"title1": "Categorias","title2": "Ingreso De Categorias"}
   
    if request.method == "POST":
        print(request.POST)
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect("core:category_list")

    else:
        data["form"] = CategoryForm() # controles formulario sin datos

    return render(request, "core/category/form.html", data)

def category_update(request,id):
    data = {
        "title1": "Categorias",
        "title2": "Editar Categoria"
    }
    category=Category.objects.get(pk=id)
    if request.method== 'POST':
        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form=CategoryForm(instance=category)
        data["form"]=form

    return render(request,"core/category/form.html",data)

def category_delete(request,id):
    data = {
        "title1": "Categorias",
        "title2": "Eliminar Categoria"
    }
    category=Category.objects.get(pk=id)
    if request.method== 'POST':
        category.delete()
        return redirect("core:category_list")
    return render(request,"core/category/delete.html",data)

