from django.urls import path
from core.views import (
    Home,
    # IntroductionWordsList,
    # LearnNewWords,
    # Result,
    # SettingsPage,
    # ResettingDictionaries,
    # ReadingSentences,
    RegisterUser,
    LoginUser,
    logout_user,
    # activate,
)
from django.urls import path, re_path


urlpatterns = [
    path("", Home.as_view(), name="home"),
    # path(
    #     "introduction_words/",
    #     IntroductionWordsList.as_view(),
    #     name="introduction_words",
    # ),
    # path("learn_new_words/", LearnNewWords.as_view(), name="learn_new_words"),
    # path("result/", Result.as_view(), name="result"),
    # path("settings/", SettingsPage.as_view(), name="settings"),
    # path("reading_sentences/", ReadingSentences.as_view(), name="reading_sentences"),
    # path(
    #     "resetting_dictionaries/",
    #     ResettingDictionaries.as_view(),
    #     name="resetting_dictionaries",
    # ),
    path("register/", RegisterUser, name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    # path('activate/<uidb64>/<token>/', activate, name='activate'),
]
