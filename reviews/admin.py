from django.contrib import admin
from reviews.models import (Publisher, Contributor, Book,
BookContributor, Review)
# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
try:
    admin.site.unregister(Contributor)
except admin.sites.NotRegistered:
    pass
class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    search_fields = ('last_names__startswith', 'first_names')
    list_filter = ('last_names',)
admin.site.register(Contributor, ContributorAdmin)



