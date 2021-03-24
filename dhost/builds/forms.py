from django.forms import ModelForm

from .models import BuildOptions, EnvironmentVariable


class EnvironmentVariableForm(ModelForm):

    class Meta:
        model = EnvironmentVariable
        fields = ['variable', 'value']

    def __init__(self, *args, **kwargs):
        self.options_id = kwargs.pop('options_id')
        self.options = BuildOptions.objects.get(id=self.options_id)
        super().__init__(*args, **kwargs)

    def save(self):
        self.instance.options = self.options
        super().save()
