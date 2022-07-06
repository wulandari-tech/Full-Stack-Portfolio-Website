from django.contrib import admin

# Register your models here.
from .models import About, Home, Project,Skill,tag

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(tag)

admin.site.register(About)
admin.site.register(Home)

