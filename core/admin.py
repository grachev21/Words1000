from django.contrib import admin

from .models import WordsCard
from .models import Word_Accumulator
from .models import SettingsWordNumber
from .models import WordsToRepeat
from .models import IntroductionWords
from .models import WordsConfigJson
from .models import RepeatNumber


class IntroductionWordsAdmin(admin.ModelAdmin):
    list_display = ('word_en',
                    'transcription',
                    'word_ru'
                    )


class WordsCardAdmin(admin.ModelAdmin):
    list_display = (
                    'word_en',
                    'transcription',
                    'word_ru',
                    'phrases_en',
                    'phrases_ru',
                    )
    search_fields = ('word_en',)

class Word_AccumulatorAdmin(admin.ModelAdmin):
    list_display = ('word_en', 'word_ru')

class SettingsWordNumberAdmin(admin.ModelAdmin):
    list_display = ('number_words',)

class WordsToRepeatAdmin(admin.ModelAdmin):
    list_display = ('word',)

class WordsConfigJsonAdmin(admin.ModelAdmin):
    list_display = (
            'WORD_DATA',
            'WORD_USER'
            )

class RepeatNumberAdmin(admin.ModelAdmin):
    list_display = ('number',)

admin.site.register(WordsCard, WordsCardAdmin)
admin.site.register(Word_Accumulator, Word_AccumulatorAdmin)
admin.site.register(SettingsWordNumber, SettingsWordNumberAdmin)
admin.site.register(WordsToRepeat, WordsToRepeatAdmin)
admin.site.register(IntroductionWords, IntroductionWordsAdmin)
admin.site.register(WordsConfigJson, WordsConfigJsonAdmin)
admin.site.register(RepeatNumber, RepeatNumberAdmin)