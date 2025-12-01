from users.models import WordsUser
from settings.models import WordsSettings
from core.models import WordsCard
import random


class SettingsStatus:
    def setup_settings_status(self, user):
        self.user = user
        self.limiter = (
            WordsSettings.objects.filter(user=self.user)
            .latest("id")
            .number_words
        )

    def installation_status_default(self):
        object_status = list(WordsUser.objects.filter(user=self.user))
        for obj_stat in object_status:
            obj_stat.status = "1"
        WordsUser.objects.bulk_update(
            object_status,
            [
                "status",
            ],
        )

    def installation_status_for_learning(self):
        for status_change in WordsUser.objects.filter(status="1")[
            : int(self.limiter)
        ]:
            status_change.status = "2"
            status_change.save()

    def form_valid(self, form):
        self.installation_status_default()
        self.installation_status_for_learning()

        return super().form_valid(form)


class SettingsReset:

    def setup_settings_reset(self, user):
        self.words_settings = WordsSettings.objects.filter(user=user)
        self.words_card = WordsCard.objects.all()
        self.user = user

    def delete_list_words_user(self, form):
        if form.cleaned_data["status"] and form.cleaned_data["yes"] == "yes":
            WordsUser.objects.filter(user=self.user).delete()

    def create_list_words_user(self):
        random_elements = random.sample(list(self.words_card), 1000)
        objects_list = [
            WordsUser(user=self.user, core_words=e) for e in random_elements
        ]
        WordsUser.objects.bulk_create(objects_list)

    def form_valid(self, form):
        # mixins method
        self.delete_list_words_user(form=form)
        self.create_list_words_user()

        return super().form_valid(form)
