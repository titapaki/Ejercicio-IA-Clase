import streamlit as st

st.set_page_config(page_title="IA y Ética Científica", layout="wide")

# ---------- ESTILO VISUAL ----------
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

.nav-buttons{
    margin-top:30px;
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
Dimensión Ética y Normativa del Uso de la Inteligencia Artificial en la Investigación Científica
</div>
""", unsafe_allow_html=True)

st.markdown(
"""
<div class="quote">
"La inteligencia artificial es una brújula extraordinaria, pero solo el juicio humano puede decidir hacia qué horizonte navegar."
</div>
""", unsafe_allow_html=True)


# ---------- PAGINA 1 ----------
if st.session_state.page == 1:

    st.markdown('<div class="section-title">1. El inicio de una nueva ciencia</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">

    En los últimos años, la Inteligencia Artificial ha dejado de ser una fantasía de la ciencia ficción para convertirse en una herramienta cotidiana dentro de universidades y laboratorios.

    Su impacto no se limita a acelerar cálculos o automatizar tareas. La IA está cambiando la forma en que los científicos observan el mundo. Gracias a su capacidad de analizar enormes cantidades de datos, permite descubrir patrones que antes eran invisibles.

    Sin embargo, este poder tecnológico también abre preguntas profundas. ¿Podemos confiar plenamente en decisiones generadas por algoritmos? ¿Quién es responsable de los resultados producidos por una máquina?

    Estas preguntas marcan el inicio de una nueva conversación sobre la ética en la ciencia contemporánea.

    </div>
    """, unsafe_allow_html=True)


# ---------- PAGINA 2 ----------
elif st.session_state.page == 2:

    st.markdown('<div class="section-title">2. Un debate ético abierto</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card text-body">

    Uno de los principales problemas en el uso de inteligencia artificial es el fenómeno conocido como la "caja negra".

    En muchos casos, los algoritmos producen resultados sin que los investigadores comprendan completamente el proceso que llevó a esa conclusión.

    Además, si los datos utilizados contienen sesgos sociales, la IA puede reproducirlos o incluso amplificarlos.

    Por esta razón, la comunidad científica insiste en que el uso de estas herramientas debe estar siempre acompañado por supervisión humana y transparencia metodológica.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Participa en el debate")

    opinion = st.radio(
        "¿Crees que la inteligencia artificial debería poder ser considerada autora de artículos científicos?",
        ["No", "Sí", "No estoy seguro"]
    )

    if opinion == "No":
        st.success("Esta es la postura predominante dentro de la comunidad científica actual.")

    elif opinion == "Sí":
        st.info("Algunos investigadores discuten esta posibilidad como un cambio futuro en la ciencia.")

    elif opinion == "No estoy seguro":
        st.warning("La discusión continúa evolucionando conforme avanza la tecnología.")


# ---------- PAGINA 3 ----------
elif st.session_state.page == 3:

    st.markdown('<div class="section-title">3. Referencias</div>', unsafe_allow_html=True)

    with st.expander("Barradas Gudiño (2023)"):
        st.write("Explora cómo la IA está transformando la investigación científica al ampliar la capacidad de análisis de datos.")

    with st.expander("Camus Jansson (2024)"):
        st.write("Analiza los dilemas éticos relacionados con la autoría científica en el contexto de la IA.")

    with st.expander("Gómez Cárdenas et al. (2024)"):
        st.write("Propone principios éticos para el uso responsable de inteligencia artificial en educación e investigación.")

    with st.expander("González Ciriaco & Medina Marín (2023)"):
        st.write("Describe avances y desafíos éticos en la producción científica mediada por IA.")

    with st.expander("Muñoz García et al. (2025)"):
        st.write("Analiza el impacto global de la inteligencia artificial en la producción científica.")

    with st.expander("Ruiz Muñoz (2024)"):
        st.write("Reflexiona sobre las implicaciones metodológicas del uso de IA en investigación.")


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
