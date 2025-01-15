from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import PostForm, CommentForm
from .models import Post, Comment


@require_http_methods(["GET"])
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})


@require_http_methods(["GET", "POST"])
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all().order_by('-created_at')  # 댓글 최신순 정렬

    if request.method == 'POST':  # 댓글 작성 요청
        if not request.user.is_authenticated:
            return redirect('accounts:login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # 데이터베이스 저장 전 인스턴스 생성
            comment.post = post  # 댓글과 게시글 연결
            comment.author = request.user.username  # 현재 사용자 설정
            comment.save()  # 데이터베이스에 저장
            return redirect('posts:post_detail', post_id=post.id)
    else:
        form = CommentForm()  # 빈 폼 생성

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})


@login_required
@require_http_methods(["GET", "POST"])
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # 데이터베이스에 저장하지 않고 인스턴스만 생성
            post.author = request.user.username  # 작성자를 현재 로그인 사용자로 설정
            post.save()  # 데이터베이스에 저장
            return redirect('posts:post_list')  # 게시글 목록으로 리다이렉트
    else:
        form = PostForm()

    return render(request, 'posts/post_create.html', {'form': form})


@login_required
@require_http_methods(["GET", "POST"])
def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 작성자만 수정할 수 있도록 권한 확인
    if request.user.username != post.author:
        return redirect('posts:post_list')  # 권한 없으면 목록 페이지로 리다이렉트

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # 기존 데이터를 기반으로 폼 생성
        if form.is_valid():
            form.save()  # 변경사항 저장
            return redirect('posts:post_detail', post_id=post.id)  # 상세 페이지로 리다이렉트
    else:
        form = PostForm(instance=post)  # 기존 데이터를 폼에 채워줌

    return render(request, 'posts/post_update.html', {'form': form})


@login_required
@require_http_methods(["GET", "POST"])
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 작성자만 삭제할 수 있도록 권한 확인
    if request.user.username != post.author:
        return redirect('posts:post_list')  # 권한 없으면 목록 페이지로 리다이렉트

    if request.method == 'POST':  # 삭제 확인 후 처리
        post.delete()
        return redirect('posts:post_list')  # 삭제 후 게시글 목록으로 리다이렉트

    return render(request, 'posts/post_delete.html', {'post': post})


@login_required
@require_http_methods(["POST"])
def post_like_toggle(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # 좋아요 취소
    else:
        post.likes.add(request.user)  # 좋아요 추가

    return redirect('posts:post_detail', post_id=post.id)


@login_required
@require_http_methods(["GET", "POST"])
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # 작성자만 수정 가능
    if request.user.username != comment.author:
        return redirect('posts:post_detail', post_id=comment.post.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # 기존 댓글 데이터로 폼 생성
        if form.is_valid():
            form.save()  # 데이터베이스에 저장
            return redirect('posts:post_detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)  # 기존 데이터를 폼에 채워서 렌더링

    return render(request, 'posts/comment_update.html', {'form': form, 'comment': comment})


@login_required
@require_http_methods(["GET", "POST"])
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # 작성자만 삭제 가능
    if request.user.username != comment.author:
        return redirect('posts:post_detail', post_id=comment.post.id)

    if request.method == 'POST':  # 삭제 확인 후 처리
        post_id = comment.post.id  # 삭제 전 연결된 게시글 ID 저장
        comment.delete()
        return redirect('posts:post_detail', post_id=post_id)

    return render(request, 'posts/comment_delete.html', {'comment': comment})
