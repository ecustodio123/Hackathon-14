from django.urls import path
from .views import LocalView, GeneroView, PostSearchView, Compra

urlpatterns = [
    path('<str:local>', LocalView.as_view(), name='local_detail'),
    # path('<str:local__local>/<str:name>', GeneroView.as_view(), name='genero_detail')
    # path('search/', PostSearchView.as_view(), name='post_search'),
    # path(r'^(?P<title>\w+)/$' , Compra.as_view(), name='compra')
    path('<str:cartelera__local>/<slug:slug>', Compra.as_view(), name='compra')
]