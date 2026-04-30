import streamlit as st
from PIL import Image

# Configuración de página
st.set_page_config(
    page_title="Portafolio IA",
    page_icon="🤖",
    layout="wide"
)

# Título principal
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🤖 Portafolio de Aplicaciones de IA</h1>", unsafe_allow_html=True)

st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("📌 Sobre este portafolio")
    st.write(
        "Este portafolio reúne aplicaciones de inteligencia artificial enfocadas en "
        "automatización, análisis de datos, visión computacional y procesamiento de lenguaje natural."
    )

    st.markdown("### 🌐 Página general")
    st.link_button("Ir al sitio principal", "https://sites.google.com/view/aplicacionesdeia/inicio")

# =========================
# FUNCION PARA TARJETAS
# =========================
def card(titulo, descripcion, url):
    st.markdown(f"### {titulo}")
    st.write(descripcion)
    st.link_button("🚀 Abrir aplicación", url)
    st.markdown("---")

# =========================
# COLUMNAS
# =========================
col1, col2, col3 = st.columns(3)

# =========================
# COLUMNA 1
# =========================
with col1:
    card("🧠 Apps Generales", "Colección de aplicaciones principales", "https://major-apps-24.streamlit.app/")
    card("🔍 Detección de Objetos (YOLO)", "Reconocimiento de objetos en imágenes", "https://yolov5-mjroldane.streamlit.app/")
    card("☁️ Nube de Palabras", "Generación de wordclouds", "https://wordcloud-mjroldan.streamlit.app/")
    card("👁️ Visión IA", "Análisis visual con IA", "https://visionapproldan-04.streamlit.app/")
    card("🌐 Traductor", "Traducción automática", "https://traductor-mjroldane.streamlit.app/")

# =========================
# COLUMNA 2
# =========================
with col2:
    card("🎤 Texto a Voz", "Conversión de texto en audio", "https://tm-mjroldane.streamlit.app/")
    card("📊 TF-IDF", "Análisis de texto con TF-IDF", "https://mjroldane-tf-idf.streamlit.app/")
    card("📈 TF-IDF Español", "Versión en español del análisis", "https://tdfesp-mjroldane.streamlit.app/")
    card("📋 Dashboard", "Visualización de datos", "https://tablero-roldan-123.streamlit.app/")
    card("😊 Análisis de Sentimiento", "Clasificación emocional de texto", "https://sentimenta-mjroldane.streamlit.app/")

# =========================
# COLUMNA 3
# =========================
with col3:
    card("📡 Envío MQTT", "Comunicación IoT (envío)", "https://sendcmqttmajo-04.streamlit.app/")
    card("📡 Recepción MQTT", "Comunicación IoT (recepción)", "https://recepmqtt-roldan.streamlit.app/")
    card("🧾 OCR", "Extracción de texto desde imágenes", "https://ocr-roldan-mj.streamlit.app/")
    card("🎧 OCR + Audio", "Texto desde imagen y audio", "https://ocr-audio-roldan-mj.streamlit.app/")
    card("💬 Chat con PDF", "Interacción con documentos", "https://chatpdfroldan-nu3nuywn5722x6n4muvam8.streamlit.app/")

# =========================
# SECCIÓN EXTRA
# =========================
st.markdown("## 🧪 Otros Proyectos")
st.markdown("---")

col4, col5 = st.columns(2)

with col4:
    card("📚 Introducción IA", "Conceptos básicos", "https://miintroduccionappmjroldane.streamlit.app/")
    card("📜 Historia Informática", "Evolución de la tecnología", "https://histinf-roldan.streamlit.app/")
    card("✋ Hand Tracking", "Seguimiento de manos", "https://hand-w-roldan.streamlit.app/")

with col5:
    card("🎨 Dibujo IA", "Reconocimiento de dibujos", "https://drawrecog-roldan664.streamlit.app/")
    card("🖌️ Ejercicio Dibujo", "Interacción gráfica", "https://ejercicio-draw-majo-roldan.streamlit.app/")
    card("🎙️ Control por Voz", "Interacción mediante voz", "https://ctrlvoicemajo-9.streamlit.app/")
