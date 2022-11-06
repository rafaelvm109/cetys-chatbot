from django.urls import path, include

urlpatterns = [
    path('', include('DBView.urls')),
    path('ChatView/', include('ChatView.urls'))
]
