import pytest
from unittest.mock import MagicMock, patch
from app import agregar_tarea, completar_tarea_action, eliminar_tarea_action



# Mock de la base de datos y el archivo JSON
@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_tareas():
    return [
        {"id": 1, "titulo": "Tarea 1", "descripcion": "Descripción 1", "completada": False},
        {"id": 2, "titulo": "Tarea 2", "descripcion": "Descripción 2", "completada": False},
    ]


# Test para agregar_tarea
@patch("app.cargar_tareas", return_value=[])
@patch("app.guardar_tareas")
@patch("app.crear_tarea")
def test_agregar_tarea(mock_crear_tarea, mock_guardar_tareas, mock_cargar_tareas, mock_db):
    agregar_tarea(mock_db, "Nueva Tarea", "Descripción nueva")

    # Verifica que crear_tarea se llamó correctamente
    mock_crear_tarea.assert_called_once_with(mock_db, "Nueva Tarea", "Descripción nueva")

    # Verifica que guardar_tareas se llamó con la lista actualizada
    mock_guardar_tareas.assert_called_once()
    tareas_actualizadas = mock_guardar_tareas.call_args[0][0]
    assert len(tareas_actualizadas) == 1
    assert tareas_actualizadas[0]["titulo"] == "Nueva Tarea"


# Test para completar_tarea_action
@patch("app.guardar_tareas")
@patch("app.completar_tarea")
def test_completar_tarea_action(mock_completar_tarea, mock_guardar_tareas, mock_db, mock_tareas):
    completar_tarea_action(mock_db, mock_tareas, 0)

    # Verifica que completar_tarea se llamó con el ID correcto
    mock_completar_tarea.assert_called_once_with(mock_db, 1)

    # Verifica que la tarea se marcó como completada
    assert mock_tareas[0]["completada"] is True

    # Verifica que guardar_tareas se llamó con la lista actualizada
    mock_guardar_tareas.assert_called_once_with(mock_tareas)


# Test para eliminar_tarea_action
@patch("app.guardar_tareas")
@patch("app.eliminar_tarea")
def test_eliminar_tarea_action(mock_eliminar_tarea, mock_guardar_tareas, mock_db, mock_tareas):
    eliminar_tarea_action(mock_db, mock_tareas, 0)

    # Verifica que eliminar_tarea se llamó con el ID correcto
    mock_eliminar_tarea.assert_called_once_with(mock_db, 1)

    # Verifica que la tarea fue eliminada de la lista
    assert len(mock_tareas) == 1
    assert mock_tareas[0]["id"] == 2

    # Verifica que guardar_tareas se llamó con la lista actualizada
    mock_guardar_tareas.assert_called_once_with(mock_tareas)
