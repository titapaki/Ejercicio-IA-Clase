import streamlit as st

st.set_page_config(page_title="IA y Ética Científica", layout="wide")

# ---------- ESTILO ----------
st.markdown("""
<style>

body {
    font-family: 'Georgia', serif;
}

.main-title{
    font-size:48px;
    font-weight:700;
    margin-bottom:10px;
}

.quote{
    text-align:right;
    font-style:italic;
    font-size:20px;
    color:#666;
    margin-bottom:40px;
}

.section-title{
    font-size:32px;
    font-weight:600;
    margin-bottom:20px;
}

.text-body{
    font-size:19px;
    line-height:1.8;
}

.card{
    border:1px solid #e6e6e6;
    border-radius:20px;
    padding:40px;
    background-color:#fafafa;
}

</style>
""", unsafe_allow_html=True)


# ---------- ESTADOS ----------
if "page" not in st.session_state:
    st.session_state.page = 1

if "opinion" not in st.session_state:
    st.session_state.opinion = None


# ---------- PROGRESO ----------
progress = st.session_state.page / 3
st.progress(progress)


# ---------- TITULO ----------
st.markdown("""
<div class="main-title">
La Brújula Ética: ¿Cómo la Inteligencia Artificial está Redibujando la Ciencia?
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="quote">
"La inteligencia artificial es una brújula extraordinaria, pero solo el juicio humano puede decidir hacia qué horizonte navegar."
</div>
""", unsafe_allow_html=True)


# ---------- PAGINA 1 ----------
if st.session_state.page == 1:

    st.markdown('<div class="section-title">Artículo de divulgación</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">

En los últimos años, la Inteligencia Artificial (IA) ha dejado de ser una fantasía de las películas de ciencia ficción para convertirse en un asistente cotidiano en los laboratorios y universidades.

Su entrada en la investigación científica no solo significa hacer las cosas más rápido, sino replantear qué es ético cuando buscamos conocimiento.

Imagine que un investigador tiene frente a sí una montaña de datos que le tomaría años analizar. Hoy, gracias a la IA, esa tarea puede resolverse en días.

Esta tecnología permite descubrir patrones invisibles y abrir nuevas formas de comprender el mundo científico.

Sin embargo, también plantea preguntas profundas sobre responsabilidad, transparencia y ética en la investigación.

    </div>
    """, unsafe_allow_html=True)


# ---------- PAGINA 2 ----------
elif st.session_state.page == 2:

    st.markdown('<div class="section-title">Participa en el debate</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">
    El uso de inteligencia artificial en la investigación científica abre preguntas profundas sobre ética, responsabilidad y autoría académica.
    Tu opinión también forma parte de esta conversación.
    </div>
    """, unsafe_allow_html=True)

    # encuesta
    st.session_state.opinion = st.radio(
        "¿Crees que la inteligencia artificial debería poder ser considerada autora de artículos científicos?",
        ["No", "Sí", "No estoy seguro"],
        index=None
    )

    # feedback SIN cambiar página
    if st.session_state.opinion == "No":
        st.success("Esta es actualmente la postura predominante en la comunidad científica.")

    elif st.session_state.opinion == "Sí":
        st.info("Algunos investigadores consideran que en el futuro podría replantearse este concepto.")

    elif st.session_state.opinion == "No estoy seguro":
        st.warning("Es un debate que continúa evolucionando con el desarrollo tecnológico.")


# ---------- PAGINA 3 ----------
elif st.session_state.page == 3:

    st.markdown('<div class="section-title">Referencias</div>', unsafe_allow_html=True)

    with st.expander("Barradas Gudiño (2023)"):
        st.write("Describe la inteligencia artificial como un elemento transformador que amplía la capacidad de análisis de datos.")

    with st.expander("Camus Jansson (2024)"):
        st.write("Analiza los dilemas éticos relacionados con la autoría científica cuando se utilizan sistemas de IA.")

    with st.expander("Gómez Cárdenas et al. (2024)"):
        st.write("Explora los principios éticos necesarios para el uso responsable de inteligencia artificial en investigación.")

    with st.expander("González Ciriaco & Medina Marín (2023)"):
        st.write("Examina los avances y desafíos éticos derivados de la integración de IA en la producción científica.")

    with st.expander("Muñoz García et al. (2025)"):
        st.write("Explora el impacto global de la inteligencia artificial en la producción científica.")

    with st.expander("Ruiz Muñoz (2024)"):
        st.write("Reflexiona sobre las implicaciones metodológicas del uso de IA y el problema de la 'caja negra'.")


# ---------- NAVEGACION ----------
st.markdown("---")

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Anterior") and st.session_state.page > 1:
        st.session_state.page -= 1
        st.rerun()

with col3:
    if st.button("Siguiente ➜") and st.session_state.page < 3:
        st.session_state.page += 1
        st.rerun()
