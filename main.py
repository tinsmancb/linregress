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
        self.slope_hist = []

    def loss(self, slope=None):
        if slope is None:
            slope = self.slope

        return np.sum((slope*self.xs - self.ys)**2)

    def fit(self, delta=1e-5, gamma=1, max_iter=100, tol=1e-8, debug=False):
        self.slope_hist = [self.slope]

        for i in range(max_iter):

            gradient = (self.loss(self.slope+delta) - self.loss(self.slope-delta))/(2*delta)

            while True:
                new_slope = self.slope - gamma*gradient

                if self.loss(new_slope) < self.loss(self.slope):
                    self.slope = new_slope
                    self.slope_hist.append(self.slope)
                    break
                else:
                    gamma /= 2
                    if debug:
                        print(f"Gamma reduced to {gamma} at iteration {i}")

            if (np.abs(self.slope_hist[-1] - self.slope_hist[-2]) / np.abs(self.slope_hist[-1])) < tol:
                break

    def predict(self, xs):
        return self.slope*xs

    def slope_hist_plot(self):
        plt.plot(self.slope_hist)
        plt.ylabel("Regression Slope")
        plt.xlabel("Iteration")

        plt.show()

    def data_plot(self):
        xrange = np.linspace(self.xs.min(), self.xs.max(), 100)
        yrange = self.predict(xrange)

        plt.plot(self.xs, self.ys, '.')
        plt.plot(xrange, yrange)
        plt.show()


def main():
    adelie_bill_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=0)
    adelie_flipper_len_mm = np.loadtxt("adelie.csv", delimiter=',', skiprows=1, usecols=1)

    adelie_regress = LinearRegression(adelie_bill_len_mm, adelie_flipper_len_mm)
    adelie_regress.fit()
    adelie_regress.data_plot()
    adelie_regress.slope_hist_plot()
    print(adelie_regress.slope_hist)

    # loss_xs = np.linspace(0, 10, 100)
    # loss_ys = np.array([adelie_regress.loss(a) for a in loss_xs])
    # plt.plot(loss_xs, loss_ys)
    # plt.show()


if __name__ == '__main__':
    main()
