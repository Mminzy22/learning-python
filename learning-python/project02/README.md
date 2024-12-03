# 클래스와 함수 활용 과제 🧑‍💻

이 프로젝트는 Python의 클래스(Class)와 함수(Function)를 활용하여 간단한 데이터 입력 및 출력 프로그램을 구현하는 것입니다. 객체 지향 프로그래밍의 기본 개념을 연습하기에 적합합니다.

---

## 📋 과제 목표
1. Python의 **클래스와 객체 지향 프로그래밍** 개념 학습.
2. **사용자 입력 처리**와 **출력 포맷팅** 연습.
3. (선택) Pandas를 활용한 데이터 처리 연습.

---

## ⚙️ 기능 설명

### 기본 기능
1. **클래스 정의**:
   - `Person` 클래스는 사용자 정보를 저장하고 관리하는 데 사용됩니다.
2. **멤버 변수**:
   - `name`: 사용자 이름 (문자열).
   - `gender`: 사용자 성별 (문자열, "male" 또는 "female").
   - `age`: 사용자 나이 (정수).
3. **생성자 `__init__`**:
   - 객체 생성 시 `name`, `gender`, `age`를 초기화합니다.
4. **정보 출력 함수 `display()`**:
   - 입력된 정보를 출력합니다.
   - 출력 예시:
     ```plaintext
     이름: 페이커, 성별: male
     나이: 28
     ```

### 추가 도전 과제
1. **CSV 파일 읽기**:
   - Pandas를 사용하여 인구 데이터 파일(`pop_kor.csv`)을 읽고 출력합니다.
   - DataFrame의 인덱스를 `구별`로 설정합니다.
2. **DataFrame 병합**:
   - 주어진 DataFrame과 읽어온 데이터를 `join`을 사용해 병합합니다.
3. **정렬**:
   - 병합된 DataFrame에서 `검거율`을 기준으로 오름차순 정렬 후 출력합니다.

---

## 💻 실행 예제

### 기본 기능
```plaintext
나이: 28
이름: 페이커
성별: male
이름: 페이커, 성별: male
나이: 28
```

### 추가 도전 과제 (선택)
1. **CSV 파일 읽기**:
   ```python
   import pandas as pd
   df = pd.read_csv('pop_kor.csv', index_col='구별')
   print(df)
   ```

2. **병합 및 정렬**:
   ```python
   merged_df = quiz_df.join(df)
   sorted_df = merged_df.sort_values(by='검거율', ascending=True)
   print(sorted_df)
   ```

---

## 📦 설치 및 실행 방법

1. **필수 환경 준비**:
   - Python 3.7 이상과 Jupyter Notebook 설치.
   - Pandas 라이브러리 설치:
     ```bash
     pip install pandas
     ```

2. **파일 실행**:
   - 프로젝트 파일 `project02.ipynb`을 실행합니다.
     ```bash
     jupyter notebook project02.ipynb
     ```

3. **Jupyter Notebook에서 실행**:
   - 셀을 실행하여 프로그램을 진행합니다.

---

## 🛠️ 주요 기술

- **클래스와 객체 지향 프로그래밍**:
  - Python의 클래스 정의, 생성자 활용, 멤버 함수 구현.
- **Pandas를 사용한 데이터 처리** (선택):
  - CSV 파일 읽기, DataFrame 병합, 정렬.

