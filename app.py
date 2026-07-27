import streamlit as st

# Configuración de página
st.set_page_config(page_title="Resumen de Ruteo SJA1", layout="wide")

# CSS Ultracompacto estilo Excel
st.markdown("""
<style>
    /* 1. Eliminar márgenes exteriores gigantes de Streamlit */
    .block-container {
        padding: 0.5rem 1rem !important;
        max-width: 100% !important;
    }
    
    .stApp {
        background-color: #F4F5F7 !important;
        color: #000000 !important;
    }

    [data-testid="stVerticalBlock"] {
        gap: 2px !important;
    }

    /* 2. Encabezado compacto */
    .header-box {
        background-color: #000000;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        font-size: 16px;
        padding: 6px;
        border-radius: 3px;
        margin-bottom: 6px;
    }

    /* 3. Reducir pestañas */
    button[data-baseweb="tab"] {
        padding: 4px 12px !important;
        font-size: 13px !important;
    }

    /* 4. Celda de texto a la izquierda ultra compacta */
    .label-cell {
        font-weight: 700;
        font-size: 12.5px;
        color: #111111;
        padding-top: 4px;
        line-height: 1.1;
    }

    /* 5. ACHICAR DESPLEGABLES (COMPACTO) */
    div[data-testid="stSelectbox"] {
        margin: 0px !important;
        padding: 0px !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 6px !important;
        border: none !important;
        min-height: 28px !important;
        height: 28px !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    /* Reducir tamaño del icono de la flechita */
    div[data-baseweb="select"] svg {
        width: 14px !important;
        height: 14px !important;
    }

   /* Colores exactos extraídos de la captura */
.purple-select div[data-baseweb="select"] > div { background-color: #D6D5F2 !important; color: #362985 !important; } /* Volumen */
.blue-select div[data-baseweb="select"] > div   { background-color: #D3E8E9 !important; color: #1E5C6B !important; } /* Rentals */
.yellow-select div[data-baseweb="select"] > div { background-color: #FFF3C4 !important; color: #78630B !important; } /* Trucks / Vans */
.gray-select div[data-baseweb="select"] > div   { background-color: #ECEEEF !important; color: #2B303A !important; } /* Extra Large Van / Opciones vacías */
.red-select div[data-baseweb="select"] > div    { background-color: #FFD2D2 !important; color: #A81818 !important; } /* Restricción */
.orange-select div[data-baseweb="select"] > div { background-color: #FEDBC3 !important; color: #A04400 !important; } /* Ruta improductiva */
.green-select div[data-baseweb="select"] > div  { background-color: #D7F0DB !important; color: #175B22 !important; } /* Alchichica ND */
.pink-select div[data-baseweb="select"] > div   { background-color: #FEE0EB !important; color: #6D1B40 !important; } /* Parámetros */

    /* Líneas divisiones delgadas */
    .dashed-line {
        border-top: 1px dashed #B0B0B0;
        margin: 3px 0px;
    }
</style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="header-box">RESUMEN DE RUTEO SJA1</div>', unsafe_allow_html=True)

# Pestañas
tab1, tab2 = st.tabs(["📌 SJA1 - Principal", "📊 Datos"])

with tab1:
    # 1. Volumen
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Volumen</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="purple-select">', unsafe_allow_html=True)
        volumen = st.selectbox("Volumen", ["Uniciclo: se ruteó el volumen disponible en logis", "C2: Se ruteó C2"], key="vol", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 2. Rentals
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Rentals</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="blue-select">', unsafe_allow_html=True)
        rentals = st.selectbox("Rentals", ["Se asignan como híbridas, pero logis cambia algunas a no híbridas", "Híbridas 100%"], key="rent", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 3. Truck 3.5 tons MLP
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Truck 3.5 tons MLP</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="yellow-select">', unsafe_allow_html=True)
        truck_mlp = st.selectbox("Truck MLP", ["Logis no la toma", "Asignada"], key="truck", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. Delivery Cell Large Van
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Delivery Cell Large Van</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="yellow-select">', unsafe_allow_html=True)
        large_van = st.selectbox("Large Van", ["Logis no la toma", "Asignada"], key="van", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 5. Extra Large Van MLP H&B
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Extra Large Van MLP H&B</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="gray-select">', unsafe_allow_html=True)
        xl_van = st.selectbox("XL Van", ["No aplica", "Aplica"], key="xl", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # Línea punteada
    st.markdown('<div class="dashed-line"></div>', unsafe_allow_html=True)

    # 6. DROPEO EN C1
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell" style="padding-top:18px;">DROPEO EN C1</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="red-select">', unsafe_allow_html=True)
        d_c1_1 = st.selectbox("Dropeo 1", ["Por zona de restricción", "Sin restricción"], key="dc1_1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="orange-select">', unsafe_allow_html=True)
        d_c1_2 = st.selectbox("Dropeo 2", ["Por ruta improductiva", "Ruta normal"], key="dc1_2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="gray-select">', unsafe_allow_html=True)
        d_c1_3 = st.selectbox("Dropeo 3", ["-- Seleccionar --"], key="dc1_3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="gray-select">', unsafe_allow_html=True)
        sub_1 = st.selectbox("Sub 1", ["-- Seleccionar --"], key="s1", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="gray-select">', unsafe_allow_html=True)
        sub_2 = st.selectbox("Sub 2", ["-- Seleccionar --"], key="s2", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="gray-select">', unsafe_allow_html=True)
        sub_3 = st.selectbox("Sub 3", ["-- Seleccionar --"], key="s3", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="dashed-line"></div>', unsafe_allow_html=True)

    # 7. DROPEO CONTINGENCIA
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">DROPEO CONTINGENCIA</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="red-select">', unsafe_allow_html=True)
        d_cont = st.selectbox("Contingencia", ["Por zona de restricción", "Sin contingencia"], key="d_cont", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 8. Alchichica ND
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Alchichica ND</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="green-select">', unsafe_allow_html=True)
        alchichica = st.selectbox("Alchichica", ["Se carga en AM0 con 2 unidades Small Van MLP", "No se rutea"], key="alch", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

    # 9. Parámetros
    col1, col2, col3 = st.columns([1.1, 1.9, 1])
    with col1:
        st.markdown('<div class="label-cell">Parámetros</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="pink-select">', unsafe_allow_html=True)
        parametros = st.selectbox("Parámetros", ["Aplicados para el día lunes", "Aplicados martes"], key="params", label_visibility="collapsed")
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.json({"Volumen": volumen, "Rentals": rentals, "Parámetros": parametros})
