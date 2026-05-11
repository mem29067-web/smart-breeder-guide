import streamlit as st

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="دليل المربي الذكي Pro", layout="wide")

# 2. تنسيق الألوان الملكي (الأخضر العشبي + الخلفية الكريمي الهادئة)
st.markdown("""
    <style>
    /* خلفية البرنامج الهادئة */
    .stApp {
        background-color: #f5f2e9 !important;
    }
    
    /* الهيدر العلوي */
    .header-box {
        background-color: #448b5a;
        padding: 25px;
        border-radius: 0 0 25px 25px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* وضوح مربعات الإدخال - خط أسود عريض */
    .stNumberInput div div input {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 22px !important;
        border: 2px solid #448b5a !important;
        border-radius: 10px !important;
    }
    
    /* عناوين الخانات باللون الأخضر الغامق */
    label {
        color: #2d5a3c !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }
    
    /* تصميم التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #e8e4d8;
        border-radius: 12px;
        padding: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        color: #448b5a !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }
    
    /* تنسيق كروت النتائج */
    .stMetric {
        background-color: #ffffff;
        border-right: 8px solid #448b5a;
        border-radius: 12px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. واجهة البرنامج
st.markdown('<div class="header-box"><h1 style="color:white; margin:0; font-size:32px;">🚜 دليل المربي الذكي</h1><p style="color:white; margin:0; opacity:0.9;">سوبر بريمكس - رفيقك في العنبر والسوق</p></div>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["📊 بورصة اليوم", "🧪 ماكينة العلف", "💰 الأرباح"])

with tab1:
    st.subheader("💹 أسعار الخامات الاسترشادية")
    c1, c2, c3 = st.columns(3)
    c1.metric("الذرة الصفراء", "13,500 ج")
    c2.metric("كسب صويا 44%", "24,000 ج")
    c3.metric("نخالة (ردة)", "11,500 ج")
    st.write("---")
    st.info("💡 هذه الأسعار للمتابعة فقط، والسوق متغير.")

with tab2:
    st.subheader("🧪 مختبر خلطة الطن الواحد")
    col1, col2 = st.columns(2)
    with col1:
        corn = st.number_input("الذرة (كيلو):", value=500, step=25)
        soya = st.number_input("الصويا (كيلو):", value=200, step=10)
        bran = st.number_input("الردة (كيلو):", value=150, step=10)
    with col2:
        alt = st.number_input("البدائل (بسكويت/بلح):", value=120, step=10)
        premix = st.number_input("إضافات (سوبر بريمكس):", value=30, step=1)
    
    total = corn + soya + bran + alt + premix
    
    st.markdown(f"<div style='background-color:#ffffff; padding:15px; border-radius:10px; border:2px dashed #448b5a; text-align:center;'><h3>إجمالي الوزن: {total} كيلو</h3></div>", unsafe_allow_html=True)
    
    if total == 1000:
        st.success("🎯 مبروك! الخلطة موزونة (1000 كيلو)")
    elif total > 1000:
        st.error(f"⚠️ الوزن زائد بمقدار {total - 1000} كيلو")
    else:
        st.warning(f"⏳ باقي {1000 - total} كيلو لتقفيل الطن")

with tab3:
    st.subheader("💰 حاسبة الربح السريع")
    b1, b2 = st.columns(2)
    buy = b1.number_input("سعر شراء العجل:", value=45000, step=500)
    sell = b2.number_input("سعر البيع المتوقع:", value=85000, step=500)
    
    profit = (sell - buy) * 10
    st.markdown(f"<div style='background-color:#448b5a; padding:20px; border-radius:15px; color:white; text-align:center;'><h2>صافي الربح المتوقع (10 رؤوس):<br>{profit:,.0f} جنيه</h2></div>", unsafe_allow_html=True)

# 4. التذييل القانوني
st.markdown("---")
st.caption("إخلاء مسؤولية: هذا التطبيق أداة حسابية مساعدة. القرارات الفنية والمالية تقع على عاتق المستخدم.")
