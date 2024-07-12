const categoriaSelect = document.getElementById('categoria');
const valorInput = document.getElementById('valor');
const unidadeDeSelect = document.getElementById('unidade_de');
const unidadeParaSelect = document.getElementById('unidade_para');
const converterButton = document.getElementById('converter');
const resultadoElement = document.getElementById('resultado');

//Atualiza as opções das unidades
function atualizarUnidades() {
  const categoria = categoriaSelect.value;
  unidadeDeSelect.innerHTML = '';
  unidadeParaSelect.innerHTML = '';

  if (categoria === 'temperatura') {
    const unidades = ['C', 'F', 'K'];
    unidades.forEach(unidade => {
      const option = document.createElement('option');
      option.value = unidade;
      option.text = unidade;
      unidadeDeSelect.appendChild(option);
      unidadeParaSelect.appendChild(option.cloneNode(true));
    });
  } else if (categoria === 'comprimento') {
    const unidades = ['m', 'cm', 'km', 'mi'];
    unidades.forEach(unidade => {
      const option = document.createElement('option');
      option.value = unidade;
      option.text = unidade;
      unidadeDeSelect.appendChild(option);
      unidadeParaSelect.appendChild(option.cloneNode(true));
    });
  } else if (categoria === 'peso') {
    const unidades = ['g', 'kg', 'lb'];
    unidades.forEach(unidade => {
      const option = document.createElement('option');
      option.value = unidade;
      option.text = unidade;
      unidadeDeSelect.appendChild(option);
      unidadeParaSelect.appendChild(option.cloneNode(true));
    });
  }
}

//Fazndo a requisição para o back
function converter() {
  const valor = valorInput.value;
  const unidadeDe = unidadeDeSelect.value;
  const unidadePara = unidadeParaSelect.value;

  if (valor && unidadeDe && unidadePara) {
    fetch(`/converter?valor=${valor}&unidade_de=${unidadeDe}&unidade_para=${unidadePara}`)
      .then(response => response.json())
      .then(data => {
        resultadoElement.textContent = `${data.resultado} ${data.unidade_para}`;
      })
      .catch(error => {
        console.error('Erro na requisição:', error);
        resultadoElement.textContent = 'Erro na conversão!';
      });
  } else {
    resultadoElement.textContent = 'Preencha todos os campos!';
  }
}


categoriaSelect.addEventListener('change', atualizarUnidades);
converterButton.addEventListener('click', converter);

atualizarUnidades();