import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الاحترافية
st.set_page_config(page_title="دليل المربي الذكي Pro", layout="wide")

# 2. لمسة التصميم العالمية (أبيض + أخضر ملكي + رمادي)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: white; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; }
    .stButton>button { 
        width: 100%; border-radius: 8px; height: 50px; font-weight: bold;
        background-color: #1e5631; color: white; border: none;
    }
    h1, h2, h3 { color: #1e5631; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    .card { background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 3. الهيدر (العنوان)
st.title("🚜 دليل المربي الذكي | Smart Breeder")
st.write("النسخة الاحترافية لإدارة التسمين وتركيب الأعلاف")

# 4. القائمة الرئيسية (Tabs) مثل البرامج العالمية
tab1, tab2, tab3 = st.tabs(["📊 لوحة التحكم", "🧪 مختبر الخلطات", "💰 حساب الأرباح"])

with tab1:
    st.subheader("📈 نبض السوق ومالية المزرعة")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("سعر الذرة اليوم", "13,500 ج", "-200")
    col2.metric("سعر الصويا", "24,000 ج", "+500")
    col3.metric("رأس المال الميداني", "450,000 ج")
    col4.metric("الأرباح المتوقعة", "85,000 ج", "12%", delta_color="normal")
    
    st.info("💡 نصيحة الذكاء الاصطناعي: أسعار البدائل (البسكويت) حالياً أوفر بنسبة 15% من الذرة.")

with tab2:
    st.subheader("🧪 تركيب خلطة الـ (18% بروتين) الموفرة")
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            corn = st.number_input("الذرة الصفراء (كيلو):", value=500)
            soya = st.number_input("صويا 44% (كيلو):", value=200)
            bran = st.number_input("نخالة (ردة) (كيلو):", value=150)
        with c2:
            alt_type = st.selectbox("البديل المتاح:", ["بسكويت ناعم", "عجينة بلح", "مكرونة"])
            alt_qty = st.number_input(f"{alt_type} (كيلو):", value=120)
            premix = st.number_input("سوبر بريمكس (إضافات) (كيلو):", value=30)
        
        total_w = corn + soya + bran + alt_qty + premix
        st.write(f"### إجمالي الوزن: {total_w} كيلو")
        
        if total_w == 1000:
            st.success("✅ التركيبة متزنة تماماً (1 طن)")
        else:
            st.warning(f"باقي {1000 - total_w} كيلو لتقفيل الطن")
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.subheader("💰 دراسة جدوى دورة الـ 10 عجول")
    buy_price = st.number_input("سعر شراء العجل الواحد (متوسط):", value=45000)
    feed_cost = st.number_input("تكلفة العلف الإجمالية للعجل:", value=25000)
    sell_expected = st.number_input("سعر البيع المتوقع للعجل:", value=85000)
    
    net_profit = (sell_expected - (buy_price + feed_cost)) * 10
    st.markdown(f"<h2 style='text-align:center; color: #2e7d32;'>صافي الربح المتوقع للدورة: {net_profit:,.0f} جنيه</h2>", unsafe_allow_html=True)

# 5. التذييل
st.markdown("---")
st.caption("دليل المربي الذكي Pro - جميع الحقوق محفوظة لشركة سوبر بريمكس 2026")
