from pprint import pprint

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet

from .models import Article, Tag, Scope
from django.forms import BaseInlineFormSet


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1
            else:
                continue
        if main_count <= 1:
            return self.save()
        else:
            raise ValidationError('Основной тег может быть только один!')


class ScopeInLine(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormSet



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    inlines = [ScopeInLine]



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']





