from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title',
                  'categorie',
                  'writer',
                  'text_1',
                  'img_1',
                  'text_2',
                  'img_2',
                  'img_3',
                  'img_4',
                  'text_3',
                  'relate1_url',
                  'title_url1',
                  'relate2_url',
                  'title_url2',
                  ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'العنوان'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
            'writer': forms.Select(attrs={'class': 'form-control'}),
            'text_1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'النص 1'}),
            'img_1': forms.FileInput(attrs={'class': 'form-control'}),
            'text_2': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'النص 2'}),
            'img_2': forms.FileInput(attrs={'class': 'form-control'}),
            'img_3': forms.FileInput(attrs={'class': 'form-control'}),
            'img_4': forms.FileInput(attrs={'class': 'form-control'}),
            'text_3': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'النص 3'}),
            'relate1_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'الرابط 1'}),
            'title_url1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان الرابط 1'}),
            'relate2_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'الرابط 2'}),
            'title_url2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان الرابط 2'}),
        }
