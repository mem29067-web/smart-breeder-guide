import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="بورصة ميست - دليل المربي", layout="wide")

# 2. تنسيق الألوان والجدول (نظام اليمين للشمال RTL)
st.markdown("""
    <style>
    /* اتجاه الصفحة من اليمين للشمال */
    .main {
        direction: rtl;
        text-align: right;
    }
    .stApp {
        background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 30px !important;
        font-weight: 900;
        padding: 20px;
    }
    /* تنسيق جدول ميست الاحترافي */
    .mist-table {
        width: 100%;
        border-collapse: collapse;
        margin: 10px 0;
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border-radius: 15px;
        overflow: hidden;
        direction: rtl;
    }
    .mist-table thead tr {
        background-color: #2ecc71;
        color: #ffffff;
        text-align: center;
    }
    .mist-table th, .mist-table td {
        padding: 12px 15px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
    }
    /* تمييز عمود اسم الخامة جهة اليمين */
    .mist-table td:first-child, .mist-table th:first-child {
        text-align: right;
        font-weight: bold;
        background-color: rgba(46, 204, 113, 0.1);
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📈 بورصة ميست للاعلاف والبورصة العالمية</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "🧪 ماكينة الخلط", "💵 الأرباح"])

with tab1:
    sub1, sub2 = st.tabs(["🌾 جدول خامات ميست المحدث", "🌍 العملات والذهب"])
    
    with sub1:
        st.markdown("### 📊 الأسعار الاسترشادية للسلع (بالجنيه المصري)")
        
        # الجدول الكامل كما في صورة ميست
        html_table = """
        <table class="mist-table">
            <thead>
                <tr>
                    <th>اسم السلعة</th>
                    <th>سعر الطن</th>
                    <th>التغيير</th>
                    <th>ملاحظات</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>ذرة صفراء أرجنتيني</td><td>13,500</td><td style="color:#e74c3c;">-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء برازيلي</td><td>13,500</td><td style="color:#e74c3c;">-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء أوكراني</td><td>12,200</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كورن فلاك أرجنتيني</td><td>14,100</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>بذرة الصويا المستوردة</td><td>28,000</td><td style="color:#2ecc71;">+500</td><td>تعبئة أرضه</td></tr>
                <tr><td>كسب صويا محلي 44%</td><td>24,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 46%</td><td>25,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>صويا فول فات مستورد</td><td>34,000</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>قمح روسي 11.5%</td><td>12,500</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>ردة محلي (Bran)</td><td>11,200</td><td>-</td><td>معبأ وصال</td></tr>
                <tr><td>جيلوتين مستورد</td><td>42,000</td><td style="color:#2ecc71;">+100</td><td>صب أرضه</td></tr>
                <tr><td>دي دي جي (DDGS) أمريكي</td><td>18,500</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>زيت صويا خام</td><td>52,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>زيت صويا مكرر</td><td>56,000</td><td>-</td><td>صب أرضه</td></tr>
            </tbody>
        </table>
        """
        st.markdown(html_table, unsafe_allow_html=True)

    with sub2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 💵 العملات")
            st.metric("الدولار (البنك)", "48.30 ج")
            st.metric("اليورو", "52.10 ج")
        with c2:
            st.markdown("### 🏆 المعادن")
            st.metric("ذهب عيار 24", "3,850 ج")
            st.metric("الفضة (أوقية)", "1,520 ج")

with tab2:
    st.subheader("🧪 تركيب الخلطة الذكية")
    # محتوى الماكينة
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("الذرة:", value=500)
        st.number_input("الصويا:", value=200)
    with col2:
        st.number_input("البدائل:", value=150)
        st.number_input("سوبر بريمكس:", value=30)

with tab3:
    st.markdown('<div style="background: rgba(4
