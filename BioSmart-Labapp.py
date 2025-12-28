import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# ==============================================================================
# 1. THEME & CORE UI ENGINE
# ==============================================================================
st.set_page_config(
    page_title="BioSmart Pro | Health Informatics Lab",
    layout="wide",
    page_icon="🧬"
)

class BioSmartUI:
    """Class to manage the professional look and feel"""
    @staticmethod
    def apply_styles():
        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Tajawal:wght@400;700;900&display=swap');
            
            :root {
                --primary: #0F172A;
                --accent: #3B82F6;
                --bg: #F8FAFC;
            }

            .stApp { background-color: var(--bg); font-family: 'Tajawal', sans-serif; }
            
            .main-card {
                background: white;
                padding: 2rem;
                border-radius: 1.2rem;
                box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05);
                border: 1px solid #E2E8F0;
                margin-bottom: 1.5rem;
            }

            .ai-badge {
                background: linear-gradient(90deg, #3B82F6, #2DD4BF);
                color: white;
                padding: 5px 15px;
                border-radius: 50px;
                font-weight: bold;
                font-size: 0.8rem;
            }

            .sidebar-text { font-size: 0.9rem; color: #64748B; }
        </style>
        """, unsafe_allow_html=True)

# ==============================================================================
# 2. INFORMATICS KNOWLEDGE & DATA ENGINE
# ==============================================================================
class InformaticsEngine:
    """Class to handle datasets, scientific references, and AI simulation"""
    
    @staticmethod
    def get_icd10_data():
        return pd.DataFrame({
            'Code': ['E11.9', 'I10', 'J45.9', 'N18.9', 'I50.9'],
            'Description': [
                'سكري النوع الثاني (بدون مضاعفات)',
                'ارتفاع ضغط الدم الأساسي',
                'الربو الشعبي غير المحدد',
                'الفشل الكلوي المزمن',
                'فشل القلب الاحتقاني'
            ],
            'System': 'ICD-10-CM'
        })

    @staticmethod
    def get_loinc_data():
        return pd.DataFrame({
            'LOINC ID': ['2339-0', '4544-3', '2160-0', '718-7'],
            'Test Name': ['Glucose [Mass/Vol] in Blood', 'HbA1c', 'Creatinine', 'Hemoglobin'],
            'Category': ['Lab - Chemistry', 'Lab - Endocrinology', 'Lab - Renal', 'Lab - Hematology']
        })

    @staticmethod
    def simulate_ai_nlp(text):
        """Simulating a Clinical NLP Engine for Entity Extraction"""
        time.sleep(1.2) # Real-world latency simulation
        text = text.lower()
        results = []
        if "diabetes" in text or "سكري" in text:
            results.append({"Entity": "Diabetes Mellitus", "Code": "E11.9", "Confidence": "98%"})
        if "heart" in text or "قلب" in text:
            results.append({"Entity": "Heart Failure", "Code": "I50.9", "Confidence": "94%"})
        if "kidney" in text or "كلى" in text:
            results.append({"Entity": "Chronic Kidney Disease", "Code": "N18.9", "Confidence": "91%"})
        return results

# ==============================================================================
# 3. APPLICATION MODULES
# ==============================================================================
def render_header():
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown("<h1 style='color:#0F172A;'>BioSmart <span style='color:#3B82F6'>Pro Lab</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748B;'>Advanced Health Informatics & Predictive Analytics Platform</p>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div style='text-align:right;'><span class='ai-badge'>AI ACTIVE</span></div>", unsafe_allow_html=True)

def main():
    BioSmartUI.apply_styles()
    engine = InformaticsEngine()

    # --- Sidebar ---
    with st.sidebar:
        st.markdown("## 🛠️ المختبرات")
        app_mode = st.radio("", ["الموسوعة المرجعية", "محرك تحليل الـ AI", "صحة المجتمع (Analytics)"], label_visibility="collapsed")
        st.divider()
        st.markdown("### 🧬 مصادر علمية")
        st.caption("- HIMSS Interoperability Standards")
        st.caption("- HL7 FHIR Implementation Guide")
        st.caption("- ICD-10 Coding Clinic")

    render_header()

    # --- MODULE 1: ENCYCLOPEDIA ---
    if app_mode == "الموسوعة المرجعية":
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("📚 مكتبة المعايير الدولية")
        st.write("بيانات مرجعية أساسية يحتاجها مهندس المعلوماتية الصحية للمطالعة والترميز.")
        
        tab_icd, tab_loinc, tab_hipaa = st.tabs(["ICD-10 (التشخيصات)", "LOINC (المختبرات)", "HIPAA (أمن البيانات)"])
        
        with tab_icd:
            st.dataframe(engine.get_icd10_data(), use_container_width=True)
            st.info("تستخدم أكواد ICD-10 لتوحيد تشخيص الأمراض عالمياً وتسهيل عمليات الفوترة والإحصاء.")
            

        with tab_loinc:
            st.table(engine.get_loinc_data())
            st.info("معيار LOINC هو اللغة العالمية لتعريف الفحوصات المخبرية والقياسات الطبية.")
            
        with tab_hipaa:
            st.markdown("""
            ### 🛡️ قائمة تدقيق HIPAA (أمن الخصوصية)
            1. **Administrative Safeguards:** تدريب الموظفين وإدارة الوصول.
            2. **Physical Safeguards:** تأمين الخوادم والأجهزة المادية.
            3. **Technical Safeguards:** تشفير البيانات (Encryption) وأنظمة التحقق.
            """)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- MODULE 2: AI ENGINE ---
    elif app_mode == "محرك تحليل الـ AI":
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("🤖 محاكي الـ NLP السريري")
        st.write("أدخل ملاحظة طبية غير منظمة وسيقوم الذكاء الاصطناعي باستخراج الكيانات الطبية وترميزها.")
        
        clinical_note = st.text_area("أدخل ملاحظات الطبيب هنا (مثلاً: مريض يعاني من السكري وفشل في القلب):", height=150)
        
        if st.button("تحليل البيانات الآن ✨"):
            if clinical_note:
                results = engine.simulate_ai_nlp(clinical_note)
                if results:
                    st.success("تم تحليل النص بنجاح!")
                    st.table(pd.DataFrame(results))
                else:
                    st.warning("لم يتم التعرف على كيانات طبية مدعومة. جرب كلمات مثل 'سكري' أو 'قلب'.")
            else:
                st.error("يرجى إدخال نص أولاً.")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- MODULE 3: ANALYTICS ---
    elif app_mode == "صحة المجتمع (Analytics)":
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.header("📊 تحليلات صحة المجتمع (Population Health)")
        
        # Simulated Analytics Data
        analytics_df = pd.DataFrame({
            'Condition': ['Diabetes', 'Hypertension', 'Asthma', 'Kidney Failure'],
            'Prevalence (%)': [15, 28, 10, 5],
            'AI Risk Prediction': [18, 32, 12, 8]
        })
        
        fig = px.bar(analytics_df, x='Condition', y=['Prevalence (%)', 'AI Risk Prediction'],
                     barmode='group', title="مقارنة بين الانتشار الحالي وتوقعات الذكاء الاصطناعي (2026)",
                     color_discrete_sequence=['#1E3A8A', '#3B82F6'])
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        **دراسة مرجعية:** بناءً على دراسات *Predictive Analytics in Population Health (2024)*، 
        تساعد هذه الرسوم البيانية صُناع القرار على توجيه الموارد الطبية للمناطق الأكثر عرضة للخطر.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- Footer ---
    st.markdown("---")
    st.markdown("<center style='color:gray;'>BioSmart Informatics Hub | Developed for LinkedIn Portfolio | 2025</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
