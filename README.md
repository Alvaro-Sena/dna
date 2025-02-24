# Analisador de DNA

Este projeto implementa um **analisador de DNA** que compara sequências genéticas para identificar indivíduos com base em seus perfis de STRs (Short Tandem Repeats). O código foi desenvolvido como parte do curso **CS50 - Introdução à Ciência da Computação com Python**, oferecido pela **Harvard University**.

## Tecnologias Utilizadas  
- **Linguagem**: Python 3.11  
- **Bibliotecas**: CSV, re (expressões regulares) 
- **Ferramentas**: Git

## Estrutura do Projeto

A pasta contém os seguintes arquivos:

- **`dna.py`**: Implementação do analisador de DNA, que compara sequências STRs para identificar indivíduos.
- **`databases/`**: Contém arquivos CSV com bancos de dados de perfis genéticos.
- **`sequences/`**: Contém sequências de DNA para análise.

## Features  
- Leitura e análise de arquivos CSV contendo perfis genéticos.
- Processamento de sequências de DNA para contagem de STRs.  
- Comparação de perfis genéticos e identificação de indivíduos.

## Minha Contribuição

A implementação do **analisador de DNA** foi desenvolvida no arquivo `dna.py`, nele, eu tive a responsabilidade de abrir o arquivo CSV, as amostras de sequências e implementar uma lógica que às comparasse e imprimisse um usuário com uma sequência correspondênte à amostra.

## Como Funciona o Analisador

O projeto analisa uma sequência de DNA e identifica a ocorrência de repetições de padrões STR. O algoritmo segue os seguintes passos:

1. **Leitura do banco de dados:**: Os perfis genéticos são carregados a partir do arquivo CSV.
2. **Leitura da sequência de DNA**: O arquivo contendo a sequência genética é processado.
3. **Cálculo das repetições STR**: O código identifica a maior sequência contínua de cada STR presente no banco de dados.
4. **Comparação com os perfis**: O programa verifica se há uma correspondência exata com algum indivíduo na base de dados.
5. **Exibição do resultado**:Se um perfil for encontrado, o nome do indivíduo é exibido. Caso contrário, o programa retorna "No match".

## Instalação e Execução

1. Clone o repositório:  
   ```bash
   git clone https://github.com/Alvaro-Sena/dna.git  
   ```
2. Navegue até a pasta do projeto:  
   ```bash  
   cd dna   
   ```  
3. Execute o analisador de DNA passando um banco de dados e um arquivo de sequência como parâmetros:  
   ```bash  
   python dna.py databases/large.csv sequences/1.txt   
   ```  


Certifique-se de que possui **Python 3** instalado no seu ambiente.

## Contato
Caso tenha dúvidas ou sugestões, entre em contato através do meu [LinkedIn](www.linkedin.com/in/alvaro-sena), [GitHub](https://github.com/Alvaro-Sena) ou [WhatsApp](https://wa.me/447356040385).
