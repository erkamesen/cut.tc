from django.shortcuts import render, redirect
from .models import URLs, Redirects
# Create your views here.


def index(request):
    args = request.GET
    if all((args.get("url"), args.get("slug"))):
        url = args.get("url")
        slug = args.get("slug")
        print(url + slug)

        # URLs modeline ekleme
        base_url, created = URLs.objects.get_or_create(base_url=url)

        # Redirects modeline ekleme
        redirect_entry = Redirects.objects.create(base_url=base_url, redirect_url=slug)

        return redirect(url + slug)

    return render(request, "index.html")





