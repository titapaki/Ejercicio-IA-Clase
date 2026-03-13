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
# ---------- PAGINA 3 ----------
elif st.session_state.page == 3:

    st.markdown('<div class="section-title">Referencias</div>', unsafe_allow_html=True)

    with st.expander("Barradas Gudiño, J. (2023). Inteligencia artificial como elemento transformador de la investigación científica."):
        st.write(
        "El artículo describe cómo la inteligencia artificial está transformando la investigación científica al ampliar la capacidad "
        "de análisis de datos y acelerar procesos de descubrimiento. El autor plantea que la IA actúa como un elemento transformador "
        "que permite a los equipos científicos procesar grandes volúmenes de información de manera similar al razonamiento humano, "
        "pero a una escala mucho mayor."
        )

    with st.expander("Camus Jansson, F. (2024). El Desafío Ético de la IA en la Autoría Científica."):
        st.write(
        "Este trabajo analiza el debate ético sobre si los sistemas de inteligencia artificial pueden considerarse autores de artículos "
        "científicos. El autor concluye que, debido a la ausencia de conciencia, responsabilidad moral y capacidad legal, la IA no puede "
        "ser considerada autora dentro de los estándares actuales de la comunidad académica."
        )

    with st.expander("Gómez Cárdenas, R., et al. (2024). El Uso Ético y Moral de la Inteligencia Artificial en Educación e Investigación."):
        st.write(
        "Los autores examinan los principios éticos necesarios para el uso responsable de la inteligencia artificial en contextos "
        "educativos y científicos. Destacan la importancia de la transparencia, la responsabilidad humana y la supervisión ética "
        "cuando se emplean herramientas de IA en procesos académicos."
        )

    with st.expander("González Ciriaco, L. A., & Medina Marín, A. J. (2023). Avances y desafíos éticos en la integración de la IA en la producción científica."):
        st.write(
        "Este estudio analiza los avances tecnológicos que han permitido integrar sistemas de inteligencia artificial en la producción "
        "científica. También discute los principales desafíos éticos asociados, como la validación de resultados, la responsabilidad "
        "de los investigadores y el papel del juicio humano en la interpretación del conocimiento."
        )

    with st.expander("González, F. (2025). Cómo hacer investigación psicológica con inteligencia artificial."):
        st.write(
        "El autor explora el uso de herramientas de inteligencia artificial dentro de la investigación psicológica. Explica cómo estas "
        "tecnologías pueden apoyar el análisis de datos y la simulación de procesos cognitivos, aunque enfatiza que la interpretación "
        "de los fenómenos psicológicos debe seguir siendo realizada por profesionales humanos."
        )

    with st.expander("Lopezosa, C., Goyanes, M., & Codina, L. (2024). Acelerando la investigación cualitativa con IA."):
        st.write(
        "Este trabajo describe cómo la inteligencia artificial puede acelerar procesos de investigación cualitativa, especialmente en "
        "tareas como la transcripción de entrevistas, la organización de datos textuales y la identificación de patrones discursivos "
        "en estudios sociales."
        )

    with st.expander("Lopezosa, C., & Goyanes, M. (2024). Evaluación del uso ético de ChatGPT en investigación científica."):
        st.write(
        "Los autores evalúan el uso de modelos de lenguaje como ChatGPT dentro del proceso de investigación científica. El estudio "
        "plantea criterios para su uso responsable, incluyendo transparencia en su utilización y supervisión humana constante."
        )

    with st.expander("Muñoz García, A. C., et al. (2025). El impacto de la inteligencia artificial en la producción científica."):
        st.write(
        "Este artículo examina el impacto global de la inteligencia artificial en la producción científica contemporánea. Los autores "
        "analizan cómo la IA está modificando los procesos de generación, análisis y difusión del conocimiento científico."
        )

    with st.expander("Ruiz Muñoz, G. F. (2024). Implicaciones de la IA en la metodología de investigación."):
        st.write(
        "El autor analiza las implicaciones metodológicas del uso de inteligencia artificial en investigación. Se discute "
        "especialmente el problema de la 'caja negra', donde los sistemas de IA generan resultados sin que los investigadores "
        "comprendan completamente el proceso que llevó a esas conclusiones."
        )


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
