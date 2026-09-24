from django.shortcuts import render

from .models import (
    SiteSettings,
    Service,
    Project,
    Article,
    Founder,
)


def home(request):
    settings = SiteSettings.objects.first()

    services = Service.objects.filter(
        is_active=True
    )

    projects = Project.objects.all().order_by(
        '-created_at'
    )

    articles = Article.objects.filter(
        published=True
    ).order_by(
        '-created_at'
    )

    founders = Founder.objects.all()

    context = {
        'settings': settings,
        'services': services,
        'projects': projects,
        'articles': articles,
        'founders': founders,
    }

    return render(
        request,
        'home.html',
        context
    )

def about(request):
    founder = Founder.objects.first()

    context = {
        'founder': founder,
    }

    return render(
        request,
        'about.html',
        context
    )

def services(request):
    services = Service.objects.filter(
        is_active=True
    )

    context = {
        'services': services,
    }

    return render(
        request,
        'services.html',
        context
    )    

def work(request):
    projects = Project.objects.all().order_by('-created_at')

    context = {
        'projects': projects,
    }

    return render(
        request,
        'work.html',
        context
    )


def insights(request):
    articles = Article.objects.filter(
        published=True
    ).order_by('-created_at')

    context = {
        'articles': articles,
    }

    return render(
        request,
        'insights.html',
        context
    )


def insight_detail(request, article_id):
    article = Article.objects.get(
        id=article_id,
        published=True
    )

    context = {
        'article': article,
    }

    return render(request,'detail.html',context)

def contact(request):
    settings = SiteSettings.objects.first()

    context = {
        'settings': settings,
    }

    return render(request,'contact.html',context)