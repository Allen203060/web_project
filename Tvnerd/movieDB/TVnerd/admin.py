# from django.contrib import admin
# from .models import User, Movie, Comment, Watchlist

# # Custom Admin Site
# class MyAdminSite(admin.AdminSite):
#     site_header = "TVNerd Admin Dashboard"
#     site_title = "TVNerd Admin Portal"
#     index_title = "Welcome to the TVNerd Admin Panel"

#     class Media:
#         css = {
#             'all': ('css/custom-admin.css',)
#         }
#         js = ('js/custom-admin.js',)

# # Instantiate the custom admin site
# admin_site = MyAdminSite(name='myadmin')

# # Define ModelAdmin classes
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email')
#     search_fields = ('username', 'email')
#     list_filter = ('username',)

# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('title', 'tmdb_id', 'poster_path')
#     search_fields = ('title', 'tmdb_id')
#     list_filter = ('title',)
#     actions = ['mark_as_featured']

#     def mark_as_featured(self, request, queryset):
#         queryset.update(is_featured=True)  # Assumes you add an `is_featured` BooleanField to the Movie model
#     mark_as_featured.short_description = "Mark selected movies as featured"

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('user', 'movie', 'content', 'created_at')
#     search_fields = ('content', 'user__username', 'movie__title')
#     list_filter = ('created_at', 'user')
#     date_hierarchy = 'created_at'

# class WatchlistAdmin(admin.ModelAdmin):
#     list_display = ('user', 'title', 'movie_id', 'poster_path')
#     search_fields = ('title', 'user__username')
#     list_filter = ('user',)

# # Register models with the custom admin site
# admin_site.register(User, UserAdmin)
# admin_site.register(Movie, MovieAdmin)
# admin_site.register(Comment, CommentAdmin)
# admin_site.register(Watchlist, WatchlistAdmin)


from django.contrib import admin
from .models import User, Movie, Comment, Watchlist, Notification

# Custom Admin Site
class MyAdminSite(admin.AdminSite):
    site_header = "TVNerd Admin Dashboard"
    site_title = "TVNerd Admin Portal"
    index_title = "Welcome to the TVNerd Admin Panel"

    class Media:
        css = {
            'all': ('css/custom-admin.css',)
        }
        js = ('js/custom-admin.js',)

# Instantiate the custom admin site
admin_site = MyAdminSite(name='myadmin')

# Define ModelAdmin classes
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'tmdb_id', 'poster_path', 'is_featured')
    search_fields = ('title', 'tmdb_id')
    list_filter = ('title',)
    actions = ['mark_as_featured']

    def mark_as_featured(self, request, queryset):
        queryset.update(is_featured=True)
    mark_as_featured.short_description = "Mark selected movies as featured"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'content', 'created_at')
    search_fields = ('content', 'user__username', 'movie__title')
    list_filter = ('created_at', 'user')
    date_hierarchy = 'created_at'

class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'movie_id', 'poster_path')
    search_fields = ('title', 'user__username')
    list_filter = ('user',)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at', 'is_read')
    search_fields = ('message', 'user__username')
    list_filter = ('is_read', 'created_at')
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected notifications as read"

# Register models with the custom admin site
admin_site.register(User, UserAdmin)
admin_site.register(Movie, MovieAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(Watchlist, WatchlistAdmin)
admin_site.register(Notification, NotificationAdmin)