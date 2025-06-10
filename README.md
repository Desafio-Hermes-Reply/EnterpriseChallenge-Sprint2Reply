# EnterpriseChallenge-Sprint2Reply

Os sensores desempenham um papel fundamental na Indústria 4.0, pois são responsáveis por transformar fenômenos físicos em dados digitais, permitindo que máquinas, sistemas e processos se tornem inteligentes e autônomos. Eles viabilizam a coleta contínua e precisa de informações sobre variáveis como temperatura, pressão, vibração, umidade, entre outras, essenciais para o monitoramento e controle em tempo real das operações industriais.

Essa capacidade de sensoriamento possibilita a implementação de soluções avançadas, como manutenção preditiva, otimização de processos, redução de falhas e aumento da eficiência produtiva. Além disso, os sensores são a base para a integração entre o mundo físico e digital, permitindo a criação de sistemas ciberfísicos, essenciais para a tomada de decisões automatizadas e a flexibilização da produção.

Em resumo, os sensores são os elementos-chave que impulsionam a transformação digital nas indústrias, tornando possível a evolução para fábricas inteligentes, mais produtivas, seguras e sustentáveis.

---

## ESTRUTURA DO PROJETO (GitHub)

Claro! Abaixo está um arquivo `README.md` completo em **Markdown**, unificando e explicando toda a estrutura do seu projeto, incluindo o backend, os sensores (firmware) e a análise de dados com notebooks e scripts.

---

```markdown
# 🌡️ Projeto de Monitoramento com Sensores e API REST

Este projeto integra sensores físicos, análise de dados e uma API RESTful para coletar, processar e expor informações sobre variáveis ambientais como temperatura, umidade, fumaça e vibração. É dividido em três partes principais: firmware embarcado, backend com Django REST e análise com Python/Notebooks.

---

## 📁 Estrutura Geral do Projeto

```

.
├── api\_rest/                  # Backend com Django REST Framework
├── notebooks/                # Notebooks Jupyter para análise de dados
├── sensores/                 # Firmware embarcado (Arduino/ESP com PlatformIO)
├── src/                      # Scripts auxiliares (ETL, download de dados)

```

---

## 🔧 API REST – `api_rest/`

Backend construído com Django e Django REST Framework.

### Estrutura:

```

api\_rest/
├── api\_sensor/               # App principal da API
│   ├── migrations/           # Arquivos de migração do Django
│   ├── admin.py              # Registro no admin do Django
│   ├── apps.py               # Configurações do app
│   ├── models.py             # Definição dos modelos (banco de dados)
│   ├── serializers.py        # Serialização dos modelos para JSON
│   ├── tests.py              # Testes automatizados
│   ├── urls.py               # Rotas específicas da API
│   └── views.py              # Lógica de negócios (endpoints)
├── src/
│   ├── asgi.py               # Entrada ASGI (async server)
│   ├── settings.py           # Configurações gerais do projeto Django
│   ├── urls.py               # Rotas principais do projeto
│   └── wsgi.py               # Entrada WSGI (servidor web padrão)
├── staticfiles/              # Arquivos estáticos coletados
├── .env                      # Variáveis de ambiente (segredos, chaves)
├── .gitignore                # Arquivos ignorados pelo Git
├── LICENSE                   # Licença do projeto
├── Procfile                  # Configuração para deploy (ex: Heroku)
├── README.md                 # Este arquivo
├── manage.py                 # CLI do Django
├── requirements.txt          # Bibliotecas Python usadas
└── runtime.txt               # Versão do Python usada

```

---

## 📟 Sensores e Firmware – `sensores/`

Código para microcontroladores (ex: ESP32/ESP8266/Arduino), simulável via Wokwi ou executável no hardware real com PlatformIO.

### Estrutura:

```

sensores/
├── src/
│   └── prog1.ino             # Código-fonte do sensor (Arduino/ESP)
├── .gitignore                # Itens ignorados no controle de versão
├── README.md                 # Descrição do código e circuito
├── circuito.png              # Esquema do circuito eletrônico
├── diagram.json              # Diagrama (para Wokwi ou Fritzing)
├── platformio.ini            # Configuração do projeto PlatformIO
└── wokwi.toml                # Configuração de simulação Wokwi

```

---

## 📊 Análise de Dados – `notebooks/` e `src/`

Scripts e notebooks para análise estatística e manipulação dos dados dos sensores.

### Estrutura:

```

notebooks/
├── stats\_sensor.ipynb        # Notebook com análise estatística e visualizações

src/
├── download\_datasets.py      # Script para baixar datasets
├── load\_data.py              # Pré-processamento e carregamento dos dados
├── LICENSE                   # Licença
├── README.md                 # Explicação dos scripts
├── requirements.txt          # Dependências dos scripts
└── .gitignore                # Arquivos ignorados

````

---

## 📈 Exemplo de Análise – Correlação

O projeto inclui uma análise de correlação linear entre variáveis numéricas dos sensores. Isso permite entender relações como:

- **Temperatura vs Pressão**: correlação negativa forte (-0.68)
- **Posição vs Pressão**: correlação positiva muito forte (0.97)
- **Velocidade vs Temperatura**: correlação moderada positiva (0.46)

Essas correlações ajudam a prever ou reagir a condições ambientais com base em múltiplas variáveis.

---

## 🚀 Como Rodar

### 1. Backend

```bash
cd api_rest
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
````

### 2. Firmware (Sensores)

* Use o [PlatformIO](https://platformio.org/) ou [Wokwi](https://wokwi.com/) para simular/testar `prog1.ino`.

### 3. Análise de Dados

```bash
cd notebooks
jupyter notebook
```

Ou execute os scripts em `src/` diretamente:

```bash
python src/load_data.py
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


| Finalidade                         | Sensor                                       | Descrição                                                          | Nome da Variável (JSON) | Unidade de Medida         |
| ---------------------------------- | -------------------------------------------- | ------------------------------------------------------------------ | ----------------------- | ------------------------- |
| **Temperatura**                    | DS18B20, PT100 com módulo ADC                | Monitoramento de temperatura de motores, rolamentos e ambientes.   | `temperatura`           | °C (graus Celsius)        |
| **Vibração**                       | ADXL345, MPU6050, SW-420                     | Detecção de vibrações anormais que indicam falhas mecânicas.       | `vibracao`              | m/s² (aceleração)         |
| **Corrente elétrica**              | SCT-013, ACS712                              | Monitoramento de consumo e proteção contra sobrecarga.             | `corrente`              | A (ampère)                |
| **Rotação e Velocidade**           | Encoder Óptico, Encoder Magnético AS5600     | Medição de velocidade de eixos e motores.                          | `velocidade`            | RPM (rotações por minuto) |
| **Proximidade e Posição**          | Sensor Indutivo, Óptico, ou Reed Switch      | Detecção de presença, posição ou fim de curso de componentes.      | `posicao`               | mm ou estado binário      |
| **Pressão**                        | Sensor de Pressão Industrial (4-20mA)        | Monitoramento de sistemas pneumáticos ou hidráulicos.              | `pressao`               | bar ou psi                |
| **Nível de líquidos**              | Sensor Ultrasônico (HC-SR04), Sensor de Boia | Controle e monitoramento de tanques e reservatórios.               | `nivel`                 | cm ou %                   |
| **Qualidade do Ar**                | MQ-135, SGP30                                | Detecção de gases tóxicos ou contaminantes no ambiente industrial. | `qualidade_ar`          | ppm (partes por milhão)   |
| **Umidade**                        | DHT22, SHT31                                 | Controle ambiental em ambientes sensíveis.                         | `umidade`               | % (umidade relativa)      |
| **Tensão**                         | Sensor de Tensão ZMPT101B                    | Monitoramento de tensão elétrica para diagnóstico e segurança.     | `tensao`                | V (volts)                 |
| **Detecção de Fumaça ou Incêndio** | MQ-2, Sensor de Chama IR                     | Sistemas de segurança contra incêndios.                            | `fumaca`                | ppm ou estado binário     |



```json
{
  "temperatura": 36.5,
  "vibracao": 2.3,
  "corrente": 5.8,
  "velocidade": 1450,
  "posicao": 1,
  "pressao": 6.2,
  "nivel": 78,
  "qualidade_ar": 350,
  "umidade": 48.2,
  "tensao": 220.5,
  "fumaca": 0
}
```

### Vantagens:

* **Mais leve** e rápido para transmitir.
* Ideal para **sistemas embarcados**, **IoT** ou **telemetria em tempo real**.
* As unidades de medida podem ser documentadas fora do JSON (ex: no protocolo ou API).


### Tabela de Sensores para Máquinas Industriais com ESP32

| **Sensor**                                | **Descrição**                                                                             | **Porta ESP32**                   | **Alimentação**    | **Código Exemplo**                                      |
| ----------------------------------------- | ----------------------------------------------------------------------------------------- | --------------------------------- | ------------------ | ------------------------------------------------------- |
| **DS18B20, PT100 com módulo ADC**         | Sensor de temperatura digital com precisão e fácil integração.                            | GPIO 15 (exemplo)                 | 3.3V               | `OneWire`, `DallasTemperature` (Biblioteca Arduino)     |
| **ADXL345, MPU6050, SW-420**              | Sensores de aceleração (vibração) e giroscópio (MPU6050), SW-420 é para vibração simples. | I2C: GPIO 21 (SDA), GPIO 22 (SCL) | 3.3V               | `Wire`, `Adafruit_Sensor`, `Adafruit_ADXL345` (Arduino) |
| **SCT-013, ACS712**                       | Sensores de corrente elétrica para medir consumo e proteger circuitos.                    | GPIO 34 (exemplo)                 | 3.3V               | `ACS712` (Biblioteca Arduino)                           |
| **Encoder Óptico, AS5600**                | Sensores para medição de rotação e posição de motores/peças.                              | GPIO 12 (exemplo)                 | 3.3V               | `Encoder` (Biblioteca Arduino)                          |
| **Sensor Indutivo, Óptico, Reed Switch**  | Sensores de proximidade e posição para detectar objetos.                                  | GPIO 4 (exemplo)                  | 3.3V               | `digitalRead()` (Arduino)                               |
| **Sensor de Pressão Industrial (4-20mA)** | Sensor analógico para medir pressão de sistemas industriais.                              | ADC (ex: GPIO 34, 35)             | 3.3V               | `analogRead()` (Arduino)                                |
| **Sensor Ultrasônico HC-SR04**            | Sensor de distância por ultrassom, usado para medir o nível de líquidos.                  | GPIO 5 (Trig), GPIO 18 (Echo)     | 5V (via regulador) | `NewPing` (Biblioteca Arduino)                          |
| **MQ-135, SGP30**                         | Sensores para medir a qualidade do ar, detectando gases tóxicos.                          | I2C: GPIO 21 (SDA), GPIO 22 (SCL) | 3.3V               | `Adafruit_SGP30` (Biblioteca Arduino)                   |
| **DHT22, SHT31**                          | Sensores de umidade e temperatura para controle ambiental.                                | GPIO 13 (exemplo)                 | 3.3V               | `DHT` ou `SHT31` (Biblioteca Arduino)                   |
| **ZMPT101B**                              | Sensor de tensão AC, utilizado para medir a tensão elétrica.                              | ADC (ex: GPIO 34, 35)             | 3.3V               | `analogRead()` (Arduino)                                |
| **MQ-2, Sensor de Chama IR**              | Sensor de gás para detectar fumaça ou incêndio.                                           | GPIO 14 (exemplo)                 | 5V                 | `MQ` (Biblioteca Arduino)                               |

### Explicação de algumas colunas:

* **Porta ESP32**: As portas GPIO fornecidas são exemplos comuns. A **porta I2C** para comunicação com os sensores que utilizam esse protocolo é especificada com `SDA` e `SCL`.
* **Alimentação**: Indica a voltagem necessária para o sensor (3.3V ou 5V).
* **Código Exemplo**: O nome da biblioteca é apresentada, que pode ser usada no ambiente Arduino para facilitar a leitura e comunicação com o sensor.

Se precisar de um exemplo de código completo ou mais detalhes sobre como configurar a alimentação ou as portas, posso ajudar também!
4-20mA (Pressão)**         | Sensor industrial padrão de pressão com saída analógica | GPIO39 (ADC1_CH3)  | conforme sensor (geralmente 24V) | `analogRead` com resistor shunt de 250Ω |

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

### 1. **DS18B20 (Temperatura)**
- **VCC**: 3.3V do ESP32
- **GND**: GND do ESP32
- **Data**: GPIO 15 (ou qualquer pino digital disponível)

### 2. **ADXL345 (Vibração)**
- **VCC**: 3.3V do ESP32
- **GND**: GND do ESP32
- **SDA**: GPIO 21 (I2C SDA)
- **SCL**: GPIO 22 (I2C SCL)

### 3. **ACS712 (Corrente Elétrica)**
- **VCC**: 5V do ESP32
- **GND**: GND do ESP32
- **OUT**: GPIO 34 (pino analógico)

### 4. **HC-SR04 (Ultrassônico - Nível de Líquido)**
- **VCC**: 5V do ESP32 (ou 3.3V com regulador de tensão)
- **GND**: GND do ESP32
- **Trig**: GPIO 5
- **Echo**: GPIO 18

### 5. **MQ-135 (Qualidade do Ar)**
- **VCC**: 5V do ESP32
- **GND**: GND do ESP32
- **A0**: GPIO 34 (pino analógico)

### 6. **DHT22 (Umidade)**
- **VCC**: 3.3V do ESP32
- **GND**: GND do ESP32
- **Data**: GPIO 13 (ou qualquer pino digital disponível)

### 7. **ZMPT101B (Tensão)**
- **VCC**: 3.3V do ESP32
- **GND**: GND do ESP32
- **OUT**: GPIO 34 (pino analógico)

### 8. **MQ-2 (Fumaça/Incêndio)**
- **VCC**: 5V do ESP32
- **GND**: GND do ESP32
- **A0**: GPIO 14 (pino analógico)


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
