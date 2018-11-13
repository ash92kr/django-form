from django import forms
from .models import Post
    
class PostForm(forms.Form):  # forms.Form을 상속받아 여러 기능을 구현할 수 있음
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable'}))   # 이것을 이용해 html 코드를 만들 수 있다
    # widget = textarea(크기 변환 가능) -> 속성으로 editable을 주니 자유롭게 글 작성 가능
    
class PostModelForm(forms.ModelForm):  # 어떤 모델을 사용하는지 파악하면 알아서 구조를 지정해줌
    class Meta:
        model = Post  # 특별한 형식 지정없이 url만 입력하면 알아서 동작함(폼 생성)
        fields= '__all__'  # models.py의 Post에서 만든 컬럼을 받아와서 자동으로 생성함

