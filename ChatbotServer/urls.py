from django.urls import path, include

urlpatterns = [
    path('DBView/', include('DBView.urls')),
    path('ChatView/', include('ChatView.urls'))
]
