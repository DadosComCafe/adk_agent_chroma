import vertexai
from vertexai.generative_models import GenerativeModel, Content, Part
from decouple import config

# Inicialização padrão
vertexai.init(
    project=config("GOOGLE_CLOUD_PROJECT"),
    location="us-central1"
)

# Criando o modelo com instruções de sistema (o seu "agente")
model = GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="Você é um assistente especializado em ChromaDB."
)

# FAZENDO A PERGUNTA DE FORMA SIMPLES
def perguntar(texto):
    # Sem dicionários complexos, sem None, sem segredos.
    response = model.generate_content(texto)
    return response.text

print(perguntar("Olá! Como integro o Gemini com o ChromaDB?"))

