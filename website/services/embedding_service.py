def extract_text(file_path):
    """
    Extrai texto de um arquivo (simulação).
    Na Fase 6, implementar PyPDF2, pdfplumber ou similar.
    """
    return "Conteúdo extraído do arquivo."

def create_chunks(text):
    """
    Realiza o chunking do texto.
    Na Fase 6, usar RecursiveCharacterTextSplitter (LangChain).
    """
    return [text[i:i+500] for i in range(0, len(text), 500)]

def generate_embeddings(chunks):
    """
    Gera embeddings para os chunks.
    Na Fase 6, usar OpenAIEmbeddings ou modelo local.
    """
    pass
