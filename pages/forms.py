from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
    def clean_title(self):
        t = self.cleaned_data['title']
        if "test" in t.lower():
            raise forms.ValidationError("Title cannot contain the word 'test'.")
        if len(t) < 3:
            raise forms.ValidationError('Title too short.')
        return t