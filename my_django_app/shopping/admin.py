from django.contrib import admin
from shopping.models import *


class WlAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(Wishlist, WlAdmin)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Review)
