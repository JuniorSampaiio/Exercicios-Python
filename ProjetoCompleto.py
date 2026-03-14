# Projeto Completo

# tupla que contém os contatos suportados pelo sistema
contatos_suportados = ("telefone", "email", "endereço")

# Dicionário de exemplo
agenda = {
    "Pessoa 1": {
        "telefone": ["11 1234-5678"],
        "email": ["pessoa@email.com", "email@profissional.com"],
        "endereço": ["Rua 123"]
    },
    "Pessoa 2": {
        "telefone": ["11 9101-1123"],
        "email": ["pessoa2@email.com", "pessoa2@profissional.com"],
        "endereço": ["Rua 345"]
    }
}

# Função que formata um contato
def contato_para_texto(nome_contato: str, **formas_contato):
    formato_texto = f"{nome_contato}"

    for meio_contato, contato in formas_contato.items():
        formato_texto = f"{formato_texto}\n{meio_contato.upper()}"

        contador = 1
        for valor in contato:
            formato_texto = f"{formato_texto}\n\t{contador} - {valor}"
            contador += 1

    return formato_texto


# Função de visualização da agenda completa
def agenda_para_texto(**agenda_completa):
    """Recebe um dicionário de dicionários com a agenda
    e retorna uma string formatada"""

    formato_texto = ""

    for nome_contato, formas_contato in agenda_completa.items():
        formato_texto = f"{formato_texto}{contato_para_texto(nome_contato, **formas_contato)}\n"
        formato_texto = f"{formato_texto}----------------------\n"

    return formato_texto


print(agenda_para_texto(**agenda))