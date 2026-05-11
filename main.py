import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. التنسيق البرمجي (الواجهة الميتاليك الاحترافية)
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

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: النسخة الشاملة</h1>', unsafe_allow_html=True)

# 3. إدارة البيانات وحالة الإدارة
if 'is_admin' not in st.session_state: st.session_state.is_admin = False

# قائمة الأسعار الكاملة (البورصة اللي كانت ناقصة)
if 'prices' not in st.session_state:
    st.session_state.prices = {
        "ذرة أرجنتيني": 13500, "ذرة برازيلي": 13500, "ذرة أوكراني": 12200,
        "صويا 44%": 24000, "صويا 46%": 25000, "صويا فول فات": 34000,
        "ردة محلي": 11200, "جيلوتين 60%": 42000, "دي دي جي (DDGS)": 18500,
        "قمح روسي 11.5%": 12500, "كسب عباد مستورد": 17500, "زيت صويا خام": 52000,
        "كسب سمسم": 21000, "كسر مكرونة": 13000, "بسكويت ناعم": 11500,
        "نواة بلح مفروم": 10000, "تفل برتقال": 4000
    }

def check_access():
    if not st.session_state.is_admin:
        st.markdown(f"""
        <div class="locked-section">
            <h2 style="color: #f1c40f;">🔒 القسم مغلق للمشتركين فقط</h2>
            <p style="font-size: 18px;">للحصول على التحاليل الفنية واستخدام الخلاط الذكي، يرجى الاشتراك</p>
            <a href="https://wa.me/201090102035" class="whatsapp-btn">تواصل واتساب: 01090102035</a>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True

tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- 1. أسعار الخامات (البورصة الكاملة) ---
with tab1:
    st.markdown("### 📊 بورصة الخامات المحدثة")
    html_prices = """<table class="custom-table"><thead><tr><th>الخامة</th><th>السعر (طن)</th><th>التغيير</th></tr></thead><tbody>"""
    for k, v in st.session_state.prices.items():
        html_prices += f"<tr><td>{k}</td><td>{v:,} ج</td><td>-</td></tr>"
    st.markdown(html_prices + "</tbody></table>", unsafe_allow_html=True)

# --- 2. تحليل الخامات (مقسم أساسي وبدائل) ---
with tab2:
    if check_access():
        st.success("🔓 وضع المدير نشط: موسوعة التحليل")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 🌾 خامات أساسية")
            st.markdown("""<table class="custom-table"><thead><tr><th>الخامة</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>88%</td></tr>
                <tr><td>صويا 46%</td><td>46%</td><td>78%</td></tr>
                <tr><td>ردة محلي</td><td>14%</td><td>65%</td></tr>
                <tr><td>جيلوتين 60%</td><td>60%</td><td>92%</td></tr>
                <tr><td>دي دي جي</td><td>27%</td><td>82%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)
        with c2:
            st.markdown("#### 💡 البدائل المبتكرة")
            st.markdown("""<table class="custom-table"><thead><tr><th>البديل</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>بسكويت مصانع</td><td>9%</td><td>95%</td></tr>
                <tr><td>شيكولاتة هالك</td><td>6%</td><td>98%</td></tr>
                <tr><td>بلح مفروم</td><td>4%</td><td>75%</td></tr>
                <tr><td>تفل برتقال</td><td>6.5%</td><td>70%</td></tr>
                <tr><td>كسر مكرونة</td><td>11%</td><td>90%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)

# --- 3. حاسبة الأعلاف (الخلاط العملاق بالبدائل) ---
with tab3:
    if check_access():
        st.subheader("🧮 الخلاط الذكي: احسب تركيبتك وبدائلك")
        col_c1, col_c2, col_c3 = st.columns(3)
        w_corn = col_c1.number_input("ذرة (كجم):", 0, 1000, 500)
        w_soy = col_c2.number_input("صويا (كجم):", 0, 1000, 200)
        w_bran = col_c3.number_input("ردة (كجم):", 0, 1000, 100)
        w_glu = col_c1.number_input("جيلوتين/دي دي جي (كجم):", 0, 1000, 50)
        w_alt = col_c2.number_input("إجمالي البدائل (كجم):", 0, 1000, 100)
        
        if st.button("🚀 احسب تحليل الخلطة"):
            total_w = w_corn + w_soy + w_bran + w_glu + w_alt
            prot = ((w_corn*8.5) + (w_soy*46) + (w_bran*14) + (w_glu*40) + (w_alt*8)) / total_w
            st.info(f"إجمالي الوزن: {total_w} كجم | البروتين المتوقع: {prot:.2f}%")

# --- 4. الإدارة (تسجيل الدخول الصحيح) ---
with tab4:
    st.subheader("🔐 لوحة تحكم المدير")
    if not st.session_state.is_admin:
        pwd = st.text_input("أدخل كلمة المرور السرية:", type="password")
        if st.button("تفعيل وضع المدير"):
            if pwd == "199208":
                st.session_state.is_admin = True
                st.success("تم الفتح بنجاح!")
                st.rerun()
            else:
                st.error("❌ الباسورد غلط")
    else:
        st.success("✅ وضع المدير نشط - جميع الأقسام مفتوحة")
        if st.button("قفل البرنامج (خروج)"):
            st.session_state.is_admin = False
            st.rerun()

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تطوير: منظومة المربي الذكي 2026</p>", unsafe_allow_html=True)
