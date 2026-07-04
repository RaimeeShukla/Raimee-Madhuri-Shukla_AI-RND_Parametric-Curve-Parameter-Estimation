from src.initial_curve import generate_curve
from src.data_loader import load_dataset
from src.loss import compute_l1_loss

observed_x, observed_y = load_dataset("dataset/xy_data.csv")
_, pred_x, pred_y = generate_curve(theta_deg=20,M=0.01,X=40)
loss = compute_l1_loss(observed_x,observed_y,pred_x,pred_y)

print(loss)