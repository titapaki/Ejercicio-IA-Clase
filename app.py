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
# ---------- PAGINA 1 : ARTICULO ----------
if st.session_state.page == 1:

    st.markdown('<div class="section-title">Artículo de divulgación</div>', unsafe_allow_html=True)

    article_text = """
La Brújula Ética: ¿Cómo la Inteligencia Artificial está Redibujando la Ciencia?

En los últimos años, la Inteligencia Artificial (IA) ha dejado de ser una fantasía de las películas de ciencia ficción para convertirse en un asistente cotidiano en los laboratorios y universidades. Sin embargo, su entrada en el mundo de la investigación científica no es solo una cuestión de "hacer las cosas más rápido"; es una revolución que nos obliga a repensar qué es ético y qué no cuando buscamos el conocimiento.

Imagine que un investigador tiene frente a sí una montaña de datos que le tomaría años analizar. Hoy, gracias a la IA, esa tarea puede resolverse en días. Como explica Barradas Gudiño (2023), esta tecnología funciona como un "elemento transformador" que dota a los equipos de una capacidad de procesamiento similar a la humana, pero a una escala masiva.

Esta madurez tecnológica está permitiendo que científicos de todo el mundo colaboren y descubran patrones que antes eran invisibles (González Ciriaco & Medina Marín, 2023; Muñoz García et al., 2025). Es, en esencia, una nueva forma de mirar el mundo a través de lentes digitales mucho más potentes.

La IA no solo hace cálculos. Según Ruiz Muñoz (2024), estas herramientas ayudan desde el principio: pueden sugerir ideas (hipótesis) o encontrar conexiones inesperadas en estudios sociales o médicos. Incluso en investigaciones donde se entrevistan personas, la IA puede transcribir y organizar las charlas de forma casi instantánea, permitiendo que el científico se concentre en lo más importante: entender el significado de lo que la gente dice (Lopezosa, Goyanes, & Codina, 2024).

No todo es perfecto. Uno de los mayores riesgos es lo que los expertos llaman la "caja negra". Esto significa que a veces la IA llega a una conclusión, pero no sabemos cómo lo hizo (Ruiz Muñoz, 2024). Además, si alimentamos a la IA con datos que contienen prejuicios humanos (por ejemplo, ideas sexistas o racistas), la máquina simplemente repetirá y aumentará esos errores. Por eso, existe una obligación moral de vigilar cada paso de la tecnología para asegurar que los resultados sean justos y válidos (Muñoz García et al., 2025).

Esta es una de las preguntas más polémicas. La respuesta actual es un no rotundo. La comunidad académica coincide en que solo los seres humanos pueden ser considerados "autores". ¿Por qué? Porque una máquina no tiene conciencia ni puede hacerse responsable legal o éticamente de lo que escribe (Camus Jansson, 2024). La IA puede ser una "aliada", pero el control final y el juicio crítico deben permanecer siempre en manos humanas (González Ciriaco & Medina Marín, 2023). En campos como la psicología, esto es vital: una IA puede simular procesos de memoria, pero nunca podrá sustituir la interpretación profunda de un profesional sobre la mente humana (González, 2025).

Para que la ciencia siga siendo confiable, el uso de la IA debe guiarse por la transparencia. Los investigadores deben declarar siempre cuándo y cómo usaron estas herramientas (Gómez Cárdenas et al., 2024).

En conclusión, la IA es una brújula poderosa, pero somos los humanos quienes debemos decidir el rumbo. Solo con una supervisión constante y un compromiso con la honestidad académica podremos aprovechar esta tecnología sin perder la esencia de la ciencia: la búsqueda de la verdad con integridad (Lopezosa & Goyanes, 2024).
"""

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(article_text)
    st.markdown('</div>', unsafe_allow_html=True)


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
