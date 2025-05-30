import os

# 📂 Criar pasta data, se não existir
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_PATH, exist_ok=True)

# 🔗 Lista de datasets
datasets = [
    {
        "id": "wkirgsn/electric-motor-temperature",
        "name": "electric-motor-temperature"
    },
    {
        "id": "claytonmiller/cubems-smart-building-energy-and-iaq-data",
        "name": "cubems-smart-building-energy-and-iaq-data"
    },
    {
        "id": "hieudaotrung/gear-vibration",
        "name": "gear-vibration"
    }
]

# 🚀 Download dos datasets
for ds in datasets:
    print(f"📥 Baixando {ds['id']} ...")
    os.system(f'kaggle datasets download -d {ds["id"]} -p {DATA_PATH} --unzip')
    print(f"✅ {ds['name']} baixado e extraído.")

print("\n🚀 Todos os datasets foram baixados e salvos na pasta /data")
