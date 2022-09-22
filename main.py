import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self, xs, ys):

        if xs is None:
            xs = np.zeros(10)

        if ys is None:
            ys = np.zeros(10)

        self.xs = xs
        self.ys = ys
        self.slope = 0

    def loss(self):
        pass

    def fit(self):
        pass

    def predict(self, xs):
        pass


def main():
    adelie_bill_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=0)
    adelie_flipper_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=1)

    plt.plot(adelie_bill_len_mm, adelie_flipper_len_mm, '.')
    plt.show()

if __name__ == '__main__':
    main()