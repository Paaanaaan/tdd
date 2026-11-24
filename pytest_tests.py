import pytest

def test_add():
    assert 2 + 2 == 4
    
def test_multiply():
    assert 2 * 3 == 6


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
