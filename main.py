import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. التنسيق البرمجي (RTL + Dark Style)
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

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: المرجع العالمي</h1>', unsafe_allow_html=True)

# 3. إدارة البيانات وحالة الإدارة (Session State)
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

if 'prices' not in st.session_state:
    st.session_state.prices = {
        "ذرة أرجنتيني": 13500, "ذرة برازيلي": 13500, "صويا 46%": 25000,
        "ردة محلي": 11200, "جيلوتين": 42000, "دي دي جي": 18500,
        "كسب عباد": 17500, "بسكويت ناعم": 11500, "نواة بلح مفروم": 10000
    }

# دالة القفل (تمنع الدخول لو مش مدير)
def check_access():
    if not st.session_state.is_admin:
        st.markdown(f"""
        <div class="locked-section">
            <h2 style="color: #f1c40f;">🔒 القسم مغلق للمشتركين فقط</h2>
            <p>للوصول للتحاليل الكاملة والحاسبة المتطورة، يرجى الاشتراك</p>
            <a href="https://wa.me/201090102035" class="whatsapp-btn">تواصل واتساب للاشتراك: 01090102035</a>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True

tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- 1. أسعار الخامات (مفتوح) ---
with tab1:
    st.markdown("### 📊 بورصة الخامات المحدثة")
    html_prices = """<table class="custom-table"><thead><tr><th>الخامة</th><th>السعر (طن)</th></tr></thead><tbody>"""
    for k, v in st.session_state.prices.items():
        html_prices += f"<tr><td>{k}</td><td>{v:,} ج</td></tr>"
    st.markdown(html_prices + "</tbody></table>", unsafe_allow_html=True)

# --- 2. تحليل الخامات (مغلق) ---
with tab2:
    if check_access():
        st.success("🔓 وضع المدير نشط: تم فتح الجداول")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### 🌾 خامات أساسية")
            st.markdown("""<table class="custom-table"><thead><tr><th>الخامة</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>88%</td></tr>
                <tr><td>صويا 46%</td><td>46%</td><td>78%</td></tr>
                <tr><td>جيلوتين 60%</td><td>60%</td><td>92%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)
        with c2:
            st.markdown("#### 💡 البدائل")
            st.markdown("""<table class="custom-table"><thead><tr><th>البديل</th><th>بروتين %</th><th>طاقة %</th></tr></thead><tbody>
                <tr><td>بسكويت مصانع</td><td>9%</td><td>95%</td></tr>
                <tr><td>تفل برتقال</td><td>6.5%</td><td>70%</td></tr>
                <tr><td>نواة بلح</td><td>6%</td><td>60%</td></tr>
            </tbody></table>""", unsafe_allow_html=True)

# --- 3. حاسبة الأعلاف (مغلق) ---
with tab3:
    if check_access():
        st.subheader("🧮 الخلاط الذكي (يشمل البدائل)")
        col_calc1, col_calc2 = st.columns(2)
        with col_calc1:
            w_c = st.number_input("ذرة (كجم):", 0, 1000, 500)
            w_s = st.number_input("صويا (كجم):", 0, 1000, 200)
        with col_calc2:
            w_a = st.number_input("بدائل (كجم):", 0, 1000, 100)
        
        if st.button("🚀 احسب التركيبة"):
            total = w_c + w_s + w_a
            prot = ((w_c*8.5) + (w_s*46) + (w_a*9)) / total
            st.info(f"إجمالي الوزن: {total} كجم | البروتين: {prot:.2f}%")

# --- 4. الإدارة (السر هنا) ---
with tab4:
    st.subheader("🔐 لوحة التحكم")
    # 1. السطر بتاع الباسورد
    pwd = st.text_input("أدخل كلمة المرور السرية:", type="password")
    
    if pwd == "199208": # الباسورد اللي كان في الصورة
        # 2. السطر اللي بيفعل وضع المدير
        st.session_state.is_admin = True
        st.success("✅ تم تفعيل وضع المدير بنجاح. يمكنك الآن تصفح الحاسبة والتحاليل.")
        
        st.divider()
        if st.button("قفل البرنامج (تسجيل خروج)"):
            st.session_state.is_admin = False
            st.rerun()
    elif pwd != "":
        st.error("❌ كلمة المرور غير صحيحة")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>منظومة المربي الذكي 2026</p>", unsafe_allow_html=True)
