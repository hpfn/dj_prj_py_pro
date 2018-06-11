from django.urls import path
from certgen.core import views

app_name = 'core'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
]
