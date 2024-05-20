# Visualizador de Dados IBGE

Este projeto Python utiliza técnicas de webscraping com Selenium e PyAutoGUI para extrair dados de crescimento populacional e pirâmide etária do site do IBGE. Os dados são processados e visualizados de forma interativa utilizando as bibliotecas Pandas, Streamlit e Altair, proporcionando uma análise dinâmica e detalhada das tendências demográficas do Brasil.

## Inspirado por

Este projeto foi inspirado pelo [Portal do IBGE](https://censo2022.ibge.gov.br/panorama/?utm_source=ibge&utm_medium=home&utm_campaign=portal), de onde são extraídos os dados utilizados para análise.

## Como Usar

### Pré-requisitos

- Python 3.9

### Instalação das Bibliotecas

Para instalar as bibliotecas necessárias, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as versões específicas das bibliotecas utilizadas neste projeto.

### Executando o Projeto

1. Clone este repositório para sua máquina local.
2. Navegue até a pasta do projeto no terminal.
3. Execute o seguinte comando para iniciar o servidor Streamlit:

```bash
streamlit run app.py
```

O aplicativo estará disponível em seu navegador padrão.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
