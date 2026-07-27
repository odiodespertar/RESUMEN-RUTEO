import streamlit as st

# Configuración de página
st.set_page_config(page_title="Resumen de Ruteo SJA1", layout="wide")

# CSS personalizado para forzar tema claro y clonar la apariencia de la imagen
st.markdown("""
<style>
    /* Forzar fondo gris claro tipo Excel en toda la app */
    .stApp {
        background-color: #ECECEC !important;
        color: #000000 !important;
    }

    /* Encabezado Negro Superior */
    .header-box {
        background-color: #000000;
        color: #FFFFFF !important;
        text-align: center;
        font-weight: 900;
        font-size: 22px;
        padding: 10px;
        letter-spacing: 1px;
        border-radius: 2px;
        margin-bottom: 0px;
    }

    /* Etiquetas de la columna izquierda */
    .row-label {
        font-weight: 800;
        font-size: 16px;
        color: #000000 !important;
        padding-left: 10px;
        display: flex;
        align-items: center;
        height: 100%;
    }

    /* Estilos base para todos los selectbox */
    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border: none !important;
        font-weight: 500 !important;
    }

    /* Colores pastel específicos para replicar la imagen */
    .bg-purple div[data-baseweb="select"] > div { background-color: #DCD6F7 !important; color: #362285 !important; }
    .bg-blue div[data-baseweb="select"] > div   { background-color: #D2E7ED !important; color: #1D5C6E !important; }
    .bg-yellow div[data-baseweb="select"] > div { background-color: #FFF3C4 !important; color: #7B6200 !important; }
    .bg-red div[data-baseweb="select"] > div    { background-color: #FFD2D2 !important; color: #B71C1C !important; }
    .bg-orange div[data-baseweb="select"] > div { background-color: #FFE0C2 !important; color: #A04000 !important; }
    .bg-green div[data-baseweb="select"] > div  { background-color: #D4EDDA !important; color: #155724 !important; }
    .bg-pink div[data-baseweb="select"] > div   { background-color: #F8D7DA !important; color: #721C24 !important; }
    .bg-gray div[data-baseweb="select"] > div   { background-color: #EAEAEA !important; color: #555555 !important; }

    /* Forzar texto de opciones desplegables a negro */
    div[role="listbox"] li {
        color: #000000 !important;
        background-color: #FFFFFF !important;
    }

    /* Fondo blanco para las celdas de la tabla */
    .grid-row {
        background-color: #F8F9FA;
        border-bottom: 1px solid #D0D0D0;
        padding: 6px 0px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado Principal
st.markdown('<div class="header-box">RESUMEN DE RUTEO SJA1</div>', unsafe_allow_html=True)

# Pestañas
tab1, tab2, tab3 = st.tabs(["📌 SJA1 - Principal", "📌 SJA2 - Secundaria", "📊 Resumen General"])

with tab1:
    
    # Fila 1: Volumen (Morado)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Volumen</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-purple">', unsafe_allow_html=True)
        volumen = st.selectbox("Volumen", ["C1: Se ruteó el volumen asignado para C1", "C2: Se ruteó el volumen asignado para C2"], key="volumen", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 2: Rentals (Azul claro)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Rentals</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-blue">', unsafe_allow_html=True)
        rentals = st.selectbox("Rentals", ["Se asignan como híbridas, pero logis cambia algunas a no híbridas", "Se asignan 100% híbridas"], key="rentals", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 3: Truck 3.5 tons MLP (Amarillo)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Truck 3.5 tons MLP</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-yellow">', unsafe_allow_html=True)
        truck_mlp = st.selectbox("Truck MLP", ["Logis no la toma", "Asignada"], key="truck_mlp", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 4: Delivery Cell Large Van (Amarillo)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Delivery Cell Large Van</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-yellow">', unsafe_allow_html=True)
        large_van = st.selectbox("Large Van", ["Logis no la toma", "Asignada"], key="large_van", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 5: Extra Large Van MLP H&B (Gris/Normal)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Extra Large Van MLP H&B</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-gray">', unsafe_allow_html=True)
        xl_van = st.selectbox("XL Van", ["No aplica", "Aplica"], key="xl_van", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 6: DROPEO EN C1 (Múltiples opciones con colores)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">DROPEO EN C1</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-red">', unsafe_allow_html=True)
        d_c1_1 = st.selectbox("Dropeo C1 1", ["Por zona de restricción", "Sin restricción"], key="d_c1_1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="bg-orange" style="margin-top: 8px;">', unsafe_allow_html=True)
        d_c1_2 = st.selectbox("Dropeo C1 2", ["Por ruta improductiva", "Ruta normal"], key="d_c1_2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="bg-gray" style="margin-top: 8px;">', unsafe_allow_html=True)
        d_c1_3 = st.selectbox("Dropeo C1 3", ["-- Seleccionar --", "Opción A"], key="d_c1_3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="bg-gray">', unsafe_allow_html=True)
        sub_1 = st.selectbox("Sub 1", ["-- Seleccionar --"], key="sub_1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="bg-gray" style="margin-top: 8px;">', unsafe_allow_html=True)
        sub_2 = st.selectbox("Sub 2", ["-- Seleccionar --"], key="sub_2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 7: DROPEO CONTINGENCIA (Rojo)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">DROPEO CONTINGENCIA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-red">', unsafe_allow_html=True)
        d_cont = st.selectbox("Contingencia", ["Por zona de restricción", "Sin contingencia"], key="d_cont", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 8: Alchichica ND (Verde)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Alchichica ND</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-green">', unsafe_allow_html=True)
        alchichica = st.selectbox("Alchichica", ["Se carga en AM0 con 2 unidades Small Van MLP", "No se rutea"], key="alchichica", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # Fila 9: Parámetros (Rosa)
    col1, col2, col3 = st.columns([1.2, 1.8, 1])
    with col1:
        st.markdown('<div class="row-label">Parámetros</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="bg-pink">', unsafe_allow_html=True)
        parametros = st.selectbox("Parámetros", ["Aplicados para el día lunes", "Aplicados para el día martes"], key="parametros", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.info("Pestaña secundaria para SJA2.")

with tab3:
    st.json({"Volumen": volumen, "Rentals": rentals, "Parámetros": parametros})
