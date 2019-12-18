from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserAccount, Timetable, Categories, Topics, Posts, Notes, Tasks
from django.contrib.auth.models import Group
from .forms import UserAccountCreation

class UserAdmin(BaseUserAdmin):
    add_form = UserAccountCreation
    list_display = ('email', 'username', 'reg_no', 'date_joined', 'last_login', 'is_admin')
    search_fields = ('email', 'username', 'reg_no')
    # readonly_fields = ('date_login', 'last_login')
    filter_horizontal = ()
    list_filter = ('is_admin',)
    fieldsets = (
                    (None, {'fields': ('username', 'email', 'password', 'reg_no')}),
                    ('Permissions', {'fields': ('is_admin',)}),
                    ('Biodata', {'fields': ('profile_img', 'bio', 'year', 'course', 'branch',)})
                )

class TopicAdmin(admin.ModelAdmin):
    list_display = ['topic_name', 'topic_by', 'topic_cat', 'topic_date', 'topic_posts']

class PostAdmin(admin.ModelAdmin):
    list_display = ['post_by', 'post_topic', 'post_date', 'post_upvote']

admin.site.unregister(Group)
admin.site.register(UserAccount, UserAdmin)
admin.site.register(Timetable)
admin.site.register(Categories)
admin.site.register(Topics, TopicAdmin)
admin.site.register(Posts, PostAdmin)
admin.site.register(Notes)
admin.site.register(Tasks)