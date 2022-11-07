from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_category/<category_id>', views.get_category, name='get_category'),
    path('edit_pattern/<tag_id>', views.edit_pattern, name='edit_pattern'),
    path('push_edit/<tag_id>', views.push_edit, name='push_edit'),
]