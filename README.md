# EcoSmart IoT 🌱 [projeto com expectativa de finalização para Novembro - 2026]

### Monitoramento Ambiental Inteligente e Análise de Dados

O **EcoSense IoT** é um sistema de monitoramento ambiental inteligente que coleta, armazena e analisa dados de sensores, como temperatura, umidade, luminosidade e qualidade do ar. O projeto utiliza tecnologias como Flask, SQLite e Pandas para transformar esses dados em informações úteis, apresentadas em um dashboard.

Inicialmente, os dados são simulados em Python. Em uma etapa futura, o projeto será integrado a um ESP32 e sensores físicos, permitindo a coleta de dados reais.

Este projeto faz parte do **Projeto Integrador IV — UNIVESP**.

## 🎯 Objetivos

* Desenvolver um sistema de monitoramento ambiental baseado em IoT.
* Simular e, futuramente, coletar dados de sensores físicos.
* Armazenar e organizar os dados em um banco de dados.
* Realizar análises utilizando Python e Pandas.
* Apresentar informações por meio de um dashboard.
* Evoluir o projeto para uma solução IoT com ESP32.

## 🛠️ Tecnologias utilizadas

* **Python** — Simulação e processamento de dados.
* **Flask** — Desenvolvimento da API e da aplicação web.
* **SQLite** — Armazenamento dos dados.
* **Pandas** — Tratamento e análise de dados.
* **NumPy** — Operações e cálculos numéricos.
* **HTML, CSS e JavaScript** — Desenvolvimento da interface.
* **Git e GitHub** — Versionamento e organização do projeto.
* **ESP32** — Integração futura com sensores físicos.

## 📊 Dados monitorados

O sistema poderá trabalhar com os seguintes dados ambientais:

| Sensor            | Informação            |
| ----------------- | --------------------- |
| DHT22             | Temperatura e umidade |
| LDR               | Luminosidade          |
| MQ-135            | Qualidade do ar       |
| Sensor de energia | Consumo de energia    |

## 🔄 Funcionamento do projeto

```text
Simulador de sensores
        ↓
      API Flask
        ↓
    Banco SQLite
        ↓
Tratamento dos dados
        ↓
  Análise com Pandas
        ↓
      Dashboard
```

## 🚀 Etapas de desenvolvimento

1. Criar um simulador de sensores utilizando Python.
2. Armazenar as leituras em arquivos e banco de dados.
3. Desenvolver uma API utilizando Flask.
4. Implementar o tratamento e a análise dos dados.
5. Criar um dashboard para visualização das informações.
6. Integrar o sistema a um ESP32 e sensores físicos.

## 📈 Análises previstas

* Temperatura média, mínima e máxima.
* Variação da umidade ao longo do tempo.
* Evolução da luminosidade.
* Identificação de possíveis anomalias.
* Relação entre temperatura e umidade.
* Análise do consumo de energia.
* Visualização do histórico das leituras.

## 🔮 Evolução futura

A proposta é substituir gradualmente os dados simulados por dados reais coletados por um ESP32 conectado a sensores físicos. A integração deverá utilizar a mesma estrutura principal da aplicação, permitindo a evolução do projeto sem a necessidade de reconstruir todo o sistema.

## 🎓 Projeto acadêmico

**Projeto Integrador IV — UNIVESP**

**Projeto:** EcoSense IoT

**Área:** Internet das Coisas (IoT), análise de dados e desenvolvimento de sistemas.

## 👨‍💻 Autor

Desenvolvido por Manoel de Souza Sá como parte das atividades acadêmicas do Projeto Integrador IV — UNIVESP.
