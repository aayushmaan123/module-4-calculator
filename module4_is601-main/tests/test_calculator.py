# test_calculator.py

"""
This test module contains unit tests for the 'app/calculator.py' module.
Each test demonstrates good testing practices using the Arrange-Act-Assert (AAA) pattern.
"""

import pytest
from app.calculator import display_help, display_history, calculator

# -----------------------------------------------------------------------------------
# Test Display Functions
# -----------------------------------------------------------------------------------

def test_display_help(capsys):
    """
    Test the display_help function to ensure it prints the correct help message.
    """
    display_help()
    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out
    assert "Supported operations:" in captured.out

def test_display_history_empty(capsys):
    """
    Test the display_history function when the history is empty.
    """
    history = []
    display_history(history)
    captured = capsys.readouterr()
    assert captured.out.strip() == "No calculations performed yet."

def test_display_history_with_entries(capsys):
    """
    Test the display_history function when there are entries in the history.
    """
    history = [
        "AddCalculation: 10.0 Add 5.0 = 15.0",
        "SubtractCalculation: 20.0 Subtract 3.0 = 17.0",
        "MultiplyCalculation: 7.0 Multiply 8.0 = 56.0",
        "DivideCalculation: 20.0 Divide 4.0 = 5.0"
    ]
    display_history(history)
    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "4. DivideCalculation: 20.0 Divide 4.0 = 5.0" in captured.out

# -----------------------------------------------------------------------------------
# Test REPL Calculator Functions
# -----------------------------------------------------------------------------------

def test_calculator_exit(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'exit' command.
    """
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "Exiting calculator. Goodbye!" in captured.out
    assert exc_info.value.code == 0

def test_calculator_help_command(monkeypatch, capsys):
    """
    Test the calculator function's ability to handle the 'help' command.
    """
    inputs = iter(['help', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Calculator REPL Help" in captured.out

def test_calculator_invalid_input(monkeypatch, capsys):
    """
    Test the calculator function's handling of invalid input format.
    """
    inputs = iter(['invalid input', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out

def test_calculator_invalid_number_input(monkeypatch, capsys):
    """
    Test the calculator's handling of invalid number input.
    """
    inputs = iter(['add ten five', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please follow the format: <operation> <num1> <num2>" in captured.out

def test_calculator_addition(monkeypatch, capsys):
    """
    Test the calculator's addition operation.
    """
    inputs = iter(['add 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out

def test_calculator_subtraction(monkeypatch, capsys):
    """
    Test the calculator's subtraction operation.
    """
    inputs = iter(['subtract 20 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: SubtractCalculation: 20.0 Subtract 5.0 = 15.0" in captured.out

def test_calculator_multiplication(monkeypatch, capsys):
    """
    Test the calculator's multiplication operation.
    """
    inputs = iter(['multiply 7 8', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: MultiplyCalculation: 7.0 Multiply 8.0 = 56.0" in captured.out

def test_calculator_division(monkeypatch, capsys):
    """
    Test the calculator's division operation.
    """
    inputs = iter(['divide 20 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Result: DivideCalculation: 20.0 Divide 4.0 = 5.0" in captured.out

def test_calculator_division_by_zero(monkeypatch, capsys):
    """
    Test the calculator's handling of division by zero.
    """
    inputs = iter(['divide 10 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero." in captured.out

def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator's ability to display calculation history.
    """
    inputs = iter(['add 10 5', 'subtract 20 3', 'history', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out

# -----------------------------------------------------------------------------------
# Test Edge Cases & Exceptions
# -----------------------------------------------------------------------------------

def test_calculator_unsupported_operation(monkeypatch, capsys):
    """
    Test the calculator's handling of an unsupported operation.
    """
    inputs = iter(['modulus 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    with pytest.raises(SystemExit):
        calculator()
    captured = capsys.readouterr()
    assert "Unsupported calculation type: 'modulus'." in captured.out

def test_calculator_keyboard_interrupt(monkeypatch, capsys):
    """
    Test the calculator's handling of KeyboardInterrupt (Ctrl+C).
    """
    def mock_input(_):
        raise KeyboardInterrupt()
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "\nKeyboard interrupt detected. Exiting calculator. Goodbye!" in captured.out

def test_calculator_eof_error(monkeypatch, capsys):
    """
    Test the calculator's handling of EOFError (Ctrl+D).
    """
    def mock_input(_):
        raise EOFError()
    monkeypatch.setattr('builtins.input', mock_input)
    with pytest.raises(SystemExit) as exc_info:
        calculator()
    captured = capsys.readouterr()
    assert "\nEOF detected. Exiting calculator. Goodbye!" in captured.out

def test_calculator_unexpected_exception(monkeypatch, capsys):
    """
    Test unexpected exceptions during calculation execution.
    """
    class MockCalculation:
        def execute(self):
            raise Exception("Mock exception during execution")
        def __str__(self):
            return "MockCalculation"

    def mock_create_calculation(operation, a, b):
        return MockCalculation()

    monkeypatch.setattr('app.calculation.CalculationFactory.create_calculation', mock_create_calculation)
    inputs = iter(['add 10 5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    with pytest.raises(SystemExit):
        calculator()
        
    captured = capsys.readouterr()
    assert "An error occurred during calculation: Mock exception during execution" in captured.out