from django.contrib import admin
from .models import (
    SiteSettings,
    Service,
    Project,
    Article,
    Founder,    
)


admin.site.register(SiteSettings)
admin.site.register(Service)
admin.site.register(Project)
admin.site.register(Article)
admin.site.register(Founder)