from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from accounts.models import User, Profile
from todo.models import Director, Task
from accounts.forms import UserCreationForm


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
 
 
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        (None, {'fields': ('is_active', 'is_admin',)}),
    )
 
    list_display = ('username', 'email', 'is_active',)
    list_filter = ()
    ordering = ()
    filter_horizontal = ()
 
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_active',)}),
    )
 
    add_form = UserCreationForm
 
    inlines = (ProfileInline,)

# Register your models here.
admin.site.register(Director)
admin.site.register(Task)
admin.site.register(User, CustomUserAdmin)

# Define an inline admin descriptor for Employee model
admin.site.unregister(Group)
