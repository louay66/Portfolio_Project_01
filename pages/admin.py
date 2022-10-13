from django.contrib import admin
from .models import Category, Prodact, Guest, Booking


class GuestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'delivery', 'receipt']
    list_filter = ['delivery']


class BookingAdmin(admin.ModelAdmin):
    @staticmethod
    def delivery(obj):
        return obj.guest.delivery

    @staticmethod
    def name(obj):
        return obj.guest.__str__()

    @staticmethod
    def receipt(obj):
        return obj.guest.receipt

    @staticmethod
    def phone_number(obj):
        return obj.guest.phone_number

    @staticmethod
    def name_product(obj):
        return obj.prodact.name

    @staticmethod
    def image(obj):
        return obj.prodact.image_table()

    list_display = ['image', 'name', 'name_product', 'delivery', 'receipt', 'phone_number']
    readonly_fields = ('delivery', 'receipt','name', 'phone_number', 'name_product', 'image')


class ProdactAdmin(admin.ModelAdmin):
    # prodact = Prodact.objects.get()
    # date = prodact.booking.delivery

    list_display = ['name', 'price', 'category', 'image_table']
    # list_filter = ['created_at']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return obj.image_tag

    # date.short_description = 'just for  test'
    # date.allow_tags = True
    image_tag.short_description = 'just for  test'
    image_tag.allow_tags = True


admin.site.register(Prodact, ProdactAdmin)
admin.site.register(Category)
admin.site.register(Guest, GuestAdmin)
admin.site.register(Booking, BookingAdmin)
# Register your models here.
