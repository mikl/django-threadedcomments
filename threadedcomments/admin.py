from django.contrib import admin
from django.contrib.comments.models import Comment
from django.contrib.comments.admin import CommentsAdmin
from threadedcomments import get_model
from django.utils.translation import ugettext_lazy as _
from threadedcomments.models import ThreadedComment

def remove_comment(modeladmin, request, queryset):
    queryset.update(is_removed=True)

def un_remove_comment(modeladmin, request, queryset):
    queryset.update(is_removed=False)

def public_comment(modeladmin, request, queryset):
    queryset.update(is_public=True)

def un_public_comment(modeladmin, request, queryset):
    queryset.update(is_public=False)


remove_comment.short_description = _("Mark selected comments as removed")
un_remove_comment.short_description = _("Mark selected comments as not removed")
public_comment.short_description = _("Mark selected comments as published")
un_public_comment.short_description = _("Mark selected comments as unpublished")
CommentsAdmin.actions.append(remove_comment)
CommentsAdmin.actions.append(un_remove_comment)
CommentsAdmin.actions.append(public_comment)
CommentsAdmin.actions.append(un_public_comment)

if get_model() is ThreadedComment:
    if Comment in admin.site._registry:
      admin.site.unregister(Comment)
    admin.site.register(Comment, CommentsAdmin)
