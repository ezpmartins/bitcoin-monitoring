# bitcoin-monitoring <a href="https://skillicons.dev"> <img width="30px" align="right" src="https://skillicons.dev/icons?i=python" /> </a>


## Descrição

O **Bitcoin Price Tracker** é uma aplicação simples desenvolvida em Python com a biblioteca Tkinter. Ele exibe, em tempo real, os preços do Bitcoin em diferentes moedas (USD, EUR, BRL e AOA), utilizando uma interface gráfica intuitiva e responsiva.

---

## Recursos

* Exibição dos valores do Bitcoin em quatro moedas:

  * Dólar Americano (USD)
  * Euro (EUR)
  * Real Brasileiro (BRL)
  * Kwanza Angolano (AOA)
* Atualização automática dos valores a cada segundo.
* Interface amigável e minimalista.

---

## Tecnologias Utilizadas

* **Python**: Linguagem principal.
* **Tkinter**: Biblioteca para criação da interface gráfica.
* **Pillow**: Para manipulação de imagens.
* **Requests**: Para buscar dados da API externa.

---

## Requisitos

Certifique-se de ter instalado:

* Python 3.8 ou superior
* Bibliotecas do Python:

  ```bash
  pip install requests pillow
  ```

---

## Como Executar

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/bitcoin-monitoring.git
   ```
2. Navegue até o diretório do projeto:

   ```bash
   cd src/bitcoin_monitoring.py
   ```
3. Certifique-se de que o arquivo de imagem `ic_bitcoin.png` está na pasta `src/images/`.
4. Execute o script principal:

   ```bash
   python app.py
   ```
