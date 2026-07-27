import streamlit as st
import pandas as pd

# Configuración de la ventana del navegador
st.set_page_config(
    page_title="Visualizador de Resumen de Ruteo",
    page_icon="📊",
    layout="wide"
)

# Título principal de la aplicación
st.title("📊 Aplicación de Resumen de Ruteo")
st.write("Esta herramienta te permite cargar y explorar interactivamente los datos de tu tabla de ruteo.")

# Componente para subir el archivo de datos
uploaded_file = st.file_uploader("Sube el archivo de datos (exportado en formato CSV desde tu hoja de cálculo)", type=["csv"])

if uploaded_file is not None:
    try:
        # Leer el archivo sin asumir una fila de encabezado fija
        df = pd.read_csv(uploaded_file, header=None)
        
        # Limpieza: Eliminar columnas que estén completamente vacías
        df = df.dropna(how='all', axis=1)
        
        # Si la primera columna contiene solo valores nulos, la removemos
        if df.iloc[:, 0].isnull().all():
            df = df.drop(df.columns[0], axis=1)
            
        # Restablecer los índices de las columnas para trabajar ordenadamente
        df.columns = range(df.shape[1])
        
        # Asignar nombres legibles a las columnas principales si tiene la estructura esperada
        if df.shape[1] >= 2:
            df = df.rename(columns={0: "Concepto / Categoría", 1: "Detalle / Estado / Comentarios"})
            # Si existen más columnas, les asignamos un nombre genérico
            for i in range(2, df.shape[1]):
                df = df.rename(columns={i: f"Información Adicional {i-1}"})
        
        # Mostrar la tabla completa
        st.subheader("📋 Vista General de la Tabla")
        st.dataframe(df, use_container_width=True)
        
        # Sección de filtros y búsqueda
        st.subheader("🔍 Buscador y Filtros Rápidos")
        termino_busqueda = st.text_input("Introduce un término para buscar en cualquier celda de la tabla:")
        
        if termino_busqueda:
            # Filtrar las filas que contengan el texto ingresado (sin importar mayúsculas/minúsculas)
            df_filtrado = df[df.astype(str).apply(lambda row: row.str.contains(termino_busqueda, case=False)).any(axis=1)]
            st.success(f"Se encontraron {len(df_filtrado)} filas que coinciden con tu búsqueda.")
            st.dataframe(df_filtrado, use_container_width=True)
            
        # Métrica rápida de resumen
        st.sidebar.header("Estadísticas del Archivo")
        st.sidebar.metric(label="Total de Filas", value=df.shape[0])
        st.sidebar.metric(label="Total de Columnas", value=df.shape[1])

    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    # Mensaje inicial cuando no se ha subido ningún archivo
    st.info("ℹ️ Para comenzar, exporta tu tabla actual como un archivo `.csv` desde tu menú de archivos y súbelo usando el botón de arriba.")

# Instrucciones de uso en el pie de página
st.markdown("---")
st.caption("Desarrollado para la visualización interactiva de datos de ruteo.")
