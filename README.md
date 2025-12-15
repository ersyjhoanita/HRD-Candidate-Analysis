# 📊 HRD Candidate Analysis – Employee Attrition

## 📌 Project Overview
Project ini bertujuan untuk menganalisis dan memprediksi **employee attrition ( pengurangan dan kinerja karyawan )**
menggunakan data HR Analytics. Analisis dilakukan untuk membantu tim HR
mengidentifikasi faktor risiko, meningkatkan retensi karyawan, dan mendukung
pengambilan keputusan berbasis data.

Project ini dibuat sebagai latihan untuk ditambahkan **portofolio Data Analyst / HR Analytics Intern**.

## 🎯 Objectives
- Mengidentifikasi faktor utama yang memengaruhi attrition
- Menyediakan insight strategis untuk HR
- Membangun model prediksi attrition yang interpretable
- Menyajikan hasil analisis dalam bentuk visual & dashboard

## 🗂 Dataset
- Sumber: IBM HR Analytics Employee Attrition Dataset
  ( https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset )
- Target: `Attrition` (Yes / No)
- Fitur: Demografi, kepuasan kerja, kompensasi, karier, dan lingkungan kerja
  
## 🔧 Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Streamlit 

## 🧪 Project Workflow

### 1️⃣ Data Cleaning & Preprocessing
Notebook: `notebook/01_data_cleaning.ipynb`
- Drop kolom tidak informatif
- Encode target variable
- One-Hot Encoding fitur kategorikal
- Feature scaling
- Dataset siap digunakan untuk EDA & modeling

### 2️⃣ Exploratory Data Analysis (EDA)
Notebook: `notebook/02_eda_visualization.ipynb`
- Distribusi attrition
- Analisis usia & pendapatan
- Kepuasan kerja & work-life balance
- Jarak rumah ke kantor
- Lama bekerja & promosi
- Correlation heatmap
- Insight HR yang actionable

### 3️⃣ Machine Learning Modeling
Notebook: `notebook/03_modeling_ml.ipynb`
Model:
- Logistic Regression
- Decision Tree
- Random Forest

Evaluasi:
- Accuracy
- Confusion Matrix
- Classification Report
- Feature Importance

### 4️⃣ Dashboard Interaktif 
- Visualisasi risiko attrition
- Faktor utama attrition
- Insight ringkas untuk HR

  
link dashboard
network url: http://192.168.0.107:8501
Local URL: http://localhost:8501 


## 📈 Key Insights
- Lembur berlebihan (OverTime) meningkatkan risiko attrition
- Kepuasan kerja dan work-life balance berpengaruh signifikan
- Kompensasi rendah dan stagnasi karier memicu turnover
- Hubungan dengan atasan meningkatkan retensi karyawan

## 🎯 Business Recommendation
- Mengurangi lembur berlebihan
- Meningkatkan employee engagement
- Menyediakan career path yang jelas
- Menerapkan kebijakan kerja fleksibel
