from django.contrib import admin
from .models import Author, Quotes


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'birth_day', 'bio')
    list_filter = ['fullname']
    search_fields = ['bio']


admin.site.register(Author, AuthorAdmin)


class QuotesAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author')
    list_filter = ['author']
    search_fields = ['quote']


admin.site.register(Quotes, QuotesAdmin)
