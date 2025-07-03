from settings.models import WordsSettings
from users.models import WordsUser
import random


class GameInitMixin:

    def init_list(self, request, *args, **kwargs):

        settings = WordsSettings.objects.filter(user=request.user).latest("id")
        elements = WordsUser.objects.filter(user=request.user).all()
        random_elements = random.sample(list(elements), int(settings.number_words))
        list_check = [e.status for e in elements]

        value_to_check = {"2", "3", "4", "5"}
        if not set(list_check) & value_to_check:
            print("yes")
        # print(list_check)
        # match list_check:
        #     case ["2", "3", "4", "5"]:
        #         print("yes")
        # if "2" not in or "3" or "4" or "5" not in [e.status for e in elements]:
        #     print("yes")
        # else:
        #     print("no")
            # for obj in random_elements:
            #     obj.status = "2"
                # obj.save()

        # counter = 0 
        # for e in elements:
        #     if e.status == "2":
        #         print(e.status)
        #         counter += 1
        
        # print(counter)