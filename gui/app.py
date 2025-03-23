from logging import config
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from etl.extract import Extractor
from etl.transform import Transform
from etl.load import Loader

import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd



class DataApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ETL - Processamento de Dados")
        self.root.geometry("500x300")
 
        # Button to upload file
        self.load_button = tk.Button(root, text="Carregar Arquivo", command=self.load_file)
        self.load_button.pack(pady=10)

        # Button to apply transformations
        self.transform_button = tk.Button(root, text="Aplicar Transformações", command=self.transform_data, state=tk.DISABLED)
        self.transform_button.pack(pady=10)

        # Button to save file
        self.save_button = tk.Button(root, text="Salvar Arquivo", command=self.save_file, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.df = None  # Stored DataFrame

    def load_file(self):
        file_path = filedialog.askopenfilename(title="Selecionar arquivo CSV", filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                extractor = Extractor(file_path=file_path)
                self.df = extractor.df  # Save Dataframe
                messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")
                self.transform_button.config(state=tk.NORMAL)  # Enable next step
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao carregar arquivo: {e}")

    def transform_data(self):
        if self.df is not None:
            try:
                transformer = transformer(self.df)
                transformer.normalize_columns()  # Apply transformation
                transformer.remove_outliers()  # Remove outliers
                messagebox.showinfo("Sucesso", "Transformações aplicadas!")
                self.save_button.config(state=tk.NORMAL)  # Enable saving
            except Exception as e:
                messagebox.showerror("Erro", f"Erro na transformação: {e}")

    def save_file(self):
        if self.df is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                try:
                    loader = Loader(self.df)
                    loader.save_data(file_path, file_format=config.DEFAULT_FILE_FORMAT)
                    messagebox.showinfo("Sucesso", "Arquivo salvo com sucesso!")
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao salvar arquivo: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DataApp(root)
    root.mainloop()
