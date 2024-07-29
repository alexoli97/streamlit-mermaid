import os
import streamlit as st
import streamlit.components.v1 as components

# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
_RELEASE = True

if not _RELEASE:
    _streamlit_mermaid = components.declare_component(
        "streamlit_mermaid",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _streamlit_mermaid = components.declare_component("streamlit_mermaid", path=build_dir)

def st_mermaid(code: str, width="auto", height="250px", key=None):
    svg = _streamlit_mermaid(code=code, width=width, height=height, key=key, default=None)
    return {"svg": svg}

# Test code to play with the component while it's in development.
if not _RELEASE:
    import streamlit as st

    code = """
    graph TD
        A --> B
        B --> C
        C --> D
        D --> E
    """

    result = st_mermaid(code)
    if result and result["svg"]:
        st.write("Diagrama renderizado:")
        st.write(result["svg"], unsafe_allow_html=True)
        
        # Añadir botón de descarga
        st.download_button(
            label="Descargar SVG",
            data=result["svg"],
            file_name="mermaid_diagram.svg",
            mime="image/svg+xml"
        )
    else:
        st.write("No se pudo generar el SVG")