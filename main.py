import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="دليل المربي الذكي", layout="wide")

# 2. تصميم الواجهة بالثور الأسود والخطوط الواضحة
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url("https://r.jina.ai/i/058690f3-93ba-42f0-91a5-812328479901");
        background-size: cover; background-position: center; background-attachment: fixed;
    }
    .main-title { text-align: center; color: white; font-size: 35px; font-weight: bold; text-shadow: 2px 2px 4px #000; padding: 20px; }
    .stTabs [data-baseweb="tab-list"] { background-color: rgba(255,255,255,0.1); border-radius: 10px; }
    .stTabs [data-baseweb="tab"] { color: white !important; font-weight: bold; font-size: 18px; }
    label { color: white !important; font-weight: bold; font-size: 18px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">🐂 دليل المربي الذكي - سوبر بريمكس</p>', unsafe_allow_html=True)

# 3. الأقسام (التبويبات)
tab1, tab2, tab3 = st.tabs(["🏠 الرئيسية", "🚜 ماكينة العلف", "💰 حاسبة الأرباح"])

with tab1:
    st.markdown('<div style="background-color:rgba(0,0,0,0.5); padding:20px; border-radius:15px; color:white; text-align:center;">', unsafe_allow_html=True)
    st.write("### أهلاً بك يا هندسة في تطبيقك الخاص")
    st.write("تم تحديث: **بورصة الخامات والبدائل** ✅")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.subheader("🚜 تركيبات العلف والبدائل الموفرة")
    corn_qty = st.number_input("كمية الذرة (كيلو):", value=500)
    alt_qty = st.number_input("كمية البديل (بلح/بسكويت) كيلو:", value=150)
    soya_qty = st.number_input("كمية الصويا (كيلو):", value=200)
    premix_qty = st.number_input("البريمكس والإضافات (كيلو):", value=30)
    
    total = corn_qty + alt_qty + soya_qty + premix_qty
    st.metric("إجمالي وزن الخلطة:", f"{total} كيلو")
    if total == 1000: st.success("✅ الخلطة كملت طن!")

with tab3:
    st.subheader("💰 حسابات دورة الـ 10 عجول")
    st.write("سيتم ربطها بأسعار البورصة قريباً.")
