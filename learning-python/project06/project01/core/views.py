from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')  # 프로젝트 수준의 템플릿
