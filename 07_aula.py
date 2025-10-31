from dotenv import load_dotenv
from openai import OpenAI

load_dotenv() # Carrega as variáveis do arquivo .env

client = OpenAI()

def geracao_texto(mensagens):
    resposta = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        max_tokens=1000,
        temperature=0,
        stream=True,
    )

    print("Assistant: ", end='', flush=True)
    texto_completo = ""
    for resposta_stream in resposta:
        texto = resposta_stream.choices[0].delta.content
        if texto:
            print(texto, end='', flush=True)
            texto_completo += texto

    print()  # Pula uma linha após a resposta completa
    mensagens.append({ "role": "assistant", "content": texto_completo })
    return mensagens


if __name__ == "__main__":
    print("Bem-vindo ao chatbot com Python da Asimov :)")
    mensagens = []
    while True:
        input_usuario = input("User: ")
        mensagens.append({ "role": "user", "content": input_usuario })
        mensagens = geracao_texto(mensagens)

