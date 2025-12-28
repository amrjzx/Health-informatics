import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json

# ==============================================================================
# 1. INTERNATIONALIZATION (قاموس اللغات)
# ==============================================================================
LANGUAGES = {
    "العربية": {
        "title": "BioSmart: مختبر المعلوماتية الصحية",
        "home": "🏠 لوحة التحكم",
        "fhir": "🧬 مختبر التوافقية (FHIR)",
        "ai": "🤖 محرك التنبؤ الإكلينيكي",
        "risk_score": "نسبة الخطورة",
        "name": "اسم المريض",
        "generate": "توليد ملف JSON",
        "lang_label": "اختر اللغة",
        "welcome": "أهلاً بك في منصة المعلوماتية العالمية",
        "desc": "نحن نحول البيانات إلى حكمة سريرية لإنقاذ الأرواح."
    },
    "English": {
        "title": "BioSmart: Health Informatics Lab",
        "home": "🏠 Dashboard",
        "fhir": "🧬 Interoperability (FHIR)",
        "ai": "🤖 Clinical Prediction AI",
        "risk_score": "Risk Score",
        "name": "Patient Name",
        "generate": "Generate JSON File",
        "lang_label": "Select Language",
        "welcome": "Welcome to Global Informatics Platform",
        "desc": "We transform data into clinical wisdom to save lives."
    },
    "Español": {
        "title": "BioSmart: Laboratorio de Informática",
        "home": "🏠 Panel de Control",
        "fhir": "🧬 Interoperabilidad (FHIR)",
        "ai": "🤖 IA de Predicción Clínica",
        "risk_score": "Puntuación de Riesgo",
        "name": "Nombre del Paciente",
        "generate": "Generar Archivo JSON",
        "welcome": "Bienvenido a la plataforma informática global",
        "desc": "Transformamos datos en sabiduría clínica para salvar vidas."
    },
    "Français": {
        "title": "BioSmart: Labo d'Informatique",
        "home": "🏠 Tableau de Bord",
        "fhir": "🧬 Interopérabilité (FHIR)",
        "ai": "🤖 IA de Prédiction Clinique",
        "risk_score": "Score de Risque",
        "name": "Nom du Patient",
        "generate": "Générer le fichier JSON",
        "welcome": "Bienvenue sur la plateforme informatique mondiale",
        "desc": "Nous transformons les données en sagesse clinique."
    }
}

# ==============================================================================
# 2. UI ENGINE & TRANSLATION LOGIC
# ==============================================================================
st.set_page_config(page_title="BioSmart Global", layout="wide")

# اختيار اللغة من الشريط الجانبي
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3859/3859284.png", width=80)
    st.divider()
    selected_lang = st.selectbox("🌐 " + LANGUAGES["English"]["lang_label"], list(LANGUAGES.keys()))
    L = LANGUAGES[selected_lang] # قاموس اللغة المختارة
    
    st.divider()
    menu = st.radio("Navigation", [L["home"], L["fhir"], L["ai"]])

# تحسين الشكل البصري
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;500;800&display=swap');
        * {{ font-family: 'Tajawal', sans-serif; text-align: {"right" if selected_lang == "العربية" else "left"}; }}
        .main-card {{ background: white; padding: 30px; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }}
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. APP MODULES
# ==============================================================================

if menu == L["home"]:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.title(L["title"])
    st.subheader(L["welcome"])
    st.write(L["desc"])
    
    
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Interoperability", "FHIR v4.0")
    col2.metric("Coding", "ICD-10-CM")
    col3.metric("Security", "HIPAA Ready")
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == L["fhir"]:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.header(L["fhir"])
    
    
    
    p_name = st.text_input(L["name"])
    if st.button(L["generate"]):
        fhir_res = {
            "resourceType": "Patient",
            "name": [{"family": p_name}],
            "status": "active"
        }
        st.json(fhir_res)
    st.markdown("</div>", unsafe_allow_html=True)

elif menu == L["ai"]:
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.header(L["ai"])
    age = st.slider("Age", 0, 100, 50)
    risk = age * 0.8 # محاكاة بسيطة
    
    st.subheader(f"{L['risk_score']}: {risk}%")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = risk,
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#3B82F6"}}
    ))
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"<hr><center><small>BioSmart Global | {selected_lang} Edition | LinkedIn Project</small></center>", unsafe_allow_html=True)
