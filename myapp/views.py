from django.shortcuts import render,redirect
import mysql.connector
from .forms import *
from .models import *
import datetime


def index(request):
    # Attempt to establish the connection to the MySQL database
    try:
        mydb = mysql.connector.connect(
            host="sql6.freesqldatabase.com",  # Your MySQL server hostname or IP address
            user="sql6689898",  # Your database username
            password="riBDPQtQPi",  # Your database password
            database="sql6689898"  # Your database name
        )
        connection_status = "✅Connected to MySQL database successfully"
    except mysql.connector.Error as err:
        connection_status = f"Failed to connect to MySQL database: {err}"

    # Perform addition operation
    a = 5
    b = 5
    output = a + b
    # Template Variables
    template_variables = {
        'title': 'Hello World',
        'blog': {
            'post': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        },
        'order': {
            'date': datetime.date(2024, 4, 5)
        },
        'list_items': ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5'],
        'total': None
    }


    # Define the data dictionary with role, name, and numbers
    data = {
        "name": "Sivasaran",
        "role": "admin",
        "numbers": [1, 2, 3, 4, 5]
    }

    #template variables

    # Pass connection status, addition output, and data to the template
    return render(request, 'myapp/index.html', {'connection_status': connection_status, 'output': output, 'data': data, 'template_variables': template_variables})
from django.shortcuts import render

def bootstrap_page_cdn_link(request):
    return render(request, 'myapp/bootstrap_page_cdn_link.html')

def BS_Installed(request):

    try:
        mydb = mysql.connector.connect(
            host="server22.secureclouddns.net",
            user="aourzcom_delete",
            password="aourzcom_delete",
            database="aourzcom_sample" #aourzcom_delete
        )
        connection_status = "✅Connected to MySQL database successfully"
    except mysql.connector.Error as err:
        connection_status = f"Failed to connect to MySQL database: {err}"
        
    data = {
        "name": "Kamalk Hasan",
        "role": "Assistent Manager",
        "numbers": [1, 2, 3, 4, 5]
    }
    return render(request, 'myapp/bootstrap_page_installated.html', {'connection_status': connection_status, 'data': data})

def about(request):
    return render(request,'web/about.html')
def home(request):
    return render(request,'web/home.html')
def contact(request):
    return render(request,'web/contact.html')
def services(request):
    return render(request,'web/services.html')
def include_directive_index(request):
    # You can add any necessary logic here
    return render(request, 'web/include_directive_index.html')
# video 11

def ProductsAdd(request):
    context = {
        'product_form': ProductForm()
        }
    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()
    return render(request, 'web/products_add.html', context)    

"""def AllProducts(request):
    all_products = Product.objects.all()
    return render(request, 'web/products.html', {'all_products': all_products})
    """
from django.shortcuts import render, redirect, get_object_or_404


def all_products(request):
    all_products = Product.objects.all()
    return render(request, 'web/products.html', {'all_products': all_products})

def ProductUpdate(request, id):
    selected_product = Product.objects.get(id=id)
    context = {
        "product_form": ProductForm(instance=selected_product)
    }
    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('all_products')  # Redirect to the product list page
    return render(request, 'web/products_update.html', context)


def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('all_products')
    return render(request, 'web/confirm_delete_product.html', {'product': product})
