from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

#templates
app.template_folder = os.path.abspath('templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter')
def converter():
    valor = float(request.args.get('valor'))
    categoria = request.args.get('categoria')
    unidade_de = request.args.get('unidade_de').upper()
    unidade_para = request.args.get('unidade_para').upper()

    if categoria == 'temperatura':
        resultado = converter_temperatura(valor, unidade_de, unidade_para)
    elif categoria == 'comprimento':
        resultado = converter_comprimento(valor, unidade_de, unidade_para)
    elif categoria == 'massa':
        resultado = converter_massa(valor, unidade_de, unidade_para)
    elif categoria == 'volume':
        resultado = converter_volume(valor, unidade_de, unidade_para)
    elif categoria == 'area':
        resultado = converter_area(valor, unidade_de, unidade_para)
    elif categoria == 'velocidade':
        resultado = converter_velocidade(valor, unidade_de, unidade_para)
    else:
        return jsonify({'erro': 'Categoria inválida!'})

    return jsonify({'resultado': resultado, 'unidade_para': unidade_para})

def converter_temperatura(valor, unidade_de, unidade_para):
    if unidade_de == 'C' and unidade_para == 'F':
        return (valor * 9/5) + 32
    elif unidade_de == 'C' and unidade_para == 'K':
        return valor + 273.15
    elif unidade_de == 'F' and unidade_para == 'C':
        return (valor - 32) * 5/9
    elif unidade_de == 'F' and unidade_para == 'K':
        return ((valor - 32) * 5/9) + 273.15
    elif unidade_de == 'K' and unidade_para == 'C':
        return valor - 273.15
    elif unidade_de == 'K' and unidade_para == 'F':
        return ((valor - 273.15) * 9/5) + 32
    else:
        return "Unidades inválidas!"

def converter_comprimento(valor, unidade_de, unidade_para):
    if unidade_de == 'M' and unidade_para == 'CM':
        return valor * 100
    elif unidade_de == 'M' and unidade_para == 'KM':
        return valor / 1000
    elif unidade_de == 'M' and unidade_para == 'MI':
        return valor * 0.000621371
    elif unidade_de == 'CM' and unidade_para == 'M':
        return valor / 100
    elif unidade_de == 'CM' and unidade_para == 'KM':
        return valor / 100000
    elif unidade_de == 'CM' and unidade_para == 'MI':
        return valor * 0.00000621371
    elif unidade_de == 'KM' and unidade_para == 'M':
        return valor * 1000
    elif unidade_de == 'KM' and unidade_para == 'CM':
        return valor * 100000
    elif unidade_de == 'KM' and unidade_para == 'MI':
        return valor * 0.621371
    elif unidade_de == 'MI' and unidade_para == 'M':
        return valor * 1609.34
    elif unidade_de == 'MI' and unidade_para == 'CM':
        return valor * 160934
    elif unidade_de == 'MI' and unidade_para == 'KM':
        return valor * 1.60934
    else:
        return "Unidades inválidas!"

def converter_massa(valor, unidade_de, unidade_para):
    if unidade_de == 'G' and unidade_para == 'KG':
        return valor / 1000
    elif unidade_de == 'G' and unidade_para == 'LB':
        return valor * 0.00220462
    elif unidade_de == 'KG' and unidade_para == 'G':
        return valor * 1000
    elif unidade_de == 'KG' and unidade_para == 'LB':
        return valor * 2.20462
    elif unidade_de == 'LB' and unidade_para == 'G':
        return valor * 453.592
    elif unidade_de == 'LB' and unidade_para == 'KG':
        return valor * 0.453592
    else:
        return "Unidades inválidas!"

def converter_volume(valor, unidade_de, unidade_para):
    if unidade_de == 'ML' and unidade_para == 'L':
        return valor / 1000
    elif unidade_de == 'ML' and unidade_para == 'GAL':
        return valor * 0.000264172
    elif unidade_de == 'L' and unidade_para == 'ML':
        return valor * 1000
    elif unidade_de == 'L' and unidade_para == 'GAL':
        return valor * 0.264172
    elif unidade_de == 'GAL' and unidade_para == 'ML':
        return valor * 3785.41
    elif unidade_de == 'GAL' and unidade_para == 'L':
        return valor * 3.78541
    else:
        return "Unidades inválidas!"

def converter_area(valor, unidade_de, unidade_para):
    if unidade_de == 'M2' and unidade_para == 'CM2':
        return valor * 10000
    elif unidade_de == 'M2' and unidade_para == 'KM2':
        return valor / 1000000
    elif unidade_de == 'M2' and unidade_para == 'HA':
        return valor / 10000
    elif unidade_de == 'CM2' and unidade_para == 'M2':
        return valor / 10000
    elif unidade_de == 'CM2' and unidade_para == 'KM2':
        return valor / 10000000000
    elif unidade_de == 'CM2' and unidade_para == 'HA':
        return valor / 100000000
    elif unidade_de == 'KM2' and unidade_para == 'M2':
        return valor * 1000000
    elif unidade_de == 'KM2' and unidade_para == 'CM2':
        return valor * 10000000000
    elif unidade_de == 'KM2' and unidade_para == 'HA':
        return valor * 100
    elif unidade_de == 'HA' and unidade_para == 'M2':
        return valor * 10000
    elif unidade_de == 'HA' and unidade_para == 'CM2':
        return valor * 100000000
    elif unidade_de == 'HA' and unidade_para == 'KM2':
        return valor / 100
    else:
        return "Unidades inválidas!"

def converter_velocidade(valor, unidade_de, unidade_para):
    if unidade_de == 'KM/H' and unidade_para == 'M/S':
        return valor * 0.277778
    elif unidade_de == 'KM/H' and unidade_para == 'MI/H':
        return valor * 0.621371
    elif unidade_de == 'M/S' and unidade_para == 'KM/H':
        return valor * 3.6
    elif unidade_de == 'M/S' and unidade_para == 'MI/H':
        return valor * 2.23694
    elif unidade_de == 'MI/H' and unidade_para == 'KM/H':
        return valor * 1.60934
    elif unidade_de == 'MI/H' and unidade_para == 'M/S':
        return valor * 0.44704
    else:
        return "Unidades inválidas!"

if __name__ == '__main__':
    app.run(debug=True)
