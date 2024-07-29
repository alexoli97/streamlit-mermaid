import React, { useRef, useEffect, ReactElement } from "react"
import {
  withStreamlitConnection,
  Streamlit,
  ComponentProps,
} from "streamlit-component-lib"
import mermaid from 'mermaid';

function MermaidViewer({args}: ComponentProps): ReactElement {
  const ref = useRef<HTMLDivElement>(null);
  const { code, width, height } = args;

  useEffect(() => {
    Streamlit.setFrameHeight();
  })

  useEffect(() => {
    if (ref.current) {
      mermaid.mermaidAPI.render('graphDiv', code).then((svgGraph) => {
        if (ref.current) {
          ref.current.innerHTML = svgGraph.svg;
          // Enviamos el SVG de vuelta a Streamlit
          Streamlit.setComponentValue(svgGraph.svg);
        }
      });
    }
  }, [code]);

  return <div ref={ref} style={{width: width, height: height, overflow: "auto"}} ></div>;
}

export default withStreamlitConnection(MermaidViewer)