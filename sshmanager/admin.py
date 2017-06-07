import uuid

from django.contrib import admin
from .models import Host, Token

# Register your models here.
admin.site.site_title = 'SSHManager - Admin'
admin.site.site_header = 'SSHManager - Admin'

class HostAdmin(admin.ModelAdmin):
	readonly_fields = ('owner','created_at',)
	list_filter = ('owner',)
	search_fields = ['host', 'owner__username']
	list_display = ('owner', 'host', 'hostname', 'port','active', 'created_at',)


	def save_model(self, request, obj, form, change):
		if not obj.has_owner():
			obj.owner = request.user

		obj.save()

	def get_queryset(self, request):
		qs = super(HostAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs

		return qs.filter(owner=request.user)

class TokenAdmin(admin.ModelAdmin):
	readonly_fields = ('owner','token','created_at',)
	list_display = ('owner', 'token', 'active', 'created_at')

	def save_model(self, request, obj, form, change):
		if not obj.has_owner():
			obj.owner = request.user

		if not obj.token:
			obj.token = uuid.uuid4()

		obj.save()

	def get_queryset(self, request):
		qs = super(TokenAdmin, self).get_queryset(request)
		if request.user.is_superuser:
			return qs

		return qs.filter(owner=request.user)

admin.site.register(Host, HostAdmin)
admin.site.register(Token, TokenAdmin)
