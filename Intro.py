import streamlit as st

st.set_page_config(
    page_title="Portafolio IA",
    page_icon="🤖",
    layout="wide"
)

# =========================
# 🎨 ESTILOS PERSONALIZADOS
# =========================
st.markdown("""
<style>
/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #eef2f3, #dfe9f3);
}

/* Títulos */
h1 {
    color: #2E7D32;
    text-align: center;
}

h3 {
    color: #1B5E20;
}

/* Tarjetas */
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
}

/* Botones */
.stLinkButton a {
    background-color: #4CAF50 !important;
    color: white !important;
    padding: 10px 15px;
    border-radius: 10px;
    text-decoration: none;
    font-weight: bold;
}

.stLinkButton a:hover {
    background-color: #388E3C !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 🧠 HEADER
# =========================
st.markdown("<h1>🤖 Portafolio de Aplicaciones de IA</h1>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# 📌 SIDEBAR
# =========================
with st.sidebar:
    st.header("📌 Sobre este portafolio")
    st.write(
        "Aplicaciones de inteligencia artificial enfocadas en automatización, "
        "visión por computador, NLP y análisis de datos."
    )
    st.link_button("🌐 Ir al sitio principal", "https://sites.google.com/view/aplicacionesdeia/inicio")

# =========================
# 🧩 FUNCION TARJETA
# =========================
def card(titulo, descripcion, url):
    st.markdown(f"""
    <div class="card">
        <h3>{titulo}</h3>
        <p>{descripcion}</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Abrir aplicación", url)

# =========================
# 📊 COLUMNAS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    card("🧠 Apps Generales", "Colección principal de apps", "https://major-apps-24.streamlit.app/")
    card("🔍 YOLO", "Detección de objetos", "https://yolov5-mjroldane.streamlit.app/")
    card("☁️ WordCloud", "Nube de palabras", "https://wordcloud-mjroldan.streamlit.app/")
    card("👁️ Visión IA", "Análisis visual", "https://visionapproldan-04.streamlit.app/")

with col2:
    card("🎤 Texto a Voz", "Conversión de texto a audio", "https://tm-mjroldane.streamlit.app/")
    card("📊 TF-IDF", "Análisis de texto", "https://mjroldane-tf-idf.streamlit.app/")
    card("📈 Dashboard", "Visualización de datos", "https://tablero-roldan-123.streamlit.app/")
    card("😊 Sentimiento", "Análisis emocional", "https://sentimenta-mjroldane.streamlit.app/")

with col3:
    card("📡 MQTT Envío", "Comunicación IoT", "https://sendcmqttmajo-04.streamlit.app/")
    card("🧾 OCR", "Texto desde imágenes", "https://ocr-roldan-mj.streamlit.app/")
    card("🎧 OCR + Audio", "Multimodal", "https://ocr-audio-roldan-mj.streamlit.app/")
    card("💬 Chat PDF", "Chat con documentos", "https://chatpdfroldan-nu3nuywn5722x6n4muvam8.streamlit.app/")

# =========================
# 🧪 EXTRA
# =========================
st.markdown("## 🧪 Otros proyectos")
st.markdown("---")

col4, col5 = st.columns(2)

with col4:
    card("📚 Introducción IA", "Conceptos básicos", "https://miintroduccionappmjroldane.streamlit.app/")
    card("📜 Historia", "Historia informática", "https://histinf-roldan.streamlit.app/")

with col5:
    card("🎨 Dibujo IA", "Reconocimiento de dibujos", "https://drawrecog-roldan664.streamlit.app/")
    card("🎙️ Control por Voz", "Interacción por voz", "https://ctrlvoicemajo-9.streamlit.app/")
