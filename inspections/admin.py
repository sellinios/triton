import nested_admin
from django.contrib import admin
from .models import InspectionTemplate, Section, Question


class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    extra = 1  # Adjust based on your preference


class SectionInline(nested_admin.NestedStackedInline):
    model = Section
    extra = 0  # No extra empty form by default
    inlines = [QuestionInline]  # This allows nesting QuestionInline within SectionInline


class InspectionTemplateAdmin(nested_admin.NestedModelAdmin):
    list_display = ('title', 'date_created', 'comments_enabled')
    inlines = [SectionInline]  # Adding SectionInline which now includes QuestionInline


admin.site.register(InspectionTemplate, InspectionTemplateAdmin)
