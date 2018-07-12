from urllib.parse import quote
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Shop, Item, Review

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon_img','name','is_public'] 
    list_display_links = ['name']
    list_filter = ['is_public']
    search_fields = ['name']
    def icon_img(self, category):
        if category.icon:
            img_tag = '<img src="{}" style="max-width: 72px;" />'
            return mark_safe(img_tag.format(category.icon.url))
        return None

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['category','name', 'address_link']
    list_display_links = ['name',]
    list_filter = ['category']
    def address_link(self, shop):
        if shop.address:
            url='http://maps.naver.com/?query=' + quote(shop.address)
            return mark_safe('<a href="{}" target="_blank">{}</a>'.format(url, shop.address))
        return None
    
    address_link.short_description = '주소 (네이버 지도)'

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['shop','name']
    list_display_links = ['name']
    list_filter = ['shop']
    search_fields = ['name']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass