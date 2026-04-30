import streamlit as st

st.set_page_config(
    page_title="Portafolio IA",
    page_icon="🤖",
    layout="wide"
)

# =========================
# 🎨 ESTILOS
# =========================
st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #e0f7fa);
}

/* Título */
h1 {
    text-align: center;
    background: linear-gradient(90deg, #7b2ff7, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtítulos */
h3 {
    color: #5e35b1;
}

/* Cards */
.card {
    background: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    transition: all 0.3s ease;
}

.card:hover {
    transform: translateY(-6px) scale(1.01);
    box-shadow: 0px 10px 30px rgba(123,47,247,0.2);
}

/* Botones */
.stLinkButton a {
    background: linear-gradient(90deg, #7b2ff7, #00c6ff) !important;
    color: white !important;
    padding: 10px 16px;
    border-radius: 12px;
    text-decoration: none;
    font-weight: 600;
    border: none;
}

.stLinkButton a:hover {
    opacity: 0.9;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("<h1>✨ Portafolio de Aplicaciones de IA</h1>", unsafe_allow_html=True)
st.markdown("---")

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.header("💡 Sobre este portafolio")
    st.write(
        "Aplicaciones de inteligencia artificial enfocadas en visión, NLP, datos e IoT."
    )
    st.link_button("🌐 Ver página principal", "https://sites.google.com/view/aplicacionesdeia/inicio")

# =========================
# FUNCION CARD
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
# COLUMNAS
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    card("🧠 Apps Generales", "Colección principal", "https://major-apps-24.streamlit.app/")
    card("🔍 YOLO", "Detección de objetos", "https://yolov5-mjroldane.streamlit.app/")
    card("☁️ WordCloud", "Nube de palabras", "https://wordcloud-mjroldan.streamlit.app/")
    card("👁️ Visión IA", "Análisis visual", "https://visionapproldan-04.streamlit.app/")

with col2:
    card("🎤 Texto a Voz", "Conversión a audio", "https://tm-mjroldane.streamlit.app/")
    card("📊 TF-IDF", "Análisis de texto", "https://mjroldane-tf-idf.streamlit.app/")
    card("📈 Dashboard", "Visualización", "https://tablero-roldan-123.streamlit.app/")
    card("😊 Sentimiento", "Clasificación emocional", "https://sentimenta-mjroldane.streamlit.app/")

with col3:
    card("📡 MQTT", "Comunicación IoT", "https://sendcmqttmajo-04.streamlit.app/")
    card("🧾 OCR", "Texto desde imágenes", "https://ocr-roldan-mj.streamlit.app/")
    card("🎧 OCR + Audio", "Multimodal", "https://ocr-audio-roldan-mj.streamlit.app/")
    card("💬 Chat PDF", "Chat con documentos", "https://chatpdfroldan-nu3nuywn5722x6n4muvam8.streamlit.app/")

# =========================
# EXTRA
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
