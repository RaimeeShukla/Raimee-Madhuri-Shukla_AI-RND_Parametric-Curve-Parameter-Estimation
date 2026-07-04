import matplotlib.pyplot as plt
from initial_curve import generate_curve

def main():
    theta = 20
    M = 0.01
    X = 40

    t, x, y = generate_curve(theta, M, X)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y)

    plt.title("Generated Parametric Curve")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.axis("equal")
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    main()