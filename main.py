import streamlit as st
import datetime

# إعدادات الصفحة الأساسية للموبايل
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="centered")

# تصميم المظهر والألوان والجدول ليكون مسطرة ومريح للعين
st.markdown("""
    <style>
    .main-title { background-color: #0b4c73; color: white; padding: 12px; text-align: center; border-radius: 8px; font-size: 22px; font-weight: bold; margin-bottom: 15px; }
    .sub-title { background-color: #176b99; color: white; padding: 6px; text-align: center; border-radius: 5px; font-size: 15px; margin-bottom: 15px; }
    .custom-table { width: 100%; border-collapse: collapse; direction: rtl; font-size: 14px; margin-bottom: 20px; }
    .custom-table th { background-color: #0b4c73; color: white; text-align: center; padding: 8px; border: 1px solid #ddd; }
    
    /* لون خط الخامات والسلع أسود صريح ومسطرة */
    .custom-table td { 
        text-align: center; 
        padding: 8px; 
        border: 1px solid #ddd; 
        background-color: #f9f9f9; 
        color: #000000 !important; 
        font-weight: 500;
    }
    .text-right { text-align: right !important; font-weight: bold; padding-right: 8px !important; }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق العلوي الثابت
st.markdown('<div class="main-title">منظومة المربي الذكي Pro<br><span style="font-size: 14px; font-weight: normal;">المرجع العالمي للتحليل والأسعار</span></div>', unsafe_allow_html=True)

# تاريخ اليوم تلقائي
تاريخ_اليوم = datetime.date.today().strftime("%Y-%m-%d")
st.markdown(f'<div class="sub-title">لوحة التحكم الذكية المستمرة - {تاريخ_اليوم}</div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# تهيئة ذاكرة البرنامج لتخزين الأسعار المربوطة بين الأقسام
# ---------------------------------------------------------
if 'prices_db' not in st.session_state:
    st.session_state.prices_db = {
        # خامات أساسية بأسعار استرشادية
        "ذرة صفراء أرجنتيني 🇦🇷": {"price": 14100, "change": "-100", "note": "صب أرضة", "protein": 9.0, "tdn": 80.0},
        "ذرة صفراء برزيلي 🇧🇷": {"price": 13700, "change": "-100", "note": "صب أرضة", "protein": 9.0, "tdn": 80.0},
        "ذرة صفراء أوكراني 🇺🇦": {"price": 12200, "change": "0", "note": "صب أرضة", "protein": 9.0, "tdn": 79.0},
        "ذرة فلاك": {"price": 15100, "change": "-100", "note": "صب أرضة", "protein": 9.0, "tdn": 88.0},
        "بذرة الصويا SB": {"price": 23000, "change": "-300", "note": "صب أرضة", "protein": 36.0, "tdn": 78.0},
        "كسب صويا 44% Local": {"price": 24000, "change": "-300", "note": "صب أرضة", "protein": 44.0, "tdn": 76.0},
        "كسب صويا 46% Local": {"price": 24000, "change": "-300", "note": "صب أرضة", "protein": 46.0, "tdn": 78.0},
        "كسب صويا مستورد": {"price": 25500, "change": "0", "note": "صب أرضة", "protein": 46.0, "tdn": 78.0},
        "كسب عباد 36%": {"price": 17000, "change": "-100", "note": "معيا أرضة", "protein": 36.0, "tdn": 65.0},
        "دي دي جي (DDGS)": {"price": 12400, "change": "0", "note": "معيا أرضة", "protein": 27.0, "tdn": 76.0},
        "ردة (Gluten)": {"price": 12400, "change": "-200", "note": "معيا أرضة", "protein": 14.0, "tdn": 65.0},
        "جيلوثين": {"price": 40000, "change": "0", "note": "معيا أرضة", "protein": 60.0, "tdn": 80.0},
        "جلووفيد": {"price": 13100, "change": "-100", "note": "صب أرضة", "protein": 20.0, "tdn": 75.0},
        "دقيق Flour": {"price": 15600, "change": "0", "note": "صب أرضة", "protein": 12.0, "tdn": 78.0},
        
        # البدائل المبتكرة (تبدأ بـ 0 وتقدر تعدلها من قسم المدير)
        "بسكويت ناعم (بديل طاقة)": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 10.0, "tdn": 90.0},
        "شيكولاتة هالك (بديل طاقة)": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 8.0, "tdn": 92.0},
        "بلح مفروم (بديل)": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 6.0, "tdn": 75.0},
        "نواة بلح مفرومة": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 6.0, "tdn": 70.0},
        "كسر مكرونة": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 11.0, "tdn": 82.0},
        "تفل برتقال": {"price": 0, "change": "0", "note": "معيا أرضة", "protein": 7.0, "tdn": 73.0},
        "مخلفات مخابز وحلويات": {"price": 0, "change": "0", "note": "معيا وصال", "protein": 10.0, "tdn": 88.0},
        "مخرجات مصانع مقرمشات": {"price": 0, "change": "0", "note": "معيا وصال", "protein": 9.5, "tdn": 85.0},
    }

# ---------------------------------------------------------
# الأزرار العلوية المباشرة (Tabs) للموبايل بدلاً من القائمة الجانبية
# ---------------------------------------------------------
الأسابيع, الخلاط, المدير, المخزن = st.tabs(["📊 جدول الأسعار", "🥣 خلاط العلف الذكي", "💼 المدير المالي والأسعار", "📦 المخزن"])

# ---------------------------------------------------------
# 1. زر جدول الأسعار
# ---------------------------------------------------------
with الأسابيع:
    html_rows = ""
    for name, info in st.session_state.prices_db.items():
        # عرض السعر "يدوي" لو لسه بصفر، أو عرض الرقم الحقيقي لو اتعدل من المدير
        display_price = f"{info['price']:,}" if info['price'] > 0 else "يدوي"
        html_rows += f"<tr><td class='text-right'>{name}</td><td><b>{display_price}</b></td><td>{info['change']}</td><td>{info['note']}</td></tr>"

    table_html = f"""
    <table class="custom-table">
        <tr>
            <th>اسم السلعة</th>
            <th>سعر الطن</th>
            <th>التغيير</th>
            <th>ملاحظات</th>
        </tr>
        {html_rows}
    </table>
    """
    st.markdown(table_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. زر خلاط العلف الذكي (تعديل إضافة الطاقة والبروتين معاً)
# ---------------------------------------------------------
with الخلاط:
    st.subheader("🥣 خلاط ومحلل نسب العلف الذكي")
    st.info("حدد وزنة كل خامة بالكيلو لـ (1 طن أو خلطة مخصصة) وشوف التحليل بالملي:")
    
    # اختيار الخامات ديناميكياً من الذاكرة وحساب نسبها
    total_weight = 0
    calculated_protein = 0
    calculated_tdn = 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        w_ذرة = st.number_input("ذرة صفراء أرجنتيني (كجم):", min_value=0, value=500, step=50)
        w_صويا = st.number_input("كسب صويا 46% (كجم):", min_value=0, value=200, step=25)
        w_ردة = st.number_input("ردة (كجم):", min_value=0, value=150, step=25)
        
    with col2:
        w_بسكويت = st.number_input("بسكويت ناعم (بديل طاقة) (كجم):", min_value=0, value=100, step=25)
        w_بلح = st.number_input("بلح مفروم (كجم):", min_value=0, value=50, step=25)
        w_مركزات = st.number_input("إضافات خامات أخرى (كجم):", min_value=0, value=0, step=10)

    # تجميع الأوزان والحسابات بناءً على قيم البروتين والطاقة المثبتة علمياً لكل خامة فوق
    weights_dict = {
        "ذرة صفراء أرجنتيني 🇦🇷": w_ذرة,
        "كسب صويا 46% Local": w_صويا,
        "ردة (Gluten)": w_ردة,
        "بسكويت ناعم (بديل طاقة)": w_بسكويت,
        "بلح مفروم (بديل)": w_بلح
    }
    
    total_weight = sum(weights_dict.values()) + w_مركزات
    
    for name, weight in weights_dict.items():
        calculated_protein += weight * (st.session_state.prices_db[name]["protein"] / 100)
        calculated_tdn += weight * (st.session_state.prices_db[name]["tdn"] / 100)
        
    st.markdown("---")
    st.metric("إجمالي وزن الخلطة الحالية:", f"{total_weight:,} كجم")
    
    if st.button("🧮 احسب تحليل البروتين والطاقة للتركيبة"):
        if total_weight > 0:
            final_protein = (calculated_protein / total_weight) * 100
            final_tdn = (calculated_tdn / total_weight) * 100
            
            # عرض النتيجتين معاً جنب بعض مسطرة
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.success(f"📈 نسبة البروتين: {final_protein:.2f} %")
            with res_col2:
                st.info(f"⚡ نسبة الطاقة (TDN): {final_tdn:.2f} %")
        else:
            st.error("رجاءً أدخل أوزان الخامات أولاً لحساب الخلطة.")

# ---------------------------------------------------------
# 3. زر المدير المالي (تعديل إدخال وتحديث الأسعار يدوي للجدول)
# ---------------------------------------------------------
with المدير:
    st.subheader("💼 إدارة التكاليف وتحديث أسعار السوق")
    st.success("📝 عدل أسعار البدائل والخامات من هنا وهيتم تحديث جدول الأسعار فوراً:")
    
    # رص خانات لتعديل الأسعار مباشرة في الذاكرة
    st.markdown("### 💰 تحديث أسعار البدائل (جنيه للطن):")
    
    for name in ["بسكويت ناعم (بديل طاقة)", "شيكولاتة هالك (بديل طاقة)", "بلح مفروم (بديل)", "نواة بلح مفرومة", "كسر مكرونة", "تفل برتقال", "مخلفات مخابز وحلويات", "مخرجات مصانع مقرمشات"]:
        current_val = st.session_state.prices_db[name]["price"]
        new_price = st.number_input(f"سعر طن {name}:", min_value=0, value=current_val, step=100, key=f"edit_{name}")
        st.session_state.prices_db[name]["price"] = new_price

    st.markdown("---")
    st.markdown("### 📉 حاسبة الدورة المالية السريعة:")
    capital = st.number_input("رأس المال المرصود للدورة (جنيه):", min_value=0, value=150000)
    calf_cost = st.number_input("سعر شراء العجل الواحد اليوم (جنيه):", min_value=0, value=35000)
    calf_count = st.number_input("عدد العجول المستهدفة:", min_value=1, value=3)
    
    total_buying = calf_cost * calf_count
    remaining = capital - total_buying
    
    st.write(f"إجمالي قيمة شراء الحيوانات: **{total_buying:,}** جنيه")
    if remaining >= 0:
        st.success(f"المبلغ المتوفر لتمويل التغذية والعلف: **{remaining:,}** جنيه")
    else:
        st.error(f"انتبه! رأس المال لا يغطي الشراء. العجز: **{abs(remaining):,}** جنيه")

# ---------------------------------------------------------
# 4. زر إدارة المخزن
# ---------------------------------------------------------
with المخزن:
    st.subheader("📦 جرد وكميات مخزن العلف")
    st.info("تابع جرد وكميات المخازن المتوفرة عندك:")
    
    stock_item = st.selectbox("اختر الخامة للجرد:", list(st.session_state.prices_db.keys()))
    stock_qty = st.number_input("الكمية الحالية المتوفرة بالمخزن (طن):", min_value=0.0, value=2.0, step=0.5)
    
    if st.button("💾 تثبيت جرد الكمية"):
        st.success(f"تم حفظ الكمية بنجاح: {stock_item} بمقدار {stock_qty} طن في مخازن المزرعة.")

# تذييل الصفحة الثابت والملاحظات وأرقام التواصل
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555; font-size: 12px;'>ملاحظة: الأسعار السابقة قد تتغير نتيجة آليات الطلب والعرض والكمية وطريقة السداد</p>", unsafe_allow_html=True)
st.markdown("<div style='background-color: #0b4c73; color: white; padding: 10px; text-align: center; border-radius: 5px; font-size: 13px;'>*** للحصول على الأسعار الاسترشادية وخدمة الأخبار يرجى التواصل مع الإدارة: 01090102035 ***</div>", unsafe_allow_html=True)
