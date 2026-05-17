import streamlit as st
import datetime

# إعدادات الصفحة الأساسية للموبايل
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="centered")

# تصميم الجدول والألوان ليكون متناسق ومسطرة على شاشة الموبايل
st.markdown("""
    <style>
    .main-title {
        background-color: #0b4c73;
        color: white;
        padding: 12px;
        text-align: center;
        border-radius: 8px;
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 15px;
    }
    .sub-title {
        background-color: #176b99;
        color: white;
        padding: 6px;
        text-align: center;
        border-radius: 5px;
        font-size: 15px;
        margin-bottom: 15px;
    }
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        direction: rtl;
        font-size: 14px;
        margin-bottom: 20px;
    }
    .custom-table th {
        background-color: #0b4c73;
        color: white;
        text-align: center;
        padding: 8px;
        border: 1px solid #ddd;
    }
    .custom-table td {
        text-align: center;
        padding: 8px;
        border: 1px solid #ddd;
        background-color: #f9f9f9;
    }
    .text-right {
        text-align: right !important;
        font-weight: bold;
        padding-right: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق العلوي
st.markdown('<div class="main-title">منظومة المربي الذكي Pro<br><span style="font-size: 14px; font-weight: normal;">المرجع العالمي للتحليل والأسعار</span></div>', unsafe_allow_html=True)

# تاريخ اليوم تلقائي
تاريخ_اليوم = datetime.date.today().strftime("%Y-%m-%d")
st.markdown(f'<div class="sub-title">الأسعار الاسترشادية للسلع بالجمهورية - {تاريخ_اليوم}</div>', unsafe_allow_html=True)

# البيانات المظبوطة بالترتيب والبدائل المبتكرة
feed_prices = [
    {"name": "ذرة صفراء أرجنتيني 🇦🇷", "price": "14,100", "change": "-100", "note": "صب أرضة"},
    {"name": "ذرة صفراء برزيلي 🇧🇷", "price": "13,700", "change": "-100", "note": "صب أرضة"},
    {"name": "ذرة صفراء أوكراني 🇺🇦", "price": "12,200", "change": "0", "note": "صب أرضة"},
    {"name": "ذرة فلاك", "price": "15,100", "change": "-100", "note": "صب أرضة"},
    {"name": "بذرة الصويا SB", "price": "23,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا 44% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا 46% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا مستورد", "price": "25,500", "change": "0", "note": "صب أرضة"},
    
    # --- البدائل المبتكرة مكان المشطوب ---
    {"name": "بسكويت ناعم (بديل طاقة)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "شيكولاتة هالك (بديل طاقة)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "بلح مفروم (بديل)", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "نواة بلح مفرومة", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "كسر مكرونة", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "تفل برتقال", "price": "يدوي", "change": "0", "note": "معيا أرضة"},
    
    # --- باقي الخامات ---
    {"name": "كسب عباد 36%", "price": "17,000", "change": "-100", "note": "معيا أرضة"},
    {"name": "دي دي جي (DDGS)", "price": "12,400", "change": "0", "note": "معيا أرضة"},
    {"name": "ردة (Gluten)", "price": "12,400", "change": "-200", "note": "معيا أرضة"},
    {"name": "جيلوثين", "price": "40,000", "change": "0", "note": "معيا أرضة"},
    {"name": "مخلفات مخابز وحلويات", "price": "يدوي", "change": "0", "note": "معيا وصال"},
    {"name": "مخرجات مصانع مقرمشات", "price": "يدوي", "change": "0", "note": "معيا وصال"},
    {"name": "جلووفيد", "price": "13,100", "change": "-100", "note": "صب أرضة"},
    {"name": "دقيق Flour", "price": "15,600", "change": "0", "note": "صب أرضة"},
]

# بناء الجدول بطريقة مبسطة تماماً لتفادي أي خطأ سينتكس
html_rows = ""
for row in feed_prices:
    html_rows += f"<tr><td class='text-right'>{row['name']}</td><td><b>{row['price']}</b></td><td>{row['change']}</td><td>{row['note']}</td></tr>"

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

# عرض الجدول
st.markdown(table_html, unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555; font-size: 12px;'>ملاحظة: الأسعار السابقة قد تتغير نتيجة آليات الطلب والعرض والكمية وطريقة السداد</p>", unsafe_allow_html=True)
st.markdown("<div style='background-color: #0b4c73; color: white; padding: 10px; text-align: center; border-radius: 5px; font-size: 13px;'>*** للحصول على الأسعار الاسترشادية وخدمة الأخبار يرجى التواصل مع الإدارة: 01090102035 ***</div>", unsafe_allow_html=True)
