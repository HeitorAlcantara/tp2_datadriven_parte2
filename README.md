# Projeto TP2 - Parte 2: LangChain
### **Descrição**
Esta parte do projeto utiliza o LangChain, uma poderosa biblioteca para criar aplicações baseadas em cadeias de linguagem, com três funcionalidades principais:

* Simulação de um Chatbot: Usando o Fake LLM para responder a perguntas pré-definidas.
* Integração com a API da Gemini: Utilização do LangChain para realizar chamadas para a API da Gemini.
* Tradução de Texto: Tradução de textos do inglês para o alemão com o modelo Helsinki-NLP/opus-mt-en-de da HuggingFace.

### **Requisitos**
* Python 3.8 ou superior
* Dependências listadas em <code>requirements.txt</code>

### **Dependências**
* LangChain: Framework para construção de pipelines e integrações com modelos de linguagem.
* Transformers: Biblioteca da HuggingFace para uso de modelos de NLP.

----

# Como Executar
Passo 1: Clone o repositório
~~~
  git clone https://github.com/seu-repositorio.git
  cd tp2_parte2
~~~
Passo 2: Crie e ative o ambiente virtual
~~~
python -m venv .venv
.venv/Scripts/activate  # Windows
source .venv/bin/activate  # Linux/Mac
~~~
Passo 3: Instale as dependências
~~~
pip install -r requirements.txt
~~~

Passo 4: Execute a aplicação
~~~
python main.py
~~~
