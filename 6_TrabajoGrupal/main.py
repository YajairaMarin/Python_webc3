from flask import Flask, render_template_string, request
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
        temperatura = request.form.get('temperatura')
        irradiancia = request.form.get('irradiancia')

        if not temperatura or not irradiancia:
            return "Por favor, ingresa valores válidos para temperatura e irradiancia."

        resultados = consultar_maximos()

        resultados_filtrados = resultados[(resultados['Temperatura'] == int(temperatura)) & (resultados['Irradiancia'] == int(irradiancia))]

        resultados_dict = resultados_filtrados.to_dict(orient='records')

        template_resultados = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Resultados de Búsqueda</title>
            <style>
                body {
                    background-color: #f0f0f0;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }

                h1 {
                    color: #333333;
                }

                table {
                    width: 60%;
                    margin: auto;
                    border-collapse: collapse;
                    margin-top: 20px;
                }

                th, td {
                    border: 1px solid #ddd;
                    padding: 12px;
                    text-align: center;
                }

                th {
                    background-color: #f2f2f2;
                }

                button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }

                button:hover {
                    background-color: #45a049;
                }
            </style>
        </head>
        <body>
            <h1>Resultados de Búsqueda</h1>

            <table>
                <tr>
                    <th>Temperatura (ºC)</th>
                    <th>Irradiancia (W/m^2)</th>
                    <th>Voltaje (V)</th>
                    <th>Corriente (A)</th>
                    <th>Potencia (W)</th>
                </tr>

                {% for resultado in resultados %}
                    <tr>
                        <td>{{ resultado['Temperatura'] }}</td>
                        <td>{{ resultado['Irradiancia'] }}</td>
                        <td>{{ resultado['Voltaje'] }}</td>
                        <td>{{ resultado['Corriente'] }}</td>
                        <td>{{ resultado['Potencia'] }}</td>
                    </tr>
                {% endfor %}
            </table>

            <form action="/" method="GET" style="margin-top: 20px;">
                <button type="submit">Volver</button>
            </form>
        </body>
        </html>
        """

        return render_template_string(template_resultados, resultados=resultados_dict)

    opciones_temperatura = obtener_opciones_temperatura()
    opciones_irradiancia = obtener_opciones_irradiancia()

    template_formulario = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulario de Búsqueda</title>
        <style>
            body {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                text-align: center;
            }

            h1 {
                color: #333333;
            }

            form {
                margin-top: 20px;
            }

            label {
                font-size: 18px;
                margin-right: 10px;
            }

            select {
                font-size: 16px;
                padding: 8px;
                margin-right: 10px;
            }

            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }

            button:hover {
                background-color: #45a049;
            }
        </style>
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
