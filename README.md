# FIAP - Faculdade de Informática e Administração Paulista 

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP" width="40%">
  </a>
</p>


<br>

# 🌡️ Projeto de Monitoramento com Sensores e API REST
## 👨‍🎓 Integrantes: 
- Vitor Eiji Fernandes Teruia
```
- RM: rm563683
- E-mail: vitorfer2018@gmail.com
- GitHub: [@Vitor985-hub](https://github.com/Vitor985-hub)
```
- Beatriz Pilecarte de Melo
```
 - RM: rm564952
 - E-mail: beatrizpilecartedemelo@gmail.com
 - GitHub: [@BPilecarte](https://github.com/BPilecarte)
```
- Francismar Alves Martins Junior
```
 - RM: m562869
 - E-mail: yggdrasil.git@gmail.com
 - GitHub: [@yggdrasilGit](https://github.com/yggdrasilGit
```
- Antônio Ancelmo Neto barros
```
 - RM: rm563683
 - E-mail: antonio.anbarros@gmail.com
 - GitHub: [@AntonioBarros19](https://github.com/AntonioBarros19)
```
- Matheus Soares Bento da Silva
```
 - RM: rm565540
 - E-mail: matheusbento044@gmail.com
 - GitHub: [matheusbento044](https://github.com/matheusbento04)
```

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/leonardoorabona/">Leonardo Ruiz Orabona</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusc">ANDRÉ GODOI CHIOVATO</a>


## 📜 Descrição

Os sensores desempenham um papel fundamental na Indústria 4.0, pois são responsáveis por transformar fenômenos físicos em dados digitais, permitindo que máquinas, sistemas e processos se tornem inteligentes e autônomos. Eles viabilizam a coleta contínua e precisa de informações sobre variáveis como temperatura, pressão, vibração, umidade, entre outras, essenciais para o monitoramento e controle em tempo real das operações industriais.

Essa capacidade de sensoriamento possibilita a implementação de soluções avançadas, como manutenção preditiva, otimização de processos, redução de falhas e aumento da eficiência produtiva. Além disso, os sensores são a base para a integração entre o mundo físico e digital, permitindo a criação de sistemas ciberfísicos, essenciais para a tomada de decisões automatizadas e a flexibilização da produção.

Em resumo, os sensores são os elementos-chave que impulsionam a transformação digital nas indústrias, tornando possível a evolução para fábricas inteligentes, mais produtivas, seguras e sustentáveis.

Este projeto integra sensores físicos, análise de dados e uma API RESTful para coletar, processar e expor informações sobre variáveis ambientais como temperatura, umidade, fumaça e vibração. É dividido em três partes principais: firmware embarcado, backend com Django REST e análise com Python/Notebooks.

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



---

## 📁 Estrutura geral do projeto

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

## 🔍 Dados Coletados

Os dados foram registrados via Monitor Serial e exportados em CSV.

## 
## 🗃 Histórico de lançamentos

* 0.1.0 - 14/05/2025

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>



