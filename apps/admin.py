from django.contrib import admin
from apps.models import Category, Food, My_User, News, Newss


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','price','category_id')

@admin.register(My_User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','job')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('image','category','date','cause',)


#
admin.site.register(Newss)
# admin.site.unregister(Group)