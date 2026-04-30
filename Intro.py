import streamlit as st

st.set_page_config(page_title="Portafolio IA", page_icon="✨", layout="wide")

# =========================
# 🎨 ESTILOS PRO
# =========================
st.markdown("""
<style>

/* Fondo */
.stApp {
    background: linear-gradient(135deg, #eef2ff, #e0f7fa);
}

/* Título */
h1 {
    text-align: center;
    font-size: 42px;
    background: linear-gradient(90deg, #7b2ff7, #00c6ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* CARD PRO */
.card {
    background: rgba(255, 255, 255, 0.7);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
    cursor: pointer;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Hover PRO */
.card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 0 25px rgba(123,47,247,0.4);
}

/* Iconos */
.icon {
    font-size: 40px;
}

/* Títulos */
.card h3 {
    color: #2d1b69;
    margin: 10px 0 5px 0;
}

/* Texto */
.card p {
    color: #444;
    font-size: 14px;
}

/* Botón */
.stLinkButton a {
    background: linear-gradient(90deg, #7b2ff7, #00c6ff) !important;
    color: white !important;
    padding: 10px 16px;
    border-radius: 12px;
    font-weight: 600;
    text-decoration: none;
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
    st.write("Aplicaciones de IA en visión, NLP, datos e IoT.")
    st.link_button("🌐 Ver página principal", "https://sites.google.com/view/aplicacionesdeia/inicio")

# =========================
# 🧩 CARD PRO
# =========================
def card(icono, titulo, descripcion, url):
    st.markdown(f"""
    <div class="card">
        <div class="icon">{icono}</div>
        <div>
            <h3>{titulo}</h3>
            <p>{descripcion}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 Abrir", url)

# =========================
# GRID
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    card("🧠", "Apps Generales", "Colección principal", "https://major-apps-24.streamlit.app/")
    card("🔍", "YOLO", "Detección de objetos", "https://yolov5-mjroldane.streamlit.app/")
    card("☁️", "WordCloud", "Nube de palabras", "https://wordcloud-mjroldan.streamlit.app/")

with col2:
    card("🎤", "Texto a Voz", "Conversión a audio", "https://tm-mjroldane.streamlit.app/")
    card("📊", "TF-IDF", "Análisis de texto", "https://mjroldane-tf-idf.streamlit.app/")
    card("📈", "Dashboard", "Visualización de datos", "https://tablero-roldan-123.streamlit.app/")

with col3:
    card("📡", "MQTT", "Comunicación IoT", "https://sendcmqttmajo-04.streamlit.app/")
    card("🧾", "OCR", "Texto desde imágenes", "https://ocr-roldan-mj.streamlit.app/")
    card("💬", "Chat PDF", "Chat con documentos", "https://chatpdfroldan-nu3nuywn5722x6n4muvam8.streamlit.app/")
