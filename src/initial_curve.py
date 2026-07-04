import numpy as np

def generate_curve(theta_deg, M, X, t_start=6, t_end=60, num_points=1500):
    """
    Parameters:
    1) theta_deg : float -> Rotation angle in degrees.
    2) M : float -> Exponential scaling parameter.
    3) X : float -> Horizontal translation.
    4) t_start : float -> Starting value of parameter t.
    5) t_end : float -> Ending value of parameter t.
    6) num_points : int -> Number of points to generate.

    Output:
    1) t : ndarray -> Parameter values.
    2) x : ndarray -> Generated x coordinates.
    3) y : ndarray -> Generated y coordinates.
    """

    # Convert degrees to radians
    theta = np.deg2rad(theta_deg)

    # Generate uniformly spaced t values
    t = np.linspace(t_start, t_end, num_points)
    exp_term = np.exp(M * np.abs(t))

    # Parametric equations
    x = (t * np.cos(theta) - exp_term * np.sin(0.3 * t) * np.sin(theta)+ X)
    y = (42 + t * np.sin(theta)+ exp_term * np.sin(0.3 * t) * np.cos(theta))

    return t, x, y