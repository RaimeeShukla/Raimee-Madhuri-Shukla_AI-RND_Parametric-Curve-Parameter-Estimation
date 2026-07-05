import matplotlib.pyplot as plt
from src.data_loader import load_dataset
from src.optimizer import baseline_grid_search

def main():
    observed_x, observed_y = load_dataset("dataset/xy_data.csv")
    theta, M, X, loss, pred_x, pred_y = baseline_grid_search(observed_x,observed_y)

    print(f"Final Theta : {theta}")
    print(f"Final M : {M}")
    print(f"Final X : {X}")
    print(f"Final Loss : {loss}")

    plt.figure(figsize=(8,6))
    plt.scatter(observed_x, observed_y,s=5,label="Observed")
    plt.plot(pred_x,pred_y,color="red",linewidth=2,label="Predicted")
    plt.legend()
    plt.axis("equal")

    plt.savefig("final_curve.png", dpi=300, bbox_inches="tight")
    plt.show()

if __name__ == "__main__":
    main()