import streamlit as st

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="بورصة المربي الذكي Pro", layout="wide")

# 2. تصميم "الفخامة العالمية" (مزيج من روح ميست والبورصات العالمية)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 38px !important;
        font-weight: 900;
        text-shadow: 0px 4px 10px rgba(0,0,0,0.7);
        padding: 20px;
        letter-spacing: 1px;
    }
    /* تأثير القزاز الشفاف المطور */
    div[data-testid="stMetric"], .stNumberInput, .stTabs, .market-box {
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px !important;
        padding: 20px;
        margin-bottom: 15px;
        transition: 0.3s;
    }
    /* توضيح أرقام البورصة */
    [data-testid="stMetricValue"] {
        color: #2ecc71 !important;
        font-size: 28px !important;
        font-weight: bold !important;
    }
    input {
        color: #ffffff !important;
        font-size: 24px !important;
        font-weight: bold !important;
    }
    label, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📈 بورصة دليل المربي الذكي</h1>', unsafe_allow_html=True)

# 3. الأقسام (البورصة العالمية والمحلية)
tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "⚙️ ماكينة الخلط", "💵 دراسة الأرباح"])

with tab1:
    # تقسيم البورصة لجزئين (الخامات - العملات والمعادن)
    sub1, sub2 = st.tabs(["🌾 أسعار الخامات (ميست)", "🌍 المؤشرات العالمية"])
    
    with sub1:
        st.subheader("سوق الخامات (تحديث يومي)")
        c1, c2, c3 = st.columns(3)
        c1.metric("ذرة أرجنتيني", "13,800 ج", "+100")
        c2.metric("صويا 44% (محلي)", "24,500 ج", "-200")
        c3.metric("نخالة خشنة", "11,500 ج", "0")
        
        c4, c5, c6 = st.columns(3)
        c4.metric("گلوتين مستورد", "42,000 ج")
        c5.metric("دي دي جي (DDGS)", "18,200 ج")
        c6.metric("زيت صويا خام", "54,000 ج")

    with sub2:
        st.subheader("العملات والمعادن الثمينة")
        col_gold, col_cash = st.columns(2)
        
        with col_gold:
            st.markdown("### 🏆 المعادن")
            st.metric("ذهب عيار 24", "3,850 ج")
            st.metric("ذهب عيار 21", "3,370 ج")
            st.metric("الفضة (أوقية)", "1,520 ج")
            
        with col_cash:
            st.markdown("### 💵 العملات")
            st.metric("الدولار (بنك)", "48.30 ج")
            st.metric("الدولار (موازي)", "??.?? ج")
            st.metric("اليورو", "52.10 ج")

with tab2:
    st.subheader("⚙️ خلاط الأعلاف الذكي")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("الذرة (كجم):", value=500)
        st.number_input("الصويا (كجم):", value=200)
    with col2:
        st.number_input("إضافات (سوبر بريمكس):", value=30)
        st.number_input("البدائل:", value=150)

with tab3:
    st.subheader("💵 تحليل مالي للدورة")
    st.markdown("""
        <div style="background: rgba(46, 204, 113, 0.15); padding:30px; border-radius:25px; text-align:center; border: 2px solid #2ecc71;">
            <h2 style="margin:0; opacity:0.8;">الربح الصافي المتوقع</h2>
            <h1 style="color:#2ecc71 !important; font-size:55px !important; margin:10px 0;">85,000 ج.م</h1>
            <p style="font-size:18px;">لدورة 10 رؤوس - بناءً على أسعار السوق الحالية</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.5;'>إحصائيات بورصة ميست والبورصة العالمية - سوبر بريمكس 2026</p>", unsafe_allow_html=True)
