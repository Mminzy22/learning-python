from django.shortcuts import render, get_object_or_404, redirect  # HTTP 응답, 객체 조회 및 리다이렉트를 위한 유틸리티 함수
from django.urls import reverse_lazy  # URL 패턴을 문자열로 반환하는 유틸리티
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View  # 제네릭 뷰 클래스
from django.contrib.auth.mixins import LoginRequiredMixin  # 로그인 필요 여부를 제어하는 믹스인
from .models import Post, Comment  # Post와 Comment 모델
from .forms import PostForm, CommentForm  # Post와 Comment에 대한 폼 클래스

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer
from rest_framework.generics import (
    RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView,
)
from rest_framework.permissions import IsAuthenticated

# 게시글 목록 API
class PostListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_at')  # 최신순 정렬
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# 게시글 상세 보기 API
class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 게시글 작성 API
class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 생성 가능

    def perform_create(self, serializer):
        # 현재 요청한 사용자를 작성자로 설정
        serializer.save(author=self.request.user)


# 게시글 수정 API
class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 수정 가능

    def get_queryset(self):
        # 현재 사용자가 작성한 게시글만 반환
        return Post.objects.filter(author=self.request.user)


# 게시글 삭제 API
class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 삭제 가능

    def get_queryset(self):
        # 현재 사용자가 작성한 게시글만 삭제 가능
        return Post.objects.filter(author=self.request.user)


# 댓글 조회 API
class CommentListAPIView(ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # 특정 게시글(post_id)에 달린 댓글만 반환
        post_id = self.kwargs.get('post_id')  # URL에서 post_id를 가져옴
        return Comment.objects.filter(post__id=post_id).order_by('created_at')


# 댓글 생성 API
class CommentCreateAPIView(CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 생성 가능

    def perform_create(self, serializer):
        # 댓글을 특정 게시글에 연결
        post_id = self.kwargs.get('post_id')  # URL에서 post_id를 가져옴
        post = Post.objects.get(id=post_id)
        serializer.save(post=post, author=self.request.user)


# 댓글 수정 API
class CommentUpdateAPIView(UpdateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 수정 가능

    def get_queryset(self):
        # 현재 사용자가 작성한 댓글만 수정 가능
        return Comment.objects.filter(author=self.request.user)


# 댓글 삭제 API
class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 삭제 가능

    def get_queryset(self):
        # 현재 사용자가 작성한 댓글만 삭제 가능
        return Comment.objects.filter(author=self.request.user)


# 좋아요를 추가하거나 제거할 수 있는 API
class PostLikeToggleAPIView(APIView):
    permission_classes = [IsAuthenticated]  # 로그인한 사용자만 접근 가능

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)  # 게시글 가져오기
        user = request.user

        if user in post.likes.all():
            # 좋아요 취소
            post.likes.remove(user)
            liked = False
        else:
            # 좋아요 추가
            post.likes.add(user)
            liked = True

        return Response({
            "liked": liked,
            "total_likes": post.total_likes()
        })


# 게시글 목록을 보여주는 뷰
class PostListView(ListView):
    model = Post  # 어떤 모델을 다룰지 지정
    template_name = "posts/post_list.html"  # 사용할 템플릿 파일 경로
    context_object_name = "posts"  # 템플릿에서 사용할 컨텍스트 이름
    ordering = ['-created_at']  # 게시글 정렬 순서 (최신순)


# 게시글 상세 보기 뷰
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        # 추가 컨텍스트 데이터를 템플릿에 전달
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()  # 댓글 작성 폼
        return context

    def post(self, request, *args, **kwargs):
        # 댓글 작성 요청을 처리
        self.object = self.get_object()  # 현재 게시글 객체
        form = CommentForm(request.POST)  # POST 요청에서 데이터 가져오기
        if form.is_valid():
            comment = form.save(commit=False)  # 데이터베이스에 저장하지 않고 객체 생성
            comment.post = self.object  # 댓글이 달린 게시글 설정
            comment.author = request.user  # 현재 유저를 댓글 작성자로 설정
            comment.save()  # 데이터베이스에 저장
            return redirect('posts:post_detail', pk=self.object.pk)  # 상세 페이지로 리다이렉트
        return self.get(request, *args, **kwargs)

# 게시글 작성 뷰
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Post 모델에 대한 폼
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:post_list')  # 성공 시 리다이렉트할 URL

    def form_valid(self, form):
        # 폼 검증이 성공하면 호출됨
        form.instance.author = self.request.user  # 현재 유저를 게시글 작성자로 설정
        return super().form_valid(form)

# 게시글 수정 뷰
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "posts/post_form.html"
    success_url = reverse_lazy('posts:post_list')

    def get_queryset(self):
        # 작성자 본인의 게시글만 수정 가능
        return Post.objects.filter(author=self.request.user)

# 게시글 삭제 뷰
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')

    def get_queryset(self):
        # 작성자 본인의 게시글만 삭제 가능
        return Post.objects.filter(author=self.request.user)

# 게시글 좋아요 토글 뷰
class PostLikeToggleView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # 게시글 객체 가져오기
        
        if not request.user.is_authenticated:
            # 로그인되지 않은 사용자는 로그인 페이지로 리다이렉트
            login_url = f"{reverse_lazy('accounts:login')}?next={reverse_lazy('posts:post_detail', kwargs={'pk': pk})}"
            return redirect(login_url)

        if request.user in post.likes.all():
            # 이미 좋아요를 누른 경우 취소
            post.likes.remove(request.user)
        else:
            # 좋아요 추가
            post.likes.add(request.user)
        
        return redirect('posts:post_detail', pk=pk)

# 댓글 수정 뷰
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "posts/post_detail.html"

    def get_context_data(self, **kwargs):
        # 댓글과 연관된 게시글 정보 추가
        context = super().get_context_data(**kwargs)
        context['post'] = self.object.post
        return context

    def form_valid(self, form):
        # 폼 검증이 성공하면 댓글 저장 후 게시글 상세 페이지로 리다이렉트
        self.object = form.save()
        return redirect('posts:post_detail', pk=self.object.post.pk)

    def get_queryset(self):
        # 본인의 댓글만 수정 가능
        return Comment.objects.filter(author=self.request.user)

# 댓글 삭제 뷰
class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment

    def get_queryset(self):
        # 본인의 댓글만 삭제 가능
        return Comment.objects.filter(author=self.request.user)

    def get_success_url(self):
        # 삭제 후 댓글이 달린 게시글로 리다이렉트
        post = self.object.post
        return reverse_lazy('posts:post_detail', kwargs={'pk': post.pk})
