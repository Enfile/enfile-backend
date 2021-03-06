from django.contrib import admin

from .models import Technology, TechnologyLevel, Product, Experience


@admin.register(Technology)
class Technology(admin.ModelAdmin):
    pass


@admin.register(TechnologyLevel)
class TechnologyLevel(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass


@admin.register(Experience)
class Experience(admin.ModelAdmin):
    pass
