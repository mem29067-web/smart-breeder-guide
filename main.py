import streamlit as st
import datetime

# إعدادات الصفحة الأساسية للموبايل
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="centered")

# --- القائمة الجانبية للتنقل بين ميزات البرنامج ---
# --- الأزرار العلوية (Tabs) للتنقل السريع ---
الأسعار, الخلاط, الحسابات, المخزن = st.tabs(["📊 الأسعار والبدائل", "🥣 خلاط العلف", "📈 المدير المالي", "📦 المخزن"])

with الأسعار:
    # حط هنا كود الجدول المنسق اللي عملناه
    st.write("جدول الأسعار يظهر هنا...")

with الخلاط:
    # حط هنا كود خلاط العلف
    st.write("أدوات الخلاط تظهر هنا...")

with الحسابات:
    # حط هنا كود حاسبة الأرباح
    st.write("الحاسبة المالية تظهر هنا...")

with المخزن:
    # حط هنا كود المخزن والجرد
    st.write("بيانات المخزن تظهر هنا...")


# ---------------------------------------------------------
# 1. قسم جدول الأسعار (مع تعديل لون خط الخامات للأسود)
# ---------------------------------------------------------
if صفحة == "📊 جدول الأسعار والبدائل":
    st.markdown("""
        <style>
        .main-title { background-color: #0b4c73; color: white; padding: 12px; text-align: center; border-radius: 8px; font-size: 22px; font-weight: bold; margin-bottom: 15px; }
        .sub-title { background-color: #176b99; color: white; padding: 6px; text-align: center; border-radius: 5px; font-size: 15px; margin-bottom: 15px; }
        .custom-table { width: 100%; border-collapse: collapse; direction: rtl; font-size: 14px; margin-bottom: 20px; }
        .custom-table th { background-color: #0b4c73; color: white; text-align: center; padding: 8px; border: 1px solid #ddd; }
        
        /* تعديل خلايا الجدول ليكون لون الخط أسود صريح */
        .custom-table td { 
            text-align: center; 
            padding: 8px; 
            border: 1px solid #ddd; 
            background-color: #f9f9f9; 
            color: #000000 !important; /* هنا لون الخط أسود صريح */
        }
        
        .text-right { text-align: right !important; font-weight: bold; padding-right: 8px !important; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">منظومة المربي الذكي Pro<br><span style="font-size: 14px; font-weight: normal;">المرجع العالمي للتحليل والأسعار</span></div>', unsafe_allow_html=True)
    
    تاريخ_اليوم = datetime.date.today().strftime("%Y-%m-%d")
    st.markdown(f'<div class="sub-title">الأسعار الاسترشادية للسلع بالجمهورية - {تاريخ_اليوم}</div>', unsafe_allow_html=True)

    feed_prices = [
        {"name": "ذرة صفراء أرجنتيني 🇦🇷", "price": "14,100", "change": "-100", "note": "صب أرضة"},
        {"name": "ذرة صفراء برزيلي 🇧🇷", "price": "13,700", "change": "-100", "note": "صب أرضة"},
        {"name": "ذرة صفراء أوكراني 🇺🇦", "price": "12,200", "change": "0", "note": "صب أرضة"},
        {"name": "ذرة فلاك", "price": "15,100", "change": "-100", "note": "صب أرضة"},
        {"name": "بذرة الصويا SB", "price": "23,000", "change": "-300", "note": "صب أرضة"},
        {"name": "كسب صويا 44% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
        {"name": "كسب صويا 46% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
        {"name": "كسب صويا مستورد", "price": "25,500", "change": "0", "note": "صب أرضة"},
        
        # البدائل المبتكرة مكان المشطوب
        {"name": "بسكويت ناعم (بديل طاقة)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        {"name": "شيكولاتة هالك (بديل طاقة)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        {"name": "بلح مفروم (بديل)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        {"name": "نواة بلح مفرومة", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        {"name": "كسر مكرونة", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        {"name": "تفل برتقال", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
        
        {"name": "كسب عباد 36%", "price": "17,000", "change": "-100", "note": "معيا أرضة"},
        {"name": "دي دي جي (DDGS)", "price": "12,400", "change": "0", "note": "معيا أرضة"},
        {"name": "ردة (Gluten)", "price": "12,400", "change": "-200", "note": "معيا أرضة"},
        {"name": "جيلوثين", "price": "40,000", "change": "0", "note": "معيا أرضة"},
        {"name": "جلووفيد", "price": "13,100", "change": "-100", "note": "صب أرضة"},
        {"name": "دقيق Flour", "price": "15,600", "change": "0", "note": "صب أرضة"},
    ]

    html_rows = ""
    for row in feed_prices:
        html_rows += f"<tr><td class='text-right'>{row['name']}</td><td><b>{row['price']}</b></td><td>{row['change']}</td><td>{row['note']}</td></tr>"

    table_html = f'<table class="custom-table"><tr><th>اسم السلعة</th><th>سعر الطن</th><th>التغيير</th><th>ملاحظات</th></tr>{html_rows}</table>'
    st.markdown(table_html, unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. قسم خلاط العلف الذكي
# ---------------------------------------------------------
elif صفحة == "🥣 خلاط العلف الذكي":
    st.title("🥣 خلاط ومحلل نسب العلف")
    st.subheader("احسب خلطتك ونسبة البروتين والطاقة")
    
    ذرة = st.number_input("كمية الذرة في الخلطة (كجم):", min_value=0, value=600)
    صويا = st.number_input("كمية كسب الصويا (كجم):", min_value=0, value=200)
    بديل = st.number_input("كمية البديل المبتكر (بسكويت/بلح) (كجم):", min_value=0, value=100)
    ردة = st.number_input("كمية الردة (كجم):", min_value=0, value=100)
    
    إجمالي = ذرة + صويا + بديل + ردة
    st.metric("إجمالي وزن الخلطة (كجم):", إجمالي)
    
    if st.button("🧮 احسب تحليل التركيبة"):
        بروتين_تقريبي = ((ذرة*9) + (صويا*44) + (بديل*10) + (ردة*14)) / (إجمالي if إجمالي > 0 else 1)
        st.success(f"📈 نسبة البروتين التقريبية في الخلطة: {بروتين_تقريبي:.2f}%")

# ---------------------------------------------------------
# 3. قسم المدير المالي
# ---------------------------------------------------------
elif صفحة == "📈 المدير المالي (الحاسبة)":
    st.title("📈 حاسبة الأرباح والتكاليف والدورة")
    
    رأس_المال = st.number_input("رأس المال المستثمر (جنيه):", min_value=0, value=100000)
    تكلفة_العجل = st.number_input("سعر شراء العجل الصغير (جنيه):", min_value=0, value=30000)
    عدد_العجول = st.number_input("عدد العجول المتوقع شراءها:", min_value=1, value=3)
    
    تكلفة_الشراء = تكلفة_العجل * عدد_العجول
    المتبقي_للعلف = رأس_المال - تكلفة_الشراء
    
    st.write(f"💵 إجمالي تكلفة الشراء: {تكلفة_الشراء:,} جنيه")
    if المتبقي_للعلف >= 0:
        st.success(f"💰 المبلغ المتبقي لتغطية العلف والرعاية: {المتبقي_للعلف:,} جنيه")
    else:
        st.error(f"⚠️ العجز: {abs(المتبقي_للعلف):,} جنيه")

# ---------------------------------------------------------
# 4. قسم إدارة المخزن
# ---------------------------------------------------------
elif صفحة == "📦 إدارة المخزن":
    st.title("📦 جرد كميات خامات المخزن")
    st.info("سجل الكميات المتوفرة عندك في المخازن حالياً")
    
    st.text_input("اسم الخامة للتخزين:", "ذرة أرجنتيني")
    st.number_input("الكمية المتوفرة (طن):", min_value=0.0, value=5.0, step=0.5)
    if st.button("💾 حفظ البيانات في المخزن"):
        st.success("تم تحديث جرد المخزن بنجاح!")
