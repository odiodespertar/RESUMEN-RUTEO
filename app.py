import streamlit as st

# Configuración de página
st.set_page_config(page_title="Resumen de Ruteo SJA1", layout="wide")

# CSS Ultracompacto estilo Google Sheets con colores exactos
st.markdown("""
<style>
    /* 1. Eliminar márgenes exteriores de Streamlit */
    .block-container {
        padding: 0.5rem 1rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        background-color: #F8F9FA !important;
        color: #000000 !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 1px !important;
    }

    /* 2. Encabezado negro superior */
    .header-box {
        background-color: #000000;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        font-size: 15px;
        padding: 5px;
        border-radius: 2px;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }

    /* 3. Pestañas pequeñas */
    button[data-baseweb="tab"] {
        padding: 3px 10px !important;
        font-size: 12px !important;
    }

    /* 4. Etiqueta izquierda */
    .label-cell {
        font-weight: bold;
        font-size: 12px;
        color: #000000;
        padding-top: 5px;
        font-family: Arial, sans-serif;
    }

    /* 5. Altura reducida para los desplegables (Compacto) */
    div[data-testid="stSelectbox"] {
        margin: 0px !important;
        padding: 0px !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border: none !important;
        min-height: 26px !important;
        height: 26px !important;
        font-size: 11.5px !important;
        font-weight: 500 !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    div[data-baseweb="select"] svg {
        width: 12px !important;
        height: 12px !important;
    }

    /* 6. Colores Exactos de las celdas de la captura */
    .c-purple div[data-baseweb="select"] > div { background-color: #D6D5F2 !important; color: #362985 !important; }
    .c-blue div[data-baseweb="select"] > div   { background-color: #D3E8E9 !important; color: #1E5C6B !important; }
    .c-yellow div[data-baseweb="select"] > div { background-color: #FFF3C4 !important; color: #78630B !important; }
    .c-gray div[data-baseweb="select"] > div   { background-color: #ECEEEF !important; color: #2B303A !important; }
    .c-red div[data-baseweb="select"] > div    { background-color: #FFD2D2 !important; color: #A81818 !important; }
    .c-orange div[data-baseweb="select"] > div { background-color: #FEDBC3 !important; color: #A04400 !important; }
    .c-green div[data-baseweb="select"] > div  { background-color: #D7F0DB !important; color: #175B22 !important; }
    .c-pink div[data-baseweb="select"] > div   { background-color: #FEE0EB !important; color: #6D1B40 !important; }

    /* Divisiones punteadas */
    .dashed-divider {
        border-top: 1px dashed #A0A0A0;
        margin: 2px 0px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="header-box">RESUMEN DE RUTEO SJA1</div>', unsafe_allow_html=True)

# Pestañas
tab1, tab2 = st.tabs(["📌 RESUMEN SJA1", "📊 Datos JSON"])

with tab1:
    # 1. Volumen (Morado)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Volumen</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-purple">', unsafe_allow_html=True)
        volumen = st.selectbox("Volumen", ["C1: Se ruteó el volumen asignado para C1", "C2: Se ruteó el volumen asignado para C2"], key="vol", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. Rentals (Azul)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Rentals</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-blue">', unsafe_allow_html=True)
        rentals = st.selectbox("Rentals", ["Se asignan como híbridas, pero logis cambia algunas a no híbridas", "No aplica"], key="rent", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. Truck 3.5 tons MLP (Amarillo)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Truck 3.5 tons MLP</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-yellow">', unsafe_allow_html=True)
        truck_mlp = st.selectbox("Truck MLP", ["Logis no la toma", "Logis la toma", "No aplica"], key="truck", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. Delivery Cell Large Van (Amarillo)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Delivery Cell Large Van</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-yellow">', unsafe_allow_html=True)
        large_van = st.selectbox("Large Van", ["Logis no la toma", "Logis la toma", "No aplica"], key="van", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. Extra Large Van MLP H&B (Gris)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Extra Large Van MLP H&B</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-gray">', unsafe_allow_html=True)
        xl_van = st.selectbox("XL Van", ["No aplica", "Aplica"], key="xl", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # División punteada arriba de DROPEO
    st.markdown('<div class="dashed-divider"></div>', unsafe_allow_html=True)

    # 6. DROPEO EN C1 (Columna principal + Subcolumnas a la derecha)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell" style="padding-top:25px;">DROPEO EN C1</div>', unsafe_allow_html=True)
    with col2:
        # Fila 1 de Dropeo (Rojo)
        st.markdown('<div class="c-red">', unsafe_allow_html=True)
        d_c1_1 = st.selectbox("Dropeo 1", ["Por zona de restricción", "No hubo"], key="dc1_1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        # Fila 2 de Dropeo (Naranja)
        st.markdown('<div class="c-orange" style="margin-top:2px;">', unsafe_allow_html=True)
        d_c1_2 = st.selectbox("Dropeo 2", ["Por ruta improductiva", "No hubo"], key="dc1_2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        # Fila 3 de Dropeo (Amarillo / Naranja Claro)
        st.markdown('<div class="c-yellow" style="margin-top:2px;">', unsafe_allow_html=True)
        d_c1_3 = st.selectbox("Dropeo 3", ["Dropeo de nodo", "No hubo"], key="dc1_3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        # Sub-desplegables grises auxiliares a la derecha
        st.markdown('<div class="c-gray">', unsafe_allow_html=True)
        sub_1 = st.selectbox("Sub 1", ["-- Seleccionar --"], key="s1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="c-gray" style="margin-top:2px;">', unsafe_allow_html=True)
        sub_2 = st.selectbox("Sub 2", ["-- Seleccionar --"], key="s2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="c-gray" style="margin-top:2px;">', unsafe_allow_html=True)
        sub_3 = st.selectbox("Sub 3", ["-- Seleccionar --"], key="s3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # División punteada abajo de DROPEO
    st.markdown('<div class="dashed-divider"></div>', unsafe_allow_html=True)

    # 7. DROPEO CONTINGENCIA (Rojo)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">DROPEO CONTINGENCIA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-red">', unsafe_allow_html=True)
        d_cont = st.selectbox("Contingencia", ["Por zona de restricción", "No hubo"], key="d_cont", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 8. Alchichica ND (Verde)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Alchichica ND</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-green">', unsafe_allow_html=True)
        alchichica = st.selectbox("Alchichica", ["Se carga en AM0 con 2 unidades Small Van MLP"], key="alch", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 9. Parámetros (Rosa)
    col1, col2, col3 = st.columns([1.2, 2, 1])
    with col1:
        st.markdown('<div class="label-cell">Parámetros</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="c-pink">', unsafe_allow_html=True)
        parametros = st.selectbox("Parámetros", ["Aplicados para el día lunes"], key="params", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.json({
        "Volumen": volumen,
        "Rentals": rentals,
        "Truck 3.5 tons MLP": truck_mlp,
        "Delivery Cell Large Van": large_van,
        "Extra Large Van MLP H&B": xl_van,
        "Dropeo C1 (1)": d_c1_1,
        "Dropeo C1 (2)": d_c1_2,
        "Dropeo C1 (3)": d_c1_3,
        "Dropeo Contingencia": d_cont,
        "Alchichica ND": alchichica,
        "Parámetros": parametros
    })
