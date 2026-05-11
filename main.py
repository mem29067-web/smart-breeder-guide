import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Smart Breeder Pro", layout="centered")

# 2. تصميم "الأبيض النظيف" (Clean White Design)
st.markdown("""
    <style>
    /* خلفية بيضاء ناصعة */
    .stApp {
        background-color: #ffffff !important;
    }
    
    /* هيدر بسيط وأنيق */
    .header {
        text-align: center;
        padding: 10px;
        border-bottom: 3px solid #2ecc71;
        margin-bottom: 30px;
    }
    
    /* مربعات إدخال واضحة جداً بحدود خضراء */
    .stNumberInput div div input {
        background-color: #f9f9f9 !important;
        color: #1a1a1a !important;
        font-weight: bold !important;
        font-size: 24px !important;
        border: 2px solid #2ecc71 !important;
        border-radius: 8px !important;
    }
    
    /* العناوين بلون رمادي غامق احترافي */
    label {
        color: #333333 !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }

    /* أزرار التبويبات */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #f0f0f0;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="header"><h1>🚜 دليل المربي الذكي</h1></div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["💰 حساب الأرباح", "🧪 ماكينة العلف"])

with tab1:
    st.subheader("💰 حاسبة الدورة")
    buy = st.number_input("سعر الشراء:", value=45000)
    sell = st.number_input("سعر البيع:", value=85000)
    st.success(f"الربح لـ 10 رؤوس: {(sell-buy)*10:,.0f} جنيه")

with tab2:
    st.subheader("🧪 خلطة الطن")
    corn = st.number_input("الذرة:", value=500)
    alt = st.number_input("البدائل:", value=200)
    st.info(f"الإجمالي: {corn + alt} كيلو")
