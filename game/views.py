from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from game.forms import WordCheck
from users.models import WordsUser
from django.urls import reverse, reverse_lazy
from users.models import WordsUser
from settings.models import WordsSettings
from django.core.serializers import serialize
from game.services import GameInitMixin



class Game(GameInitMixin, LoginRequiredMixin, FormView):
    template_name = "game/game.html"
    form_class = WordCheck


#     # Переведет на другую страницу не авторизованных пользователей
    login_url = reverse_lazy("register")
    success_url = reverse_lazy("game")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.init_list(self.request)

        queryset_words = WordsUser.objects.all()
        queryset_settings = WordsSettings.objects.all()
        context["words_json"] = serialize("json", queryset_words)
        context["settings_json"] = serialize("json", queryset_settings)
#         check = (
#             Word_Accumulator.objects.select_related("user")
#             .filter(user=self.request.user)
#             .count()
#         )
#         if check == 1000:
#             context["check_finish"] = "finish"
#             var = self.list_variables(title="Финиш", user=self.request.user)
#             return dict(list(context.items()) + list(var.items()))
#         else:
#             context["words"] = play_on_words.main(self.request.user)
#             WordsConfigJson.objects.select_related("user").filter(
#                 user=self.request.user
#             ).all().delete()
#             self.update(context)
#             context["user"] = self.request.user
#             var = self.list_variables(title="Учить новые слова", user=self.request.user)
#             return dict(list(context.items()) + list(var.items()))
        return context

#     def update(self, context):
#         data = {"WORD_DATA": context["words"]}
#         WordsConfigJson.objects.select_related("user").update_or_create(
#             defaults=data, user=self.request.user
#         )

#     def post(self, request, **kwargs):
#         data = {"WORD_USER": list(request.POST)[-1]}
#         WordsConfigJson.objects.select_related("user").update_or_create(
#             defaults=data, user=self.request.user
#         )
#         return redirect("result")



# class Result(DataMixin, LoginRequiredMixin, CreateView):

#     form_class = AddWordAccumulator
#     template_name = "core/result.html"
#     success_url = reverse_lazy("reading_sentences")
#     login_url = reverse_lazy("register")

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Результат"
#         # Получаем слова на русском
#         word_ru = (
#             WordsConfigJson.objects.select_related("user")
#             .get(user=self.request.user)
#             .WORD_DATA
#         )
#         # Оставляем только первое слово
#         word_ru = word_ru["translate_ru"].split(",")
#         context["word_ru"] = word_ru[0]
#         context["user"] = self.request.user
#         self.user_filter(context)
#         var = self.list_variables(title="Результат", user=self.request.user)
#         return dict(list(context.items()) + list(var.items()))

#     def get_initial(self):
#         initial = super().get_initial()
#         initial = initial.copy()
#         initial["user"] = self.request.user
#         initial["status"] = "0"
#         return initial

#     def user_filter(self, context):
#         data = WordsConfigJson.objects.select_related("user").get(
#             user=self.request.user
#         )
#         context["correct_word"] = data.WORD_DATA["correct_word"][0]
#         # print(data.WORD_USER)
#         # print(data.WORD_DATA['correct_word'][0])
#         if data.WORD_DATA["correct_word"][0] == data.WORD_USER:
#             context["response"] = 1
#             return redirect("reading_sentences")
#         else:
#             context["response"] = 0

#     def form_valid(self, form):

#         def update_db(number):
#             num = RepeatNumber.objects.get(pk=number)
#             WordsToRepeat.objects.select_related("user").filter(
#                 word=word_user, user=self.request.user
#             ).update(repeat_number=num)

#         word_user = (
#             WordsConfigJson.objects.select_related("user")
#             .get(user=self.request.user)
#             .WORD_USER
#         )
#         check = WordsToRepeat.objects.select_related("user").get(
#             user=self.request.user, word=word_user
#         )
#         if str(check.repeat_number) == "one":
#             update_db(2)
#             return redirect("learn_new_words")
#         if str(check.repeat_number) == "two":
#             update_db(3)
#             return redirect("learn_new_words")
#         if str(check.repeat_number) == "tree":
#             # Удаляем угаданное слова из дневной базы слов
#             WordsToRepeat.objects.select_related("user").get(
#                 user=self.request.user, word=word_user
#             ).delete()
#             return super().form_valid(form)