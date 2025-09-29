# tests.py
import unittest
from main import GerenciadorTarefas

class TestGerenciadorDeTarefas(unittest.TestCase):

    def setUp(self):
        self.gerenciador = GerenciadorTarefas()

    def test_adicionar_tarefa_alta_prioridade(self):
        self.gerenciador.adicionar_tarefa("Estudar Python", "alta")
        tarefas = self.gerenciador.obter_todas()

        self.assertEqual(len(tarefas), 1)
        self.assertEqual(tarefas[0]['nome'], "Estudar Python")
        self.assertEqual(tarefas[0]['prioridade'], 'alta')
        self.assertFalse(tarefas[0]['concluida'])

    def test_adicionar_tarefa_normal(self):
        self.gerenciador.adicionar_tarefa("Ler um livro", "normal")
        tarefa = self.gerenciador.obter_todas()[0]
        self.assertEqual(tarefa['prioridade'], 'normal')

    def test_marcar_tarefa_como_concluida(self):
        self.gerenciador.adicionar_tarefa("Fazer exercício", "alta")
        self.gerenciador.marcar_como_concluida(0)
        tarefa = self.gerenciador.obter_todas()[0]
        self.assertTrue(tarefa['concluida'])

    def test_listar_nomes_de_prioridade_alta(self):
        self.gerenciador.adicionar_tarefa("Urgente 1", "alta")
        self.gerenciador.adicionar_tarefa("Normal", "normal")
        self.gerenciador.adicionar_tarefa("Urgente 2", "alta")

        nomes_altas = self.gerenciador.listar_nomes_alta_prioridade()

        self.assertEqual(len(nomes_altas), 2)
        self.assertIn("Urgente 1", nomes_altas)
        self.assertNotIn("Normal", nomes_altas)

    def test_filtrar_tarefas_por_palavra(self):
        self.gerenciador.adicionar_tarefa("Comprar leite", "normal")
        self.gerenciador.adicionar_tarefa("Estudar Python", "alta")

        # O teste continua usando lambda para simular o comportamento do filtro
        filtradas = self.gerenciador.filtrar_tarefas(lambda t: "python" in t['nome'].lower())

        self.assertEqual(len(filtradas), 1)
        self.assertEqual(filtradas[0]['nome'], "Estudar Python")


if __name__ == "__main__":
    unittest.main()