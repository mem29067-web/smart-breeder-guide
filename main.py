import streamlit as st

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="مرجع المربي الذكي Pro", layout="wide")

# 2. التنسيق (RTL + ألوان ميتاليك + جداول احترافية)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 35px !important; font-weight: 900; padding: 20px; }
    
    /* تنسيق الجداول العلمية */
    .analysis-table { 
        width: 100%; border-collapse: collapse; 
        background-color: rgba(255, 255, 255, 0.05); color: white; 
        border-radius: 15px; overflow: hidden; direction: rtl; margin-bottom: 25px;
    }
    .analysis-table thead tr { background-color: #388e3c; color: #ffffff; }
    .analysis-table th, .analysis-table td { padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .analysis-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(46, 204, 113, 0.1); }
    
    /* تمييز الخامات بفلوس */
    .premium { color: #f1c40f; font-weight: bold; }
    
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 موسوعة تحليل الخامات والأعلاف</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "🔬 تحليل خامات الأعلاف", "💵 الأرباح"])

# --- القسم المطلوب تعديله (تحليل الخامات) ---
with tab2:
    sub_a, sub_b = st.tabs(["🌾 خامات الأعلاف الأساسية", "💡 بدائل الخامات المبتكرة"])
    
    with sub_a:
        st.markdown("### 📊 جدول تحليل القيمة الغذائية (خامات أساسية)")
        html_basic = """
        <table class="analysis-table">
            <thead>
                <tr>
                    <th>الخامة</th>
                    <th>البروتين %</th>
                    <th>الطاقة (Kcal)</th>
                    <th>الألياف %</th>
                    <th>المادة الجافة %</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>ذرة صفراء (أرجنتيني)</td><td>8.5%</td><td>3350</td><td>2.2%</td><td>88%</td></tr>
                <tr><td>كسب صويا 44%</td><td>44%</td><td>2230</td><td>7.0%</td><td>89%</td></tr>
                <tr><td>كسب صويا 46%</td><td>46%</td><td>2450</td><td>6.0%</td><td>90%</td></tr>
                <tr><td>نخالة قمح (ردة)</td><td>14%</td><td>1300</td><td>10.0%</td><td>88%</td></tr>
                <tr><td>جلوتين مستورد 60%</td><td>60%</td><td>3700</td><td>1.5%</td><td>91%</td></tr>
                <tr><td>دي دي جي (DDGS)</td><td>27%</td><td>2800</td><td>9.0%</td><td>91%</td></tr>
            </tbody>
        </table>
        """
        st.markdown(html_basic, unsafe_allow_html=True)

    with sub_b:
        st.markdown("### 🧬 بنك البدائل (كنوز التوفير)")
        html_alt = """
        <table class="analysis-table">
            <thead>
                <tr>
                    <th>الخامة البديلة</th>
                    <th>البروتين %</th>
                    <th>الطاقة %</th>
                    <th>الحالة</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>بسكويت مصانع (ناعم)</td><td>8-9%</td><td>3800</td><td>✅ متاح</td></tr>
                <tr><td>شيكولاتة خام (هالك)</td><td>6%</td><td>4200</td><td>✅ متاح</td></tr>
                <tr><td>بلح مفروم (عجوة)</td><td>3-4%</td><td>2900</td><td>✅ متاح</td></tr>
                <tr><td>كسر كورن فليكس</td><td>8%</td><td>3400</td><td>✅ متاح</td></tr>
                <tr class="premium"><td>🔒 خلطة "سوبر بريمكس" السرية</td><td>تحليل خاص</td><td>طاقة قصوى</td><td>⭐ بريميوم</td></tr>
                <tr class="premium"><td>🔒 مسحوق بروتين الحشرات</td><td>70%</td><td>خاص</td><td>⭐ بريميوم</td></tr>
                <tr class="premium"><td>🔒 هالك مصانع الحلويات (VIP)</td><td>متغير</td><td>4500</td><td>⭐ بريميوم</td></tr>
            </tbody>
        </table>
        """
        st.markdown(html_alt, unsafe_allow_html=True)
        st.warning("⚠️ بعض التحاليل المتقدمة والبدائل النادرة متاحة فقط لمشتركي الباقة الذهبية.")

# --- الأقسام الأخرى (للحفاظ على قوام البرنامج) ---
with tab1:
    st.info("راجع قسم البورصة لمتابعة الأسعار لحظة بلحظة")

with tab3:
    st.success("حاسبة الأرباح تعمل بناءً على التحاليل أعلاه")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>مرجع المربي الذكي - الإصدار العالمي 2026</p>", unsafe_allow_html=True)
