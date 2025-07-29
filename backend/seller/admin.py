from django.contrib import admin
from .models import SellerModel, CategoryModel, SubCategoryModel


class SubCategoryInline(admin.TabularInline):
    model = SubCategoryModel
    extra = 1
    fields = ['seller', 'name', 'image', 'category']
    autocomplete_fields = ['category']


class CategoryInline(admin.TabularInline):
    model = CategoryModel
    extra = 1
    fields = ['name', 'image']
    show_change_link = True


@admin.register(SellerModel)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'store_name', 'gstin_number', 'phone']
    inlines = [CategoryInline]
    search_fields = ['store_name', 'user__email', 'gstin_number']
    ordering = ['id']
    list_filter = ['created_at']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'image', 'seller']
    list_display = ['id', 'name', 'seller']
    inlines = [SubCategoryInline]
    search_fields = ['name']
    list_filter = ['seller']


@admin.register(SubCategoryModel)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'seller']
    search_fields = ['name']
    list_filter = ['category', 'seller']