from google.colab import drive
drive.mount('/content/drive')

import os

# Define o caminho base no seu Drive
base_path = '/content/drive/MyDrive/E-commerce_Insight_Pipeline'

folders = [
    f'{base_path}/scripts',
    f'{base_path}/data',
    f'{base_path}/dbt_ecommerce',
    f'{base_path}/dbt_ecommerce/models'
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Pasta criada: {folder}")

# Ferramentas para Scraping, Banco de Dados e Transformação
!pip install requests beautifulsoup4 duckdb pandas dbt-duckdb
