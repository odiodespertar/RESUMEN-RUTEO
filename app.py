import streamlit as st

# Configuración de página
st.set_page_config(page_title="Resumen de Ruteo SJA1", layout="wide")

# Estilos adaptados para ser totalmente visibles en Modo Oscuro y Claro
st.markdown("""
<style>
    /* Caja de título superior */
    .header-box {
        background-color: #000000;
        color: #ffffff !important;
        text-align: center;
        font-weight: bold;
        font-size: 22px;
        padding: 12px;
        border-radius: 6px;
        margin-bottom: 25px;
        border: 1px solid #333333;
    }
    
    /* Etiquetas de la izquierda (nombres de la tabla) */
    .row-label {
        font-weight: bold;
        font-size: 16px;
        color: #ffffff !important; /* Texto blanco para que no se pierda en fondo oscuro */
        padding-top: 8px;
    }

    /* Forzar que el texto dentro de las opciones desplegables sea visible */
    div[data-baseweb="select"] {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado principal
st.markdown('<div class="header-box">RESUMEN DE RUTEO SJA1</div>', unsafe_allow_html=True)

# Pestañas
tab1, tab2, tab3 = st.tabs(["📌 SJA1 - Principal", "📌 SJA2 - Secundaria", "📊 Resumen General"])

with tab1:
    st.markdown("### Selección de Parámetros y Estados - SJA1")
    st.write("")
    
    # Fila 1: Volumen
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Volumen</div>', unsafe_allow_html=True)
    with col2:
        volumen = st.selectbox(
            "Volumen", 
            ["C1: Se ruteó el volumen asignado para C1", "C2: Se ruteó el volumen asignado para C2", "Sin asignar"],
            key="volumen", label_visibility="collapsed"
        )

    st.divider()

    # Fila 2: Rentals
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Rentals</div>', unsafe_allow_html=True)
    with col2:
        rentals = st.selectbox(
            "Rentals", 
            [
                "Se asignan como híbridas, pero logis cambia algunas a no híbridas",
                "Se asignan como 100% híbridas",
                "No híbridas"
            ],
            key="rentals", label_visibility="collapsed"
        )

    st.divider()

    # Fila 3: Truck 3.5 tons MLP
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Truck 3.5 tons MLP</div>', unsafe_allow_html=True)
    with col2:
        truck_mlp = st.selectbox(
            "Truck 3.5 tons MLP", 
            ["Logis no la toma", "Asignada", "En revisión"],
            key="truck_mlp", label_visibility="collapsed"
        )

    st.divider()

    # Fila 4: Delivery Cell Large Van
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Delivery Cell Large Van</div>', unsafe_allow_html=True)
    with col2:
        large_van = st.selectbox(
            "Delivery Cell Large Van", 
            ["Logis no la toma", "Asignada", "En espera"],
            key="large_van", label_visibility="collapsed"
        )

    st.divider()

    # Fila 5: Extra Large Van MLP H&B
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Extra Large Van MLP H&B</div>', unsafe_allow_html=True)
    with col2:
        xl_van = st.selectbox(
            "Extra Large Van MLP H&B", 
            ["No aplica", "Aplica", "Pendiente"],
            key="xl_van", label_visibility="collapsed"
        )

    st.divider()

    # Fila 6: DROPEO EN C1
    col1, col2, col3 = st.columns([1, 1.5, 1.5])
    with col1:
        st.markdown('<div class="row-label">DROPEO EN C1</div>', unsafe_allow_html=True)
    with col2:
        dropeo_c1_1 = st.selectbox("Dropeo 1", ["Por zona de restricción", "Por horario", "Sin dropeo"], key="d_c1_1", label_visibility="collapsed")
        dropeo_c1_2 = st.selectbox("Dropeo 2", ["Por ruta improductiva", "Capacidad excedida", "N/A"], key="d_c1_2", label_visibility="collapsed")
        dropeo_c1_3 = st.selectbox("Dropeo 3", ["-- Seleccionar opción --", "Opción A", "Opción B"], key="d_c1_3", label_visibility="collapsed")
    with col3:
        sub_1 = st.selectbox("Sub 1", ["-- Seleccionar --", "Filtro 1", "Filtro 2"], key="s1", label_visibility="collapsed")
        sub_2 = st.selectbox("Sub 2", ["-- Seleccionar --", "Filtro 3", "Filtro 4"], key="s2", label_visibility="collapsed")
        sub_3 = st.selectbox("Sub 3", ["-- Seleccionar --", "Filtro 5", "Filtro 6"], key="s3", label_visibility="collapsed")

    st.divider()

    # Fila 7: DROPEO CONTINGENCIA
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">DROPEO CONTINGENCIA</div>', unsafe_allow_html=True)
    with col2:
        dropeo_cont = st.selectbox(
            "Dropeo Contingencia", 
            ["Por zona de restricción", "Sin contingencia", "Por fuerza mayor"],
            key="dropeo_cont", label_visibility="collapsed"
        )

    st.divider()

    # Fila 8: Alchichica ND
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Alchichica ND</div>', unsafe_allow_html=True)
    with col2:
        alchichica = st.selectbox(
            "Alchichica ND", 
            [
                "Se carga en AM0 con 2 unidades Small Van MLP",
                "Se carga en PM0 con 1 unidad Large Van",
                "No se rutea"
            ],
            key="alchichica", label_visibility="collapsed"
        )

    st.divider()

    # Fila 9: Parámetros
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown('<div class="row-label">Parámetros</div>', unsafe_allow_html=True)
    with col2:
        parametros = st.selectbox(
            "Parámetros", 
            ["Aplicados para el día lunes", "Aplicados para el día martes", "Aplicados para el fin de semana"],
            key="parametros", label_visibility="collapsed"
        )

with tab2:
    st.info("Aquí puedes replicar la misma estructura para SJA2.")

with tab3:
    st.success("Opciones seleccionadas actualmente:")
    st.json({
        "Volumen": volumen,
        "Rentals": rentals,
        "Truck 3.5 tons MLP": truck_mlp,
        "Delivery Cell Large Van": large_van,
        "Extra Large Van MLP H&B": xl_van,
        "Dropeo C1 (1)": dropeo_c1_1,
        "Dropeo C1 (2)": dropeo_c1_2,
        "Dropeo Contingencia": dropeo_cont,
        "Alchichica ND": alchichica,
        "Parámetros": parametros
    })
