import unittest
from unittest.mock import patch, MagicMock
import main


class TestOrquestrador(unittest.TestCase):

    @patch('main.outlook.verificar_email_novo')
    @patch('main.datajud.pesquisar_numero_processo')
    @patch('main.bd.inserir_bd')
    @patch('main.outlook.enviar_email_outlook')
    def test_sem_emails_novos(self, mock_enviar_email, mock_inserir_bd, mock_pesquisar_numero_processo,
                              mock_verificar_email_novo):
        mock_verificar_email_novo.return_value = []
        erro, resultado = main.orquestrador()
        self.assertEqual(erro, "Nenhum email não lido encontrado com o padrão esperado.")
        self.assertEqual(resultado, "")

    @patch('main.outlook.verificar_email_novo')
    @patch('main.datajud.pesquisar_numero_processo')
    @patch('main.bd.inserir_bd')
    @patch('main.outlook.enviar_email_outlook')
    def test_erro_durante_processamento(self, mock_enviar_email, mock_inserir_bd, mock_pesquisar_numero_processo,
                                        mock_verificar_email_novo):
        mock_verificar_email_novo.side_effect = Exception("Erro de teste")
        erro, resultado = main.orquestrador()
        self.assertEqual(erro, "Houve algum erro durante o processamento")
        self.assertEqual(resultado, "")

    @patch('main.outlook.verificar_email_novo')
    @patch('main.datajud.pesquisar_numero_processo')
    @patch('main.bd.inserir_bd')
    @patch('main.outlook.enviar_email_outlook')
    def test_processamento_sucesso(self, mock_enviar_email, mock_inserir_bd, mock_pesquisar_numero_processo,
                                   mock_verificar_email_novo):
        mock_verificar_email_novo.return_value = [{'tribunal': 'Tribunal1', 'numero_processo': '12345'}]
        mock_pesquisar_numero_processo.return_value = {"resultado": "dados"}
        erro, resultado = main.orquestrador()
        self.assertEqual(erro, "")
        self.assertEqual(resultado, "Processamento finalizado com sucesso!")
        mock_inserir_bd.assert_called_once()
        mock_enviar_email.assert_called_once()


if __name__ == '__main__':
    unittest.main()