import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="HR Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HR Employee Attrition Dashboard")
st.markdown("**HR Analytics | Employee Retention Insight**")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    df = pd.read_csv("../dataset/HR-Employee-Attrition.csv")

    drop_cols = ["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"]
    df.drop(columns=drop_cols, inplace=True)

    df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})
    return df

df = load_data()

# ===============================
# KPI SECTION
# ===============================
total_employee = len(df)
attrition_rate = df["Attrition"].mean() * 100
active_employee = total_employee - df["Attrition"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("👥 Total Employees", total_employee)
col2.metric("❌ Attrition Rate", f"{attrition_rate:.2f}%")
col3.metric("✅ Active Employees", active_employee)

st.divider()

# ===============================
# DISTRIBUTION
# ===============================
st.subheader("📌 Attrition Distribution")

fig, ax = plt.subplots(figsize=(5,4))
sns.countplot(x="Attrition", data=df, ax=ax)
ax.set_xticklabels(["No", "Yes"])
ax.set_xlabel("Attrition")
ax.set_ylabel("Employee Count")
st.pyplot(fig)

# ===============================
# FACTORS ANALYSIS
# ===============================
st.subheader("🔍 Key Risk Factors")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.boxplot(x="Attrition", y="Age", data=df, ax=ax)
    ax.set_title("Age vs Attrition")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.boxplot(x="Attrition", y="MonthlyIncome", data=df, ax=ax)
    ax.set_title("Monthly Income vs Attrition")
    st.pyplot(fig)

# ===============================
# SATISFACTION
# ===============================
st.subheader("😊 Job Satisfaction & Work-Life Balance")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    sns.countplot(x="JobSatisfaction", hue="Attrition", data=df, ax=ax)
    ax.set_title("Job Satisfaction")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    sns.countplot(x="WorkLifeBalance", hue="Attrition", data=df, ax=ax)
    ax.set_title("Work-Life Balance")
    st.pyplot(fig)

# ===============================
# HR INSIGHT
# ===============================
st.subheader("🧠 HR Insight Summary")

st.markdown("""
- Karyawan dengan **income rendah dan usia lebih muda** memiliki risiko attrition lebih tinggi  
- **Job satisfaction & work-life balance** berperan besar terhadap retensi  
- Attrition meningkat pada karyawan dengan **jarak rumah jauh**
- Faktor finansial & lingkungan kerja lebih dominan dibanding demografis
""")

