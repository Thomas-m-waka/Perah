from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='about'),
    path('services/', views.services, name='services'),
    path('work/', views.work, name='work'),
    path('insights/',views.insights,name='insights'),
    path('insight/<int:article_id>/',views.insight_detail,name=''),
    path('contact/',views.contact,name='contact'),
]