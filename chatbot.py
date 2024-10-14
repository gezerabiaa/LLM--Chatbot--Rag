import requests
import json
import difflib

def load_knowledge_base(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_text(text):
    # Türkçe karakterleri normalize et
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

# Retrieve relevant information from the knowledge base using fuzzy matching
def retrieve_answer(knowledge_base, query):
    query = normalize_text(query.lower()) # query=prompt
    
    # Anahtar kelimeleri normalize et
    normalized_keys = {normalize_text(key): key for key in knowledge_base.keys()}
    
    # Anahtar kelimelerle eşleşen sorguları kontrol et
    if query in normalized_keys:
        return knowledge_base[normalized_keys[query]]
    
    # closet meanings
    closest_match = difflib.get_close_matches(query, normalized_keys.keys(), n=1, cutoff=0.5) # n=1 en yakın bir eşleşmeyi döndür. cutoff=0.5 en az %50 benzerlik olması gerekiyor.
    
    if closest_match:
        return knowledge_base[normalized_keys[closest_match[0]]]
    
    return None  # No match found

# Integrate RAG with the language model (only if no result is found in the knowledge base)
def generate_with_rag(model_url, model, prompt, knowledge_base):
    retrieved_info = retrieve_answer(knowledge_base, prompt)

    # Eğer bilgi bulunamazsa, modelden API çağrısı yapılmasın ve hata mesajı döndürülsün
    if retrieved_info is None:
        return "Bu bilgiye ulaşılamadı."
    
    # Bilgi bulunduysa, döndür
    return retrieved_info
    
  