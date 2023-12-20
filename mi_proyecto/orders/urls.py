from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup"),
    
    path("reset_password/", auth_views.PasswordResetView.as_view(template_name="orders/reset_password.html"), name="reset_password"), #template_name="orders/reset_password.html"
    path("reset_password_sent/", auth_views.PasswordResetDoneView.as_view(template_name="orders/reset_password_sent.html"), name="password_reset_done"), #template_name="orders/reset_password_send.html"
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="orders/reset.html"), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name="orders/reset_password_complete.html"), name="password_reset_complete"),
    
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
