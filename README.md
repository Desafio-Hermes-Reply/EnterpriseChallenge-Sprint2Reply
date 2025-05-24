# EnterpriseChallenge-Sprint2Reply
Este projeto simula um ambiente industrial digitalizado, utilizando o ESP32 e sensores virtuais. A proposta é coletar dados de sensores simulados, analisar e gerar insights, replicando cenários da Indústria 4.0.
Perfeito! Vou te ajudar a criar uma **estrutura organizada do projeto**, incluindo os **cartões para gerenciamento de tarefas (Kanban)** e a **estrutura de diretórios e arquivos no GitHub**. Assim, você e seu grupo terão um roteiro bem definido para executar e documentar todo o desafio.

---

# ✅ ESTRUTURA DO PROJETO (GitHub)

```
desafio-hermes-reply-fase4/
├── 📁 circuito/
│   ├── circuito.png            # Print do circuito montado no Wokwi (ou plataforma utilizada)
│   └── esquema.pdf             # (Opcional) Esquema elétrico desenhado
├── 📁 codigo/
│   ├── main.ino                # Código-fonte ESP32
│   ├── platformio.ini          # Arquivo de configuração (se usar PlatformIO)
│   └── README.md               # Descrição do código e instruções de execução
├── 📁 dados/
│   ├── dados_coletados.csv     # Dados coletados da simulação
│   └── dados_exemplares.xlsx   # Dados de exemplo (se usar Kaggle ou gerar manualmente)
├── 📁 analise/
│   ├── grafico_temperatura.png # Gráficos gerados na análise
│   ├── analise.ipynb           # Código Python ou R para análise dos dados
│   └── README.md               # Descrição dos insights da análise
├── 📁 imagens/
│   └── monitor_serial.png      # Print do monitor serial com dados
├── README.md                   # Arquivo principal com resumo do projeto
└── LICENSE                     # (Opcional) Licença do projeto
```

---

# 🗂️ ESTRUTURA DO README (Modelo)

````markdown
# Desafio Hermes Reply - Fase 4 🚀

## 💡 Descrição
Este projeto simula um ambiente industrial digitalizado, utilizando o ESP32 e sensores virtuais. A proposta é coletar dados de sensores simulados, analisar e gerar insights, replicando cenários da Indústria 4.0.

## 🧠 Objetivos
- Construir um circuito simulado com ESP32.
- Realizar a leitura de sensores virtuais.
- Coletar e exportar dados para análise.
- Gerar gráficos e insights iniciais.

## 🏗️ Circuito
- **Plataforma:** Wokwi / PlatformIO / VSCode
- **Sensores utilizados:**
  - Sensor de Temperatura (DHT22) 🌡️
    - Justificativa: Monitoramento térmico é essencial em ambientes industriais.
  - Sensor de Vibração (SW-420) 📳
    - Justificativa: Identificar anomalias em motores e máquinas.
  - Sensor de Luminosidade (LDR) 💡
    - Justificativa: Controle de ambientes e segurança.

### 🔌 Esquema do Circuito
![Esquema do Circuito](./circuito/circuito.png)

## 🧑‍💻 Código
- Linguagem: C++ (Arduino IDE)
- Principais funções:
  - Leitura de sensores
  - Impressão no Monitor Serial
  - Simulação de dados

```cpp
#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  Serial.print("Temperatura: ");
  Serial.println(temp);
  delay(2000);
}
````

## 🔍 Dados Coletados

* Os dados foram registrados via Monitor Serial e exportados em CSV.

## 📊 Análise e Gráficos

![Gráfico Temperatura](./analise/grafico_temperatura.png)

## 🚀 Como Executar

1. Acesse [https://wokwi.com](https://wokwi.com) e carregue o arquivo `main.ino`.
2. Configure o ESP32 e os sensores conforme o esquema.
3. Execute a simulação e acompanhe via Monitor Serial.

## 👨‍👩‍👦‍👦 Integrantes

* Nome 1
* Nome 2
* Nome 3
* Nome 4

## 📜 Licença

MIT License

```

---

# 📅 KANBAN (CARTÕES)

### 🔧 Planejamento
- [ ] Definir sensores a serem utilizados
- [ ] Distribuir funções entre os integrantes
- [ ] Criar repositório no GitHub

### 🔌 Montagem do Circuito
- [ ] Criar o circuito no Wokwi / PlatformIO
- [ ] Testar funcionamento dos sensores
- [ ] Capturar print do circuito

### 👨‍💻 Programação
- [ ] Programar leitura dos sensores
- [ ] Implementar impressão no Monitor Serial
- [ ] Simular diferentes cenários (valores variados)

### 📑 Coleta de Dados
- [ ] Registrar dados do Monitor Serial
- [ ] Exportar para CSV

### 📈 Análise dos Dados
- [ ] Criar gráficos (Python ou R)
- [ ] Gerar insights iniciais

### 📄 Documentação
- [ ] Preencher README
- [ ] Organizar imagens, código e dados no repositório
- [ ] Verificar coerência técnica da documentação

### 🚀 Finalização
- [ ] Fazer revisão geral
- [ ] Compartilhar link do GitHub no formulário da turma
