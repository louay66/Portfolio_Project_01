from django.contrib import admin
from .models import Category, Prodact, Booking


class BookingAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'delivery', 'receipt']
    list_filter = ['delivery']


class ProdactAdmin(admin.ModelAdmin):
    # prodact = Prodact.objects.get()
    # date = prodact.booking.delivery

    list_display = ['name', 'price', 'category', 'booking','date', 'image_table']
    # list_filter = ['created_at']
    readonly_fields = ('image_tag',)

    # def date(self):
    #     return "{}".format(self.date)

    def image_tag(self, obj):
        return obj.image_tag

    # date.short_description = 'just for  test'
    # date.allow_tags = True
    image_tag.short_description = 'just for  test'
    image_tag.allow_tags = True


admin.site.register(Prodact, ProdactAdmin)
admin.site.register(Category)
admin.site.register(Booking, BookingAdmin)
# Register your models here.
