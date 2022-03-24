from django.shortcuts import render
from .models import *


def home(request):
    name = Main.objects.all()
    banner = Banner.objects.all()
    new = News.objects.all
    swipers = Swipers.objects.all()
    icons = Icons.objects.all()
    details = Details.objects.all()
    pictures = Pictures.objects.all()
    link = Link.objects.all()
    splitted = Splitted.objects.all()
    footer = Footer.objects.all()
    context = {"name": name, "banner": banner, "new": new,
               "swipers": swipers, "icons": icons, "details": details,
               "pictures": pictures, "link": link, "splitted": splitted, "footer": footer}

    return render(request, 'index.html', context)


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'base.html', context)


def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product-inner.html', context)


def service(request):
    name = Service.objects.all()
    context = {'name': name}
    return render(request, 'service.html', context)


def company(request):
    about = Company.objects.all()
    context = {'about': about}
    return render(request, 'about.html', context)


def news(request, pk):
    news = News.objects.get(pk=pk)
    context = {'news': news}
    return render(request, 'base.html')


# def news_page(request):
#     read_more = Truncator(New.description)
#     news_list = New.object.filter
#     page = request.GET.get('page', 1)
#     paginator = Paginator(news_list, 4)
#
#     try:
#         news = paginator.page(page)
#     except PageNotAnInteger:
#         news = paginator.page(1)
#     except EmptyPage:
#         news = paginator.page(paginator.num_pages)
#
#     context = {'news': news, 'read_more': read_more}
#
#     return render(request, 'pages/')


def icons(request):
    detail = Icons.objects.all()
    context = {'detail': detail}
    return render(request, 'contacts.html', context)


def detail(request):
    title = Details.objects.all()
    context = {'title': title}
    return render(request, 'contacts.html', context)


def pictures(request):
    title = Pictures.objects.all()
    context = {'title': title}
    return render(request, 'index.html', context)


def link(request):
    title = Link.objects.all()
    context = {'title': title}
    return render(request, 'index.html', context)


def splitted(request):
    title = Splitted.objects.all()
    context = {'title': title}
    return render(request, 'index.html', context)


def footer(request):
    title = Footer.objects.all()
    context = {'title': title}
    return render(request, 'base.html', context)