from django.contrib import admin
from breaks.models import organisations, groups, replacements
from django.contrib.admin import TabularInline

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
    list_display = ('id', 'name', 'manager', 'min_active', )


@admin.register(replacements.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'is_active')


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', )
    
    inlines = (
        ReplacementEmployeeInline,
    )

