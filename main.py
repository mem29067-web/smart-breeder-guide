import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="دليل المربي الذكي Pro", layout="wide")

# 2. تصميم احترافي بتباين عالي (High Contrast) لسهولة القراءة
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    /* تعديل المربعات لتكون واضحة جداً */
    .stNumberInput div div input {
        background-color: #ffffff !important;
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 20px !important;
        border: 2px solid #1e5631 !important;
    }
    /* تعديل العناوين فوق المربعات */
    label {
        color: #1e5631 !important;
        font-weight: bold !important;
        font-size: 18px !important;
    }
    .stMetric {
        background-color: #ffffff;
        border: 2px solid #1e5631;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #e0e0e0;
        border-radius: 5px 5px 0 0;
        padding: 10px 20px;
        color: #1e5631 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.title("🚜 دليل المربي الذكي - سوبر بريمكس")

# 4. الأقسام
tab1, tab2, tab3 = st.tabs(["📊 بورصة السوق", "🧪 ماكينة الخلط", "💰 حساب الأرباح"])

with tab1:
    st.subheader("💹 أسعار الخامات اليوم")
    c1, c2, c3 = st.columns(3)
    c1.metric("الذرة الصفراء", "13,500 ج")
    c2.metric("كسب صويا 44%", "24,000 ج")
    c3.metric("نخالة (ردة)", "11,500 ج")
    st.write("---")
    st.caption("ملاحظة: الأسعار استرشادية وتختلف حسب المنطقة والمورد.")

with tab2:
    st.subheader("🧪 تركيب الخلطة الحالية")
    col1, col2 = st.columns(2)
    with col1:
        corn = st.number_input("الذرة (كيلو):", value=500, step=25)
        soya = st.number_input("الصويا (كيلو):", value=200, step=10)
        bran = st.number_input("الردة (كيلو):", value=150, step=10)
    with col2:
        alt = st.number_input("البدائل (بسكويت/بلح):", value=120, step=10)
        premix = st.number_input("إضافات (سوبر بريمكس):", value=30, step=1)
    
    total = corn + soya + bran + alt + premix
    st.write(f"### الإجمالي الحالي: {total} كيلو")
    
    if total == 1000:
        st.success("✅ الوزن مضبوط: 1 طن")
    else:
        st.info(f"باقي {1000 - total} كيلو على الطن")

with tab3:
    st.subheader("💰 آلة حساب الأرباح")
    st.write("أدخل بيانات التكلفة والبيع:")
    b1, b2 = st.columns(2)
    buy = b1.number_input("سعر الشراء:", value=45000)
    sell = b2.number_input("سعر البيع المتوقع:", value=85000)
    profit = (sell - buy) * 10
    st.markdown(f"### صافي ربح الدورة (10 رؤوس): {profit:,.0f} جنيه")

st.markdown("---")
st.caption("إخلاء مسؤولية: هذا البرنامج أداة حسابية مساعدة، وقرار البيع والشراء ومكونات العلف تقع تحت مسؤولية المستخدم بالكامل.")
