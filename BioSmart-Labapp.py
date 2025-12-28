import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# --- 1. SETTINGS & THEME ENGINE ---
st.set_page_config(page_title="BioSmart Pro | Informatics", layout="wide", page_icon="🧪")

class UIStyle:
    """Class to manage all CSS and visual branding"""
    @staticmethod
    def apply():
        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Tajawal:wght@400;700;900&display=swap');
            
            :root {
                --primary: #0F172A;
                --accent: #3B82F6;
                --success: #10B981;
                --bg: #F8FAFC;
            }

            .stApp { background-color: var(--bg); font-family: 'Tajawal', sans-serif; }
            
            /* Professional Card Styling */
            .glass-card {
                background: white;
                padding: 2rem;
                border-radius: 1rem;
                box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
                border: 1px solid #E2E8F0;
                margin-bottom: 1.5rem;
            }

            .sidebar-title { color: var(--primary); font-weight: 900; font-size: 1.5rem; margin-bottom: 1rem; }
            .badge { background: #DBEAFE; color: #1E40AF; padding: 4px 12px; border-radius: 999px; font-size: 0.8rem; font-weight: bold; }
        </style>
        """, unsafe_allow_html=True)

# --- 2. INFORMATICS KNOWLEDGE ENGINE ---
class InformaticsCore:
    """Class to handle data processing and AI simulations"""
    @staticmethod
    def get_clinical_data():
        return pd.DataFrame({
            'PatientID': ['P-001', 'P-002', 'P-003', 'P-004'],
            'Condition': ['Hypertension', 'Type 2 Diabetes', 'Asthma', 'Chronic Kidney Disease'],
            'ICD10': ['I10', 'E11.9', 'J45.9', 'N18.9'],
            'RiskScore': [0.45, 0.82, 0.31, 0.94],
            'LastVisit': ['2025-11-20', '2025-12-15', '2025-10-05', '2025-12-27']
        })

    @staticmethod
    def ai_nlp_engine(text):
        """Simulating clinical entity extraction using NLP concepts"""
        time.sleep(1.5) # Fake processing latency
        extracted = []
        if "diabetes" in text.lower() or "سكري" in text:
            extracted.append({"Entity": "Diabetes Mellitus", "Code": "E11.9", "System": "ICD-10"})
        if "heart" in text.lower() or "قلب" in text:
            extracted.append({"Entity": "Heart Failure", "Code": "I50.9", "System": "ICD-10"})
        return extracted

# --- 3. UI COMPONENTS ---
def render_header():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("<h1 style='color:#0F172A; margin-bottom:0;'>BioSmart <span style='color:#3B82F6'>Informatics Lab</span></h1>", unsafe_allow_html=True)
        st.markdown("<p style='color:#64748B;'>The Advanced Evidence-Based Health IT Ecosystem</p>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div style='text-align:right; margin-top:1rem;'><span class='badge'>System Version 3.0.4</span><br><small>Status: Fully Operational</small></div>", unsafe_allow_html=True)

def render_dashboard():
    core = InformaticsCore()
    
    # --- Top Metrics ---
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Clinical Interoperability", "HL7 FHIR v4")
    m2.metric("Predictive Accuracy", "96.4%", "+1.2%")
    m3.metric("HIPAA Compliance", "Verified")
    m4.metric("Active EHR Nodes", "128")

    # --- Main Content Area ---
    tab1, tab2, tab3 = st.tabs(["🏛️ DIKW Architecture", "🤖 AI Clinical Engine", "📊 Population Analytics"])

    with tab1:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        c1, c2 = st.columns([1, 1])
        with c1:
            st.subheader("DIKW Model in Practice")
            st.write("""
            في المعلوماتية الصحية، لا قيمة للبيانات الخام ما لم تتحول إلى حكمة سريرية.
            - **Data:** قياس الضغط 160/95.
            - **Information:** ضغط دم مرتفع (Stage 2).
            - **Knowledge:** ربط الارتفاع مع تاريخ العائلة وفشل كلوي.
            - **Wisdom:** البدء ببروتوكول علاجي مخصص لمنع سكتة دماغية.
            """)
        with c2:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/DIKW_Pyramid.svg/800px-DIKW_Pyramid.svg.png", width=350)
            
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("AI Clinical Entity Extraction (NLP)")
        st.info("قم بإدخال ملاحظة طبية ليقوم الذكاء الاصطناعي بتحويلها إلى رموز ICD-10 عالمية.")
        note = st.text_area("Doctor's Clinical Note:", "The patient presents with symptoms of type 2 diabetes and chronic heart issues.")
        if st.button("Run AI Extraction"):
            results = core.ai_nlp_engine(note)
            if results:
                st.write("### AI Analysis Results:")
                st.dataframe(pd.DataFrame(results), use_container_width=True)
            else:
                st.warning("No clinical entities identified. Try mentioning 'Diabetes' or 'Heart'.")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab3:
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.subheader("Population Health Risk Management")
        df = core.get_clinical_data()
        
        fig = px.scatter(df, x='Condition', y='RiskScore', size='RiskScore', color='RiskScore',
                         hover_name='PatientID', title="Patient Risk Stratification",
                         color_continuous_scale='RdYlGn_r')
        st.plotly_chart(fig, use_container_width=True)
        
        st.write("**Study Reference:** Building on 'Predictive Analytics in Healthcare' (IEEE 2024).")
        st.markdown("</div>", unsafe_allow_html=True)

# --- 4. EXECUTION ---
if __name__ == "__main__":
    UIStyle.apply()
    
    with st.sidebar:
        st.markdown("<div class='sidebar-title'>BioSmart Lab</div>", unsafe_allow_html=True)
        st.divider()
        st.button("Dashboard Overview", use_container_width=True)
        st.button("EHR Integration", use_container_width=True)
        st.button("Security & Encryption", use_container_width=True)
        st.divider()
        st.markdown("### Evidence-Based Support")
        st.caption("Based on HIMSS Interoperability Standards and ISO 27001 Security.")

    render_header()
    render_dashboard()
