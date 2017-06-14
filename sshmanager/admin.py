import uuid

from django.contrib import admin
from .models import Host, Token, Category

# Register your models here.
admin.site.site_title = 'SSHManager - Admin'
admin.site.site_header = 'SSHManager - Admin'


class MainAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.has_owner():
            obj.owner = request.user

        obj.save()


class HostAdmin(MainAdmin):
    readonly_fields = ('owner', 'created_at',)
    list_filter = ('owner', 'category')
    search_fields = ['host']
    list_display = ('full_host', 'hostname', 'port',
                    'active', 'owner', 'created_at',)


class TokenAdmin(MainAdmin):
    readonly_fields = ('owner', 'token', 'created_at',)
    list_display = ('token', 'active', 'owner', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.token:
            obj.token = uuid.uuid4()

        super().save_model(request, obj, form, change)


class CategoryAdmin(MainAdmin):
    readonly_fields = ('owner', 'slug', )
    list_display = ('name', 'name_chain', 'owner', 'created_at',)


admin.site.register(Host, HostAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Category, CategoryAdmin)
