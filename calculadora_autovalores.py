import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.set_page_config(page_title="Calculadora de Autovalores", page_icon="🧮")
    
    st.title("🧮 Calculadora de Autovalores y Autovectores")
    st.markdown("""
    Esta aplicación calcula los autovalores ($\lambda$) y autovectores ($v$) 
    de una matriz cuadrada utilizando **NumPy**.
    """)

    st.divider()

    st.subheader("1. Configurar Matriz")
    dimension = st.number_input(
        "Dimensión de la matriz (N x N)", 
        min_value=2, 
        max_value=10, 
        value=3,
        step=1
    )

    st.write("Edita los valores de la matriz directamente en la tabla:")
    
    if 'matrix_data' not in st.session_state:
        st.session_state.matrix_data = pd.DataFrame(
            np.zeros((dimension, dimension)),
            columns=[f"Col {i+1}" for i in range(dimension)]
        )
    
    current_df = pd.DataFrame(
        np.zeros((dimension, dimension)),
        columns=[f"Col {i+1}" for i in range(dimension)]
    )
    
    edited_df = st.data_editor(current_df, key=f"editor_{dimension}")

    # 3. Cálculo
    if st.button("Calcular Resultados", type="primary"):
        try:
            matrix = edited_df.to_numpy()
            
            st.divider()
            st.subheader("Resultados")

            st.write("**Matriz $A$ analizada:**")
            st.info(str(matrix))

            eigenvalues, eigenvectors = np.linalg.eig(matrix)

            st.write("### 🔹 Autovalores ($\lambda$)")
            st.write("Son los factores de escala:")
            
            evals_df = pd.DataFrame(eigenvalues, columns=["Valor"])
            st.dataframe(evals_df, hide_index=True)

            st.write("### 🔸 Autovectores ($v$)")
            st.write("Cada columna corresponde al autovector del autovalor respectivo:")
            st.write(eigenvectors)

            st.caption("""
            Nota: Los autovectores están normalizados tal que la suma de sus cuadrados es 1. 
            Si obtienes números complejos (j), significa que la matriz tiene rotación.
            """)

        except Exception as e:
            st.error(f"Ocurrió un error en el cálculo: {e}")

if __name__ == "__main__":
    main()