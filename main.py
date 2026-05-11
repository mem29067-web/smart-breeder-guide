import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Smart Breeder Luxury", layout="wide")

# 2. تصميم الفخامة (التدرج الأخضر الميتاليك + تأثير القزاز الشفاف)
st.markdown("""
    <style>
    /* خلفية بتدرج أخضر ميتاليك فخم */
    .stApp {
        background: linear-gradient(135deg, #0d2315 0%, #1e5631 100%) !important;
    }
    
    /* تصميم الهيدر - خط عريض مع ظل */
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 40px !important;
        font-weight: 800;
        text-shadow: 2px 4px 8px rgba(0,0,0,0.5);
        padding: 20px;
    }

    /* تأثير القزاز الشفاف للمربعات (Glassmorphism) */
    div[data-testid="stMetric"], .stNumberInput, .stTabs {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px !important;
        padding: 15px;
    }

    /* وضوح الأرقام جوه المربعات (أبيض ناصع) */
    input {
        color: #ffffff !important;
        font-size: 24px !important;
        font-weight: bold !important;
        text-align: center;
    }
    
    /* ألوان التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: transparent !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-size: 20px;
        font-weight: bold;
    }
    
    /* تغيير لون الكتابة التوضيحية للأبيض */
    label, p, h1, h2, h3 {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة البرنامج الفخمة
st.markdown('<h1 class="main-title">🚜 مستشار التسمين الذكي PRO</h1>', unsafe_allow_html=True)

tabs = st.tabs(["💎 البورصة", "⚙️ ماكينة الخلط", "💵 الأرباح"])

with tabs[0]:
    st.subheader("💹 أسعار الخامات العالمية")
    c1, c2, c3 = st.columns(3)
    c1.metric("ذرة صفراء", "13,500 ج")
    c2.metric("صويا 44%", "24,000 ج")
    c3.metric("ردة خشنة", "11,200 ج")

with tabs[1]:
    st.subheader("⚙️ هندسة الخلطة الموفرة")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("الذرة (كجم):", value=500)
        st.number_input("الصويا (كجم):", value=200)
    with col2:
        st.number_input("البدائل (كجم):", value=150)
        st.number_input("سوبر بريمكس (كجم):", value=30)
    
    st.markdown('<div style="text-align:center; padding:10px; border:2px solid #2ecc71; border-radius:15px;">✅ الخلطة جاهزة للتنفيذ</div>', unsafe_allow_html=True)

with tabs[2]:
    st.subheader("💵 تحليل صافي الأرباح")
    st.markdown("""
        <div style="background: rgba(46, 204, 113, 0.2); padding:30px; border-radius:20px; text-align:center; border: 1px solid #2ecc71;">
            <h2 style="margin:0;">صافي الربح التقديري</h2>
            <h1 style="color:#2ecc71 !important; font-size:50px !important;">85,000 ج.م</h1>
            <p>لدورة تسمين 10 رؤوس</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.6;'>جميع الحقوق محفوظة - سوبر بريمكس 2026</p>", unsafe_allow_html=True)
