from django.forms import Widget


class JsonWidget(Widget):
    template_name = 'backend/json.html'

    def format_value(self, value):
        return value