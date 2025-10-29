"""
Interface gráfica para o contador de palavras.
"""
import tkinter as tk
from tkinter import ttk, scrolledtext
from main import analisar_texto

class ContadorPalavrasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contador de Palavras")
        self.root.geometry("600x400")
        
        # Configurar estilo
        style = ttk.Style()
        style.configure("Stats.TLabel", padding=5)
        
        self._criar_widgets()
        self._configurar_layout()
    
    def _criar_widgets(self):
        # Frame principal
        self.main_frame = ttk.Frame(self.root, padding="10")
        
        # Área de texto com scrollbar
        self.text_label = ttk.Label(self.main_frame, text="Digite ou cole seu texto:")
        self.text_area = scrolledtext.ScrolledText(
            self.main_frame, 
            wrap=tk.WORD,
            width=50,
            height=10
        )
        
        # Botões
        self.button_frame = ttk.Frame(self.main_frame)
        self.analisar_btn = ttk.Button(
            self.button_frame,
            text="Analisar Texto",
            command=self._analisar
        )
        self.limpar_btn = ttk.Button(
            self.button_frame,
            text="Limpar",
            command=self._limpar
        )
        
        # Área de resultados
        self.results_frame = ttk.LabelFrame(
            self.main_frame,
            text="Resultados",
            padding="10"
        )
        
        # Labels para resultados
        self.total_label = ttk.Label(
            self.results_frame,
            text="Total de palavras: 0",
            style="Stats.TLabel"
        )
        self.media_label = ttk.Label(
            self.results_frame,
            text="Média de caracteres: 0",
            style="Stats.TLabel"
        )
        self.maior_label = ttk.Label(
            self.results_frame,
            text="Maior palavra: -",
            style="Stats.TLabel"
        )
        self.menor_label = ttk.Label(
            self.results_frame,
            text="Menor palavra: -",
            style="Stats.TLabel"
        )

    def _configurar_layout(self):
        # Configurar grid
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Área de texto
        self.text_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.text_area.grid(row=1, column=0, sticky="nsew", pady=(0, 10))
        
        # Botões
        self.button_frame.grid(row=2, column=0, sticky="ew", pady=(0, 10))
        self.analisar_btn.pack(side="left", padx=5)
        self.limpar_btn.pack(side="left", padx=5)
        
        # Resultados
        self.results_frame.grid(row=3, column=0, sticky="nsew")
        self.total_label.grid(row=0, column=0, sticky="w")
        self.media_label.grid(row=1, column=0, sticky="w")
        self.maior_label.grid(row=2, column=0, sticky="w")
        self.menor_label.grid(row=3, column=0, sticky="w")
        
        # Configurar expansão
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
    
    def _analisar(self):
        """Analisa o texto e atualiza os resultados."""
        texto = self.text_area.get("1.0", tk.END).strip()
        if not texto:
            self._limpar()
            return
        
        resultados = analisar_texto(texto)
        
        # Atualizar labels
        self.total_label["text"] = f"Total de palavras: {resultados['total_palavras']}"
        self.media_label["text"] = f"Média de caracteres: {resultados['media_caracteres']:.1f}"
        self.maior_label["text"] = f"Maior palavra: '{resultados['maior_palavra']}'"
        self.menor_label["text"] = f"Menor palavra: '{resultados['menor_palavra']}'"
    
    def _limpar(self):
        """Limpa o texto e os resultados."""
        self.text_area.delete("1.0", tk.END)
        self.total_label["text"] = "Total de palavras: 0"
        self.media_label["text"] = "Média de caracteres: 0"
        self.maior_label["text"] = "Maior palavra: -"
        self.menor_label["text"] = "Menor palavra: -"

def main():
    root = tk.Tk()
    app = ContadorPalavrasGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()