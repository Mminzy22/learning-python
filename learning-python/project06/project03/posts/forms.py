from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 사용자 입력 필드만 포함
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': '제목을 입력하세요', 'class': 'form-control'}),
            'content': forms.Textarea(attrs={'placeholder': '내용을 입력하세요', 'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 댓글 내용만 입력받음
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력하세요', 'class': 'form-control', 'rows': 3}),
        }
