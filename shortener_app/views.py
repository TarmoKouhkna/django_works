from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponseNotFound
from .models import AliasedUrl
from .forms import AliasedUrlForm
from .utils import generate_random_alias

class AliasCreateView(CreateView):
    form_class = AliasedUrlForm
    template_name = 'create_alias.html'

    def form_valid(self, form):
        alias = generate_random_alias()
        while AliasedUrl.objects.filter(alias=alias).exists():
            alias = generate_random_alias()
        form.instance.alias = alias
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        urls = AliasedUrl.objects.all()

        for url in urls:
            url.full_url = self.request.build_absolute_uri(f'/{url.alias}/')

        context['urls'] = urls
        return context

def redirect_view(request, alias):
    try:
        aliased_url = AliasedUrl.objects.get(alias=alias)
        return redirect(aliased_url.url)
    except AliasedUrl.DoesNotExist:
        return HttpResponseNotFound("There is no such alias")

def clear_aliases(request):
    if request.method == "POST":
        AliasedUrl.objects.all().delete()
        return redirect('create')  # Redirect back to the main page after clearing
