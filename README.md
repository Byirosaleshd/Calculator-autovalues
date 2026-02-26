# Calculadora de Autovalores

Aplicación de Streamlit para calcular autovalores y autovectores de matrices cuadradas.

## Estructura del proyecto

- `calculadora_autovalores.py`: código principal de la app.
- `requirements.txt`: dependencias para instalar en el entorno virtual.
- `README.md`: este documento.
- `.gitignore`: archivos y carpetas que no deben subirse.

## Uso local

1. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows (PowerShell)
   # o source .venv/bin/activate en macOS/Linux
   ```
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   streamlit run calculadora_autovalores.py
   ```

La app estará disponible en `http://localhost:8501`.

## Despliegue en la nube

- Sera desplegado en streamlit localmente.
- Asegúrate de tener `requirements.txt` en la raíz y que el archivo principal se llame `calculadora_autovalores.py`.
