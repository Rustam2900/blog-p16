from django import forms


from .models import Blog, Tag, Comment

class TagForm(forms.Form):
    name = forms.CharField(max_length=100,
                           help_text="tag name kiriting",
                           label='Tag name',
                           widget=forms.TextInput(attrs={"class": "form-control"})
                           )

class BlogForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"class": "form-control"})
        self.fields['category'].widget.attrs.update({"class": "form-control"})

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

