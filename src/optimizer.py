import numpy as np
from src.initial_curve import generate_curve
from src.loss import compute_l1_loss

def baseline_grid_search(observed_x, observed_y):
    """
    Baseline grid search for estimating theta, M and X.
    """

    best_loss = float("inf")
    best_theta = None
    best_M = None
    best_X = None

    # Initial search range
    theta_values = np.arange(0, 51, 2)
    M_values = np.arange(-0.05, 0.051, 0.01)
    X_values = np.arange(0, 101, 2)

    for theta in theta_values:
        for M in M_values:
            for X in X_values:
                _, pred_x, pred_y = generate_curve(theta,M,X,num_points=len(observed_x))
                loss = compute_l1_loss(observed_x,observed_y,pred_x,pred_y)
                if loss < best_loss:
                    best_loss = loss
                    best_theta = theta
                    best_M = M
                    best_X = X
                    best_pred_x = pred_x.copy()
                    best_pred_y = pred_y.copy()

                    print(
                        f"New Best -> "
                        f"Theta={theta}, "
                        f"M={M:.3f}, "
                        f"X={X}, "
                        f"Loss={loss:.6f}"
                    )

    return best_theta, best_M, best_X, best_loss, best_pred_x, best_pred_y