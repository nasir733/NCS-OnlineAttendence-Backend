from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount as Account
from.models import last_detected_images 
class AccountAdmin(UserAdmin):

  

    search_field = ("email", "first_name", "last_name","Grade","address")
    readonly_fields = (
        "id",
        "created",
    )


admin.site.register(Account )
admin.site.register(last_detected_images)
