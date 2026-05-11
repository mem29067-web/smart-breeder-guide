import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. هندسة الواجهة (Dark Metallic + RTL)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stApp { background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }
    .main-title { color: #ffffff; text-align: center; font-size: 35px !important; font-weight: 900; padding: 20px; }
    
    /* ستايل الجداول */
    .custom-table { 
        width: 100%; border-collapse: collapse; 
        background-color: rgba(255, 255, 255, 0.05); color: white; 
        border-radius: 15px; overflow: hidden; direction: rtl; margin-bottom: 25px;
    }
    .custom-table thead tr { background-color: #1e7e34; color: #ffffff; }
    .custom-table th, .custom-table td { padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }
    .custom-table td:first-child { text-align: right; font-weight: bold; background-color: rgba(40, 167, 69, 0.1); }
    
    /* قفل الأقسام البريميوم */
    .locked-section {
        background: rgba(0,0,0,0.9); padding: 60px; border-radius: 20px;
        text-align: center; border: 2px dashed #f1c40f; margin-top: 20px;
    }
    .whatsapp-btn {
        background-color: #25d366; color: white !important; padding: 12px 30px;
        border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block; font-size: 18px;
    }
    
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] { color: #ffffff !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: النسخة الاحترافية</h1>', unsafe_allow_html=True)

# 3. إدارة الحالة والبيانات
if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

if 'prices' not in st.session_state:
    st.session_state.prices = {
        "ذرة أرجنتيني": "13,500", "ذرة برازيلي": "13,500", "ذرة أوكراني": "12,200",
        "كسب صويا 44%": "24,000", "كسب صويا 46%": "25,000", "ردة محلي": "11,200",
        "جيلوتين مستورد": "42,000", "دي دي جي": "18,500", "زيت صويا خام": "52,000"
    }

# دالة القفل الموحدة
def check_access():
    if not st.session_state.is_admin:
        st.markdown(f"""
        <div class="locked-section">
            <h2 style="color: #f1c40f;">🔒 القسم مغلق للمشتركين فقط</h2>
            <p style="font-size: 18px;">للحصول على التحاليل الكاملة واستخدام حاسبة الأعلاف المتطورة، يرجى الاشتراك</p>
            <br>
            <a href="https://wa.me/201090102035" class="whatsapp-btn">اضغط هنا للاشتراك عبر واتساب: 01090102035</a>
        </div>
        """, unsafe_allow_html=True)
        return False
    return True

# 4. الأقسام الرئيسية
tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- القسم الأول: الأسعار (مفتوح للجميع) ---
with tab1:
    st.markdown("### 📊 بورصة الخامات اليومية")
    html_prices = """<table class="custom-table"><thead><tr><th>الخامة</th><th>السعر (طن)</th><th>التغيير</th></tr></thead><tbody>"""
    for k, v in st.session_state.prices.items():
        html_prices += f"<tr><td>{k}</td><td>{v}</td><td>-</td></tr>"
    html_prices += "</tbody></table>"
    st.markdown(html_prices, unsafe_allow_html=True)

# --- القسم الثاني: التحليل (مغلق) ---
with tab2:
    if check_access():
        st.success("🔓 وضع المدير نشط: يمكنك رؤية موسوعة التحاليل")
        html_analysis = """
        <table class="custom-table">
            <thead><tr><th>الخامة</th><th>بروتين %</th><th>طاقة (Kcal)</th><th>ألياف %</th></tr></thead>
            <tbody>
                <tr><td>ذرة صفراء</td><td>8.5%</td><td>3350</td><td>2.2%</td></tr>
                <tr><td>كسب صويا 46%</td><td>46%</td><td>2450</td><td>6.0%</td></tr>
                <tr><td>بسكويت مصانع</td><td>9%</td><td>3800</td><td>1.5%</td></tr>
                <tr><td>شيكولاتة هالك</td><td>6%</td><td>4200</td><td>2.0%</td></tr>
                <tr><td>بلح مفروم</td><td>4%</td><td>2900</td><td>10.0%</td></tr>
                <tr><td>تفل برتقال مجفف</td><td>6.5%</td><td>2600</td><td>12.0%</td></tr>
                <tr><td>كسب سمسم</td><td>42%</td><td>3100</td><td>6.5%</td></tr>
                <tr><td>كسر مكرونة</td><td>11%</td><td>3500</td><td>0.5%</td></tr>
                <tr><td>نواة بلح مفرومة</td><td>6%</td><td>2400</td><td>15.0%</td></tr>
            </tbody>
        </table>"""
        st.markdown(html_analysis, unsafe_allow_html=True)

# --- القسم الثالث: الحاسبة (مغلق) ---
with tab3:
    if check_access():
        st.success("🔓 وضع المدير نشط: الحاسبة جاهزة للاستخدام")
        c1, c2 = st.columns(2)
        with c1:
            st.subheader("🛠️ حساب تركيبة يدوية")
            st.multiselect("اختر خاماتك:", list(st.session_state.prices.keys()))
            st.number_input("الكمية بالطن:", 0.1, 10.0, 1.0)
            st.button("احسب القيمة الغذائية")
        with c2:
            st.subheader("🎯 المهندس الذكي (تكوين آلي)")
            st.number_input("البروتين المطلوب %:", 12, 22, 18)
            st.number_input("الطاقة المطلوبة:", 2500, 3500, 3000)
            st.button("اقترح أرخص خلطة")

# --- القسم الرابع: الإدارة (البواب) ---
with tab4:
    st.subheader("🔐 لوحة تحكم المدير")
    pwd = st.text_input("أدخل كلمة المرور السرية:", type="password")
    if pwd == "admin123":
        st.session_state.is_admin = True
        st.success("تم فتح البرنامج بالكامل! يمكنك الآن تصفح كل الأقسام.")
        
        st.divider()
        st.write("📝 **تعديل الأسعار:**")
        target = st.selectbox("اختر الخامة لتعديل سعرها:", list(st.session_state.prices.keys()))
        new_val = st.text_input(f"السعر الجديد لـ {target}:", value=st.session_state.prices[target])
        if st.button("حفظ التعديلات"):
            st.session_state.prices[target] = new_val
            st.rerun()
            
        if st.button("تسجيل الخروج (قفل البرنامج)"):
            st.session_state.is_admin = False
            st.rerun()
    else:
        st.warning("هذا القسم مخصص للإدارة فقط. استخدم الباسورد admin123 للتجربة.")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تطوير: منظومة المربي الذكي 2026</p>", unsafe_allow_html=True)
