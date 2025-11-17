import numpy as np
from typing import List, Tuple

def calculate_lineament_metrics(lineaments: List) -> dict:
    """
    Calculate metrics for detected lineaments.
    
    Args:
        lineaments (List): List of detected lineaments
        
    Returns:
        dict: Calculated metrics
    """
    if not lineaments:
        return {
            'count': 0,
            'total_length': 0,
            'average_length': 0,
            'orientations': []
        }
    
    lengths = []
    orientations = []
    
    for line in lineaments:
        (x1, y1), (x2, y2) = line
        
        # Calculate length
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        lengths.append(length)
        
        # Calculate orientation
        orientation = np.degrees(np.arctan2(y2 - y1, x2 - x1))
        orientations.append(orientation)
    
    return {
        'count': len(lineaments),
        'total_length': sum(lengths),
        'average_length': np.mean(lengths),
        'std_length': np.std(lengths),
        'orientations': orientations
    }

def filter_lineaments_by_length(lineaments: List, min_length: float) -> List:
    """
    Filter lineaments by minimum length.
    
    Args:
        lineaments (List): List of lineaments
        min_length (float): Minimum length threshold
        
    Returns:
        List: Filtered lineaments
    """
    filtered = []
    
    for line in lineaments:
        (x1, y1), (x2, y2) = line
        length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        if length >= min_length:
            filtered.append(line)
    
    return filtered
