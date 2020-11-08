from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Genero, Pelicula, Local, Cartelera, Compra
from django.db.models import Q

from django.http import HttpResponseRedirect

# Create your views here.
class Home(TemplateView):
    template_name = 'cine/index.html'

    def get_context_data(self, **kwargs):
        # generos = Genero.objects.filter(status=1)
        # peliculas = Pelicula.objects.filter(status=1)
        locales = Local.objects.filter(status=1)
        context = super(Home, self).get_context_data(**kwargs)
        # context['peliculas'] = peliculas
        # context['generos'] = generos
        context['locales'] = locales
        return context

class LocalView(TemplateView):
    template_name = 'cine/local.html'

    def get_context_data(self, **kwargs):
        carteleras = Cartelera.objects.filter(status=1, local__local=kwargs['local'])
        generos = Genero.objects.filter(status=1)
        peliculas = Pelicula.objects.filter(status=1)
        locales = Local.objects.filter(status=1)
        context = super(LocalView, self).get_context_data(**kwargs)
        context['peliculas'] = peliculas
        context['generos'] = generos
        context['locales'] = locales
        context['carteleras'] = carteleras
        return context

class GeneroView(TemplateView):
    template_name = 'cine/genero.html'

    def get_context_data(self, **kwargs):
        carteleras = Cartelera.objects.filter(status=1, genero__name=kwargs['name'])
        print(peliculas)
        generos = Genero.objects.filter(status=1)
        locales = Local.objects.filter(status=1)
        carteleras = Cartelera.objects.filter(status=1)
        context = super(GeneroView, self).get_context_data(**kwargs)
        context['peliculas'] = peliculas
        context['generos'] = generos
        context['locales'] = locales
        context['carteleras'] = carteleras
        print(context)
        return context

class PostSearchView(TemplateView):
    template_name = 'cine/search.html'

    def post(self, request):
        post_name = request.POST['post_name']
        carteleras = Cartelera.objects.filter(Q(num_asientos__contains=post_name), status=1)
        peliculas = Pelicula.objects.filter(status=1)
        generos = Genero.objects.filter(status=1)
        locales = Local.objects.filter(status=1)
        context = self.get_context_data()
        context['peliculas'] = peliculas
        context['generos'] = generos
        context['locales'] = locales
        context['carteleras'] = carteleras
        print(carteleras)
        return self.render_to_response(context=context)

class Compra(DetailView):
    model = Cartelera
    template_name = 'cine/compra.html'

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get('slug')
        compras = Compra.objects.filter(status=1, cartelera__slug=slug)
        context = super(Compra, self).get_context_data(**kwargs)
        context['compras'] = compras
        return context

    # def post(self, request, **kwargs):
    #     post_comment = request.POST['compra']
    #     cartelera_id = request.POST['id']
    #     Compra.objects.create(user_id=request.user.id, cartelera_id=cartelera_id, content=cartlera_pelicula)
    #     self.get_object()
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

