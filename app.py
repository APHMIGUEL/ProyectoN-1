import streamlit as st
import pandas as pd

# ---------------- MENÚ ----------------
st.sidebar.image("LOGO_DMC.png", width=150)
st.sidebar.title("Menú")


opcion = st.sidebar.selectbox(
    "Seleccione una opción",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# ---------------- HOME ----------------
if opcion == "Home":
    st.image("logo.png", width = 200)
    st.title("Mi Proyecto N°1")

    st.subheader("Python Fundamentals - Módulo 1")

    st.markdown("### 👤 Datos del Estudiante")
    st.write("Nombre completo: Miguel Ángel Pizarro Huaraca")
    st.write("Carrera: Estudiante de Ingeniería de Minas")
    st.write("Año: 2026")

    st.markdown("### 📌 Descripción del Proyecto")
    st.write(
        "Esta aplicación fue desarrollada en Streamlit como parte del módulo de Python Fundamentals. "
        "Integra conceptos de programación como estructuras de datos, control de flujo, funciones y "
        "programación orientada a objetos mediante una interfaz interactiva."
    )

    st.markdown("### 🛠️ Tecnologías utilizadas")
    st.write("- Streamlit")
    st.write("- Pandas")
    st.write("- NumPy")

# ---------------- EJERCICIO 1 ----------------

elif opcion == "Ejercicio 1":
    import pandas as pd

    st.image("imagen1.png", width = 200)
    st.title("💰 Ejercicio 1 - Flujo de Caja")

    st.markdown("### 📥 Registro de movimientos financieros")

    # Inicializar lista
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # ---------------- FORMULARIO ----------------
    concepto = st.text_input("📝 Concepto")
    tipo = st.selectbox("📌 Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("💵 Valor (S/)", min_value=0.0, step=1.0)

    # ---------------- BOTÓN ----------------
    if st.button("➕ Agregar movimiento"):
        if concepto.strip() == "":
            st.warning("⚠️ Ingrese un concepto válido")
        elif valor <= 0:
            st.warning("⚠️ El valor debe ser mayor a 0")
        else:
            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": valor
            }
            st.session_state.movimientos.append(movimiento)
            st.success("✅ Movimiento agregado correctamente")

    # ---------------- MOSTRAR DATOS ----------------
    if len(st.session_state.movimientos) > 0:
        st.markdown("### 📊 Movimientos registrados")

        df = pd.DataFrame(st.session_state.movimientos)

        # Formato en soles
        df["Valor"] = df["Valor"].apply(lambda x: f"S/ {x:,.2f}")

        st.dataframe(df, use_container_width=True)

        # Cálculos (usar valores originales)
        valores = pd.DataFrame(st.session_state.movimientos)
        ingresos = valores[valores["Tipo"] == "Ingreso"]["Valor"].sum()
        gastos = valores[valores["Tipo"] == "Gasto"]["Valor"].sum()
        saldo = ingresos - gastos

        # ---------------- MÉTRICAS ----------------
        st.markdown("### 📈 Resumen financiero")

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Ingresos", f"S/ {ingresos:,.2f}")
        col2.metric("💸 Gastos", f"S/ {gastos:,.2f}")
        col3.metric("📊 Saldo", f"S/ {saldo:,.2f}")

        # ---------------- ESTADO FINAL ----------------
        if saldo > 0:
            st.success("🟢 Flujo de caja a favor")
        elif saldo < 0:
            st.error("🔴 Flujo de caja en contra")
        else:
            st.info("🟡 Flujo de caja equilibrado")

# ---------------- EJERCICIO 2 ----------------

elif opcion == "Ejercicio 2":
    import numpy as np
    import pandas as pd

    st.image("imagen2.png", width = 200)
    st.title("🛒 Ejercicio 2 - Registro de Ventas de Insumos Mineros")

    st.markdown("### 📦 Registro de productos y ventas")

    # Inicializar arrays
    if "productos" not in st.session_state:
        st.session_state.productos = []
        st.session_state.categorias = []
        st.session_state.precios = []
        st.session_state.cantidades = []
        st.session_state.totales = []

    # ---------------- FORMULARIO ----------------
    producto = st.text_input("📝 Nombre del producto")
    categoria = st.selectbox("📌 Categoría", ["Explosivos", "Repuestos", "Combustible", "Herramientas"])
    precio = st.number_input("💲 Precio unitario (USD)", min_value=0.0, step=1.0)
    cantidad = st.number_input("🔢 Cantidad vendida", min_value=1, step=1)

    # ---------------- BOTÓN ----------------
    if st.button("➕ Registrar venta"):
        if producto.strip() == "":
            st.warning("⚠️ Ingrese un nombre válido")
        else:
            total = precio * cantidad

            # Guardar en arrays
            st.session_state.productos.append(producto)
            st.session_state.categorias.append(categoria)
            st.session_state.precios.append(precio)
            st.session_state.cantidades.append(cantidad)
            st.session_state.totales.append(total)

            st.success("✅ Venta registrada correctamente")

    # ---------------- MOSTRAR DATOS ----------------
    if len(st.session_state.productos) > 0:
        st.markdown("### 📊 Historial de ventas")

        # Convertir a NumPy
        productos_np = np.array(st.session_state.productos)
        categorias_np = np.array(st.session_state.categorias)
        precios_np = np.array(st.session_state.precios)
        cantidades_np = np.array(st.session_state.cantidades)
        totales_np = np.array(st.session_state.totales)

        # Crear DataFrame
        df = pd.DataFrame({
            "Producto": productos_np,
            "Categoría": categorias_np,
            "Precio (USD)": precios_np,
            "Cantidad": cantidades_np,
            "Total (USD)": totales_np
        })

        # Formato en dólares
        df["Precio (USD)"] = df["Precio (USD)"].apply(lambda x: f"$ {x:,.2f}")
        df["Total (USD)"] = df["Total (USD)"].apply(lambda x: f"$ {x:,.2f}")

        st.dataframe(df, use_container_width=True)

# ---------------- EJERCICIO 3 ----------------

elif opcion == "Ejercicio 3":
    import pandas as pd
    import libreria_funciones_proyecto1 as lf

    st.image("imagen3.png", width = 200)
    st.title("⚙️ Dashboard de Mantenimiento")
    st.markdown("### 📊 Análisis de confiabilidad de equipos mineros")

    # ---------------- SELECTOR ----------------
    funcion = st.selectbox(
        "🔧 Seleccione el cálculo",
        ["MTBF • MTTR • Disponibilidad"]
    )

    # ---------------- ESTADO ----------------
    if "historial_funciones" not in st.session_state:
        st.session_state.historial_funciones = []

    # ---------------- FORMULARIO ----------------
    st.markdown("### 📥 Ingreso de datos operativos")

    col1, col2, col3 = st.columns(3)

    with col1:
        tiempo_op = st.number_input("⏱️ Horas de operación", min_value=1.0)

    with col2:
        fallas = st.number_input("⚠️ Número de fallas", min_value=1)

    with col3:
        tiempo_rep = st.number_input("🛠️ Horas de reparación", min_value=0.0)

    # ---------------- BOTÓN ----------------
    if st.button("🚀 Calcular indicadores"):
        try:
            resultado = lf.calcular_indicadores_mantenimiento(
                tiempo_op,
                fallas,
                tiempo_rep
            )

            st.markdown("### 📊 Resultados del análisis")

            col1, col2, col3 = st.columns(3)

            col1.metric("⚙️ MTBF (h)", resultado["mtbf_h"])
            col2.metric("🔧 MTTR (h)", resultado["mttr_h"])
            col3.metric("📈 Disponibilidad (%)", f"{resultado['disponibilidad_pct']}%")

            # Indicador visual
            if resultado["disponibilidad_pct"] >= 90:
                st.success("🟢 Excelente disponibilidad del equipo")
            elif resultado["disponibilidad_pct"] >= 70:
                st.warning("🟡 Disponibilidad aceptable, revisar mantenimiento")
            else:
                st.error("🔴 Baja disponibilidad, requiere intervención urgente")

            # Guardar historial
            registro = {
                "Horas Operación": tiempo_op,
                "Fallas": fallas,
                "Horas Reparación": tiempo_rep,
                "MTBF": resultado["mtbf_h"],
                "MTTR": resultado["mttr_h"],
                "Disponibilidad (%)": resultado["disponibilidad_pct"]
            }

            st.session_state.historial_funciones.append(registro)

        except Exception as e:
            st.error(f"❌ Error: {e}")

    # ---------------- HISTORIAL ----------------
    if len(st.session_state.historial_funciones) > 0:
        st.markdown("### 📋 Historial de análisis")

        df = pd.DataFrame(st.session_state.historial_funciones)

        st.dataframe(df, use_container_width=True)

# ---------------- EJERCICIO 4 ----------------

elif opcion == "Ejercicio 4":
    import pandas as pd
    from libreria_clases_proyecto1 import MezclaConcreto

    st.image("imagen4.png", width = 200)
    st.title("🏗️ Diseño de Mezcla de Concreto")
    st.markdown("### ⚙️ Cálculo y gestión de volúmenes y materiales")

    # ---------------- ESTADO ----------------
    if "mezclas" not in st.session_state:
        st.session_state.mezclas = []

    # ---------------- TABS ----------------
    tab1, tab2, tab3 = st.tabs(["➕ Crear", "📊 Ver", "✏️ Actualizar / ❌ Eliminar"])

    # =========================================================
    # 🟢 CREAR
    # =========================================================
    with tab1:
        st.markdown("### ➕ Registrar nueva mezcla")

        largo = st.number_input("📏 Largo (m)", min_value=0.1)
        ancho = st.number_input("📐 Ancho (m)", min_value=0.1)
        espesor = st.number_input("📏 Espesor (m)", min_value=0.01)
        desperdicio = st.number_input("♻️ Desperdicio (%)", min_value=0.0, max_value=100.0)
        dosificacion = st.number_input("🧱 Dosificación cemento (kg/m³)", min_value=1.0)

        if st.button("➕ Calcular y guardar"):
            try:
                mezcla = MezclaConcreto(
                    largo,
                    ancho,
                    espesor,
                    desperdicio,
                    dosificacion
                )

                resultado = mezcla.resumen()

                st.session_state.mezclas.append(resultado)

                st.success("✅ Mezcla registrada correctamente")

            except Exception as e:
                st.error(f"❌ Error: {e}")

    # =========================================================
    # 🔵 LEER
    # =========================================================
    with tab2:
        st.markdown("### 📊 Mezclas registradas")

        if len(st.session_state.mezclas) > 0:
            df = pd.DataFrame(st.session_state.mezclas)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("ℹ️ No hay registros aún")

    # =========================================================
    # 🟡 ACTUALIZAR + 🔴 ELIMINAR
    # =========================================================
    with tab3:
        st.markdown("### ✏️ Editar o eliminar mezcla")

        if len(st.session_state.mezclas) > 0:
            df = pd.DataFrame(st.session_state.mezclas)
            st.dataframe(df, use_container_width=True)

            indice = st.number_input(
                "🔢 Índice de la mezcla",
                min_value=0,
                max_value=len(df) - 1,
                step=1
            )

            st.markdown("### ✏️ Nuevos datos")

            nuevo_largo = st.number_input("📏 Nuevo largo", min_value=0.1, key="largo")
            nuevo_ancho = st.number_input("📐 Nuevo ancho", min_value=0.1, key="ancho")
            nuevo_espesor = st.number_input("📏 Nuevo espesor", min_value=0.01, key="espesor")
            nuevo_desperdicio = st.number_input("♻️ Nuevo desperdicio (%)", min_value=0.0, max_value=100.0, key="desp")
            nueva_dosificacion = st.number_input("🧱 Nueva dosificación (kg/m³)", min_value=1.0, key="dos")

            # -------- ACTUALIZAR --------
            if st.button("✏️ Actualizar mezcla"):
                try:
                    mezcla = MezclaConcreto(
                        nuevo_largo,
                        nuevo_ancho,
                        nuevo_espesor,
                        nuevo_desperdicio,
                        nueva_dosificacion
                    )

                    st.session_state.mezclas[indice] = mezcla.resumen()
                    st.success("✅ Mezcla actualizada")

                except Exception as e:
                    st.error(f"❌ Error: {e}")

            # -------- ELIMINAR --------
            if st.button("❌ Eliminar mezcla"):
                st.session_state.mezclas.pop(indice)
                st.success("🗑️ Mezcla eliminada")

        else:
            st.info("ℹ️ No hay datos para modificar")