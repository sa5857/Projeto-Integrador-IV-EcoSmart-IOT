import csv #permite criar arquivos csv
import random #gera valores aleatorios para simular sensores
from datetime import datetime, timedelta #trabalha com datas e horarios
# EcoSense IoT - Etapa 1
# Simulador de dados ambientais

ARQUIVO_CSV = "dados_sensores.csv"
QUANTIDADE_LEITURAS = 100

# Valores iniciais simulados
temperatura = 25.0
umidade = 65.0

# Data e hora inicial
momento = datetime.now() - timedelta(
    minutes=QUANTIDADE_LEITURAS - 1
)

with open(ARQUIVO_CSV, "w", newline="", encoding="utf-8") as arquivo:
    campos = [
        "data_hora",
        "temperatura_c",
        "umidade_percentual",
        "luminosidade_lux",
        "qualidade_ar_indice_simulado",
        "consumo_energia_w"
    ]

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=campos
    )

    escritor.writeheader()

    for i in range(QUANTIDADE_LEITURAS):

        # Simula pequenas variações ambientais
        temperatura += random.uniform(-0.3, 0.3)
        temperatura = max(18, min(35, temperatura))

        umidade += random.uniform(-1.0, 1.0)
        umidade = max(30, min(90, umidade))

        luminosidade = random.randint(100, 900)

        qualidade_ar = random.randint(20, 100)

        consumo_energia = random.uniform(80, 250)

        # Grava uma leitura no CSV
        escritor.writerow({
            "data_hora": momento.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "temperatura_c": round(temperatura, 2),
            "umidade_percentual": round(umidade, 2),
            "luminosidade_lux": luminosidade,
            "qualidade_ar_indice_simulado": qualidade_ar,
            "consumo_energia_w": round(consumo_energia, 2)
        })

        momento += timedelta(minutes=1)

print("Simulação concluída!")
print(f"Leituras geradas: {QUANTIDADE_LEITURAS}")
print(f"Arquivo criado: {ARQUIVO_CSV}")