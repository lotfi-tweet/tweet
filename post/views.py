from django.shortcuts import render, get_object_or_404
from .models import Post, Category, About, AdsPublic, Discount
from  django.core.paginator import Paginator


def index(request):
    context = {
        'mobile_list': Post.objects.filter(categorie__in=Category.objects.filter(cat_name='الهواتف النقالة')).distinct().order_by('-id')[:8],
        'offer_list': Post.objects.filter(categorie__in=Category.objects.filter(cat_name='عروض')).distinct().order_by('-id')[:4],
        'computer_list': Post.objects.filter(categorie__in=Category.objects.filter(cat_name='كمبيوتر')).distinct().order_by('-id')[:4],
        'mix_list': Post.objects.filter(categorie__in=Category.objects.filter(cat_name='منوعات')).distinct().order_by('-id')[:5],
        'ads_list': AdsPublic.objects.all(),
        'discount_list': Discount.objects.all().order_by('-id')[:3],
    }
    return render(request, 'post/index.html', context)


def post_detaill(request, id=None, *args,**kwargs):
    element = get_object_or_404(Post, pk=id)
    element.visit_num += 1
    element.save()

    related_post = Post.objects.filter(categorie = element.categorie)

    context = {
        'object': element,
        'latest_post': Post.objects.order_by('-id')[:5],
        'relate_post': related_post.order_by('-id')[:5],
        'puplic_list': Post.objects.order_by('visit_num')[:5],
        'ads_list': AdsPublic.objects.all(),
    }
    return render(request, 'post/topic.html', context)


def mobile_part(request):
    mobile_list = Post.objects.filter(categorie__in=Category.objects.filter(cat_name='الهواتف النقالة')).distinct().order_by('-id')
    paginator = Paginator(mobile_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'mobile_list': posts,
        'latest_post': Post.objects.order_by('-id')[:5],
        'puplic_list': Post.objects.order_by('visit_num')[:5],
        'ads_list': AdsPublic.objects.all(),
        'discount_list': Discount.objects.all().order_by('-id')[:4],
    }
    return render(request, 'post/mobile.html', context)


def offer_part(request):
    offer_list = Post.objects.filter(categorie__in=Category.objects.filter(cat_name='عروض')).distinct().order_by('-id')
    paginator = Paginator(offer_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'offer_list':posts,
        'latest_post': Post.objects.order_by('id')[:5],
        'puplic_list': Post.objects.order_by('visit_num')[:5],
        'ads_list': AdsPublic.objects.all(),
        'discount_list': Discount.objects.all().order_by('-id')[:4],
    }
    return render(request, 'post/offer.html', context)


def technology_part(request):
    computer_list = Post.objects.filter(categorie__in=Category.objects.filter(cat_name='كمبيوتر')).distinct().order_by('-id')
    paginator = Paginator(computer_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'computer_list': posts,
        'latest_post': Post.objects.order_by('-id')[:5],
        'puplic_list': Post.objects.order_by('visit_num')[:5],
        'discount_list': Discount.objects.all().order_by('-id')[:4],
        "ads_list" : AdsPublic.objects.all(),
    }
    return render(request, 'post/computer.html', context)


def mix_part(request):
    mix_list = Post.objects.filter(categorie__in=Category.objects.filter(cat_name='منوعات')).distinct().order_by('-id')
    paginator = Paginator(mix_list,10)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'mix_list': posts,
        'latest_post': Post.objects.order_by('-id')[:5],
        'puplic_list': Post.objects.order_by('visit_num')[:5],
        'discount_list': Discount.objects.all().order_by('-id')[:4],
        "ads_list" : AdsPublic.objects.all(),
    }
    return render(request, 'post/mix_news.html', context)


def about_as(request):
    context = About.objects.all()
    return render(request, 'post/portfolio.html', {'context': context})


def ads_puplic(request):
    context = {
        "ads_list" : AdsPublic.objects.all()
    }

    return render(request, 'post/base.html', context)


def discount_mob(request):
    discount_list = Discount.objects.order_by('-id')
    paginator = Paginator(discount_list, 9)
    page = request.GET.get('page')
    discount = paginator.get_page(page)
    context = {
        'disc_list' : discount,
        'latest_post': Post.objects.order_by('-id')[:4],
        'puplic_list': Post.objects.order_by('visit_num')[:4],
    }

    return render(request, 'post/discount.html', context)
