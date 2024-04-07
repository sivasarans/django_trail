from django.contrib import admin

from .models import *
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(UserProfile)
admin.site.register(Article)
admin.site.register(Customer)

class TagAdmin(admin.ModelAdmin):
    fields = ("name",)  # Fields to use for add/edit/show page
    list_display = ("name",)  # Fields to display in the search page
    list_display_links = ("name",)  # Fields that will be a link in the search page
    search_fields = ("name",)  # Search fields allowed in the search page

# Register the Tag model with its admin class
admin.site.register(Tag, TagAdmin)


from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # Fields to use for add/edit/show page
    fields = ("name", "email", "slug")
    
    # Fields to display in search page
    list_display = ("name", "email", "slug")
    
    # Fields that will be a link in search page
    list_display_links = ("name","email",)
    
    # Ordering allowed in the search page
    ordering = ("name",)
    
    # Search fields allowed in the search page
    search_fields = ("name", "email", "slug")


# Register the Profile model with the ProfileAdmin
admin.site.register(Profile, ProfileAdmin)

