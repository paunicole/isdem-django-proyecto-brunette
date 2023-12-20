from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Sum
from django.contrib import messages


from .models import Size, Category, Topping, Price_List, Item_List, Cart_List, Extra, Order, Caja, Proveedor, Factura

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})
	context = {
		"categories" : Category.objects.exclude(name="Topping").all(),
		"items" : Item_List.objects.all(),
		"toppings" : Topping.objects.all(),
		"extras" : Extra.objects.all(), 
		"sizes" : Size.objects.all(),
		"user" : request.user
	}
	return render(request, "orders/index.html", context)
    # return HttpResponse("Project 3: TODO")

def login_view(request):

    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
    	return render(request, "orders/login.html", {"message": "El usuario o la contraseña son incorrectos"})
	# else:
	# return render(request, "orders/login.html")

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Desconectado"})

def signup_view(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
				return render (request = request,
                  template_name = "orders/signup.html",
                  context={"form":form})
	
	form = UserCreationForm        
	return render(request = request,
                  template_name = "orders/signup.html",
                  context={"form":form})

def apertura_caja(request):
	cajas = Caja.objects.filter(empleado=request.user, abierta=False)
	context = {
		"empleado": request.user,
		"cajas": cajas
	}
	if request.method == "POST":
		numero = request.POST.get("numero")
		empleado = request.user
		turno = request.POST.get("turno")
		abierta = True
		fecha_hora_apertura = request.POST.get("fecha_hora_apertura")
		monto_inicial = request.POST.get("monto_inicial")
		apertura_caja = Caja(numero=numero, empleado=empleado, turno=turno, abierta=abierta, fecha_hora_apertura=fecha_hora_apertura, monto_inicial=monto_inicial)
		apertura_caja.save()
		messages.success(request,"Caja abierta con éxito.")
		return redirect("apertura-caja")
	return render(request, "orders/apertura.html", context)

def cierre_caja(request):
	cajas = Caja.objects.all()
	context = {
		"empleado": request.user,
		"cajas": cajas
	}
	return render(request, "orders/cierre.html", context)

def ver_proveedores(request):
	proveedores = Proveedor.objects.all()
	context = {
		"proveedores": proveedores
	}
	return render(request, "orders/proveedores.html", context)

def eliminar_proveedor(request, id_proveedor):
	proveedor = Proveedor.objects.get(id=id_proveedor)
	proveedor.delete()
	messages.success(request,"Proveedor eliminado con éxito.")
	return redirect("ver-proveedores")

def editar_proveedor(request, id_proveedor):
	proveedor = Proveedor.objects.get(id=id_proveedor)
	if request.method == "POST":
		nombre = request.POST.get("nombre")
		
		servicio = request.POST.get("servicio")
		telefono = request.POST.get("telefono")
		correo = request.POST.get("correo")
		direccion = request.POST.get("direccion")

		# Actualiza los campos del proveedor existente
		proveedor.nombre = nombre
		proveedor.tipo_proveedor = servicio
		proveedor.telefono = telefono
		proveedor.correo = correo
		proveedor.direccion = direccion
		proveedor.save()

		messages.success(request,"Proveedor guardado con éxito.")
		return redirect("ver-proveedores")
	context = {
        "nombre": proveedor.nombre,
        "servicio": proveedor.tipo_proveedor,
        "telefono": proveedor.telefono,
        "correo": proveedor.correo,
        "direccion": proveedor.direccion,
    }
	return render(request, "orders/editar_proveedor.html", context)

def crear_proveedor(request):
	if request.method == "POST":
		nombre = request.POST.get("nombre")
		servicio = request.POST.get("servicio")
		telefono = request.POST.get("telefono")
		correo = request.POST.get("correo")
		direccion = request.POST.get("direccion")
		nuevo_proveedor = Proveedor(nombre=nombre, tipo_proveedor=servicio, telefono=telefono, correo=correo, direccion=direccion)
		nuevo_proveedor.save()
		messages.success(request,"Proveedor añadido con éxito.")
		return redirect("ver-proveedores")
	return render(request, "orders/crear_proveedor.html")

def pago_impuestos(request):
	facturas = Factura.objects.all()
	context = {
		"facturas": facturas
	}
	return render(request, "orders/pago_impuestos.html", context)

def crear_factura(request):
	proveedores = Proveedor.objects.all()
	if request.method == "POST":
		proveedor = Proveedor.objects.get(id = request.POST.get("proveedor"))
		tipo_servicio = request.POST.get("tipo_servicio")
		estado_factura = request.POST.get("estado_factura")
		monto = request.POST.get("monto")
		fecha_vencimiento = request.POST.get("fecha_vencimiento")

		nueva_factura = Factura(proveedor=proveedor, tipo_servicio=tipo_servicio, estado_factura=estado_factura, monto=monto, fecha_vencimiento=fecha_vencimiento)
		nueva_factura.save()
		
		messages.success(request,"Factura añadida con éxito.")
		return redirect("pago-impuestos")
	context = {
		"proveedores": proveedores
	}
	return render(request, "orders/crear_factura.html", context)

def eliminar_factura(request, id_factura):
	factura = Factura.objects.get(id=id_factura)
	factura.delete()
	messages.success(request,"Factura eliminada con éxito.")

	return redirect("pago-impuestos")

def editar_factura(request, id_factura):
	factura = Factura.objects.get(id=id_factura)
	proveedores = Proveedor.objects.all()
	if request.method == "POST":
		proveedor = Proveedor.objects.get(id = request.POST.get("proveedor"))
		tipo_servicio = request.POST.get("tipo_servicio")
		estado_factura = request.POST.get("estado_factura")
		monto = request.POST.get("monto")
		fecha_vencimiento = request.POST.get("fecha_vencimiento")

		# Actualiza los campos del proveedor existente
		factura.proveedor = proveedor
		factura.tipo_servicio = tipo_servicio
		factura.estado_factura = estado_factura
		factura.monto = monto
		factura.fecha_vencimiento = fecha_vencimiento
		factura.save()

		messages.success(request,"Factura guardada con éxito.")
		return redirect("pago-impuestos")
	fecha_vencimiento_formateada = factura.fecha_vencimiento.strftime('%Y-%m-%d')
	context = {
		"proveedores": proveedores,
        "proveedor": factura.proveedor,
        "tipo_servicio": factura.tipo_servicio,
        "estado_factura": factura.estado_factura,
        "monto": factura.monto,
        "fecha_vencimiento": fecha_vencimiento_formateada,
    }

	return render(request, "orders/editar_factura.html", context)

def ventas(request):
	return render(request, "orders/ventas.html")

def cart_view(request):
	
	if request.method == "POST":
		item_id = request.POST.get("item_id")
		toppings = request.POST.getlist("topping_id")
		extras = request.POST.getlist("extra_id")
		size = request.POST.get("size_id")
		user = request.user

		p = Item_List.objects.get(pk=item_id)
		price_id = p.base_price_id.id

		# Calculate Price:

		# Calculate topping quantity
		count_topping = 0
		for topping in toppings: 
			count_topping+=1
		# Calculate extra quantity
		count_extra = 0
		for extra in extras: 
			count_extra+=1


		topping_price = Price_List.objects.get(name="Topping")
		extra_price = Price_List.objects.get(name="Extra")
		item = Price_List.objects.get(pk=price_id)


		# if large option selected
		if size and int(size) == 7:
			total_price = item.base_price + item.large_supp + count_topping*topping_price.large_supp + count_extra*extra_price.base_price
		else:
			total_price = item.base_price + count_topping*topping_price.base_price + count_extra*extra_price.base_price

		# Add new item to cart
		if size == None:
			new_item = Cart_List(user_id=user, item_id=Item_List.objects.get(pk = item_id), size=None, calculated_price=total_price)
		else:
			new_item = Cart_List(user_id=user, item_id=Item_List.objects.get(pk = item_id), size=Size.objects.get(pk = size), calculated_price=total_price)

		# add item to cart
		new_item.save()

		# add toppping and extras to item
		for topping in toppings: 
			new_item.toppings.add(topping)
		for extra in extras: 
			new_item.extra.add(extra)
		# return HttpResponseRedirect(reverse("cart"))
		messages.success(request, "Comida agrega al carrito!")
		return HttpResponseRedirect(reverse("index"))
		# return render(request, "orders/index.html", {"message": "Meal added to cart!"})

	else:
		try:
			cart = Cart_List.objects.filter(user_id=request.user, is_current=True)
		except Cart_List.DoesNotExist:
			raise Http404("Cart does not exist")
		
		total_price = cart.aggregate(Sum('calculated_price'))['calculated_price__sum']

		cart_ordered = Cart_List.objects.filter(user_id=request.user, is_current=False)

		context = {
		"cart_items" : cart,
		"total_price": total_price,
		"cart_items_ordered" : cart_ordered,
		}

		return render(request, "orders/cart.html", context)

def topping_view(request, cart_id):
	# view topping from cart

	try:
		pizza = Cart_List.objects.get(pk=cart_id)
	except Cart.DoesNotExist:
		raise Http404("Pizza not in Cart or does not include topping")
	context = {
		"toppings" : pizza.toppings.all()
		}
	return render(request, "orders/topping.html", context)


def order_view(request):
	# place an order

	if request.method == "POST":
		user = request.user
		items = request.POST.getlist("cart_id")
		print(items)

		new_order = Order(user_id=user)

		new_order.save()

		for item in items:
			new_order.cart_id.add(item)

		# set current attribute to False 
		cart = Cart_List.objects.filter(user_id=request.user)
		for item in cart:
			item.is_current=False
			item.save()
	messages.success(request,"Gracias por comprarnos, su pedido ha sido realizado.")
	return HttpResponseRedirect(reverse("index"))

def removefromcart_view(request, cart_id):
	# view topping from cart

	item_toremove = Cart_List.objects.get(pk=cart_id)
	item_toremove.delete()
	messages.info(request,"This item has been removed from your cart.")
	return HttpResponseRedirect(reverse("cart"))









