import numpy as np

def compute_l1_loss(observed_x,observed_y,predicted_x,predicted_y):
    """
    Compute average L1 distance between curves
    """
    loss = np.mean(np.abs(observed_x - predicted_x) + np.abs(observed_y - predicted_y))
    return loss