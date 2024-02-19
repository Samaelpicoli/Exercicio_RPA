# RPA Exercise 

# Sobre o projeto

Atividade realizada com base no exercício 'RPA Exercice' proposto no site: https://rpaexercise.aisingapore.org/.

RPA Exercise é uma aplicação web para treinamento de RPA, onde deve ser feito download de um arquivo CSV e realizar a leitura e o preenchimento de dados sobre vagas de emprego
no formulário do site, e após isso, fazer uma verificação na lista de candidatos para as vagas, realizando uma leitura dos dados e assim aprovando e rejeitando candidatos.

Ao final da inclusão e verificação dos candidatos, a página mostra uma mensagem de Congratulations, nesse momento o robô faz um screenshot da tela e salva na pasta do projeto.

## Layout da web
![Web 1](https://github.com/Samaelpicoli/Exercicio_RPA/blob/main/assets/job.PNG)

![Web 2](https://github.com/Samaelpicoli/Exercicio_RPA/blob/main/assets/lista.PNG)

![Web 3](https://github.com/Samaelpicoli/Exercicio_RPA/blob/main/assets/verificar.PNG)

## Desenho do Projeto

O mesmo modelo esta disponível no site do exercício.

![Web 1](https://github.com/Samaelpicoli/Exercicio_RPA/blob/main/assets/modelo.png)

# Tecnologias Utilizadas

Python

## Bibliotecas Utilizadas

Pandas

Selenium

Requests

Webdriver-Manager


## Sobre o código

O projeto foi dividido em módulos, onde um arquivo faz as interações com o site, e outro arquivo faz a requisição e faz download do CSV, 
o arquivo config.py é onde está sendo armazenado o usuário e a senha (esses dados estão disponíveis no site do exercício).

Os arquivos são chamados dentro do arquivo main que os executa.

No main, o projeto foi desenvolvido como uma máquina de estados (INITIALIZATION, GET TRANSACTION, PROCESS, END), emulando o ReFramework do UiPath,
auxiliando a criar automações mais confiáveis, flexíveis e fáceis de manter ao longo do tempo.

# Como executar o projeto
Pré-requisitos: Python 3.11

```bash
#insalar dependências, dentro do seu projeto e com ambiente virtual ativo:
pip install -r requirements.txt
```

# Executar o projeto
python main.py

## Observações:

Por ser uma automação web baseada no código fonte do site e utilizando Xpaths, Ids e Class, pode ser que em 
algum momento a automação pare de funcionar caso o site mude.

# Autor
Samael Muniz Picoli
