from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomepageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_statement"] = "Nice to see  you!"
        context["math_result"] = self._do_math()
        return context

    def _do_math(sefl):
        return 6 + 6

    def say_bye(self):
        return f"Goodbye!"
