import os
import nbformat
import subprocess
import threading

from nbconvert.preprocessors import ExecutePreprocessor

class CodeRunner:
    def __init__(self, paths: list):
        self.paths = paths
        self.threads = []
        self.run()

    def execute_ipynb(self, ipynb_path):
        """
        Executa um notebook Jupyter.

        Args:
            ipynb_path (str): O caminho para o notebook Jupyter.
        """
        print(f"Executando o notebook: {ipynb_path}")
        with open(ipynb_path, "r", encoding="utf-8") as ipynb:
            nb = nbformat.read(ipynb, as_version=4)
            ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
            ep.preprocess(nb, {"metadata": {"path": os.path.dirname(ipynb_path)}})
        with open(ipynb_path, "w", encoding="utf-8") as ipynb:
            nbformat.write(nb, ipynb)
        print(f"\n{ipynb_path} executado com sucesso.")

    def execute_py(self, py_path):
        """
        Executa um script Python.

        Args:
            py_path (str): O caminho para o script Python.
        """
        print(f"Executando o script Python: {py_path}")
        try:
            subprocess.run(["python", py_path], check=True)
            print(f"\n{py_path} executado com sucesso.")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar {py_path}: {e}")

    def run(self):
        for path in self.paths:
            target = self.execute_ipynb if path.endswith(".ipynb") else self.execute_py
            thread = threading.Thread(target=target, args=(path,))
            thread.start()
            self.threads.append(thread)

        for thread in self.threads:
            thread.join()
