from models.app import App, AppVersion, AppOperation
from django.contrib import admin

class OperationInline(admin.TabularInline):
    model = AppOperation

class VersionAdmin(admin.ModelAdmin):
    inlines = [OperationInline]

    list_filter = ['app']

admin.site.register(App)
admin.site.register(AppVersion, VersionAdmin)
