from django import forms

from .models import Post
#PostForm:フォームの名前(ModelFormの一種)
class PostForm(forms.ModelForm):

    class Meta:
        model = Post    #Postモデルを使う事を伝達
        fields = ('title', 'text',) #フォームではタイトルとテキストのフィールドを使用する