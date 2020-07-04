from django.contrib import admin
from product_index.models import App, Groups, Category, Disease, Product


class AppAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'image')
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


class GroupsAdmin(admin.ModelAdmin):
    fields = ('app', 'type', 'name', 'image', 'description')
    list_display = ('id', 'app', 'type', 'name', 'description')
    list_filter = ('app', 'name')
    search_fields = ('id', 'name', 'app', 'type')


class CategoryAdmin(admin.ModelAdmin):
    fields = ('app', 'groups', 'type', 'name', 'description')
    list_display = ('id', 'app', 'groups', 'type', 'name', 'description')
    list_filter = ('name', 'app', 'groups')
    search_fields = ('id', 'name', 'app', 'groups')
    list_per_page = 15


class DiseaseAdmin(admin.ModelAdmin):
    fields = ('app', 'category', 'name', 'sub_title', 'description')
    list_display = ('id', 'app', 'groups', 'category', 'name', 'sub_title')
    list_filter = ('name', 'app', 'groups')
    search_fields = ('id', 'name', 'app', 'groups', 'sub_title')
    list_per_page = 15


class ProductAdmin(admin.ModelAdmin):
    fields = ('app', 'category', 'name', 'sub_title', 'description')
    list_display = ('id', 'app', 'groups', 'category', 'name', 'sub_title')
    list_filter = ('name', 'app', 'groups')
    search_fields = ('id', 'name', 'app', 'groups', 'sub_title')
    list_per_page = 15


admin.site.register(App, AppAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Product, ProductAdmin)
