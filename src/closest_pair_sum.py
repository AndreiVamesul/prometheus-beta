from typing import List, Tuple

def find_closest_pair_sum(arr: List[int], target: int) -> Tuple[int, int]:
    """
    Find the pair of elements in the array whose sum is closest to the target value.
    
    Args:
        arr (List[int]): Input array of integers
        target (int): Target sum to find closest pair to
    
    Returns:
        Tuple[int, int]: A tuple containing the first pair of elements 
                         whose sum is closest to the target
    
    Raises:
        ValueError: If the input array has fewer than 2 elements
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Check for invalid input
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    # Initialize variables to track closest pair
    closest_sum = float('inf')
    closest_pair = (arr[0], arr[1])
    
    # Brute force approach to find closest pair
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if current pair is closer to target
            # Or if it's the first pair encountered
            closest_diff = abs(closest_pair[0] + closest_pair[1] - target)
            if current_diff < closest_diff:
                closest_sum = current_sum
                closest_pair = (arr[i], arr[j])
    
    return closest_pair