import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="مستشار التسمين الذكي", layout="wide")

# 2. هندسة الألوان (نفس درجات الصورة: أخضر غامق + كريمي + أصفر تحذيري)
st.markdown("""
    <style>
    /* الخلفية الكريمي الفاتحة جداً */
    .stApp {
        background-color: #fdfaf1 !important;
    }
    
    /* الهيدر الأخضر الكبير بنفس درجة الصورة */
    .main-header {
        background-color: #388e3c;
        color: white;
        padding: 30px;
        text-align: center;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }
    
    /* تصميم الخانات (المربعات البيضاء بحدود خضراء) */
    .stNumberInput div div input {
        background-color: #ffffff !important;
        color: #1b5e20 !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border: 2px solid #388e3c !important;
        border-radius: 12px !important;
    }
    
    /* العناوين الجانبية (Label) */
    label {
        color: #2e7d32 !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }

    /* الكروت (الجداول المصغرة) */
    .stMetric {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 2px 4px 10px rgba(0,0,0,0.05);
    }
    
    /* التبويبات (Tabs) بشكل احترافي */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #e8f5e9;
        border-radius: 15px;
        padding: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #388e3c !important;
        font-weight: bold !important;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. محتوى الصفحة
st.markdown('<div class="main-header"><h1>🐄 مستشار التسمين الذكي</h1><p>صمم خلطتك — احسب تكلفتك — ضاعف أرباحك</p></div>', unsafe_allow_html=True)

tabs = st.tabs(["📋 مكتبة الخامات", "🚜 خلاط العلف", "💰 الأرباح"])

with tabs[0]:
    st.subheader("📊 بورصة الخامات")
    c1, c2, c3 = st.columns(3)
    c1.metric("ذرة صفراء", "13,500")
    c2.metric("صويا 44%", "24,000")
    c3.metric("ردة خشنة", "11,200")

with tabs[1]:
    st.subheader("🚜 خلطة الطن النموذجية")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("كمية الذرة (كجم):", value=500)
        st.number_input("كمية الصويا (كجم):", value=200)
    with col2:
        st.number_input("كمية البدائل (كجم):", value=150)
        st.number_input("البريمكس (كجم):", value=30)
    
    st.success("✅ تم تحديث بيانات الخلطة تلقائياً")

with tabs[2]:
    st.markdown('<div style="background-color:#fff9c4; padding:20px; border-radius:15px; border-right:10px solid #fbc02d;">', unsafe_allow_html=True)
    st.subheader("💰 حساب الأرباح المتوقعة")
    st.write("إجمالي الربح الصافي لـ 10 رؤوس: **85,000 ج.م**")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("دليل المربي الذكي - نسخة المحترفين 2026")
