import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="بورصة ميست - دليل المربي", layout="wide")

# 2. التنسيق والستايل (RTL وجدول ميست الفخم)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 30px !important; font-weight: 900; padding: 20px; }
    .mist-table { width: 100%; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.05); color: white; border-radius: 15px; overflow: hidden; direction: rtl; }
    .mist-table thead tr { background-color: #2ecc71; color: #ffffff; }
    .mist-table th, .mist-table td { padding: 12px 15px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .mist-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(46, 204, 113, 0.1); }
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    .stNumberInput div div input { background-color: #ffffff !important; color: #000000 !important; font-weight: bold !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📈 بورصة ميست والبورصة العالمية</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "🧪 ماكينة الخلط", "💵 الأرباح"])

with tab1:
    sub1, sub2 = st.tabs(["🌾 جدول خامات ميست", "🌍 العملات والذهب"])
    with sub1:
        # الجدول الكامل من اليمين لليسار
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
                <tr><td>ذرة صفراء أرجنتيني</td><td>13,500</td><td style="color:#ff4b4b;">-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء برازيلي</td><td>13,500</td><td style="color:#ff4b4b;">-100</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 44%</td><td>24,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 46%</td><td>25,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>ردة محلي (Bran)</td><td>11,200</td><td>-</td><td>معبأ وصال</td></tr>
                <tr><td>جيلوتين مستورد</td><td>42,000</td><td style="color:#2ecc71;">+100</td><td>صب أرضه</td></tr>
                <tr><td>دي دي جي (DDGS)</td><td>18,500</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>زيت صويا خام</td><td>52,000</td><td>-</td><td>صب أرضه</td></tr>
            </tbody>
        </table>
        """
        st.markdown(html_table, unsafe_allow_html=True)
    with sub2:
        c1, c2 = st.columns(2)
        with c1:
            st.metric("الدولار الأمريكي", "48.30 ج")
            st.metric("اليورو", "52.10 ج")
        with c2:
            st.metric("ذهب عيار 24", "3,850 ج")
            st.metric("الفضة", "1,520 ج")

with tab2:
    st.subheader("🧪 تركيب الخلطة")
    col1, col2 = st.columns(2)
    with col1:
        st.number_input("الذرة (كجم):", value=500)
        st.number_input("الصويا (كجم):", value=200)
    with col2:
        st.number_input("البدائل:", value=150)
        st.number_input("بريمكس:", value=30)

with tab3:
    st.markdown('<div style="background:rgba(46,204,113,0.2); padding:20px; border-radius:15px; text-align:center;"><h2>الربح المتوقع: 85,000 ج.م</h2></div>', unsafe_allow_html=True)
