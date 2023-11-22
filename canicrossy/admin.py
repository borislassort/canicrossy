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
    list_display = ('name', 'gender', 'dog_name', 'license', 'federation')
    search_fields = ['name']
admin.site.register(Athlete, AthleteAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
admin.site.register(Category, CategoryAdmin)

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'race', 'category', 'race_number', 'delay', 'time')
    search_fields = ['athlete', 'race', 'race_number']

admin.site.register(Participant, ParticipantAdmin)

class ParticipantInline(admin.TabularInline):
    model = Participant

class RaceDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "products.view_order"
    template_name = "admin/canicrossy/race/detail.html"
    context_object_name = 'race'
    model = Race

class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'detail')
    inlines = [
        ParticipantInline,
    ]

    def get_urls(self):
        return [
            path(
                "<pk>/detail",
                self.admin_site.admin_view(RaceDetailView.as_view()),
                name=f"race_detail",
            ),
            *super().get_urls(),
        ]

    def detail(self, obj: Race) -> str:
        url = reverse("admin:race_detail", args=[obj.pk])
        return format_html(f'<a href="{url}">📝</a>')
    
admin.site.register(Race, RaceAdmin)

class FederationAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Federation, FederationAdmin)
