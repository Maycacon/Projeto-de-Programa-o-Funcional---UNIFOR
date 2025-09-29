# main.py
import tkinter as tk
from tkinter import messagebox


# --- Lógica do Gerenciador de Tarefas ---
class GerenciadorTarefas:
    """manipulação das tarefas."""

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, nome, prioridade):
        tarefa = {'nome': nome, 'prioridade': prioridade, 'concluida': False}
        self.tarefas.append(tarefa)

    def marcar_como_concluida(self, index):
        if 0 <= index < len(self.tarefas):
            # A lambda
            marcar = lambda t: {**t, 'concluida': True}
            self.tarefas[index] = marcar(self.tarefas[index])

    def listar_nomes_alta_prioridade(self):
        # A list comprehension
        return [t['nome'] for t in self.tarefas if t['prioridade'] == 'alta']

    def filtrar_tarefas(self, filtro_func):
        # A Função de alta ordem.
        return list(filter(filtro_func, self.tarefas))

    def obter_todas(self):
        return self.tarefas


# --- Interface Gráfica (GUI) ---
class App:
    def __init__(self, root):
        self.root = root
        self.gerenciador = GerenciadorTarefas()
        self.criar_widgets()
        self.atualizar_lista()

    def criar_widgets(self):
        self.root.title("Gerenciador de Tarefas")
        self.root.geometry("650x450")
        self.root.configure(bg="#f0f0f0")

        self.entry_tarefa = tk.Entry(self.root, width=40, font=("Arial", 12))
        self.entry_tarefa.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

        btn_urgente = tk.Button(self.root, text="Adicionar Urgente", command=self.add_tarefa_urgente, bg="#ff6666",
                                fg="white")
        btn_urgente.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        btn_normal = tk.Button(self.root, text="Adicionar Normal", command=self.add_tarefa_normal, bg="#66b3ff",
                               fg="white")
        btn_normal.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        btn_filtrar = tk.Button(self.root, text="Filtrar por Palavra", command=self.filtrar_por_palavra, bg="#ffe066")
        btn_filtrar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        frame_lista = tk.Frame(self.root)
        frame_lista.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        scrollbar = tk.Scrollbar(frame_lista)
        self.listbox = tk.Listbox(frame_lista, width=80, height=15, font=("Arial", 11), yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        btn_concluir = tk.Button(self.root, text="Marcar como Concluída", command=self.concluir_tarefa, bg="#66ff66")
        btn_concluir.grid(row=3, column=0, pady=10, sticky="ew")

        btn_mostrar_altas = tk.Button(self.root, text="Listar Urgentes", command=self.mostrar_tarefas_altas,
                                      bg="#ffcc66")
        btn_mostrar_altas.grid(row=3, column=1, pady=10, sticky="ew")

        btn_mostrar_todas = tk.Button(self.root, text="Mostrar Todas", command=self.atualizar_lista, bg="#cccccc")
        btn_mostrar_todas.grid(row=3, column=2, pady=10, sticky="ew")

        self.root.grid_columnconfigure((0, 1, 2), weight=1)
        self.root.grid_rowconfigure(2, weight=1)

    def atualizar_lista(self, tarefas_para_mostrar=None):
        self.listbox.delete(0, tk.END)

        lista = tarefas_para_mostrar if tarefas_para_mostrar is not None else self.gerenciador.obter_todas()

        for i, tarefa in enumerate(lista):
            status = "✔" if tarefa['concluida'] else "✖"
            display = f"{tarefa['nome']} [{tarefa['prioridade'].capitalize()}] - {status}"
            self.listbox.insert(tk.END, display)

            if tarefa['concluida']:
                self.listbox.itemconfig(i, bg="#d4edda", fg="#155724")
            elif tarefa['prioridade'] == 'alta':
                self.listbox.itemconfig(i, fg="#ff3333")
            else:
                self.listbox.itemconfig(i, fg="#3333ff")

    def _adicionar_tarefa_base(self, prioridade):
        nome = self.entry_tarefa.get()
        if not nome:
            messagebox.showwarning("Aviso", "O nome da tarefa não pode ser vazio.")
            return

        self.gerenciador.adicionar_tarefa(nome, prioridade)
        self.entry_tarefa.delete(0, tk.END)
        self.atualizar_lista()

    def add_tarefa_urgente(self):
        self._adicionar_tarefa_base('alta')

    def add_tarefa_normal(self):
        self._adicionar_tarefa_base('normal')

    def concluir_tarefa(self):
        selecao = self.listbox.curselection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir!")
            return

        self.gerenciador.marcar_como_concluida(selecao[0])
        self.atualizar_lista()

    def mostrar_tarefas_altas(self):
        nomes_altas = self.gerenciador.listar_nomes_alta_prioridade()
        mensagem = "\n".join(nomes_altas) if nomes_altas else "Nenhuma tarefa de prioridade alta."
        messagebox.showinfo("Tarefas Urgentes", mensagem)

    def filtrar_por_palavra(self):
        palavra = self.entry_tarefa.get().lower()
        if not palavra:
            self.atualizar_lista()  # Se o campo estiver vazio, mostra todas
            return

        filtradas = self.gerenciador.filtrar_tarefas(lambda t: palavra in t['nome'].lower())
        self.atualizar_lista(filtradas)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()