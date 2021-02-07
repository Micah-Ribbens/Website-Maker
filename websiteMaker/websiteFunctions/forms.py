from django import forms
from websiteFunctions.models import Function


class FunctionForm(forms.ModelForm):
    class Meta:
        model = Function
        fields = ('command',)
    
    def clean_command(self, *args, **kwargs):
         return self.cleaned_data.get("command")

