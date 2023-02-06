from django.shortcuts import render
from django.http import HttpResponse
from Products.models import Product
from Products.forms import ProductForm
from Categories.models import Category
from django.views.generic import CreateView, DeleteView, UpdateView

def inicio(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products':products,
        'categories' : categories,
    }
    return render(request, "Products/inicio.html", context=context)

def add_product(request):
        if request.method == 'GET':
            context = {
                'form': ProductForm()
            }

            return render(request, 'Products/add_product.html', context=context)

        elif request.method == 'POST':

            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                Product.objects.create(
                    name=form.cleaned_data['name'],
                    model=form.cleaned_data['model'],
                    style=form.cleaned_data['style'],
                    price=form.cleaned_data['price'],
                    stock=form.cleaned_data['stock'],
                    image=form.cleaned_data['image'],
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, "Products/add_product.html", context=context)

        else: 
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'Products/add_product.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        
        products = Product.objects.filter(name__icontains=search,)
        
    else:
        products = Product.objects.all()
        
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories' : categories,
    }
    return render(request, 'Products/list_products.html', context=context)

def list_offroad(request):
    if 'search' in request.GET:
        search = request.GET['search']
        
        products = Product.objects.filter(name__icontains=search, style__icontains='offroad')
        
    else:
        products = Product.objects.all()
        
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories' : categories,
    }
    return render(request, 'Products/list_perStyle.html', context=context)

def list_scooter(request):
    if 'search' in request.GET:
        search = request.GET['search']
        
        products = Product.objects.filter(name__icontains=search, style__icontains='scooter')
        
    else:
        products = Product.objects.all()
        
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories' : categories,
    }
    return render(request, 'Products/list_perStyle.html', context=context)

def list_street(request):
    if 'search' in request.GET:
        search = request.GET['search']
        
        products = Product.objects.filter(name__icontains=search, style__icontains='street')
        
    else:
        products = Product.objects.all()
        
    categories = Category.objects.all()
    context = {
        'products':products,
        'categories' : categories,
    }
    return render(request, 'Products/list_perStyle.html', context=context)

def searchform(request):

    if  request.GET['name']:

        
            name = request.GET['name'] 
        

            return render(request, "Products/search-results.html", {"name":name})

    else: 
            respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

class ProductCreateView(CreateView):
    model = Product
    template_name = 'Products/add_product.html'
    fields = '__all__'
    success_url = '/Products/'