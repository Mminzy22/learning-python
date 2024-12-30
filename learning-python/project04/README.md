# 데이터 분석 및 모델링 과제

---

## 📋 과제 목표

주어진 데이터를 탐색하고 전처리한 후 다양한 회귀 모델을 비교하여 최적의 모델을 선택하고, 모델 성능을 시각적으로 표현하는 것입니다.

## ⚙️ 과제 구성 및 주요 기능

### 데이터 파일

- `housingdata.csv`: 주택 관련 데이터로, 각 컬럼은 다양한 주택 특성과 관련된 정보를 포함합니다.

### 주요 기능

1. **데이터셋 탐색 및 전처리**

   - 결측치 처리
   - 이상치 탐지 및 제거
   - 특징 선택

2. **여러 회귀 모델 비교**

   - 선형 회귀
   - 의사결정나무
   - 랜덤 포레스트

3. **모델 성능 평가**

   - Mean Absolute Error (MAE)
   - Mean Squared Error (MSE)
   - R² Score

4. **결과 분석**

   - 각 모델의 성능 비교 및 최적 모델 선택
   - matplotlib 및 seaborn을 사용한 성능 지표 시각화

### 도전 과제 (선택 사항)

- **모델 앙상블**: 배깅, 부스팅 등 앙상블 기법 적용
- **하이퍼파라미터 튜닝**: Grid Search 또는 Random Search 사용
- **시간적 요소 추가**: 시간적 데이터를 추가하여 예측력 개선

## 💻 실행 예제

### 기본 데이터 출력

```bash
# housingdata.csv 파일 로드 후, 데이터의 기본 정보를 확인합니다.
# 예시 코드:
print(data.info())
```

### 최종 데이터 출력 예시

```bash
# 최적의 모델로 예측한 결과를 출력합니다.
# 예시 코드:
print(predictions)
```

## 📦 설치 및 실행 방법

1. **필수 라이브러리 설치**
   ```bash
   pip install -r requirements.txt
   ```
2. **프로젝트 실행**
   ```bash
   python project04.py
   ```

## 🛠️ 주요 기술

- Python
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
