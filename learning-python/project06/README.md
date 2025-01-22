# 🛠️ Project06: Django 앱 개발

이 디렉토리는 Django를 활용하여 사용자 인증 및 게시글 관리 기능을 구현한 프로젝트들을 포함하고 있습니다. 세 개의 프로젝트 `project01`과 `project02`, `project03`으로 구성되어 있습니다.

---

## 📂 프로젝트 구조

```
project06/
├── project01/      # Django 기반 사용자 인증 및 게시글 관리 앱(FBV)
├── project02/      # Django 기반 사용자 인증 및 게시글 관리 앱(CBV)
├── project03/      # DRF 및 데이터베이스 마이그레이션을 포함한 확장 프로젝트
└── README.md       # 현재 파일
```

---

## 📁 프로젝트 설명

### 1️⃣ **project01**
- **설명**: 사용자 인증 및 게시글/댓글 CRUD 기능을 포함한 Django 프로젝트.
- **완료된 과제**:
  - 사용자 인증 (회원가입, 로그인, 로그아웃)
  - 사용자 프로필 보기
  - 게시글 CRUD (작성, 조회, 수정, 삭제)
  - 댓글 CRUD (작성, 수정, 삭제)
  - 게시글 좋아요 기능
  - FBV 형식
- **제외된 과제**:
  - DRF 변환
  - 데이터베이스 마이그레이션
- **기술 스택**:
  - Python, Django, SQLite3, HTML
- **디렉토리 구조**:

  ```
  project01/
  │
  ├── accounts/                  # 사용자 인증 앱
  │   ├── migrations/            # 데이터베이스 마이그레이션 파일
  │   ├── templates/accounts/    # 인증 관련 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── forms.py               # 사용자 폼
  │   ├── models.py              # 사용자 모델
  │   ├── tests.py               # 테스트 코드
  │   ├── urls.py                # URL 라우팅
  │   └── views.py               # 인증 관련 뷰
  │
  ├── posts/                     # 게시글 관리 앱
  │   ├── migrations/            # 데이터베이스 마이그레이션 파일
  │   ├── templates/posts/       # 게시글 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── forms.py               # 게시글 폼
  │   ├── models.py              # 게시글 모델
  │   ├── tests.py               # 테스트 코드
  │   ├── urls.py                # URL 라우팅
  │   └── views.py               # 게시글 관련 뷰
  │
  ├── core/                      # 프로젝트 기본 설정
  │   ├── templates/core/        # 기본 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── urls.py                # 메인 URL 설정
  │   └── views.py               # 기본 뷰
  │
  ├── templates/                 # 공통 템플릿
  │   └── base.html              # 기본 레이아웃
  ├── manage.py                  # Django 관리 명령어 스크립트
  └── requirements.txt           # 필요한 라이브러리
  ```

---

### 2️⃣ **project02**
- **설명**: 사용자 인증 및 게시글/댓글 CRUD 기능을 포함한 Django 프로젝트.
- **완료된 과제**:
  - 사용자 인증 (회원가입, 로그인, 로그아웃)
  - 사용자 프로필 보기
  - 게시글 CRUD (작성, 조회, 수정, 삭제)
  - 댓글 CRUD (작성, 수정, 삭제)
  - 게시글 좋아요 기능
  - CBV 형식
- **제외된 과제**:
  - DRF 변환
  - 데이터베이스 마이그레이션
- **기술 스택**:
  - Python, Django, SQLite3, HTML
- **디렉토리 구조** : `project01`과 동일

---

### 3️⃣ **project03**
- **설명**: DRF(Django Rest Framework)를 활용한 API 기반 Django 프로젝트 및 데이터베이스 확장.
- **추가 기능**:
  - DRF 변환 (APIView, Serializer 활용)
  - 데이터베이스 SQLite3에서 MySQL로 마이그레이션
- **기술 스택**:
  - Python, Django, Django Rest Framework, MySQL, HTML
- **디렉토리 구조** :

  ```
  project03/
  │
  ├── accounts/                  # 사용자 인증 앱
  │   ├── migrations/            # 데이터베이스 마이그레이션 파일
  │   ├── templates/accounts/    # 인증 관련 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── forms.py               # 사용자 폼
  │   ├── models.py              # 사용자 모델
  │   ├── serializers.py         # serializer
  │   ├── tests.py               # 테스트 코드
  │   ├── urls.py                # URL 라우팅
  │   └── views.py               # 인증 관련 뷰
  │
  ├── posts/                     # 게시글 관리 앱
  │   ├── migrations/            # 데이터베이스 마이그레이션 파일
  │   ├── templates/posts/       # 게시글 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── forms.py               # 게시글 폼
  │   ├── models.py              # 게시글 모델
  │   ├── serializers.py         # serializer
  │   ├── tests.py               # 테스트 코드
  │   ├── urls.py                # URL 라우팅
  │   └── views.py               # 게시글 관련 뷰
  │
  ├── core/                      # 프로젝트 기본 설정
  │   ├── templates/core/        # 기본 템플릿
  │   ├── admin.py               # 어드민 설정
  │   ├── apps.py                # 앱 설정
  │   ├── urls.py                # 메인 URL 설정
  │   └── views.py               # 기본 뷰
  │
  ├── templates/                 # 공통 템플릿
  │   └── base.html              # 기본 레이아웃
  ├── static/                    # 공통 static
  │   ├── css/
  │   ├── js/
  │   └── images/
  ├── manage.py                  # Django 관리 명령어 스크립트
  └── requirements.txt           # 필요한 라이브러리
  ```

---

## 📈 학습 목표

1. Django의 기본 구조(MTV 패턴)와 기능 활용.
2. DRF를 사용하여 RESTful API 설계 및 구현.
3. 데이터베이스 마이그레이션 및 확장(MySQL).
4. 사용자 인증, 게시글 및 댓글 CRUD 기능의 API 기반 구현.

---

## 🚀 진행 계획

- **1단계**: `project01`의 기능을 기반으로 `project02`를 CBV 형식으로 변환.
- **1단계**: `project02`의 기능을 기반으로 `project03`을 DRF로 변환.
- **2단계**: SQLite3에서 MySQL로 데이터베이스 마이그레이션.

---

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows에서는 venv\Scripts\activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 설정

**MySQL 서버 실행 및 설정 (project03 실행)**
1. MySQL 서버 실행:

   ```bash
   mysqld --console
   ```

2. MySQL 접속:

   ```bash
   mysql -u root -p
   ```

3. 데이터베이스 및 사용자 생성:

   ```sql
   CREATE DATABASE <DB_name> CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'user_password';
   GRANT ALL PRIVILEGES ON <DB_name>.* TO 'user_name'@'localhost';
   FLUSH PRIVILEGES;
   ```

4. 데이터베이스 접속 확인:

   ```bash
   mysql -u user_name -p
   USE <DB_name>;
   ```

5. 프로젝트 루트 경로 `.env` 파일 생성 및 작성:

   ```
   DB_NAME=<DB_name>
   DB_USER=user_name
   DB_PASSWORD=user_password
   DB_HOST=127.0.0.1
   DB_PORT=3306
   ```

#### **공통 데이터베이스 설정**

```bash
python manage.py makemigrations
python manage.py migrate
```


### 4. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 5. 개발 서버 실행

```bash
python manage.py runserver
```

브라우저에서 다음 주소를 방문하세요:
- 메인 페이지: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- 관리자 페이지: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


---


## 📜 라이센스

이 프로젝트는 학습 목적으로 작성되었습니다. 코드 및 아이디어는 개인 학습 및 비상업적 목적으로 자유롭게 사용할 수 있습니다.
