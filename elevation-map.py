import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange


def window3x3(arr, shape=(3, 3)):
    r_win = np.floor(shape[0] / 2).astype(int)
    c_win = np.floor(shape[1] / 2).astype(int)
    x, y = arr.shape
    for i in range(x):
        xmin = max(0, i - r_win)
        xmax = min(x, i + r_win + 1)
        for j in range(y):
            ymin = max(0, j - c_win)
            ymax = min(y, j + c_win + 1)
            yield arr[xmin:xmax, ymin:ymax]


def gradient(XYZ_file, vmin=0, vmax=15, figsize=(15, 10), **kwargs):
    kwargs.setdefault('plot', True)

    grid = XYZ_file.to_numpy()

    nx = XYZ_file[0].nunique()
    ny = XYZ_file[1].nunique()

    xs = grid[:, 0].reshape(ny, nx, order='F')
    ys = grid[:, 1].reshape(ny, nx, order='F')
    zs = grid[:, 2].reshape(ny, nx, order='F')
    dx = abs((xs[:, 1:] - xs[:, :-1]).mean())
    dy = abs((ys[1:, :] - ys[:-1, :]).mean())

    gen = window3x3(zs)
    windows_3x3 = np.asarray(list(gen))
    windows_3x3 = windows_3x3.reshape(ny, nx)

    dzdx = np.empty((ny, nx))
    dzdy = np.empty((ny, nx))
    loc_string = np.empty((ny, nx), dtype="S25")

    for ax_y in trange(ny):
        for ax_x in range(nx):
            # Corner points
            if ax_x == 0 and ax_y == 0:  # Top left corner
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [0][1] - windows_3x3[ax_y, ax_x][0][0]) / dx
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][0] - windows_3x3[ax_y, ax_x][0][0]) / dy
                loc_string[ax_y, ax_x] = b'top left corner'

            # Top right corner
            elif ax_x == nx - 1 and ax_y == 0:
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [0][1] - windows_3x3[ax_y, ax_x][0][0]) / dx
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][0][1]) / dy
                loc_string[ax_y, ax_x] = b'top right corner'

            # Bottom left corner
            elif ax_x == 0 and ax_y == ny - 1:
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][1][0]) / dx
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][0] - windows_3x3[ax_y, ax_x][0][0]) / dy
                loc_string[ax_y, ax_x] = b'bottom left corner'

            # Bottom right corner
            elif ax_x == nx - 1 and ax_y == ny - 1:
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][1][0]) / dx
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][0][1]) / dy
                loc_string[ax_y, ax_x] = b'bottom right corner'

            # Top border
            elif ax_y == 0 and 0 < ax_x < nx - 1:
                dzdx[ax_y, ax_x] = (
                    windows_3x3[ax_y, ax_x][0][-1] - windows_3x3[ax_y, ax_x][0][0]) / (2 * dx)
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][0][1]) / dy
                loc_string[ax_y, ax_x] = b'top border'

            # Bottom border
            elif ax_y == ny - 1 and 0 < ax_x < nx - 1:
                dzdx[ax_y, ax_x] = (
                    windows_3x3[ax_y, ax_x][1][-1] - windows_3x3[ax_y, ax_x][1][0]) / (2 * dx)
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][0][1]) / dy
                loc_string[ax_y, ax_x] = b'bottom border'

            # Left border
            elif ax_x == 0 and 0 < ax_y < ny - 1:
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][1][0]) / dx
                dzdy[ax_y, ax_x] = (windows_3x3[ax_y, ax_x][-1]
                                    [0] - windows_3x3[ax_y, ax_x][0][0]) / (2 * dy)
                loc_string[ax_y, ax_x] = b'left border'

            # Right border
            elif ax_x == nx - 1 and 0 < ax_y < ny - 1:
                dzdx[ax_y, ax_x] = (windows_3x3[ax_y, ax_x]
                                    [1][1] - windows_3x3[ax_y, ax_x][1][0]) / dx
                dzdy[ax_y, ax_x] = (
                    windows_3x3[ax_y, ax_x][-1][-1] - windows_3x3[ax_y, ax_x][0][-1]) / (2 * dy)
                loc_string[ax_y, ax_x] = b'right border'

            # Middle grid
            else:
                a = windows_3x3[ax_y, ax_x][0][0]
                b = windows_3x3[ax_y, ax_x][0][1]
                c = windows_3x3[ax_y, ax_x][0][-1]
                d = windows_3x3[ax_y, ax_x][1][0]
                f = windows_3x3[ax_y, ax_x][1][-1]
                g = windows_3x3[ax_y, ax_x][-1][0]
                h = windows_3x3[ax_y, ax_x][-1][1]
                i = windows_3x3[ax_y, ax_x][-1][-1]

                dzdx[ax_y, ax_x] = (
                    (c + 2 * f + i) - (a + 2 * d + g)) / (8 * dx)
                dzdy[ax_y, ax_x] = (
                    (g + 2 * h + i) - (a + 2 * b + c)) / (8 * dy)
                loc_string[ax_y, ax_x] = b'middle grid'

    hpot = np.hypot(abs(dzdy), abs(dzdx))
    slopes_angle = np.degrees(np.arctan(hpot))
    if kwargs['plot']:
        slopes_angle[(slopes_angle < min) | (slopes_angle > max)] = np.nan

        plt.figure(figsize=figsize)
        plt.pcolormesh(xs, ys, slopes_angle,
                       cmap=plt.cm.gist_yarg, vmax=max, vmin=min)
        plt.colorbar()
        plt.tight_layout()
        plt.show()

    return slopes_angle


if __name__ == '__main__':
    XYZ = pd.read_csv('resources/ahuna-mons.csv',
                      delimiter=',', header=None, skiprows=1)
    slopes = gradient(XYZ)
