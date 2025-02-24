import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_case():
    """Test a basic scenario with multiple pairs"""
    arr = [10, 22, 28, 29, 30, 40]
    target = 54
    result = find_closest_pair_sum(arr, target)
    assert result == (22, 30) or result == (30, 22)

def test_exact_match():
    """Test when there's an exact match to the target"""
    arr = [1, 3, 4, 5, 10, 15]
    target = 9
    result = find_closest_pair_sum(arr, target)
    assert result == (4, 5) or result == (5, 4)

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, -3, 5, 7, 8, 12, -15]
    target = 4
    result = find_closest_pair_sum(arr, target)
    assert result == (-1, 5) or result == (5, -1)

def test_first_occurrence_when_multiple_closest():
    """Ensure first occurrence is returned when multiple pairs are equally close"""
    arr = [1, 2, 3, 4, 5, 6]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result == (1, 6) or result == (6, 1)

def test_error_cases():
    """Test error handling for invalid inputs"""
    # Empty array
    with pytest.raises(ValueError):
        find_closest_pair_sum([], 10)
    
    # Single element array
    with pytest.raises(ValueError):
        find_closest_pair_sum([5], 10)

def test_large_numbers():
    """Test with large numbers"""
    arr = [1000000, 2000000, 3000000, 4000000]
    target = 5000000
    result = find_closest_pair_sum(arr, target)
    assert result == (2000000, 3000000) or result == (3000000, 2000000)

def test_all_same_numbers():
    """Test array with identical numbers"""
    arr = [5, 5, 5, 5, 5]
    target = 10
    result = find_closest_pair_sum(arr, target)
    assert result == (5, 5)