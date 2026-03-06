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
    padding:35px;
    background-color:#fafafa;
    line-height:1.7;
    font-size:16px;
}

.ref-box{
    border:1px solid #e6e6e6;
    border-radius:12px;
    padding:20px;
    background-color:#ffffff;
    margin-top:15px;
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

# ---------- ARTICULO ----------
article = """
En los últimos años, la Inteligencia Artificial (IA) ha dejado de ser una fantasía de las películas de ciencia ficción para convertirse en un asistente cotidiano en los laboratorios y universidades. Sin embargo, su entrada en el mundo de la investigación científica no es solo una cuestión de hacer las cosas más rápido; es una revolución que nos obliga a repensar qué es ético y qué no cuando buscamos el conocimiento.

Imagine que un investigador tiene frente a sí una montaña de datos que le tomaría años analizar. Hoy, gracias a la IA, esa tarea puede resolverse en días. Esta tecnología funciona como un elemento transformador que dota a los equipos de investigación de una capacidad de procesamiento similar a la humana, pero a una escala masiva.

Esta madurez tecnológica permite que científicos de todo el mundo colaboren y descubran patrones que antes eran invisibles. En esencia, la IA ofrece una nueva forma de mirar el mundo a través de lentes digitales mucho más potentes.

Además, estas herramientas pueden ayudar desde el inicio del proceso científico. Pueden sugerir hipótesis, identificar conexiones inesperadas entre estudios e incluso apoyar investigaciones cualitativas. En proyectos donde se realizan entrevistas, por ejemplo, la IA puede transcribir y organizar conversaciones de forma casi instantánea, permitiendo que los investigadores se concentren en interpretar el significado de lo que las personas expresan.

Sin embargo, el uso de la IA también plantea desafíos importantes. Uno de los principales riesgos es lo que se conoce como la “caja negra”. En algunos casos, los sistemas de IA generan conclusiones sin que los investigadores comprendan completamente cómo se produjo ese resultado.

Además, si los datos con los que se entrena la IA contienen prejuicios humanos, como sesgos sociales o culturales, la tecnología puede reproducir e incluso amplificar esos errores. Por esta razón, existe una responsabilidad ética de supervisar constantemente el uso de estas herramientas.

Otro debate relevante gira en torno a la autoría científica. Actualmente, la comunidad académica coincide en que solo los seres humanos pueden ser considerados autores de un trabajo científico. La IA puede ser una aliada en el proceso de investigación, pero no posee conciencia ni puede asumir responsabilidad ética o legal.

En disciplinas como la psicología, este principio resulta fundamental. Aunque una IA pueda simular ciertos procesos cognitivos, la interpretación profunda del comportamiento y la experiencia humana sigue dependiendo del juicio profesional.

Para mantener la confianza en la ciencia, el uso de la IA debe estar guiado por la transparencia. Los investigadores deben declarar cuándo y cómo han utilizado estas herramientas durante su trabajo.

En conclusión, la inteligencia artificial representa una herramienta poderosa para el avance del conocimiento. No obstante, su verdadero valor depende de la responsabilidad con la que los seres humanos decidan utilizarla.
"""

st.markdown(f'<div class="article-box">{article}</div>', unsafe_allow_html=True)

# ---------- REFERENCIAS ----------
st.markdown("### Referencias")

references = {
"Barradas Gudiño (2023) – Inteligencia artificial como elemento transformador de la investigación científica":
"La IA se analiza como una herramienta que transforma los procesos científicos al ampliar la capacidad de procesamiento y análisis de datos en la investigación.",

"Camus Jansson (2024) – El Desafío Ético de la IA en la Autoría Científica":
"El artículo discute los dilemas éticos sobre la autoría cuando se utilizan sistemas de inteligencia artificial y argumenta que solo los humanos pueden asumir responsabilidad científica.",

"Gómez Cárdenas et al. (2024) – Uso ético y moral de la IA en educación e investigación":
"Explora principios éticos para el uso responsable de la inteligencia artificial en entornos académicos, destacando la transparencia y la supervisión humana.",

"González Ciriaco & Medina Marín (2023) – Avances y desafíos éticos en la producción científica":
"Analiza cómo la IA está transformando la producción científica y examina los desafíos éticos asociados a su implementación.",

"González (2025) – Cómo hacer investigación psicológica con inteligencia artificial":
"Presenta estrategias para integrar herramientas de IA en la investigación psicológica sin perder el análisis crítico humano.",

"Lopezosa, Goyanes & Codina (2024) – Acelerando la investigación cualitativa con IA":
"Describe cómo la IA puede apoyar el análisis cualitativo, especialmente en procesos como transcripción, organización y exploración de datos.",

"Lopezosa & Goyanes (2024) – Evaluación del uso ético de ChatGPT en investigación científica":
"Analiza el uso de modelos de lenguaje en investigación y propone criterios para su uso responsable.",

"Muñoz García et al. (2025) – Impacto de la inteligencia artificial en la producción científica":
"Examina el impacto global de la IA en la producción de conocimiento científico y sus implicaciones metodológicas.",

"Ruiz Muñoz (2024) – Implicaciones de la IA en la metodología de investigación":
"Reflexiona sobre cómo la inteligencia artificial está modificando las metodologías científicas y plantea los desafíos del fenómeno de la 'caja negra'."
}

selected_ref = st.selectbox(
    "Selecciona un artículo para ver su resumen:",
    list(references.keys())
)

st.markdown(
    f'<div class="ref-box">{references[selected_ref]}</div>',
    unsafe_allow_html=True
)
