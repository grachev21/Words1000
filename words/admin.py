from django.contrib import admin

from .models import WordsCard
from .models import Word_status
from .models import Word_Accumulator
from .models import SettingsWordNumber
from .models import WordsToRepead

class WordStatusAdmin(admin.ModelAdmin):
    list_display = ('status',)


class WordsCardAdmin(admin.ModelAdmin):
    list_display = (
                    'word_en',
                    'transcription',
                    'word_ru',
                    'phrases_en',
                    'phrases_ru',
                    )

class Word_AccumulatorAdmin(admin.ModelAdmin):
    list_display = ('word',)

class SettingsWordNumberAdmin(admin.ModelAdmin):
    list_display = ('number_words',)

class WordsToRepeadAdmin(admin.ModelAdmin):
    list_display = ('word',)


admin.site.register(Word_status, WordStatusAdmin)
admin.site.register(WordsCard, WordsCardAdmin)
admin.site.register(Word_Accumulator, Word_AccumulatorAdmin)
admin.site.register(SettingsWordNumber, SettingsWordNumberAdmin)
admin.site.register(WordsToRepead, WordsToRepeadAdmin)
