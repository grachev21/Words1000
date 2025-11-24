from django.template.response import TemplateResponse

class HtmxMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name_template"] = self.partial_template_name
        return context

    def render_to_response(self, context, **response_kwargs):
        print(self.request.headers.get)
        if self.request.headers.get("HX-Request"):
            
            return TemplateResponse(self.request, self.partial_template_name, context)
        else:
            return TemplateResponse(self.request, self.template_name, context)
