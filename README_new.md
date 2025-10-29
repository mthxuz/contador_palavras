# Contador de Palavras

Um programa simples e eficiente para contar palavras em textos, com suporte a diferentes idiomas e formatos.

## Novidades da Versão 1.2

### Interface Gráfica!
Agora com uma interface gráfica moderna e fácil de usar:

![Interface Gráfica do Contador de Palavras](assets/images/gui_demo.png)

#### Principais Recursos:
- **Interface intuitiva** com área de texto ampla
- **Análise em tempo real** dos textos
- **Resultados detalhados:**
  - Contagem total de palavras
  - Média de caracteres por palavra
  - Identificação da maior e menor palavra
- **Botões de ação rápida:**
  - Analisar Texto: Processa instantaneamente o conteúdo
  - Limpar: Reinicia a aplicação

## Como Usar

### Versão GUI (Recomendada - v1.2+)
```bash
python gui.py
```

1. Execute o programa
2. Digite ou cole seu texto na área principal
3. Clique em "Analisar Texto" ou use o botão "Limpar" para recomeçar

### Versão Linha de Comando
```bash
python main.py
```

## Instalação

```bash
# Clone o repositório
git clone https://github.com/mthxuz/contador_palavras.git
cd contador_palavras

# Criar ambiente virtual (recomendado)
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Instalar dependências
pip install -r requirements.txt
```

## Exemplos

### Interface Gráfica
Como mostrado na imagem acima, a interface apresenta:
- Campo de texto grande para entrada
- Botões intuitivos
- Painel de resultados com estatísticas detalhadas

### Linha de Comando
```python
Digite um texto: O rato roeu a roupa do rei de Roma

Análise do texto:
Total de palavras: 9
Média de caracteres por palavra: 3.4
Maior palavra: 'roupa'
Menor palavra: 'a'
```

## Desenvolvimento

### Testes
```bash
pytest
```

Para testes com cobertura:
```bash
pytest --cov=. tests/
```

## Contribuindo

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.