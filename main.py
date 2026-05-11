import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. التنسيق (الستايل الميتاليك)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 35px !important; font-weight: 900; padding: 20px; }
    .custom-table { width: 100%; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.05); color: white; border-radius: 12px; overflow: hidden; direction: rtl; margin-bottom: 25px; }
    .custom-table thead tr { background-color: #1e7e34; color: #ffffff; }
    .custom-table th, .custom-table td { padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .locked-section { background: rgba(0,0,0,0.9); padding: 60px; border-radius: 20px; text-align: center; border: 2px dashed #f1c40f; margin-top: 20px; }
    .whatsapp-btn { background-color: #25d366; color: white !important; padding: 12px 30px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; }
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: المرجع النهائي</h1>', unsafe_allow_html=True)

# 3. تثبيت حالة الإدارة في الذاكرة (Session State)
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# دالة القفل (التأكد من حالة المدير)
def check_access():
    if not st.session_state.is_admin:
        st.markdown(f"""
        <div class="locked-section">
            <h2 style="color: #f1c40f;">🔒 القسم مغلق للمشتركين فقط</h2>
            <p style="color:white;">للوصول للتحاليل والحاسبة، يرجى الاشتراك وتفعيل الحساب</p>
            <a href="https://wa.me/201090102035" class="whatsapp-btn">تواصل واتساب للاشتراك: 01090102035</a>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True

tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- 1. أسعار الخامات (مفتوح) ---
with tab1:
    st.markdown("### 📊 بورصة الخامات المحدثة")
    # بيانات الأسعار
    prices = {"ذرة أرجنتيني": 13500, "صويا 46%": 25000, "ردة محلي": 11200, "جيلوتين": 42000, "دي دي جي": 18500}
    html_prices = """<table class="custom-table"><thead><tr><th>الخامة</th><th>السعر (طن)</th></tr></thead><tbody>"""
    for k, v in prices.items():
        html_prices += f"<tr><td>{k}</td><td>{v:,} ج</td></tr>"
    st.markdown(html_prices + "</tbody></table>", unsafe_allow_html=True)

# --- 2. تحليل الخامات (مغلق) ---
with tab2:
    if check_access():
        st.success("🔓 وضع المدير نشط: الجداول متاحة الآن")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 🌾 خامات أساسية")
            st.markdown("""<table class="custom-table"><thead><tr><th>الخامة</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>88%</td></tr>
                <tr><td>كسب صويا 46%</td><td>46%</td><td>78%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)
        with c2:
            st.markdown("#### 💡 البدائل المبتكرة")
            st.markdown("""<table class="custom-table"><thead><tr><th>البديل</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>بسكويت مصانع</td><td>9%</td><td>95%</td></tr>
                <tr><td>تفل برتقال</td><td>6.5%</td><td>70%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)

# --- 3. حاسبة الأعلاف (مغلق) ---
with tab3:
    if check_access():
        st.subheader("🧮 خلاط العلف الذكي")
        w_c = st.number_input("ذرة (كجم):", 0, 1000, 500)
        w_s = st.number_input("صويا (كجم):", 0, 1000, 200)
        w_alt = st.number_input("إجمالي البدائل (كجم):", 0, 1000, 100)
        
        if st.button("🚀 احسب تحليل الخلطة"):
            total = w_c + w_s + w_alt
            prot = ((w_c*8.5) + (w_s*46) + (w_alt*9)) / total
            st.info(f"إجمالي الوزن: {total} كجم | البروتين: {prot:.2f}%")

# --- 4. الإدارة (المفتاح السحري) ---
with tab4:
    st.subheader("🔐 لوحة تحكم المدير")
    if not st.session_state.is_admin:
        pwd = st.text_input("أدخل كلمة المرور السرية لفتح البرنامج:", type="password")
        if st.button("تسجيل الدخول"):
            if pwd == "199208":
                st.session_state.is_admin = True
                st.rerun() # دي اللي هتخلي البرنامج يفتح فوراً
            else:
                st.error("❌ الباسورد غلط")
    else:
        st.success("✅ أنت الآن في وضع المدير والأقسام مفتوحة")
        if st.button("قفل البرنامج (تسجيل خروج)"):
            st.session_state.is_admin = False
            st.rerun()

st.markdown("<br><p style='text-align:center; opacity:0.5;'>منظومة المربي الذكي 2026</p>", unsafe_allow_html=True)
