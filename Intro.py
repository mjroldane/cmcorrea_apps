import streamlit as st

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="Portafolio IA", page_icon="✨", layout="wide")

# =========================
# 🎨 ESTILOS PRO
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eef2ff, #e0f7fa);
}

h1 {
    text-align: center;
    font-size: 42px;
    background: linear-gradient(90deg, #7b2ff7, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* CARD */
.card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    padding: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    transition: 0.3s;
    margin-bottom: 15px;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 0 25px rgba(123,47,247,0.3);
}

.card h3 {
    color: #2d1b69;
}

.card p {
    color: #444;
}

.stLinkButton a {
    background: linear-gradient(90deg, #7b2ff7, #00c6ff) !important;
    color: white !important;
    border-radius: 10px;
    padding: 8px 14px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🧩 FUNCIÓN CARD (IMPORTANTE)
# =========================
def card(icono, titulo, descripcion, url):
    st.markdown(f"""
    <div class="card">
        <h3>{icono} {titulo}</h3>
        <p>{descripcion}</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Abrir", url)

# =========================
# HEADER
# =========================
st.markdown("<h1>✨ Portafolio de Aplicaciones de IA</h1>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# 👁️ VISIÓN
# =========================
st.markdown("## 👁️ Visión por Computador")
col1, col2, col3 = st.columns(3)

with col1:
    card("🔍", "YOLO", "Detección de objetos", "https://yolov5-mjroldane.streamlit.app/")
    card("👁️", "Visión IA", "Análisis visual", "https://visionapproldan-04.streamlit.app/")

with col2:
    card("🧾", "OCR", "Texto desde imágenes", "https://ocr-roldan-mj.streamlit.app/")
    card("🎧", "OCR + Audio", "Multimodal", "https://ocr-audio-roldan-mj.streamlit.app/")

with col3:
    card("✋", "Hand Tracking", "Seguimiento de manos", "https://hand-w-roldan.streamlit.app/")
    card("🎨", "Dibujo IA", "Reconocimiento de dibujos", "https://drawrecog-roldan664.streamlit.app/")

# =========================
# 💬 NLP
# =========================
st.markdown("## 💬 NLP")
col4, col5, col6 = st.columns(3)

with col4:
    card("🌐", "Traductor", "Traducción automática", "https://traductor-mjroldane.streamlit.app/")
    card("☁️", "WordCloud", "Nube de palabras", "https://wordcloud-mjroldan.streamlit.app/")

with col5:
    card("📊", "TF-IDF", "Análisis de texto", "https://mjroldane-tf-idf.streamlit.app/")
    card("📈", "TF-IDF Español", "Versión español", "https://tdfesp-mjroldane.streamlit.app/")

with col6:
    card("😊", "Sentimiento", "Análisis emocional", "https://sentimenta-mjroldane.streamlit.app/")
    card("💬", "Chat PDF", "Chat con documentos", "https://chatpdfroldan-nu3nuywn5722x6n4muvam8.streamlit.app/")

# =========================
# 🎤 AUDIO
# =========================
st.markdown("## 🎤 Audio")
col7, col8 = st.columns(2)

with col7:
    card("🎤", "Texto a Voz", "Conversión a audio", "https://tm-mjroldane.streamlit.app/")
    card("🎙️", "Control por Voz", "Comandos por voz", "https://ctrlvoicemajo-9.streamlit.app/")

with col8:
    card("🎧", "Audio IA", "Procesamiento", "https://ocr-audio-roldan-mj.streamlit.app/")

# =========================
# 📊 DATOS
# =========================
st.markdown("## 📊 Datos")
col9, col10 = st.columns(2)

with col9:
    card("📋", "Dashboard", "Visualización", "https://tablero-roldan-123.streamlit.app/")
    card("🧠", "Apps Generales", "Colección", "https://major-apps-24.streamlit.app/")

with col10:
    card("📜", "Historia Informática", "Evolución", "https://histinf-roldan.streamlit.app/")

# =========================
# 📡 IoT
# =========================
st.markdown("## 📡 IoT")
col11, col12 = st.columns(2)

with col11:
    card("📡", "MQTT Envío", "Comunicación", "https://sendcmqttmajo-04.streamlit.app/")

with col12:
    card("📡", "MQTT Recepción", "Recepción", "https://recepmqtt-roldan.streamlit.app/")

# =========================
# 📚 FUNDAMENTOS
# =========================
st.markdown("## 📚 Fundamentos")
col13, col14 = st.columns(2)

with col13:
    card("📚", "Intro IA 1", "Base", "https://intro-copia-profe-mjroldane.streamlit.app/")
    card("📚", "Intro IA 2", "Versión", "https://intro-copia-profe-roldan.streamlit.app/")

with col14:
    card("📚", "Mi Introducción", "Personal", "https://miintroduccionappmjroldane.streamlit.app/")
    card("📚", "Intro Extra", "Extra", "https://imm1-copia-profe-roldan.streamlit.app/")
