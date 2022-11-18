from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Post


class PostForm(ModelForm):
    # user_type = forms.CharField(widget=forms.HiddenInput(), initial= USER_TYPES[1][0], max_length=9)
    class Meta:
        model = Post
        # Put Candidate forms
        fields = ['position','type','location','skills','description','company','expiration','status',]
        widgets = {
            'expiration': DateTimeInput()
        }


