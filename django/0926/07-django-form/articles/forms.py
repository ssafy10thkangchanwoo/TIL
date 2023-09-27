# from django import forms 
# from .models import Article 


# # class ArticleForm(forms.Form):
# #     title = forms.CharField(max_length=10)
# #     content = forms.CharField(widget=forms.Textarea) 
#     # forms 안에도 많은 필드가 있다.
#     # form에 문자 필드는 CharField밖에 없다.

# class Article(forms.ModelForm):
#     title = forms.CharField(
#         label = '제목', label_suffix="",
#         widget = forms.TextInput(
#             attrs = {
#                 'class': 'article-title my-title',
#                 "placeholder": "제목을 입력하세요" 
#             }
#         )
#     )

# class ArticleForm(forms.ModelForm):
#     # Model 등록
#     class Meta:
#         model = Article 
#         fields = '__all__'
#         # fields = ('title',)  # 나오게 하는 것을 지정
#         # exclude = ('title',) # 제외


from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


# formfield 및 widget 활용
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/
# https://docs.djangoproject.com/en/4.2/topics/forms/
# https://docs.djangoproject.com/en/4.2/ref/forms/widgets/




class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력해주세요.'
        }
    )

    # model 등록
    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('title',)
        # exclude = ('title',)
