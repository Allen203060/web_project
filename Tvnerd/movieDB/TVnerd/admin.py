from django.contrib import admin


# Register your models here.
admin.site.site_header = "TVNerd Admin Dashboard"
admin.site.site_title = "TVNerd Admin Portal"
admin.site.index_title = "Welcome to the TVNerd Admin Panel"

class MyAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ('css/custom-admin.css',)
        }
        js = ('js/custom-admin.js',)




