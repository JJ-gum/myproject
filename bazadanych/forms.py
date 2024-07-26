from django import forms
from .models import Zgloszenie


class ZgloszenieFormularz(forms.ModelForm):
    class Meta:
        model = Zgloszenie
        fields = ' __all__ '
