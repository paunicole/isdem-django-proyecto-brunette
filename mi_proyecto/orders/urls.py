from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    path("apertura-caja", views.apertura_caja, name="apertura-caja"),
    path("cierre-caja", views.cierre_caja, name="cierre-caja"),
    path("ver-proveedores", views.ver_proveedores, name="ver-proveedores"),
    path("crear-proveedor", views.crear_proveedor, name="crear-proveedor"),
    path("eliminar-proveedor/<int:id_proveedor>/", views.eliminar_proveedor, name="eliminar-proveedor"),
    path("editar-proveedor/<int:id_proveedor>/", views.editar_proveedor, name="editar-proveedor"),    
    path("pago-impuestos", views.pago_impuestos, name="pago-impuestos"),
    path("crear-factura", views.crear_factura, name="crear-factura"),
    path("eliminar-factura/<int:id_factura>/", views.eliminar_factura, name="eliminar-factura"),
    path("editar-factura/<int:id_factura>/", views.editar_factura, name="editar-factura"),
    path("ventas", views.ventas, name="ventas"),
    path("cart", views.cart_view, name="cart"),
    path("order", views.order_view, name="order"),
    path("topping/<int:cart_id>/", views.topping_view, name="topping"),
    path("removefromcart/<int:cart_id>/", views.removefromcart_view, name="removefromcart"),
    ]
