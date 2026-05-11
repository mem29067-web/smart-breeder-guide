import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="بورصة ميست الكاملة", layout="wide")

# 2. التنسيق (RTL + ألوان ميتاليك + وضوح فائق)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 32px !important; font-weight: 900; padding: 15px; }
    
    /* تصميم جدول ميست الشامل */
    .mist-table { 
        width: 100%; border-collapse: collapse; 
        background-color: rgba(255, 255, 255, 0.05); color: white; 
        border-radius: 15px; overflow: hidden; direction: rtl; 
    }
    .mist-table thead tr { background-color: #2ecc71; color: #ffffff; }
    .mist-table th, .mist-table td { padding: 10px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; font-size: 14px; }
    .mist-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(46, 204, 113, 0.1); width: 30%; }
    
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    .stNumberInput div div input { background-color: #ffffff !important; color: #000000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📈 بورصة ميست الكاملة والعملات</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "🧪 ماكينة الخلط", "💵 الأرباح"])

with tab1:
    sub1, sub2 = st.tabs(["🌾 جدول جميع الخامات", "🌍 العملات والمعادن"])
    with sub1:
        # الجدول الكامل بنسبة 100% من صورة ميست
        html_table = """
        <table class="mist-table">
            <thead>
                <tr>
                    <th>اسم السلعة</th>
                    <th>السعر</th>
                    <th>التغيير</th>
                    <th>الملاحظات</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>ذرة صفراء أرجنتيني Arg</td><td>13,500</td><td>-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء برازيلي Brz</td><td>13,500</td><td>-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء أوكراني Ukr</td><td>12,200</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كورن فلاك أرجنتيني</td><td>14,100</td><td>-10</td><td>صب أرضه</td></tr>
                <tr><td>بذرة الصويا المستوردة SB</td><td>28,000</td><td>-</td><td>تعبئة أرضه</td></tr>
                <tr><td>كسب صويا محلي 44% SM</td><td>24,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 46% SM</td><td>25,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا مستورد SM</td><td>26,500</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>صويا فول فات مستورد</td><td>34,000</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>صويا هاي فات 43% مستورد</td><td>32,500</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>قمح روسي 11.5%</td><td>12,500</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>قمح أوكراني 11.5%</td><td>12,500</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب عباد +36% مستورد</td><td>17,500</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>دي دي جي DDGS أمريكي</td><td>18,500</td><td>-</td><td>معبأ أرضه</td></tr>
                <tr><td>ردة محلي (Bran)</td><td>11,200</td><td>-</td><td>معبأ وصال</td></tr>
                <tr><td>جيلوتين مستورد (جلوتين)</td><td>42,000</td><td>+100</td><td>صب أرضه</td></tr>
                <tr><td>دقيق Flour (24/27)</td><td>16,500</td><td>-</td><td>تعبئة وصال</td></tr>
                <tr><td>زيت صويا خام / مستورد</td><td>52,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>زيت صويا مكرر</td><td>56,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>جلوتوفيد محلي Local</td><td>12,500</td><td>+10</td><td>معبأ أرضه</td></tr>
                <tr><td>زيت أولين RBD</td><td>58,000</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>زيت ذرة مكرر</td><td>62,000</td><td>-</td><td>صب أرضه</td></tr>
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
