from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_category/<category_id>', views.get_category, name='get_category'),
    path('edit_pattern/<tag_id>', views.edit_pattern, name='edit_pattern'),
    path('push_edit/<tag_id>', views.push_edit, name='push_edit'),
    path('add_pattern/<category_id>', views.add_pattern, name='add_pattern'),
    path('add_category/', views.add_category, name='add_category'),
    path('commit_category/', views.commit_category, name='commit_category'),
    path('remove_category/', views.remove_category, name='remove_category'),
    path('commit_remove_category/', views.commit_remove_category, name='commit_remove_category'),
    path('go_home/', views.go_home, name='go_home'),
    path('remove_pattern/<category_id>/<tag_id>', views.remove_pattern, name='remove_pattern'),
]
