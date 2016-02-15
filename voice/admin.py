from django.contrib import admin
from .models import Question, Contact, Event, Host, Post

class QuestionAdmin(admin.ModelAdmin):

    list_display = ('question', 'answer', 'submit_date')

    list_filter = ('submit_date',)


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'message', 'submit_date')

    list_filter = ('submit_date',)


class EventAdmin(admin.ModelAdmin):

    list_display = ('name', 'content', 'date')

    list_filter = ('date',)


class HostAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'biography')


class PostAdmin(admin.ModelAdmin):

    list_display = ('name', 'post', 'posted_by')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Post, PostAdmin)
