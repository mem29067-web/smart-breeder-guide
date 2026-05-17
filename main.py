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
    /* تنسيق الجدول الحقيقي للموبايل */
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
    .negative-change {
        color: white;
        background-color: #d9534f !important; /* أحمر خفيف للهبوط */
        border-radius: 4px;
        padding: 2px 5px;
        font-weight: bold;
    }
    .stable-change {
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق العلوي
st.markdown('<div class="main-title">منظومة المربي الذكي Pro<br><span style="font-size: 14px; font-weight: normal;">المرجع العالمي للتحليل والأسعار</span></div>', unsafe_allow_html=True)

# تاريخ اليوم
تاريخ_اليوم = datetime.date.today().strftime("%Y-%m-%d")
st.markdown(f'<div class="sub-title">الأسعار الاسترشادية للسلع بالجمهورية - {تاريخ_اليوم}</div>', unsafe_allow_html=True)

# البيانات المظبوطة بالترتيب والبدائل المبتكرة
feed_prices = [
    # --- قسم الذرة والصويا الأساسي ---
    {"name": "ذرة صفراء أرجنتيني 🇦🇷", "price": "14,100", "change": "-100", "note": "صب أرضة"},
    {"name": "ذرة صفراء برزيلي 🇧🇷", "price": "13,700", "change": "-100", "note": "صب أرضة"},
    {"name": "ذرة صفراء أوكراني 🇺🇦", "price": "12,200", "change": "0", "note": "صب أرضة"},
    {"name": "ذرة فلاك", "price": "15,100", "change": "-100", "note": "صب أرضة"},
    {"name": "بذرة الصويا SB", "price": "23,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا 44% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا 46% Local", "price": "24,000", "change": "-300", "note": "صب أرضة"},
    {"name": "كسب صويا مستورد", "price": "25,500", "change": "0", "note": "صب أرضة"},
    
    # --- قسم البدائل المبتكرة (مكان المشطوب أزرق) ---
    {"name": "بسكويت ناعم (بديل طاقة)", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "شيكولاتة هالك (بديل طاقة)", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "بلح مفروم (بديل)", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "نواة بلح مفرومة", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "كسر مكرونة", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    {"name": "تفل برتقال", "price": "السعر يدوي", "change": "0", "note": "معيا أرضة"},
    
    # --- باقي الخامات الأساسية ---
    {"name": "كسب عباد 36%", "price": "17,000", "change": "-100", "note": "معيا أرضة"},
    {"name": "دي دي جي (DDGS)", "price": "12,400", "change": "0", "note": "معيا أرضة"},
    {"name": "ردة (Gluten)", "price": "12,400", "change": "-200", "note": "معيا أرضة"},
    {"name": "جيلوثين", "price": "40,000", "change": "0", "note": "معيا أرضة"},
    {"name": "مخلفات مخابز وحلويات", "price": "السعر يدوي", "change": "0", "note": "معيا وصال"},
    {"name": "مخرجات مصانع مقرمشات", "price": "السعر يدوي", "change": "0", "note": "معيا وصال"},
    {"name": "جلووفيد", "price": "13,100", "change": "-100", "note": "صب أرضة"},
    {"name": "دقيق Flour", "price": "15,600", "change": "0", "note": "صب أرضة"},
]

# بناء الجدول كـ HTML حقيقي مخصص للموبايل
table_html = """
<table class="custom-table">
    <tr>
        <th>اسم السلعة</th>
        <th>سعر الطن</th>
        <th>التغيير</th>
        <th>ملاحظات</th>
    </tr>
"""

for row in feed_prices:
    # تنسيق لون التغيير (أحمر لو سالب)
    change_class = 'class="negative-change"' if '-' in row["change"] else 'class="stable-change"'
    
    table_html += f"""
    <tr>
        <td class="text-right">{row['name']}</td>
        <td><b>{row['price']}</b></td>
        <td><span {change_class}>{row['change']}</span></td>
        <td>{row['note']}</td>
    </tr>
    """

table_html += "</table>"

# عرض الجدول الحقيقي
st.markdown(table_html, unsafe_allow_html=True)

# تذييل الصفحة
st.markdown("---")
st.markdown("<p style='text-align: center; color: #555; font-size: 12px;'>ملاحظة: الأسعار السابقة قد تتغير نتيجة آليات الطلب والعرض والكمية وطريقة السداد</p>", unsafe_allow_html=True)
st.markdown("<div style='background-color: #0b4c73; color: white; padding: 10px; text-align: center; border-radius: 5px; font-size: 13px;'>*** للحصول على الأسعار الاسترشادية وخدمة الأخبار يرجى التواصل مع الإدارة: 01090102035 ***</div>", unsafe_allow_html=True)
