from django.urls import path, include

urlpatterns = [
    path('DBView/', include('DBView.urls'))
]
