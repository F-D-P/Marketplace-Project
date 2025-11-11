from .models import Opinion
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import Producto
from django.contrib.auth.decorators import login_required
from .models import Compra

def index(request):
    opiniones = Opinion.objects.all().order_by('-fecha')  # últimas primero
    return render(request, "index.html", {"opiniones": opiniones})

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("productos")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


def productos(request):
    lista = Producto.objects.all()
    return render(request, "productos.html", {"productos": lista})

@login_required
def crear_producto(request):
    if not request.user.perfil.es_vendedor:
        return redirect("productos")

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        precio = request.POST.get("precio")
        imagen = request.FILES.get("imagen")

        if nombre and descripcion and precio and imagen:
            Producto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                precio=precio,
                imagen=imagen,
                vendedor=request.user
            )
            return redirect("productos")

    return render(request, "crear_producto.html")

def enviar_opinion(request):
    if request.method == "POST":
        mensaje = request.POST.get("mensaje")
        if mensaje and request.user.is_authenticated:
            Opinion.objects.create(nombre=request.user.username, mensaje=mensaje)
    return redirect("inicio")

@login_required
def carrito(request):
    mostrar_pago = request.GET.get("comprar") == "1"
    return render(request, "carrito.html", {"mostrar_pago": mostrar_pago})


def confirmar_pago(request, metodo):
    if not request.user.is_authenticated:
        return redirect("login")

    # Simulación: guardar una compra ficticia
    Compra.objects.create(
        usuario=request.user,
        metodo_pago=metodo,
        total=calcular_total_carrito(request),  # función que suma los ítems
        estado="simulado"
    )

    return redirect(f"/?confirmacion=1&metodo={metodo}")

def calcular_total_carrito(request):
    # Simulación: suma ficticia de ítems del carrito
    # En producción, deberías sumar los precios reales desde sesión o base de datos
    return 1000.00  # valor simulado en ARS



def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # o redirigí a donde quieras
    else:
        form = UserCreationForm()
    return render(request, "registro.html", {"form": form})
