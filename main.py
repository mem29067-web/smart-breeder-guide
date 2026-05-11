
import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="سوبر بريمكس", layout="centered")

# التصميم الاحترافي
st.markdown("""
    <style>
    .main { background-color: #1a1a1a; }
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                    url("https://r.jina.ai/i/058690f3-93ba-42f0-91a5-812328479901");
        background-size: cover;
    }
    h1 { color: #ffd700; text-align: center; font-size: 28px !important; }
    .stButton>button { 
        background-color: #2e7d32; color: white; border-radius: 10px; 
        height: 60px; font-size: 18px; width: 100%;
    }
    label { color: white !important; font-size: 16px !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🐂 دليل المربي الذكي")
st.write("<p style='text-align:center; color:white;'>مرحباً بك في النسخة الاحترافية</p>", unsafe_allow_html=True)

# الأزرار
col1, col2 = st.columns(2)
with col1:
    st.button("📈 البورصة")
    st.button("🚜 الماكينة")
with col2:
    st.button("🤖 المستشار")
    st.button("💰 الأرباح")

# الماكينة البسيطة
st.markdown("---")
st.subheader("🚜 تجربة ماكينة الخلط")
corn = st.number_input("الذرة (كيلو):", value=500)
alt = st.number_input("البدائل (كيلو):", value=200)
st.success(f"الإجمالي: {corn + alt} كيلو")
