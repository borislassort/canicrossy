from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.detail import DetailView
from django.utils.html import format_html
from django.urls import path, reverse
from .models import *

# Disable auth
#anonymous_user = User.objects.all().first()
#admin.site.has_permission = lambda r: setattr(r, 'user', anonymous_user) or True
# Hide auth in Admin
admin.site.unregister(User)
admin.site.unregister(Group)

class AthleteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'license', 'federation')
    search_fields = ['first_name', 'last_name']
admin.site.register(Athlete, AthleteAdmin)

class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'ident')
    search_fields = ['name', 'ident']
admin.site.register(Dog, DogAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
admin.site.register(Category, CategoryAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'dog', 'race', 'category', 'race_number', 'delay', 'time')
    search_fields = ['athlete__first_name', 'athlete__last_name', 'dog__name', 'dog__ident', 'race__name', 'race_number']
admin.site.register(Participant, ParticipantAdmin)

class ParticipantInline(admin.TabularInline):
    model = Participant
    search_fields = ["first_name"]

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'event')
    inlines = [
        ParticipantInline,
    ]
    search_fields = ['name', 'event__name']
admin.site.register(Race, RaceAdmin)

class RaceInline(admin.TabularInline):
    model = Race
    search_fields = ["name"]

class EventDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "products.view_order"
    template_name = "admin/canicrossy/event/detail.html"
    context_object_name = 'event'
    model = Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'detail')
    inlines = [
        RaceInline,
    ]

    def get_urls(self):
        return [
            path(
                "<pk>/detail",
                self.admin_site.admin_view(EventDetailView.as_view()),
                name=f"event_detail",
            ),
            *super().get_urls(),
        ]

    def detail(self, obj: Event) -> str:
        url = reverse("admin:event_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>')
admin.site.register(Event, EventAdmin)

class FederationAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Federation, FederationAdmin)
