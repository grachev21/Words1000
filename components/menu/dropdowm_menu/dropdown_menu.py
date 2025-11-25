from django_components import component


@component.register("dropdown_menu")
class DropDowMenu(component.Component):
    template_name = "menu/dropdown_menu/dropdown_menu.html"

    class Media:
        js = ["menu/dropdown_menu/index.js"]

    def get_context_data(self):
        return {"text": "Профиль"}