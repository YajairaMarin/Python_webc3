from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3
import pandas as pd

app = Flask(__name__)

def consultar_maximos():
    with sqlite3.connect("data.db") as conn:
        query = """
            SELECT Temperatura, Irradiancia, ROUND(MAX(Voltaje), 2) as Voltaje, ROUND(MAX(Corriente), 2) as Corriente, ROUND(MAX(Potencia), 2) as Potencia
            FROM data
            GROUP BY Temperatura, Irradiancia
        """
        df = pd.read_sql_query(query, conn)
    return df

def obtener_opciones_temperatura():
    return list(range(5, 50, 5))

def obtener_opciones_irradiancia():
    return list(range(100, 1100, 100))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener los valores del formulario
        temperatura = request.form.get('temperatura')
        irradiancia = request.form.get('irradiancia')

        # Validar los valores (puedes agregar más validaciones según tus necesidades)
        if not temperatura or not irradiancia:
            return "Por favor, ingresa valores válidos para temperatura e irradiancia."

        # Consultar los resultados desde la base de datos
        resultados = consultar_maximos()

        # Filtrar los resultados para la temperatura e irradiancia seleccionadas
        resultados_filtrados = resultados[(resultados['Temperatura'] == int(temperatura)) & (resultados['Irradiancia'] == int(irradiancia))]

        # Convertir el DataFrame a un diccionario de Python para pasar los datos al template
        resultados_dict = resultados_filtrados.to_dict(orient='records')

        # Renderizar el template con los resultados
        template_resultados = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resultados de Búsqueda</title>
        </head>
        <body>
            <h1>Resultados de Búsqueda</h1>
            
            {% for resultado in resultados %}
                <p>
                    <strong>Temperatura:</strong> {{ resultado['Temperatura'] }} ºC<br>
                    <strong>Irradiancia:</strong> {{ resultado['Irradiancia'] }} W/m^2<br>
                    <strong>Voltaje:</strong> {{ resultado['Voltaje'] }} V<br>
                    <strong>Corriente:</strong> {{ resultado['Corriente'] }} A<br>
                    <strong>Potencia:</strong> {{ resultado['Potencia'] }} W<br>
                </p>
                <hr>
            {% endfor %}

            <form action="{{ url_for('index') }}" method="GET">
                <button type="submit">Volver</button>
            </form>
        </body>
        </html>
        """

        return render_template_string(template_resultados, resultados=resultados_dict)

    # Renderizar el formulario
    opciones_temperatura = obtener_opciones_temperatura()
    opciones_irradiancia = obtener_opciones_irradiancia()

    template_formulario = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulario de Búsqueda</title>
    </head>
    <body>
        <h1>Formulario de Búsqueda</h1>
        <form method="POST" action="/">
            <label for="temperatura">Temperatura:</label>
            <select name="temperatura" required>
                {% for opcion in opciones_temperatura %}
                    <option value="{{ opcion }}">{{ opcion }}</option>
                {% endfor %}
            </select>

            <label for="irradiancia">Irradiancia:</label>
            <select name="irradiancia" required>
                {% for opcion in opciones_irradiancia %}
                    <option value="{{ opcion }}">{{ opcion }}</option>
                {% endfor %}
            </select>

            <button type="submit">Buscar</button>
        </form>
    </body>
    </html>
    """

    return render_template_string(template_formulario, opciones_temperatura=opciones_temperatura, opciones_irradiancia=opciones_irradiancia)

if __name__ == '__main__':
    app.run(debug=True)