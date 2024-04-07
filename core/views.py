from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UrlForm
from .models import Url
from .documents import UrlDocument
import time
from django.core.cache import cache


# from django.views.decorators.cache import cache_page


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            form.save()
    form = UrlForm()
    context = {
        'form': form
    }
    return render(request, 'core/index.html', context)


def redirect_url(request, short_url):
    current = time.time()
    url = Url.objects.get(short_url=short_url)
    t = (time.time() - current)
    return JsonResponse({'original_url': url.original_url, 'time': t})


# @cache_page(60 * 1)
def redirect_url_elastic(request, short_url):
    current = time.time()
    url = UrlDocument.search().filter('term', short_url=short_url).execute()[0]
    t = (time.time() - current)
    return JsonResponse({'original_url': url.original_url, 'time': t})
    # return redirect(url.original_url)


def redirect_url_cache(request, short_url):
    current = time.time()
    url = cache.get(short_url)
    if not url:
        url = Url.objects.get(short_url=short_url)
        cache.set(short_url, url)
    t = (time.time() - current)
    # return JsonResponse({'original_url': url.original_url, 'time': t})
    return redirect(url.original_url)
