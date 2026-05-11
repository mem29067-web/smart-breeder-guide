import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Smart Breeder Luxury", layout="wide")

# 2. تصميم الفخامة (التدرج الميتاليك وتنسيق الأعمدة)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d2315 0%, #1e5631 100%) !important;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 35px !important;
        font-weight: 800;
        text-shadow: 2px 4px 8px rgba(0,0,0,0.5);
        padding: 15px;
    }
    /* تأثير القزاز الشفاف للمربعات */
    div[data-testid="stMetric"], .stNumberInput, .stTabs, .market-card {
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px !important;
        padding: 15px;
        margin-bottom: 10px;
    }
    input {
        color: #ffffff !important;
        font-size: 22px !important;
        font-weight: bold !important;
    }
    label, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-size: 18px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 مستشار التسمين والبورصة العالمية</h1>', unsafe_allow_html=True)

# 3. الأقسام الرئيسية
tab1, tab2, tab3 = st.tabs(["💎 البورصة العالمية", "⚙️ ماكينة الخلط", "💵 الأرباح"])

with tab1:
    # تقسيم البورصة لجزئين
    sub_tab1, sub_tab2 = st.tabs(["🌾 بورصة الخامات", "🌍 العملات والمعادن"])
    
    with sub_tab1:
        st.subheader("أسعار الخامات المحلية")
        c1, c2, c3 = st.columns(3)
        c1.metric("ذرة صفراء", "13,500 ج", "-100")
        c2.metric("كسب صويا 44%", "24,000 ج", "+300")
        c3.metric("ردة خشنة", "11,200 ج", "0")

    with sub_tab2:
        st.subheader("المؤشرات العالمية (لحظة بلحظة)")
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("### 💵 العملات")
            st.metric("الدولار الأمريكي", "48.50 ج")
            st.metric("اليورو الأوروبي", "52.30 ج")
            
        with col_b:
            st.markdown("### 🏆 المعادن")
            st.metric("الذهب (عيار 24)", "3,650 ج")
            st.metric("الفضة (أوقية)", "1,450 ج")

with tab2:
    st.subheader("⚙️ هندسة الخلطة الموفرة")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("الذرة (كجم):", value=500)
        st.number_input("الصويا (كجم):", value=200)
    with col2:
        st.number_input("البدائل (بسكويت/بلح):", value=150)
        st.number_input("سوبر بريمكس (كجم):", value=30)

with tab3:
    st.subheader("💵 تحليل الأرباح")
    st.markdown("""
        <div style="background: rgba(46, 204, 113, 0.2); padding:20px; border-radius:20px; text-align:center; border: 1px solid #2ecc71;">
            <h2 style="margin:0;">صافي الربح التقديري (10 رؤوس)</h2>
            <h1 style="color:#2ecc71 !important; font-size:45px !important;">85,000 ج.م</h1>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.6;'>تم التصميم بمعايير عالمية - سوبر بريمكس 2026</p>", unsafe_allow_html=True)
