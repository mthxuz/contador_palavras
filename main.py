"""
Módulo para contagem de palavras em textos.

Este módulo fornece funcionalidades para contar palavras em textos,
com suporte a diferentes formatos e opções de processamento.
"""

import re
from typing import Union, List


def limpar_texto(texto: str) -> str:
    """
    Remove caracteres especiais e normaliza espaços no texto.

    Args:
        texto: String contendo o texto a ser limpo.

    Returns:
        String limpa e normalizada.
    """
    # Remove caracteres especiais mantendo pontuação básica
    texto = re.sub(r'[^\w\s.,!?-]', ' ', texto)
    # Normaliza espaços
    return ' '.join(texto.split())


def contar_palavras(texto: Union[str, List[str]], ignorar_pontuacao: bool = True) -> int:
    """
    Conta o número de palavras em um texto ou lista de textos.

    Args:
        texto: String ou lista de strings contendo o texto a ser analisado.
        ignorar_pontuacao: Se True, remove pontuação antes de contar.

    Returns:
        Número total de palavras no texto.

    Raises:
        TypeError: Se o texto não for string ou lista de strings.
        ValueError: Se o texto estiver vazio.
    """
    if not texto:
        raise ValueError("O texto não pode estar vazio")

    if isinstance(texto, list):
        texto = ' '.join(texto)
    elif not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string ou lista de strings")

    if ignorar_pontuacao:
        texto = limpar_texto(texto)
    
    palavras = [p for p in texto.split() if p.strip()]
    return len(palavras)


def analisar_texto(texto: str) -> dict:
    """
    Realiza uma análise completa do texto.

    Args:
        texto: String contendo o texto a ser analisado.

    Returns:
        Dicionário com estatísticas do texto (total de palavras,
        média de caracteres por palavra, etc).
    """
    if not isinstance(texto, str):
        raise TypeError("O texto deve ser uma string")

    texto_limpo = limpar_texto(texto)
    palavras = texto_limpo.split()
    
    if not palavras:
        return {
            "total_palavras": 0,
            "media_caracteres": 0,
            "maior_palavra": "",
            "menor_palavra": ""
        }

    return {
        "total_palavras": len(palavras),
        "media_caracteres": sum(len(p) for p in palavras) / len(palavras),
        "maior_palavra": max(palavras, key=len),
        "menor_palavra": min(palavras, key=len)
    }


if __name__ == "__main__":
    try:
        texto = input("Digite um texto: ").strip()
        if not texto:
            print("Erro: O texto não pode estar vazio!")
            exit(1)

        analise = analisar_texto(texto)
        
        print("\nAnálise do texto:")
        print(f"Total de palavras: {analise['total_palavras']}")
        print(f"Média de caracteres por palavra: {analise['media_caracteres']:.1f}")
        print(f"Maior palavra: '{analise['maior_palavra']}'")
        print(f"Menor palavra: '{analise['menor_palavra']}'")

    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
    except Exception as e:
        print(f"Erro: {str(e)}")