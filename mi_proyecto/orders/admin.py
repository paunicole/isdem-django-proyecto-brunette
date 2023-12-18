from django.contrib import admin
from .models import Size, Category, Topping, Price_List, Item_List, Cart_List, Extra, Order, Caja, Proveedor, Factura


# Register your models here.


class CartInLine(admin.StackedInline):
	model = Cart_List.toppings.through
	# model = Cart_List.extra.through
	extra = 1

class ToppingAdmin(admin.ModelAdmin):
	inlines = [CartInLine]


class CartAdmin(admin.ModelAdmin):
	filter_horizontal = ("toppings",)
	# filter_horizontal = ("extra",)

class CajaAdmin(admin.ModelAdmin):
	list_display = ("numero", "empleado", "turno", "abierta", "fecha_hora_apertura", "fecha_hora_cierre", "monto_inicial", "monto_final")

class ProveedorAdmin(admin.ModelAdmin):
	list_display = ("nombre", "tipo_proveedor", "telefono", "correo", "direccion")

class FacturaAdmin(admin.ModelAdmin):
	list_display = ("proveedor", "tipo_servicio", "estado_factura", "monto", "fecha_vencimiento")

admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Price_List)
admin.site.register(Item_List)
admin.site.register(Cart_List, CartAdmin)
admin.site.register(Extra)
admin.site.register(Order)
admin.site.register(Caja, CajaAdmin)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Factura, FacturaAdmin)



# class MenuPriceResource(resources.ModelResource):

#     class Meta:
#         model = MenuPrice