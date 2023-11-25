from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from breaks.models import organisations, groups, replacements, dicts, breaks
from django.contrib.admin import TabularInline
from django.db.models import Count

###############################
# INLINES
###############################

class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status')




###############################
# MODELS
###############################
@admin.register(organisations.Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active', 'replacement_count', )

    def replacement_count(self, obj):
        return obj.replacement_count
    
    replacement_count.short_description = 'Кол-во смен'

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        QuerySet = groups.Group.objects.annotate(
            replacement_count=Count('replacements__id')
        )
        return QuerySet

@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', )
    
    inlines = (
        ReplacementEmployeeInline,
    )


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement', 'employee', 'break_start', 'break_end',
    )
