import pytest

from src.base_class import Figure

def test_create_base_instance_class():
    with pytest.raises(Exception) as instance_error:
        instance_class = Figure('Figure')

    assert 'FAILED to instantiate parent class! It must be subclassed.' in str(instance_error.value), \
        "There must be an error message'FAILED to instantiate parent class! It must be subclassed.'"
