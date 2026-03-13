import streamlit as st

st.set_page_config(page_title="Dimensión Ética de la IA", layout="wide")

# ---------- ESTILOS ----------
st.markdown("""
<style>

.main-title{
    font-size:36px;
    font-weight:600;
    margin-bottom:10px;
}

.quote{
    text-align:right;
    font-style:italic;
    color:#555;
    margin-bottom:30px;
}

.article-box{
    border:1px solid #e6e6e6;
    border-radius:18px;
    padding:30px;
    background-color:#fafafa;
    line-height:1.7;
    font-size:16px;
}

.ref-box{
    border:1px solid #e6e6e6;
    border-radius:12px;
    padding:15px;
    background-color:#ffffff;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITULO ----------
st.markdown(
    '<div class="main-title">Dimensión Ética y Normativa del Uso de la Inteligencia Artificial en la Investigación Científica</div>',
    unsafe_allow_html=True
)

# ---------- FRASE ----------
st.markdown(
    '<div class="quote">La inteligencia artificial es una brújula extraordinaria, pero solo el juicio humano puede decidir hacia qué horizonte navegar.</div>',
    unsafe_allow_html=True
)

# ---------- SECCIONES DEL ARTICULO ----------
tabs = st.tabs([
"Introducción",
"IA en la investigación",
"Riesgos éticos",
"Autoría científica",
"Conclusión"
])

with tabs[0]:
    st.markdown('<div class="article-box">\
    En los últimos años, la Inteligencia Artificial (IA) ha dejado de ser una fantasía de las películas de ciencia ficción para convertirse en un asistente cotidiano en los laboratorios y universidades. \
    Su llegada al mundo de la investigación científica no solo significa hacer las cosas más rápido, sino replantear qué es ético cuando buscamos conocimiento.\
    </div>', unsafe_allow_html=True)

with tabs[1]:
    st.markdown('<div class="article-box">\
    Imagine que un investigador tiene frente a sí una enorme cantidad de datos que tardaría años en analizar. \
    Gracias a la IA, esta tarea puede resolverse en días. \
    Estas herramientas pueden identificar patrones invisibles para el ojo humano y ayudar a generar hipótesis o descubrir conexiones inesperadas entre estudios.\
    </div>', unsafe_allow_html=True)

with tabs[2]:
    st.markdown('<div class="article-box">\
    Uno de los mayores desafíos éticos es el fenómeno conocido como la "caja negra". \
    Esto ocurre cuando un sistema de IA llega a conclusiones sin que sepamos exactamente cómo lo hizo. \
    Además, si los datos utilizados contienen sesgos humanos, la IA puede amplificarlos. \
    Por ello, es indispensable una supervisión constante por parte de los investigadores.\
    </div>', unsafe_allow_html=True)

with tabs[3]:
    st.markdown('<div class="article-box">\
    Actualmente la comunidad científica coincide en que la inteligencia artificial no puede ser considerada autora de un artículo científico. \
    La razón es simple: una máquina no posee conciencia ni responsabilidad ética. \
    La IA puede ser una aliada poderosa, pero el juicio final siempre debe permanecer en manos humanas.\
    </div>', unsafe_allow_html=True)

with tabs[4]:
    st.markdown('<div class="article-box">\
    Para mantener la confianza en la ciencia, el uso de la IA debe ser transparente. \
    Los investigadores deben declarar cuándo y cómo utilizaron estas herramientas. \
    La inteligencia artificial puede ser una brújula poderosa, pero el rumbo de la ciencia siempre debe estar guiado por la integridad humana.\
    </div>', unsafe_allow_html=True)

# ---------- REFERENCIAS EXPANDIBLES ----------
st.markdown("## Referencias")

with st.expander("Barradas Gudiño (2023) – Inteligencia artificial como elemento transformador de la investigación científica"):
    st.write("Analiza cómo la IA amplía la capacidad de procesamiento de datos en la investigación científica.")

with st.expander("Camus Jansson (2024) – El Desafío Ético de la IA en la Autoría Científica"):
    st.write("Discute los dilemas éticos sobre la autoría científica cuando se utilizan herramientas de inteligencia artificial.")

with st.expander("Gómez Cárdenas et al. (2024) – Uso ético y moral de la IA en educación e investigación"):
    st.write("Explora principios de transparencia y responsabilidad en el uso de IA en contextos académicos.")

with st.expander("González Ciriaco & Medina Marín (2023) – Avances y desafíos éticos en la producción científica"):
    st.write("Estudia los beneficios y desafíos éticos derivados del uso de IA en la producción científica.")

with st.expander("González (2025) – Cómo hacer investigación psicológica con inteligencia artificial"):
    st.write("Propone estrategias para integrar herramientas de IA en la investigación psicológica.")

with st.expander("Lopezosa, Goyanes & Codina (2024) – Acelerando la investigación cualitativa con IA"):
    st.write("Describe cómo la IA puede apoyar el análisis de entrevistas y datos cualitativos.")

with st.expander("Lopezosa & Goyanes (2024) – Evaluación del uso ético de ChatGPT en investigación científica"):
    st.write("Analiza el uso de modelos de lenguaje en investigación científica.")

with st.expander("Muñoz García et al. (2025) – Impacto de la inteligencia artificial en la producción científica"):
    st.write("Examina el impacto global de la IA en la producción científica.")

with st.expander("Ruiz Muñoz (2024) – Implicaciones de la IA en la metodología de investigación"):
    st.write("Reflexiona sobre los cambios metodológicos generados por el uso de inteligencia artificial.")

# ---------- ENCUESTA ----------
st.markdown("## Tu opinión")

opinion = st.radio(
"¿Crees que la inteligencia artificial debería poder ser considerada autora de artículos científicos?",
["Sí", "No", "No estoy seguro"]
)

if opinion == "Sí":
    st.info("Algunos investigadores discuten esta posibilidad, pero actualmente la comunidad científica no la acepta.")

elif opinion == "No":
    st.success("Esta es la postura predominante en la comunidad académica actual.")

elif opinion == "No estoy seguro":
    st.warning("Es un debate abierto que seguirá evolucionando con el desarrollo de la tecnología.")
