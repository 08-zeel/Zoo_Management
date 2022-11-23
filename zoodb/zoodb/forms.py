from django import forms
from zoodb.models import zoo


class zooforms(forms.ModelForm):
    class Meta:
        model = zoo
        fields = "__all__"
