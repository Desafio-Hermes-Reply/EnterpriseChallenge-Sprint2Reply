# EnterpriseChallenge-Sprint2Reply

Os sensores desempenham um papel fundamental na Indústria 4.0, pois são responsáveis por transformar fenômenos físicos em dados digitais, permitindo que máquinas, sistemas e processos se tornem inteligentes e autônomos. Eles viabilizam a coleta contínua e precisa de informações sobre variáveis como temperatura, pressão, vibração, umidade, entre outras, essenciais para o monitoramento e controle em tempo real das operações industriais.

Essa capacidade de sensoriamento possibilita a implementação de soluções avançadas, como manutenção preditiva, otimização de processos, redução de falhas e aumento da eficiência produtiva. Além disso, os sensores são a base para a integração entre o mundo físico e digital, permitindo a criação de sistemas ciberfísicos, essenciais para a tomada de decisões automatizadas e a flexibilização da produção.

Em resumo, os sensores são os elementos-chave que impulsionam a transformação digital nas indústrias, tornando possível a evolução para fábricas inteligentes, mais produtivas, seguras e sustentáveis.

---

## ESTRUTURA DO PROJETO (GitHub)

```desafio-hermes-reply-fase4/
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
├── 📁 sensores/
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
└── .gitignore                     # (Opcional) Licença do projeto
```

---

## Desafio Hermes Reply - Fase 4 🚀

## Descrição

Este projeto simula um ambiente industrial digitalizado, utilizando o ESP32 e sensores virtuais. A proposta é coletar dados de sensores simulados, analisar e gerar insights, replicando cenários da Indústria 4.0.

## Objetivos

- Construir um circuito simulado com ESP32.
- Realizar a leitura de sensores virtuais.
- Coletar e exportar dados para análise.
- Gerar gráficos e insights iniciais.

## Circuito

- **Plataforma:** Wokwi / PlatformIO / VSCode

### **Sensores utilizados:**

| Finalidade                          | Sensor                                       | Descrição                                                                 |
|--------------------------------------|---------------------------------------------|---------------------------------------------------------------------------|
| **Temperatura**                     | DS18B20, PT100 com módulo ADC               | Monitoramento de temperatura de motores, rolamentos e ambientes.          |
| **Vibração**                        | ADXL345, MPU6050, SW-420                    | Detecção de vibrações anormais que indicam falhas mecânicas.              |
| **Corrente elétrica**               | SCT-013, ACS712                             | Monitoramento de consumo e proteção contra sobrecarga.                    |
| **Rotação e Velocidade**            | Encoder Óptico, Encoder Magnético AS5600    | Medição de velocidade de eixos e motores.                                 |
| **Proximidade e Posição**           | Sensor Indutivo, Óptico, ou Reed Switch     | Detecção de presença, posição ou fim de curso de componentes.             |
| **Pressão**                         | Sensor de Pressão Industrial (4-20mA)       | Monitoramento de sistemas pneumáticos ou hidráulicos.                     |
| **Nível de líquidos**               | Sensor Ultrasônico (HC-SR04), Sensor de Boia| Controle e monitoramento de tanques e reservatórios.                      |
| **Qualidade do Ar**                 | MQ-135, SGP30                               | Detecção de gases tóxicos ou contaminantes no ambiente industrial.        |
| **Umidade**                         | DHT22, SHT31                                | Controle ambiental em ambientes sensíveis.                                |
| **Tensão**                          | Sensor de Tensão ZMPT101B                   | Monitoramento de tensão elétrica para diagnóstico e segurança.            |
| **Detecção de Fumaça ou Incêndio**  | MQ-2, Sensor de Chama IR                    | Sistemas de segurança contra incêndios.                                   |

### Tabela de Sensores para Máquinas Industriais com ESP32

| **Sensor**                   | **Descrição**                                           | **Porta ESP32**    | **Alimentação** | **Código Exemplo** |
|------------------------------|---------------------------------------------------------|--------------------|-----------------|--------------------|
| **DS18B20 (Temperatura)**    | Sensor digital de temperatura, resistente               | D4 (GPIO4)         | 3.3V ou 5V      | `DallasTemperature` + `OneWire` |
| **SW-420 (Vibração)**        | Sensor para detecção de impactos e vibrações             | D5 (GPIO5)         | 3.3V ou 5V      | `digitalRead` para detectar vibração |
| **SCT-013 (Corrente)**       | Transformador de corrente não-invasivo                   | GPIO36 (ADC1_CH0)  | -               | `analogRead` para tensão proporcional |
| **Encoder Óptico (Rotação)** | Medição de rotação, RPM ou ângulo                        | D18 (GPIO18), D19 (GPIO19) | 5V      | `attachInterrupt` para contagem de pulsos |
| **HC-SR04 (Nível)**          | Sensor ultrassônico para medição de distância            | TRIG: D12 (GPIO12), ECHO: D14 (GPIO14) | 5V | `pulseIn` para calcular distância |
| **4-20mA (Pressão)**         | Sensor industrial padrão de pressão com saída analógica | GPIO39 (ADC1_CH3)  | conforme sensor (geralmente 24V) | `analogRead` com resistor shunt de 250Ω |

---

## Códigos por Sensor

### **DS18B20 - Temperatura**

```cpp
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  Serial.begin(115200);
  sensors.begin();
}

void loop() {
  sensors.requestTemperatures();
  Serial.println(sensors.getTempCByIndex(0));
  delay(1000);
}
```

---

### **SW-420 - Vibração**

```cpp
#define VIBRATION_PIN 5

void setup() {
  Serial.begin(115200);
  pinMode(VIBRATION_PIN, INPUT);
}

void loop() {
  if (digitalRead(VIBRATION_PIN) == LOW) {
    Serial.println("Vibração detectada!");
  }
  delay(200);
}
```

---

### **SCT-013 - Corrente**

```cpp
#define CURRENT_SENSOR_PIN 36

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(CURRENT_SENSOR_PIN);
  float voltage = sensorValue * (3.3 / 4095.0);
  Serial.println(voltage);
  delay(1000);
}
```

---

### **Encoder Óptico - Rotação**

```cpp
#define ENCODER_A 18
#define ENCODER_B 19

volatile int encoderCount = 0;

void IRAM_ATTR handleEncoder() {
  encoderCount++;
}

void setup() {
  Serial.begin(115120);
  pinMode(ENCODER_A, INPUT_PULLUP);
  pinMode(ENCODER_B, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(ENCODER_A), handleEncoder, RISING);
}

void loop() {
  Serial.println(encoderCount);
  delay(1000);
}
```

---

### **HC-SR04 - Nível**

```cpp
#define TRIG_PIN 12
#define ECHO_PIN 14

void setup() {
  Serial.begin(115200);
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = (duration * 0.0343) / 2;

  Serial.println(distance);
  delay(1000);
}
```

---

### **4-20mA - Pressão**

```cpp
#define PRESSURE_SENSOR_PIN 39

void setup() {
  Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(PRESSURE_SENSOR_PIN);
  float voltage = sensorValue * (3.3 / 4095.0);
  float current = voltage / 250.0; // Resistor shunt de 250Ω
  Serial.print("Corrente: ");
  Serial.println(current, 3);
  delay(1000);
}
```

## Código

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
```

### Esquema do Circuito

#### 1. DS18B20 - Sensor de Temperatura

- **VCC** → 3.3V (ou 5V)
- **GND** → GND
- **DATA** → D4 (GPIO4)
- **OBS**: Adicionar resistor de **4.7kΩ** entre **DATA** e **VCC** (pull-up).

---

#### 2. SW-420 - Sensor de Vibração

- **VCC** → 3.3V (ou 5V)
- **GND** → GND
- **DO (Saída Digital)** → D5 (GPIO5)

---

#### 3. SCT-013 - Sensor de Corrente

- **Buraco central** → passar o fio fase da carga.
- **Saída de tensão** → A0 (GPIO36) — entrada analógica.
- **OBS**: Verificar se o modelo possui carga interna; se não, adicionar resistor de carga conforme especificações (ex.: 33Ω).

---

#### 4. Encoder Óptico - Medidor de Rotação

- **VCC** → 5V
- **GND** → GND
- **OUT A** → D18 (GPIO18)
- **OUT B** → D19 (GPIO19)

---

#### 5. HC-SR04 - Sensor Ultrassônico (Nível)

- **VCC** → 5V
- **GND** → GND
- **TRIG** → D12 (GPIO12)
- **ECHO** → D14 (GPIO14)
- **OBS**: Adicionar divisor de tensão no pino **ECHO** (pois ele gera 5V e o ESP32 aceita até 3.3V).

---

#### 6. Sensor de Pressão - Saída 4-20mA

- **Saída +** → 24V (fonte externa)
- **Saída -** → uma ponta do resistor de **250Ω** → GND da fonte.
- **Entre o resistor** → GPIO39 (ADC1_CH3).
- **OBS**: A tensão sobre o resistor será proporcional à corrente de loop (1V a 5V).

---

### Código

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
```

## 🔍 Dados Coletados

Os dados foram registrados via Monitor Serial e exportados em CSV.

## Análise e Gráficos

![Gráfico Temperatura](./analise/grafico_temperatura.png)

## Como Executar

1. Acesse [https://wokwi.com](https://wokwi.com) e carregue o arquivo `main.ino`.
2. Configure o ESP32 e os sensores conforme o esquema.
3. Execute a simulação e acompanhe via Monitor Serial.

## Integrantes

Nome 1
Nome 2
Nome 3
Nome 4

## Licença

MIT License

---

## KANBAN (CARTÕES)

### Planejamento

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

- [ ] Preencher README.md
- [ ] Organizar imagens, código e dados no repositório
- [ ] Verificar coerência técnica da documentação

### 🚀 Finalização

- [ ] Fazer revisão geral
- [ ] Compartilhar link do GitHub no formulário da turma
