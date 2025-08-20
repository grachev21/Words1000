from django import template
from settings.models import WordsSettings
from users.models import WordsUser

register = template.Library()

@register.inclusion_tag("includes/progress_bar_game.html")
def progress_bar_game(**kwargs):
    setting_words = WordsSettings.objects.select_related("user").get(user=kwargs["user"]).number_words
    count_words = setting_words - WordsUser.objects.select_related("user").filter(user=kwargs["user"]).count()
    out = setting_words / 100
    result = count_words / out
    data = {"count_words": int(result)}
    return data
