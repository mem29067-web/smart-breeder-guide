import streamlit as st

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="دليل المربي الذكي Pro", layout="wide")

# 2. هندسة الألوان (Dark Metallic & RTL)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 32px !important; font-weight: 900; padding: 15px; text-shadow: 2px 2px 10px #000; }
    
    /* تنسيق الجداول */
    .custom-table { 
        width: 100%; border-collapse: collapse; 
        background-color: rgba(255, 255, 255, 0.05); color: white; 
        border-radius: 12px; overflow: hidden; direction: rtl; margin-bottom: 20px;
    }
    .custom-table thead tr { background-color: #28a745; color: #ffffff; }
    .custom-table th, .custom-table td { padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .custom-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(40, 167, 69, 0.1); width: 35%; }
    
    /* ستايل الكتابة */
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    .premium-lock { color: #f1c40f !important; font-weight: bold; }
    .stNumberInput div div input { background-color: #ffffff !important; color: #000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: البورصة والتحليل الفني</h1>', unsafe_allow_html=True)

# 3. إدارة البيانات (لوحة التحكم السرية)
if 'price_list' not in st.session_state:
    st.session_state.price_list = {
        "ذرة أرجنتيني": "13,500", "ذرة برازيلي": "13,500", "صويا 44%": "24,000",
        "صويا 46%": "25,000", "ردة محلي": "11,200", "جيلوتين": "42,000", "دي دي جي": "18,500"
    }

# 4. الأقسام الرئيسية
tab1, tab2, tab3, tab4 = st.tabs(["💎 مركز البورصة", "🔬 تحليل الخامات", "💵 الأرباح", "⚙️ الإدارة"])

# --- القسم الأول: البورصة ---
with tab1:
    sub1, sub2 = st.tabs(["🌾 جدول ميست المحدث", "🌍 المؤشرات العالمية"])
    with sub1:
        html_mist = f"""
        <table class="custom-table">
            <thead><tr><th>اسم السلعة</th><th>السعر (طن)</th><th>التغيير</th><th>ملاحظات</th></tr></thead>
            <tbody>
                <tr><td>ذرة صفراء أرجنتيني</td><td>{st.session_state.price_list['ذرة أرجنتيني']}</td><td>-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء برازيلي</td><td>{st.session_state.price_list['ذرة برازيلي']}</td><td>-100</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 44%</td><td>{st.session_state.price_list['صويا 44%']}</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا محلي 46%</td><td>{st.session_state.price_list['صويا 46%']}</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>ردة محلي (Bran)</td><td>{st.session_state.price_list['ردة محلي']}</td><td>-</td><td>معبأ وصال</td></tr>
                <tr><td>جيلوتين مستورد</td><td>{st.session_state.price_list['جيلوتين']}</td><td>+100</td><td>صب أرضه</td></tr>
                <tr><td>دي دي جي (DDGS)</td><td>{st.session_state.price_list['دي دي جي']}</td><td>-</td><td>معبأ أرضه</td></tr>
            </tbody>
        </table>"""
        st.markdown(html_mist, unsafe_allow_html=True)
    with sub2:
        c1, c2 = st.columns(2)
        c1.metric("الدولار (تحديث تلقائي)", "48.35 ج")
        c2.metric("ذهب عيار 24", "3,850 ج")

# --- القسم الثاني: تحليل الخامات والبدائل ---
with tab2:
    sub_a, sub_b = st.tabs(["🌾 الخامات الأساسية", "💡 البدائل والكنوز"])
    with sub_a:
        html_basic = """
        <table class="custom-table">
            <thead><tr><th>الخامة</th><th>البروتين %</th><th>الطاقة</th><th>الألياف</th></tr></thead>
            <tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>3350</td><td>2.2%</td></tr>
                <tr><td>صويا 44%</td><td>44%</td><td>2230</td><td>7.0%</td></tr>
                <tr><td>نخالة قمح</td><td>14%</td><td>1300</td><td>10.0%</td></tr>
            </tbody>
        </table>"""
        st.markdown(html_basic, unsafe_allow_html=True)
    with sub_b:
        html_alt = """
        <table class="custom-table">
            <thead><tr><th>البديل المبتكر</th><th>البروتين %</th><th>الطاقة</th><th>الحالة</th></tr></thead>
            <tbody>
                <tr><td>بسكويت مصانع</td><td>9%</td><td>3800</td><td>✅ متاح</td></tr>
                <tr><td>شيكولاتة هالك</td><td>6%</td><td>4200</td><td>✅ متاح</td></tr>
                <tr class="premium-lock"><td>🔒 سوبر بريمكس (سر المهنة)</td><td>خاص</td><td>عالية</td><td>⭐ بريميوم</td></tr>
                <tr class="premium-lock"><td>🔒 مسحوق بروتين الحشرات</td><td>70%</td><td>وسط</td><td>⭐ بريميوم</td></tr>
            </tbody>
        </table>"""
        st.markdown(html_alt, unsafe_allow_html=True)

# --- القسم الثالث: الأرباح ---
with tab3:
    st.markdown('<div style="background:rgba(40,167,69,0.2); padding:30px; border-radius:15px; text-align:center; border:1px solid #28a745;"><h2>صافي الربح التقديري: 85,000 ج.م</h2></div>', unsafe_allow_html=True)

# --- القسم الرابع: لوحة التحكم (لك أنت فقط) ---
with tab4:
    st.subheader("🔐 لوحة التحكم في الأسعار")
    pwd = st.text_input("أدخل كلمة المرور للتعديل:", type="password")
    if pwd == "1234": # تقدر تغير الباسورد ده
        st.success("تم تسجيل الدخول.. عدل الأسعار واضغط حفظ")
        new_price = st.text_input("سعر الذرة الأرجنتيني الجديد:", value=st.session_state.price_list["ذرة أرجنتيني"])
        if st.button("تحديث وحفظ"):
            st.session_state.price_list["ذرة أرجنتيني"] = new_price
            st.rerun()
    else:
        st.warning("هذا القسم مخصص لإدارة التطبيق فقط.")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تصميم: سوبر بريمكس - الإصدار العالمي 2026</p>", unsafe_allow_html=True)
