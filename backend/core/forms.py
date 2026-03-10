from django.core.exceptions import ValidationError
from django import forms

list_status = ["Удалить весь прогресс", "hello"]




# class AddWordAccumulator(forms.ModelForm):
#     word_en = forms.CharField(
#         label="Английский",
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Напишите слово на английском",
#                 "class": "user_form_add_word_accum",
#             }
#         ),
#     )
#     word_ru = forms.CharField(
#         label="Русский",
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Напишите слово на русском",
#                 "class": "user_form_add_word_accum",
#             }
#         ),
#     )
#     user = forms.Field(
#         disabled=True,
#         label="",
#         widget=forms.TextInput(attrs={"class": "user_form_label"}),
#     )
#     status = forms.Field(
#         disabled=True,
#         label="",
#         widget=forms.TextInput(attrs={"class": "user_form_label"}),
#     )

#     class Meta:
#         model = WordsUser
#         fields = ("word_en", "word_ru", "user", "status")

#     def clean_word_en(self):
#         val_en_user = self.cleaned_data["word_en"]
#         user_word_en = WordsConfigJson.objects.first().WORD_USER
#         if val_en_user != user_word_en:
#             raise ValidationError("Слово должно совпадать")
#         else:
#             return val_en_user

#     def clean_word_ru(self):
#         val_ru_user = self.cleaned_data["word_ru"]
#         user_word_ru = WordsConfigJson.objects.first().WORD_DATA
#         user_word_ru = user_word_ru["translate_ru"].split(",")
#         if val_ru_user != user_word_ru[0]:
#             raise ValidationError("Слово должно совпадать")
#         else:
#             return val_ru_user




class ResettingDictionariesForm(forms.Form):
    yes = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": ""}),
        label='Напишите для подтверждения "yes"',
    )
    status = forms.BooleanField(label="Подтвердите сброс прогресса")




