from django.contrib import admin
from reviewSystem.models import Item,Category,User,Rating

# register your model here
class CategoryInline(admin.TabularInline):
    model = Category
    extra = 0
    #raw_id_fields = ("item",)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name','item_rating')
    #list_display_links = ('item_id', 'item_name')
    list_editable=('item_id', 'item_name','item_rating')
    inlines = [CategoryInline,]
    fieldsets = [
        ('Item',               {'fields': ['item_id','item_name']}),
        ('Avg. Rating', {'fields': ['item_rating']}),
    ]
    search_fields = ['item_name']
    #fields = ['item_id', 'item_name','item_rating']
admin.site.register(Item,ItemAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'first_name','last_name','email')
    list_display_links = ('user_id', 'first_name','last_name')
    fields = ('user_id',('first_name', 'last_name'), 'email','tiemstamp') 
admin.site.register(User,UserAdmin) # hide show timestamp

class CategoryAdmin(admin.ModelAdmin):
    fields = ['items_type', 'item']
    #search_fields = ['item']
    list_display = ( 'items_type','item')
    list_filter = ['items_type']
admin.site.register(Category,CategoryAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ( 'item','user','ratings')
    list_display_links = ( 'item','user')
    fieldsets = [
        ('Item',               {'fields': ['item']}),
        ('User Rating', {'fields': ['user','ratings']}),
        ('timestamp',{'fields':['timestamp'],'classes': ['collapse']}),
    ]
    list_filter = ['timestamp']
    search_fields = ['item']
    #fields = ['item', 'user','ratings','timestamp']
admin.site.register(Rating,RatingAdmin)


# can call field of other non linked table if the fields are readonly fields... for list_display ??
# view on site ??