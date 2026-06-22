import os
from google import genai
from .retrieval_service import retrieve_context

def generate_answer(query, chatbot):
    """
    Recebe a pergunta do aluno, recupera o contexto e envia para a LLM.
    Inclui instruções para redução de alucinação.
    """
    context = retrieve_context(query, chatbot)
    
    prompt = f"""
    Você é um assistente acadêmico.
    Responda à pergunta do aluno utilizando APENAS o contexto fornecido.
    Se a resposta não estiver no contexto, diga "Não tenho informações suficientes para responder."
    
    Contexto: {context}
    
    Pergunta: {query}
    """
    
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or api_key == "sua_chave_do_gemini_aqui":
        return "Erro: Chave do Gemini (GEMINI_API_KEY) não configurada no .env"
    
    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        bot_response = response.text
    except Exception as e:
        bot_response = f"Erro ao contatar o Gemini: {e}"

    return bot_response
