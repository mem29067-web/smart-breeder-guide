import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الفخمة
st.set_page_config(page_title="منظومة المربي الذكي Pro", layout="wide")

# 2. هندسة الواجهة (Dark Metallic + RTL + Premium Locking)
st.markdown(f"""
    <style>
    .main {{ direction: rtl; text-align: right; }}
    .stApp {{ background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important; }}
    .main-title {{ color: #ffffff; text-align: center; font-size: 35px !important; font-weight: 900; padding: 20px; text-shadow: 2px 2px 10px #000; }}
    
    /* ستايل الجداول */
    .custom-table {{ 
        width: 100%; border-collapse: collapse; 
        background-color: rgba(255, 255, 255, 0.05); color: white; 
        border-radius: 15px; overflow: hidden; direction: rtl; margin-bottom: 25px;
    }}
    .custom-table thead tr {{ background-color: #1e7e34; color: #ffffff; }}
    .custom-table th, .custom-table td {{ padding: 12px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); text-align: center; }}
    .custom-table td:first-child {{ text-align: right; font-weight: bold; background-color: rgba(40, 167, 69, 0.1); }}
    
    /* قفل الأقسام البريميوم */
    .locked-section {{
        background: rgba(0,0,0,0.85);
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        border: 2px dashed #f1c40f;
        margin-top: 20px;
    }}
    .premium-text {{ color: #f1c40f; font-size: 24px; font-weight: bold; margin-bottom: 15px; }}
    .whatsapp-btn {{
        background-color: #25d366; color: white !important; padding: 10px 25px;
        border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-block;
    }}
    
    label, p, h1, h2, h3, .stTabs [data-baseweb="tab"] {{ color: #ffffff !important; font-weight: bold !important; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">🚜 منظومة المربي الذكي: النسخة الاحترافية</h1>', unsafe_allow_html=True)

# 3. مخزن البيانات الافتراضي (يمكنك تعديله من لوحة التحكم بالداخل)
if 'prices' not in st.session_state:
    st.session_state.prices = {
        "ذرة أرجنتيني": "13,500", "ذرة برازيلي": "13,500", "ذرة أوكراني": "12,200",
        "صويا 44%": "24,000", "صويا 46%": "25,000", "ردة محلي": "11,200",
        "جيلوتين": "42,000", "دي دي جي": "18,500", "زيت صويا": "52,000"
    }

# رسالة القفل الموحدة
def premium_lock():
    st.markdown(f"""
    <div class="locked-section">
        <div class="premium-text">🔒 هذا القسم متاح للمشتركين فقط</div>
        <p>للاشتراك في باقة "المربي الذكي" والوصول للحاسبة والتحاليل الكاملة:</p>
        <a href="https://wa.me/201090102035" class="whatsapp-btn">تواصل عبر واتساب: 01090102035</a>
    </div>
    """, unsafe_allow_html=True)

# 4. الأقسام الرئيسية (Tabs)
tab1, tab2, tab3, tab4 = st.tabs(["💰 اسعار الخامات", "🔬 تحليل خامات الأعلاف", "🧮 حاسبة الأعلاف", "⚙️ الإدارة"])

# --- القسم الأول: الأسعار (مجاني) ---
with tab1:
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.markdown("### 📊 بورصة الخامات (تحديث لحظي)")
        html_prices = f"""
        <table class="custom-table">
            <thead><tr><th>الخامة</th><th>السعر (طن)</th><th>التغيير</th></tr></thead>
            <tbody>
                {"".join([f"<tr><td>{k}</td><td>{v}</td><td>-</td></tr>" for k, v in st.session_state.prices.items()])}
            </tbody>
        </table>"""
        st.markdown(html_prices, unsafe_allow_html=True)
    with col_b:
        st.metric("الدولار الأمريكي", "48.40 ج")
        st.metric("ذهب عيار 24", "3,850 ج")

# --- القسم الثاني: تحليل الخامات (مغلق بالكامل) ---
with tab2:
    premium_lock()

# --- القسم الثالث: حاسبة الأعلاف (مغلق بالكامل) ---
with tab3:
    premium_lock()

# --- القسم الرابع: لوحة التحكم (خاصة بك) ---
with tab4:
    st.subheader("🔐 إدارة النظام")
    pwd = st.text_input("باسورد المدير:", type="password")
    if pwd == "admin123":
        st.success("مرحباً يا هندسة! عدل الأسعار هنا:")
        for x in st.session_state.prices:
            st.session_state.prices[x] = st.text_input(f"سعر {x}:", value=st.session_state.prices[x])
        if st.button("حفظ جميع التعديلات"):
            st.rerun()
    else:
        st.info("سجل دخولك لتعديل بيانات البورصة.")

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تطوير: منظومة المربي الذكي 2026 | جميع الحقوق محفوظة</p>", unsafe_allow_html=True)
