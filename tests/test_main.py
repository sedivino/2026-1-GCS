import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from utils.helpers import format_task, validate_task_name

def test_format_task_pending():
    task = {"id": 1, "name": "Estudar GCS", "done": False}
    assert format_task(task) == "[○] #1 - Estudar GCS"
    print("  [OK] format_task pendente")

def test_format_task_done():
    task = {"id": 2, "name": "Fazer relatório", "done": True}
    assert format_task(task) == "[✓] #2 - Fazer relatório"
    print("  [OK] format_task concluída")

def test_validate_task_name_valid():
    assert validate_task_name("Comprar leite") == True
    print("  [OK] nome válido")

def test_validate_task_name_invalid():
    assert validate_task_name("") == False
    assert validate_task_name("ab") == False
    print("  [OK] nome inválido rejeitado")

if __name__ == "__main__":
    print("Executando testes...")
    test_format_task_pending()
    test_format_task_done()
    test_validate_task_name_valid()
    test_validate_task_name_invalid()
    print("Todos os testes passaram!")
