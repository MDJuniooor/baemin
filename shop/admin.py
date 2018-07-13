from urllib.parse import quote
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Shop, Item, Review, Order

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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display_links = ['name']
    list_display = ['imp_uid', 'user', 'name', 'amount_html',]
                    # 'status_html', 'paid_at', 'receipt_link']
    actions = ['do_update', 'do_cancel']

    def do_update(self, request, queryset):
        '주문 정보를 갱신합니다.'
        print('update')
        total = queryset.count()
        if total > 0:
            for Order in queryset:
                Order.update()
            self.message_user(request, '주문 {}건의 정보를 갱신했습니다.'.format(total))
        else:
            self.message_user(request, '갱신할 주문이 없습니다.')
    do_update.short_description = '선택된 주문들의 아임포트 정보 갱신하기'

    def do_cancel(self, request, queryset):
        '선택된 주문에 대해 결제취소요청을 합니다.'
        print('cancel')
        queryset = queryset.filter(status='paid')
        total = queryset.count()
        if total > 0:
            for Order in queryset:
                Order.cancel()
            self.message_user(request, '주문 {}건을 취소했습니다.'.format(total))
        else:
                self.message_user(request, '취소할 주문이 없습니다.')
    do_cancel.short_description = '선택된 주문에 대해 결제 취소 요청하기'
