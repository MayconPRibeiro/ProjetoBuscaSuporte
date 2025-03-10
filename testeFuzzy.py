
from fuzzywuzzy import process

# Lista de títulos (simulando um banco de dados)
titles = ["Cachorro preto", "Gato branco", "Passarinho azul", "Cachorro dourado", "Cachorro feliz", "Cachorrinho pequeno"]

# Função para busca ao vivo
def live_search():
    print("Digite seu termo de busca (digite 'sair' para finalizar):")
    
    while True:
        search_term = input("> ")  # Recebe o texto do usuário
        
        if search_term.lower() == 'sair':
            print("Busca encerrada.")
            break
        
        # Realiza o fuzzy matching
        matches = process.extract(search_term, titles, limit=5)
        
        # Exibe os resultados ao vivo
        print("Resultados encontrados:")
        for match in matches:
            print(f"- {match[0]} (Similaridade: {match[1]}%)")
        
        print("\nDigite mais termos ou 'sair' para encerrar.")

# Inicia a busca ao vivo
live_search()