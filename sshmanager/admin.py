from django.contrib import admin
from .models import Host

# Register your models here.

class HostAdmin(admin.ModelAdmin):
	readonly_fields = ('owner','created_at',)
	list_filter = ('owner',)
	search_fields = ['host', 'owner__username']

	def save_model(self, request, obj, form, change):
		obj.owner = request.user
		obj.save()

admin.site.register(Host, HostAdmin)
