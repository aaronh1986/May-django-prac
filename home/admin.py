from django.contrib import admin
from .models import Band

# Register your models here.
class BandAdmin(admin.ModelAdmin):
    list_display = (
        'number',
        'band_name',
    )

admin.site.register(Band, BandAdmin)
