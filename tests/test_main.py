"""
Testes unitários para o módulo de contagem de palavras.
"""

import pytest
from main import contar_palavras, limpar_texto, analisar_texto


def test_contar_palavras_simples():
    """Testa contagem de palavras em texto simples."""
    texto = "O rato roeu a roupa"
    assert contar_palavras(texto) == 5


def test_contar_palavras_espacos_multiplos():
    """Testa contagem com múltiplos espaços entre palavras."""
    texto = "O    rato    roeu    a    roupa"
    assert contar_palavras(texto) == 5


def test_contar_palavras_lista():
    """Testa contagem de palavras em lista de strings."""
    texto = ["O rato", "roeu", "a roupa"]
    assert contar_palavras(texto) == 5


def test_contar_palavras_vazio():
    """Testa erro ao passar texto vazio."""
    with pytest.raises(ValueError):
        contar_palavras("")


def test_contar_palavras_tipo_invalido():
    """Testa erro ao passar tipo inválido."""
    with pytest.raises(TypeError):
        contar_palavras(123)


def test_limpar_texto():
    """Testa limpeza de texto com caracteres especiais."""
    texto = "Texto@com#caracteres&especiais!"
    esperado = "Texto com caracteres especiais!"
    assert limpar_texto(texto) == esperado


def test_analisar_texto_completo():
    """Testa análise completa do texto."""
    texto = "O rato roeu a roupa do rei"
    analise = analisar_texto(texto)
    
    assert analise["total_palavras"] == 7
    assert isinstance(analise["media_caracteres"], float)
    assert analise["maior_palavra"] == "roupa"
    assert analise["menor_palavra"] == "a"


def test_analisar_texto_vazio():
    """Testa análise de texto vazio."""
    analise = analisar_texto("")
    
    assert analise["total_palavras"] == 0
    assert analise["media_caracteres"] == 0
    assert analise["maior_palavra"] == ""
    assert analise["menor_palavra"] == ""