from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount as Account

class AccountAdmin(UserAdmin):

  

    search_field = ("email", "first_name", "last_name","Grade","address")
    readonly_fields = (
        "id",
        "created",
    )


admin.site.register(Account, )
