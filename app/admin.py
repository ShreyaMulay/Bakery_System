from django.contrib import admin

# Register your models here.

from .models import Category,Sub_Category,Product,Contact_Us,Order,Brand,OrderNew,OrderItem


class OrderItemTubleinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTubleinline]
    list_display = ['name','phone','email','payment_id','paid','date']
    search_fields = ['name','email','payment_id']

admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_Us)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(OrderNew,OrderAdmin)
admin.site.register(OrderItem)




