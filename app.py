code = '''import streamlit as st

# Configuración de página
st.set_page_config(page_title="Resumen de Ruteo SJA1", layout="wide")

# Estilos personalizados para emular la apariencia de la tabla
st.markdown("""
<style>
    .header-box {
        background-color: #000000;
        color: white;
        text-align: center;
        font-weight: bold;
        font-size: 20px;
        padding: 10px;
        border-radius: 4px;
        margin-bottom: 20px;
    }
    .row-label {
        font-weight: bold;
        font-size: 16px;
        padding-top: 10px;
        color: #111111;
    }
    /* Personalización de colores de los selectbox si se requiere */
    div[data-baseweb="select"] {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=unsafe_allow_html)

st.markdown('<div class="header-box">RESUMEN DE RUTEO SJA1</div>', unsafe_allow_html=True)

# Pestañas para diferentes sedes o vistas (ejemplo: SJA1, SJA2, General)
tab1, tab2, tab3 = st.tabs(["📌 SJA1 - Principal", "📌 SJA2 - Secundaria", "📊 Resumen General"])

with tab1:
    st.write("### Selección de Parámetros y Estados - SJA1")
    
    # Usamos st.container y st.columns para simular la estructura de la tabla
    with st.container():
        # Fila 1: Volumen
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Volumen</div>', unsafe_allow_html=True)
        with col2:
            volumen = st.selectbox(
                "Volumen", 
                options=[
                    "C1: Se ruteó el volumen asignado para C1", 
                    "C2: Se ruteó el volumen asignado para C2", 
                    "Sin asignar"
                ],
                key="volumen",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 2: Rentals
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Rentals</div>', unsafe_allow_html=True)
        with col2:
            rentals = st.selectbox(
                "Rentals", 
                options=[
                    "Se asignan como híbridas, pero logis cambia algunas a no híbridas",
                    "Se asignan como 100% híbridas",
                    "No híbridas"
                ],
                key="rentals",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 3: Truck 3.5 tons MLP
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Truck 3.5 tons MLP</div>', unsafe_allow_html=True)
        with col2:
            truck_mlp = st.selectbox(
                "Truck 3.5 tons MLP", 
                options=["Logis no la toma", "Asignada", "En revisión"],
                key="truck_mlp",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 4: Delivery Cell Large Van
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Delivery Cell Large Van</div>', unsafe_allow_html=True)
        with col2:
            large_van = st.selectbox(
                "Delivery Cell Large Van", 
                options=["Logis no la toma", "Asignada", "En espera"],
                key="large_van",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 5: Extra Large Van MLP H&B
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Extra Large Van MLP H&B</div>', unsafe_allow_html=True)
        with col2:
            xl_van = st.selectbox(
                "Extra Large Van MLP H&B", 
                options=["No aplica", "Aplica", "Pendiente"],
                key="xl_van",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 6: DROPEO EN C1 (múltiples selecciones en paralelo)
        col1, col2, col3 = st.columns([1, 1.5, 1.5])
        with col1:
            st.markdown('<div class="row-label">DROPEO EN C1</div>', unsafe_allow_html=True)
        with col2:
            dropeo_c1_1 = st.selectbox(
                "Dropeo C1 Motivo 1", 
                options=["Por zona de restricción", "Por horario", "Sin dropeo"],
                key="dropeo_c1_1",
                label_visibility="collapsed"
            )
            dropeo_c1_2 = st.selectbox(
                "Dropeo C1 Motivo 2", 
                options=["Por ruta improductiva", "Capacidad excedida", "N/A"],
                key="dropeo_c1_2",
                label_visibility="collapsed"
            )
            dropeo_c1_3 = st.selectbox(
                "Dropeo C1 Motivo 3", 
                options=["Seleccionar opción...", "Opción A", "Opción B"],
                key="dropeo_c1_3",
                label_visibility="collapsed"
            )
        with col3:
            sub_opt_1 = st.selectbox("Sub-opción 1", ["-- Ninguna --", "Detalle 1", "Detalle 2"], key="sub1", label_visibility="collapsed")
            sub_opt_2 = st.selectbox("Sub-opción 2", ["-- Ninguna --", "Detalle 3", "Detalle 4"], key="sub2", label_visibility="collapsed")
            sub_opt_3 = st.selectbox("Sub-opción 3", ["-- Ninguna --", "Detalle 5", "Detalle 6"], key="sub3", label_visibility="collapsed")

        st.divider()

        # Fila 7: DROPEO CONTINGENCIA
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">DROPEO CONTINGENCIA</div>', unsafe_allow_html=True)
        with col2:
            dropeo_cont = st.selectbox(
                "Dropeo Contingencia", 
                options=["Por zona de restricción", "Sin contingencia", "Por fuerza mayor"],
                key="dropeo_cont",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 8: Alchichica ND
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Alchichica ND</div>', unsafe_allow_html=True)
        with col2:
            alchichica = st.selectbox(
                "Alchichica ND", 
                options=[
                    "Se carga en AM0 con 2 unidades Small Van MLP",
                    "Se carga en PM0 con 1 unidad Large Van",
                    "No se rutea"
                ],
                key="alchichica",
                label_visibility="collapsed"
            )

        st.divider()

        # Fila 9: Parámetros
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown('<div class="row-label">Parámetros</div>', unsafe_allow_html=True)
        with col2:
            parametros = st.selectbox(
                "Parámetros", 
                options=[
                    "Aplicados para el día lunes",
                    "Aplicados para el día martes",
                    "Aplicados para el fin de semana"
                ],
                key="parametros",
                label_visibility="collapsed"
            )

with tab2:
    st.info("Aquí puedes replicar la misma estructura para la sede SJA2 u otras regiones.")

with tab3:
    st.success("Resumen de las opciones seleccionadas:")
    st.json({
        "Volumen": volumen,
        "Rentals": rentals,
        "Truck 3.5 tons MLP": truck_mlp,
        "Delivery Cell Large Van": large_van,
        "Extra Large Van MLP H&B": xl_van,
        "Dropeo C1 Motivo 1": dropeo_c1_1,
        "Dropeo C1 Motivo 2": dropeo_c1_2,
        "Dropeo Contingencia": dropeo_cont,
        "Alchichica ND": alchichica,
        "Parámetros": parametros
    })
'''

with open("app_ruteo.py", "w", encoding="utf-8") as f:
    f.write(code)

print("File generated successfully: app_ruteo.py")
