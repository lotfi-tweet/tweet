from django.contrib import admin
from .models import Post, Category,\
    About, AdsPublic,AdsPersonal,Discount


class PostDisplay(admin.ModelAdmin):

    list_display = ['title', 'categorie', 'pup_date', 'writer', 'visit_num']

    class Meta:
        module = Post


admin.site.register(Category)
admin.site.register(Post, PostDisplay)
admin.site.register(About)
admin.site.register(AdsPublic)
admin.site.register(AdsPersonal)
admin.site.register(Discount)
