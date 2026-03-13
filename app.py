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

# ---------- ESTADO ----------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PROGRESO ----------
progress = st.session_state.page / 3
st.progress(progress)

# ---------- TITULO ----------
st.markdown(
"""
<div class="main-title">
La Brújula Ética: ¿Cómo la Inteligencia Artificial está Redibujando la Ciencia?
</div>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="quote">
"La inteligencia artificial es una brújula extraordinaria, pero solo el juicio humano puede decidir hacia qué horizonte navegar."
</div>
""",
unsafe_allow_html=True
)

# ---------- PAGINA 1 : ARTICULO ----------
if st.session_state.page == 1:

    st.markdown('<div class="section-title">Artículo de divulgación</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">

En los últimos años, la Inteligencia Artificial (IA) ha dejado de ser una fantasía de las películas de ciencia ficción para convertirse en un asistente cotidiano en los laboratorios y universidades. Sin embargo, su entrada en el mundo de la investigación científica no es solo una cuestión de "hacer las cosas más rápido"; es una revolución que nos obliga a repensar qué es ético y qué no cuando buscamos el conocimiento.

Imagine que un investigador tiene frente a sí una montaña de datos que le tomaría años analizar. Hoy, gracias a la IA, esa tarea puede resolverse en días. Como explica Barradas Gudiño (2023), esta tecnología funciona como un "elemento transformador" que dota a los equipos de una capacidad de procesamiento similar a la humana, pero a una escala masiva.

Esta madurez tecnológica está permitiendo que científicos de todo el mundo colaboren y descubran patrones que antes eran invisibles (González Ciriaco & Medina Marín, 2023; Muñoz García et al., 2025). Es, en esencia, una nueva forma de mirar el mundo a través de lentes digitales mucho más potentes.

La IA no solo hace cálculos. Según Ruiz Muñoz (2024), estas herramientas ayudan desde el principio: pueden sugerir ideas (hipótesis) o encontrar conexiones inesperadas en estudios sociales o médicos. Incluso en investigaciones donde se entrevistan personas, la IA puede transcribir y organizar las charlas de forma casi instantánea, permitiendo que el científico se concentre en lo más importante: entender el significado de lo que la gente dice (Lopezosa, Goyanes, & Codina, 2024).

No todo es perfecto. Uno de los mayores riesgos es lo que los expertos llaman la "caja negra". Esto significa que a veces la IA llega a una conclusión, pero no sabemos cómo lo hizo (Ruiz Muñoz, 2024). Además, si alimentamos a la IA con datos que contienen prejuicios humanos (por ejemplo, ideas sexistas o racistas), la máquina simplemente repetirá y aumentará esos errores. Por eso, existe una obligación moral de vigilar cada paso de la tecnología para asegurar que los resultados sean justos y válidos (Muñoz García et al., 2025).

Esta es una de las preguntas más polémicas. La respuesta actual es un no rotundo. La comunidad académica coincide en que solo los seres humanos pueden ser considerados "autores". ¿Por qué? Porque una máquina no tiene conciencia ni puede hacerse responsable legal o éticamente de lo que escribe (Camus Jansson, 2024). La IA puede ser una "aliada", pero el control final y el juicio crítico deben permanecer siempre en manos humanas (González Ciriaco & Medina Marín, 2023). En campos como la psicología, esto es vital: una IA puede simular procesos de memoria, pero nunca podrá sustituir la interpretación profunda de un profesional sobre la mente humana (González, 2025).

Para que la ciencia siga siendo confiable, el uso de la IA debe guiarse por la transparencia. Los investigadores deben declarar siempre cuándo y cómo usaron estas herramientas (Gómez Cárdenas et al., 2024).

En conclusión, la IA es una brújula poderosa, pero somos los humanos quienes debemos decidir el rumbo. Solo con una supervisión constante y un compromiso con la honestidad académica podremos aprovechar esta tecnología sin perder la esencia de la ciencia: la búsqueda de la verdad con integridad (Lopezosa & Goyanes, 2024).

    </div>
    """, unsafe_allow_html=True)


# ---------- PAGINA 2 : OPINION ----------
elif st.session_state.page == 2:

    st.markdown('<div class="section-title">Participa en el debate</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">
    El uso de inteligencia artificial en la investigación científica abre preguntas profundas sobre ética, responsabilidad y autoría académica.
    Tu opinión también forma parte de esta conversación.
    </div>
    """, unsafe_allow_html=True)

    opinion = st.radio(
        "¿Crees que la inteligencia artificial debería poder ser considerada autora de artículos científicos?",
        ["No", "Sí", "No estoy seguro"]
    )

    if opinion == "No":
        st.success("Esta es actualmente la postura predominante en la comunidad científica.")

    elif opinion == "Sí":
        st.info("Algunos investigadores consideran que en el futuro podría replantearse este concepto.")

    elif opinion == "No estoy seguro":
        st.warning("Es un debate que continúa evolucionando con el desarrollo de la tecnología.")


# ---------- PAGINA 3 : REFERENCIAS ----------
elif st.session_state.page == 3:

    st.markdown('<div class="section-title">Referencias</div>', unsafe_allow_html=True)

    with st.expander("Barradas Gudiño (2023)"):
        st.write("Describe la inteligencia artificial como un elemento transformador que amplía la capacidad de análisis de datos y acelera los procesos de investigación científica.")

    with st.expander("Camus Jansson (2024)"):
        st.write("Analiza los dilemas éticos relacionados con la autoría científica cuando se utilizan sistemas de inteligencia artificial.")

    with st.expander("Gómez Cárdenas et al. (2024)"):
        st.write("Explora los principios éticos y morales necesarios para el uso responsable de inteligencia artificial en educación e investigación.")

    with st.expander("González Ciriaco & Medina Marín (2023)"):
        st.write("Examina los avances y desafíos éticos derivados de la integración de IA en la producción científica.")

    with st.expander("González (2025)"):
        st.write("Presenta estrategias para incorporar herramientas de inteligencia artificial en la investigación psicológica.")

    with st.expander("Lopezosa, Goyanes & Codina (2024)"):
        st.write("Analiza cómo la IA puede acelerar procesos de investigación cualitativa como la transcripción y organización de entrevistas.")

    with st.expander("Lopezosa & Goyanes (2024)"):
        st.write("Evalúa el uso ético de ChatGPT y modelos de lenguaje en la investigación científica.")

    with st.expander("Muñoz García et al. (2025)"):
        st.write("Explora el impacto global de la inteligencia artificial en la producción científica contemporánea.")

    with st.expander("Ruiz Muñoz (2024)"):
        st.write("Reflexiona sobre las implicaciones metodológicas del uso de IA y el problema de la 'caja negra' en la investigación.")

# ---------- NAVEGACION ----------
st.markdown("---")

col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Anterior"):
        if st.session_state.page > 1:
            st.session_state.page -= 1

with col3:
    if st.button("Siguiente ➜"):
        if st.session_state.page < 3:
            st.session_state.page += 1
