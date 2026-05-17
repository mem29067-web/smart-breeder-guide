import streamlit as st
import datetime

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# تصميم المظهر (CSS) لضبط الألوان الزرقاء والخلفيات المريحة للعين
st.markdown("""
    <style>
    .main-title {
        background-color: #0b4c73;
        color: white;
        padding: 15px;
        text-align: center;
        border-radius: 10px;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .sub-title {
        background-color: #176b99;
        color: white;
        padding: 8px;
        text-align: center;
        border-radius: 5px;
        font-size: 18px;
        margin-bottom: 15px;
    }
    .stNumberInput div {
        margin-top: -5px;
    }
    </style>
""", unsafe_allowed_html=True)

# عنوان التطبيق العلوي
st.markdown('<div class="main-title">منظومة المربي الذكي Pro <br><span style="font-size: 16px;">المرجع العالمي للتحليل والأسعار</span></div>', unsafe_allowed_html=True)

# تاريخ اليوم تلقائي
تاريخ_اليوم = datetime.date.today().strftime("%Y-%m-%d")
st.markdown(f'<div class="sub-title">الأسعار الاسترشادية للسلع بالجمهورية - يوم {تاريخ_اليوم}</div>', unsafe_allowed_html=True)

# إنشاء أعمدة العرض الرئيسية للجدول
col_name, col_price, col_change, col_note = st.columns([3, 2, 2, 2])

with col_name:
    st.markdown("**اسم السلعة**")
with col_price:
    st.markdown("**سعر الطن (جنيه)**")
with col_change:
    st.markdown("**التغيير**")
with col_note:
    st.markdown("**ملاحظات**")

st.markdown("---")

# قائمة الخامات والبدائل بالترتيب المظبوط ونظيفة تماماً
if 'feed_prices' not in st.session_state:
    st.session_state.feed_prices = {
        # --- قسم الذرة والصويا الأساسي ---
        "ذرة صفراء أرجنتيني 🇦🇷": {"price": 14100, "change": "-100", "note": "صب أرضة"},
        "ذرة صفراء برزيلي 🇧🇷": {"price": 13700, "change": "-100", "note": "صب أرضة"},
        "ذرة صفراء أوكراني 🇺🇦": {"price": 12200, "change": "0", "note": "صب أرضة"},
        "ذرة فلاك": {"price": 15100, "change": "-100", "note": "صب أرضة"},
        "بذرة الصويا SB": {"price": 23000, "change": "-300", "note": "صب أرضة"},
        "كسب صويا 44% Local": {"price": 24000, "change": "-300", "note": "صب أرضة"},
        "كسب صويا 46% Local": {"price": 24000, "change": "-300", "note": "صب أرضة"},
        "كسب صويا مستورد": {"price": 25500, "change": "0", "note": "صب أرضة"},
        
        # --- قسم البدائل المبتكرة (مكان المشطوب بالكامل) ---
        "بسكويت ناعم (بديل طاقة)": {"price": 0, "change": "0", "note": "معيا أرضة"},
        "شيكولاتة هالك (بديل طاقة)": {"price": 0, "change": "0", "note": "معيا أرضة"},
        "بلح مفروم": {"price": 0, "change": "0", "note": "معيا أرضة"},
        "نواة بلح": {"price": 0, "change": "0", "note": "معيا أرضة"},
        "كسر مكرونة": {"price": 0, "change": "0", "note": "معيا أرضة"},
        "تفل برتقال": {"price": 0, "change": "0", "note": "معيا أرضة"},
        
        # --- باقي الخامات الأساسية ---
        "كسب عباد 36%": {"price": 17000, "change": "-100", "note": "معيا أرضة"},
        "دي دي جي (DDGS)": {"price": 12400, "change": "0", "note": "معيا أرضة"},
        "ردة (Gluten)": {"price": 12400, "change": "-200", "note": "معيا أرضة"},
        "جيلوثين": {"price": 40000, "change": "0", "note": "معيا أرضة"},
        "مخلفات مخابز وحلويات": {"price": 0, "change": "0", "note": "معيا وصال"},
        "مخرجات مصانع مقرمشات": {"price": 0, "change": "0", "note": "معيا وصال"},
        "جلووفيد": {"price": 13100, "change": "-100", "note": "صب أرضة"},
        "دقيق Flour": {"price": 15600, "change": "0", "note": "صب أرضة"},
    }

# عرض البيانات في الجدول مع إمكانية تعديل الأسعار يدويًا
for item, info in st.session_state.feed_prices.items():
    c_name, c_price, c_change, c_note = st.columns([3, 2, 2, 2])
    
    with c_name:
        st.info(item)
        
    with c_price:
        # خانة إدخال رقمية لتعديل السعر بسهولة من الموبايل
        new_price = st.number_input(f"السعر ({item})", min_value=0, value=info["price"], step=50, label_visibility="collapsed")
        st.session_state.feed_prices[item]["price"] = new_price
        
    with c_change:
        st.success(info["change"])
        
    with c_note:
        st.warning(info["note"])

# تذييل الصفحة والملاحظات
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555;'>ملاحظة: الأسعار السابقة قد تتغير نتيجة آليات الطلب والعرض والكمية وطريقة السداد</p>", unsafe_allowed_html=True)
st.markdown("<div style='background-color: #0b4c73; color: white; padding: 10px; text-align: center; border-radius: 5px;'>*** للحصول على الأسعار الاسترشادية وخدمة الأخبار يرجى التواصل مع الإدارة: 01090102035 ***</div>", unsafe_allowed_html=True)
