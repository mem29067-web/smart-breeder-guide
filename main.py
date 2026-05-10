import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="دليل المربي الذكي", layout="wide")

# 2. تصميم الواجهة (صورة الثور والخلفية)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)), 
                    url("https://r.jina.ai/i/60835f8f5e7a4b8b9b8b9b8b9b8b9b8b");
        background-size: cover;
    }
    .stButton>button {
        width: 100%; height: 80px; font-size: 22px !important; font-weight: bold;
        border-radius: 15px; background-color: #1e5631; color: white;
        margin-bottom: 12px; border: 2px solid #ffd700;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🐂 دليل المربي الذكي - سوبر بريمكس")
st.info("مرحباً بك في النسخة الاحترافية لمشروعك")

# 3. الأزرار الرئيسية
col1, col2 = st.columns(2)
with col1:
    st.button("📈 بورصة الخامات والبدائل")
    st.button("🚜 ماكينة خلط العلف")
with col2:
    st.button("🤖 مستشار التسمين الذكي")
    st.button("💰 حاسبة أرباح الدورة")

# 4. زر واتساب للتواصل (تقدر تغير الرقم لرقمك)
st.markdown('<a href="https://wa.me/201000000000" target="_blank" style="text-decoration:none;"><div style="background-color:#25d366;color:white;padding:15px;text-align:center;border-radius:10px;font-size:20px;">💬 تواصل مع الدعم الفني (واتساب)</div></a>', unsafe_allow_html=True)
