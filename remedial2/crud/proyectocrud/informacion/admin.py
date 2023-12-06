from django.contrib import admin
from . models import Teams, Player, Stadium

# Register your models here.

admin.site.register(Teams)
admin.site.register(Player)
admin.site.register(Stadium)