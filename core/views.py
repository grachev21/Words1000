from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, CreateView
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from core.token import account_activation_token
from django.core.mail import EmailMessage
from django.contrib import messages

# User
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

# Custom service
# from core.services.views_logic import DataMixin
# from core.services import play_on_words
# from core.services import str_to_list

# Models
from .models import WordsCard

# Forms
# from .forms import WordCheck, ResettingDictionariesForm

# Other
import random
import json


class Home(ListView):
    model = WordsCard
    template_name = "core/home.html"
    context_object_name = "words_counter_home"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     var = self.list_variables(title="Words1000", user=self.request.user)
    #     self.logics()
    #     context["user"] = self.request.user
    #     context["spinner_data"] = self.word_dict()
    #     context["all_words"] = WordsCard.objects.all()
    #     return dict(list(context.items()) + list(var.items()))

    # def word_dict(self):
    #     send_dict = {}
    #     out_list = []
    #     list_for_spinner_word_en = [data.word_en for data in WordsCard.objects.all()]
    #     list_for_spinner_word_ru = [data.word_ru for data in WordsCard.objects.all()]
    #     number = [n for n in range(1000)]
    #     number = random.sample(number, 10)
    #     word_en = [list_for_spinner_word_en[n] for n in number]
    #     word_ru = [list_for_spinner_word_ru[n] for n in number]
    #     for val in range(10):
    #         send_dict["en"] = word_en[val]
    #         send_dict["ru"] = word_ru[val]
    #         out_list.append(dict(send_dict))
    #     return out_list






class ReadingSentences(LoginRequiredMixin, TemplateView):
    template_name = "core/reading_sentences.html"
    login_url = reverse_lazy("register")


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = "Тесты"
#         context["result_word"] = (
#             WordsConfigJson.objects.select_related("user")
#             .get(user=self.request.user)
#             .WORD_USER
#         )
#         context["phrases_set"], context = self.init_word(context)
#         context["word_ru"] = (
#             WordsConfigJson.objects.select_related("user")
#             .get(user=self.request.user)
#             .WORD_DATA
#         )
#         context["words_count"] = (
#             SettingsWordNumber.objects.select_related("user")
#             .get(user=self.request.user)
#             .number_words
#         )

#         val = self.list_variables(title="Тесты", user=self.request.user)
#         return dict(list(context.items()) + list(val.items()))

#     def init_word(self, context):
#         word = (
#             WordsConfigJson.objects.select_related("user")
#             .get(user=self.request.user)
#             .WORD_USER
#         )
#         db = WordsCard.objects.get(word_en=word)
#         phrases_set = str_to_list.str_list(db.phrases_en, db.phrases_ru)
#         check = (
#             WordsToRepeat.objects.select_related("user")
#             .filter(user=self.request.user)
#             .count()
#         )
#         if check == 0:
#             context["check_congratulation"] = "off"
#         else:
#             context["check_congratulation"] = "on"
#         return phrases_set, context



