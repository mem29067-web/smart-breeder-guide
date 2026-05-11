import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. هندسة الواجهة (الستايل المتفق عليه)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 35px !important; font-weight: 900; padding: 20px; }
    .custom-table { width: 100%; border-collapse: collapse; background-color: rgba(255, 255, 255, 0.05); color: white; border-radius: 15px; overflow: hidden; direction: rtl; margin-bottom: 25px; }
    .custom-table thead tr { background-color: #1e7e34; color: #ffffff; }
    .custom-table th, .custom-table td { padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .custom-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(40, 167, 69, 0.1); }
    .locked-section { background: rgba(0,0,0,0.85); padding: 50px; border-radius: 20px; text-align: center; border: 2px dashed #f1c40f; margin-top: 20px; }
    .whatsapp-btn { background-color: #25d366; color: white !important; padding: 10px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; }
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: النسخة الاحترافية</h1>', unsafe_allow_html=True)

# 3. إدارة الحالة (الأسعار ووضع المدير)
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

if 'prices' not in st.session_state:
    st.session_state.prices = {
        "ذرة أرجنتيني": "13,500", "ذرة برازيلي": "13,500", "صويا 44%": "24,000",
        "صويا 46%": "25,000", "ردة محلي": "11,200", "جيلوتين": "42,000"
    }

# دالة رسالة القفل
def premium_lock():
    if not st.session_state.is_admin:
        st.markdown(f"""
        <div class="locked-section">
            <div style="color: #f1c40f; font-size: 24px; font-weight: bold;">🔒 هذا القسم متاح للمشتركين فقط</div>
            <p>للاشتراك والوصول للحاسبة والتحاليل الكاملة:</p>
            <a href="https://wa.me/201090102035" class="whatsapp-btn">تواصل عبر واتساب: 01090102035</a>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True

# 4. الأقسام (Tabs)
tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- القسم الأول: الأسعار (مجاني) ---
with tab1:
    st.markdown("### 📊 بورصة الخامات المحدثة")
    html_prices = f"""
    <table class="custom-table">
        <thead><tr><th>الخامة</th><th>السعر (طن)</th><th>التغيير</th></tr></thead>
        <tbody>
            {"".join([f"<tr><td>{k}</td><td>{v}</td><td>-</td></tr>" for k, v in st.session_state.prices.items()])}
        </tbody>
    </table>"""
    st.markdown(html_prices, unsafe_allow_html=True)

# --- القسم الثاني: تحليل الخامات (مفتوح للمدير فقط) ---
with tab2:
    if premium_lock():
        st.success("🔓 وضع المدير نشط: يمكنك رؤية التحاليل الآن")
        st.markdown("""
        <table class="custom-table">
            <thead><tr><th>الخامة</th><th>البروتين %</th><th>الطاقة</th><th>ألياف %</th></tr></thead>
            <tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>3350</td><td>2.2%</td></tr>
                <tr><td>صويا 44%</td><td>44%</td><td>2230</td><td>7.0%</td></tr>
                <tr><td>بسكويت هالك</td><td>9.5%</td><td>3800</td><td>1.5%</td></tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)

# --- القسم الثالث: حاسبة الأعلاف (مفتوح للمدير فقط) ---
with tab3:
    if premium_lock():
        st.success("🔓 وضع المدير نشط: الحاسبة جاهزة للعمل")
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("1️⃣ حساب تركيبة")
            st.number_input("كمية الذرة (كجم):", 0, 1000, 500)
            st.number_input("كمية الصويا (كجم):", 0, 1000, 200)
            st.button("احسب التحليل النهائي")
        with col2:
            st.subheader("2️⃣ المهندس الذكي")
            st.write("اكتب البروتين المطلوب والبرنامج يقترح الخلطة")
            st.slider("البروتين المستهدف %", 12, 22, 18)
            st.button("توليد أفضل خلطة بأقل سعر")

# --- القسم الرابع: لوحة التحكم (لتفعيل وضع المدير) ---
with tab4:
    st.subheader("🔐 لوحة تحكم المدير")
    pwd = st.text_input("أدخل الباسورد لفتح الأقسام وتعديل الأسعار:", type="password")
    if pwd == "admin123":
        st.session_state.is_admin = True
        st.success("أهلاً بك يا هندسة! تم فتح جميع أقسام البرنامج.")
        if st.button("تسجيل الخروج (قفل الأقسام ثانية)"):
            st.session_state.is_admin = False
            st.rerun()
    else:
        st.session_state.is_admin = False
        st.info("سجل دخولك بـ admin123 عشان تجرب كل حاجة.")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تطوير: منظومة المربي الذكي 2026</p>", unsafe_allow_html=True)
