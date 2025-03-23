import pandas as pd

class Loader:
    def __init__(self, df):
#Initialize the class with a DataFrame. :para mdf: DataFrame that will be saved.

        self.df = df

    def save_data(self, file_path, file_format="csv", index=False):
# Save the DataFrame in different formats.

#:param file_path: Path where the file will be saved.
#:param file_format: File format ('csv', 'excel', 'json', 'parquet').
#:param index: Whether to include the DataFrame index in the file (default: False).
        try:
            if file_format == "csv":
                self.df.to_csv(file_path, index=index)
            elif file_format == "excel":
                self.df.to_excel(file_path, index=index)
            elif file_format == "json":
                self.df.to_json(file_path, orient="records")
            elif file_format == "parquet":
                self.df.to_parquet(file_path, index=index)
            else:
                raise ValueError("Formato não suportado. Escolha entre: 'csv', 'excel', 'json' ou 'parquet'.")

            print(f"Arquivo salvo com sucesso em: {file_path}")

        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
