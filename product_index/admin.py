import base64

from django import forms
from django.contrib import admin
from product_index.models import App, Groups, Category, Disease, Product


def image_upload(instance, image_file):
    if image_file:
        image_str64 = base64.b64encode(image_file.read())
        instance.image = image_str64.decode('utf-8')
        instance.save()

    return instance


class AppAdminForm(forms.ModelForm):
    logo = forms.FileField(required=False)

    class Meta:
        model = App
        fields = ('name', 'description', 'logo')

    def save(self, commit=True):
        image_file = self.cleaned_data.get('logo', None)
        instance = super(AppAdminForm, self).save(commit=commit)

        return image_upload(instance, image_file)


class GroupsAdminForm(forms.ModelForm):
    logo = forms.FileField(required=False)

    class Meta:
        model = Groups
        fields = ('app', 'type', 'name', 'description', 'logo')

    def save(self, commit=True):
        image_file = self.cleaned_data.get('logo', None)
        instance = super(GroupsAdminForm, self).save(commit=commit)

        return image_upload(instance, image_file)


def category_form_factory(groups):
    class CategoryForm(forms.ModelForm):
        m_file = forms.ModelChoiceField(
            queryset=App.objects.filter(type=groups)
        )
    return CategoryForm


class AppAdmin(admin.ModelAdmin):
    form = AppAdminForm
    list_display = ('id', 'name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


class GroupsAdmin(admin.ModelAdmin):
    form = GroupsAdminForm
    list_display = ('id', 'app', 'type', 'name', 'description')
    list_filter = ('app', 'name')
    search_fields = ('id', 'name', 'app', 'type')


class CategoryAdmin(admin.ModelAdmin):
    fields = ('app', 'groups', 'type', 'name', 'description')
    list_display = ('id', 'app', 'groups', 'type', 'name', 'description')
    list_filter = ('name', 'app', 'groups')
    search_fields = ('id', 'name', 'app', 'groups')
    list_per_page = 15

    def get_form(self, request, obj=None, **kwargs):
        if obj is not None and obj.groups is not None:
            kwargs['form'] = category_form_factory(obj.groups)
        return super(CategoryAdmin, self).get_form(request, obj, **kwargs)


class DiseaseAdmin(admin.ModelAdmin):
    fields = ('app', 'category', 'name', 'sub_title', 'description')
    list_display = ('id', 'app', 'groups', 'category', 'name', 'sub_title')
    list_filter = ('name', 'app')
    search_fields = ('id', 'name', 'app', 'groups', 'sub_title')
    list_per_page = 15


class ProductAdmin(admin.ModelAdmin):
    fields = ('app', 'category', 'name', 'sub_title', 'description')
    list_display = ('id', 'app', 'groups', 'category', 'name', 'sub_title')
    list_filter = ('name', 'app')
    search_fields = ('id', 'name', 'app', 'groups', 'sub_title')
    list_per_page = 15


admin.site.register(App, AppAdmin)
admin.site.register(Groups, GroupsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Product, ProductAdmin)
