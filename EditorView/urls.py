from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categorias', views.categorias, name='categorias'),
    path('reportes', views.reportes, name='reportes'),
    path('login', views.login, name='login'),
    path('editar_patron/<patron>', views.editar_patron, name='editar_patron'),
    path('eliminar_patron/<patron>', views.eliminar_patron, name='eliminar_patron'),
    path('chatbot', views.chatbot, name='chatbot')
]
