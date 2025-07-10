# 🔐 IP Allow List Cleaner

Um script Python para automatizar a limpeza de uma lista de endereços IP permitidos com base em uma lista de remoção. Ideal para ambientes que exigem controle de acesso refinado, como empresas de saúde, finanças ou qualquer cenário DevSecOps.

---

## 📌 Descrição do Projeto

Em ambientes seguros, o controle de acesso baseado em IP é fundamental. Este projeto oferece um algoritmo simples, porém eficaz, que atualiza automaticamente um arquivo de texto (`allow_list.txt`) contendo IPs autorizados, **removendo aqueles que constam em uma `remove_list`**.

Isso é especialmente útil para organizações que precisam **revogar acessos de forma dinâmica**, sem depender de intervenção manual, garantindo que apenas IPs autorizados mantenham o acesso.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** A linguagem principal para o desenvolvimento do script.
* **Manipulação de Arquivos:** Uso das funções `open`, `read` e `write` para interagir com os arquivos de texto.
* **Estruturas de Controle:** Implementação de `for` e `if` para lógica de processamento.
* **Listas e Strings:** Utilização de estruturas de dados essenciais para gerenciar os IPs.
* **Terminal / CLI:** O script é executado via linha de comando.

---

## 🚀 Como Usar

Siga os passos abaixo para configurar e executar o script:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Matheuslimabjj/ip-allow-list-cleaner.git](https://github.com/Matheuslimabjj/ip-allow-list-cleaner.git)
    cd ip-allow-list-cleaner
    ```

2.  **Configure a `allow_list.txt`:** Edite o arquivo `allow_list.txt` e adicione os IPs autorizados, **um por linha**.

3.  **Configure a `remove_list`:** No arquivo `main.py`, edite a variável `remove_list` com os IPs que devem ser removidos. Por exemplo:
    ```python
    remove_list = ["192.168.97.225", "192.168.201.40"]
    ```

4.  **Execute o script:**
    ```bash
    python3 main.py
    ```

Após a execução, o arquivo `allow_list.txt` será **automaticamente atualizado** com os IPs removidos.

---

## 🧠 Conceitos Demonstrados

Este projeto serve como um excelente exemplo prático dos seguintes conceitos de Python:

* **`with open()`:** Uso para manipulação segura e eficiente de arquivos, garantindo que sejam fechados corretamente.
* **`.read()` e `.write()`:** Métodos para leitura e escrita de conteúdo em arquivos.
* **`.split()`:** Conversão de strings (conteúdo do arquivo) para listas de IPs.
* **`.remove()`:** Remoção de elementos específicos de uma lista.
* **`.join()`:** Reescrita de uma lista de IPs como uma string, formatada para o arquivo.

---

## 🧪 Exemplo de Uso

Vamos ver um exemplo prático de como o script funciona:

**`allow_list.txt` original:**
192.168.97.225
192.168.1.101
192.168.201.40

**`remove_list` (definida em `main.py`):**
```python
["192.168.97.225", "192.168.201.40"]

## Resultado final em allow_list.txt após a execução do script:

192.168.1.101# ip-allow-list-cleaner
