import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(page_title="مستشار التسمين - البورصة", layout="wide")

# 2. تصميم "الفخامة الرقمية" وتنسيق الجداول
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0d1a10 0%, #1b3d26 100%) !important;
    }
    .main-title {
        color: #ffffff;
        text-align: center;
        font-size: 32px !important;
        font-weight: 900;
        padding: 20px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }
    /* تنسيق الجدول ليكون مثل ميست */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 18px;
        text-align: right;
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border-radius: 15px;
        overflow: hidden;
    }
    .styled-table thead tr {
        background-color: #2ecc71;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
    }
    .styled-table th, .styled-table td {
        padding: 12px 15px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    .styled-table tbody tr:nth-of-type(even) {
        background-color: rgba(255, 255, 255, 0.02);
    }
    /* تأثير القزاز للتبويبات */
    .stTabs {
        background: rgba(255, 255, 255, 0.07) !important;
        backdrop-filter: blur(15px);
        border-radius: 20px !important;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📈 بورصة الخامات والعملات العالمية</h1>', unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["💎 مركز البورصة", "🧪 ماكينة الخلط", "💵 الأرباح"])

with tab1:
    sub1, sub2 = st.tabs(["🌾 جدول الخامات (نظام ميست)", "🌍 العملات والذهب"])
    
    with sub1:
        st.subheader("📊 الأسعار الاسترشادية للسلع بالجنيه")
        
        # تصميم الجدول بنفس أعمدة ميست
        html_table = """
        <table class="styled-table">
            <thead>
                <tr>
                    <th>اسم السلعة</th>
                    <th>سعر الطن</th>
                    <th>التغيير</th>
                    <th>ملاحظات</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>ذرة صفراء (أرجنتيني)</td><td>13,500</td><td style="color:#e74c3c;">-100</td><td>صب أرضه</td></tr>
                <tr><td>ذرة صفراء (برازيلي)</td><td>13,500</td><td style="color:#e74c3c;">-100</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا 44% (محلي)</td><td>24,000</td><td style="color:#2ecc71;">+200</td><td>صب أرضه</td></tr>
                <tr><td>كسب صويا 46% (محلي)</td><td>25,200</td><td>-</td><td>صب أرضه</td></tr>
                <tr><td>ردة خشنة (نخالة)</td><td>11,200</td><td>-</td><td>تعبئة وصال</td></tr>
                <tr><td>دي دي جي (DDGS)</td><td>18,500</td><td style="color:#2ecc71;">+50</td><td>معبأ أرضه</td></tr>
                <tr><td>گلوتين مستورد</td><td>42,000</td><td>-</td><td>صب أرضه</td></tr>
            </tbody>
        </table>
        """
        st.markdown(html_table, unsafe_allow_html=True)

    with sub2:
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### 💵 العملات")
            st.metric("الدولار الأمريكي", "48.30 ج")
            st.metric("اليورو الأوروبي", "52.10 ج")
        with col_b:
            st.markdown("### 🏆 المعادن")
            st.metric("ذهب عيار 24", "3,850 ج")
            st.metric("الفضة (أوقية)", "1,520 ج")

with tab2:
    st.subheader("🧪 تركيب الخلطة")
    c1, c2 = st.columns(2)
    with c1:
        st.number_input("الذرة:", value=500)
        st.number_input("الصويا:", value=200)
    with c2:
        st.number_input("البدائل:", value=150)
        st.number_input("سوبر بريمكس:", value=30)

with tab3:
    st.markdown('<div style="background: rgba(46, 204, 113, 0.2); padding:30px; border-radius:20px; text-align:center;"><h2>صافي الربح المتوقع</h2><h1 style="color:#2ecc71 !important;">85,000 ج.م</h1></div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; opacity:0.5;'>تصميم مستوحى من بورصة ميست العالمية - سوبر بريمكس 2026</p>", unsafe_allow_html=True)
