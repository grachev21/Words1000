# Mixins

from django.shortcuts import render


class Htm_xMixin:
    """Mixin for processing HTML requests"""

    partial_template_name = None

    def get_partial_template(self):
        return self.partial_template_name or self.template_name

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            # HTM_X request - return only content
            return render(self.request, self.get_partial_template(), context)
        else:
            # Normal request - full page
            return super().render_to_response(context, **response_kwargs)
