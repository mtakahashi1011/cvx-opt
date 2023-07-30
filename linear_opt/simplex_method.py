import numpy as np 
import scipy.linalg as linalg
MEPS = 1.0e-10

# Maximize c_B^T A_B^{-1} b + (c_N - c_B^T A_B^{-1} A_N)^T x_N
# subject to x_B = A_B^{-1} b - A_B^{-1} A_N x_N, x >= 0

def lp_RevisedSimplex(c, A, b):
    np.seterr(divide='ignore')
    (m, n) = A.shape 
    AI = np.hstack((A, np.identity(m)))
    c0 = np.r_[c, np.zeros(m)]
    basis = [n+i for i in range(m)]
    nonbasis = [j for j in range(n)]

    while True:
        # cc = c_N - c_B^T A_B^{-1} A_Nの計算
        # まずはy = c_B^T A_B^{-1}を計算する
        y = linalg.solve(AI[:, basis].T, c0[basis])
        cc = c0[nonbasis] - np.dot(y, AI[:, nonbasis])

        # cc<=0の場合はx_N=0(とそれに応じて定まるx_B = A_B^{-1} b)が最適解
        if np.all(cc <= MEPS): 
            x = np.zeros(n+m) 
            x[basis] = linalg.solve(AI[:, basis], b)
            print('Optimmal')
            print('Optimal value = ', np.dot(c0[basis], x[basis]))
            for i in range(m):
                print('x', i, '=', x[i])
            break 
        # cc>0の場合は係数が正の非基底変数を更新するために一つ選択する
        # ここでは係数が最大のものを選択することとする
        else:
            s = np.argmax(cc)

        # d = A_B^{-1} A_Sを計算
        d = linalg.solve(AI[:, basis], AI[:, nonbasis[s]])

        # dの成分が全て非負の場合はx_sをいくらでも大きく取れるので目的関数値は非有界になる
        if np.all(d <= MEPS): 
            print('Unbounded')
            break 
        # そうでない場合はx_s d <= A_B^{-1}を満たすようにx_sを更新する
        else:
            # bb = A_B^{-1} bの計算
            bb = linalg.solve(AI[:, basis], b)
            # x_s <= bb / dを満たすようにx_sを更新する
            ratio = bb / d 
            ratio[ratio < -MEPS] = np.inf 
            r = np.argmin(ratio)
            print('replace', s, 'with', r)
            # 基底と非基底の入れ替え
            nonbasis[s], basis[r] = basis[r], nonbasis[s]

if __name__ == '__main__':
    A = np.array([[2, 2, -1], [2, -2, 3], [0, 2, -1]])
    c = np.array([4, 3, 5])
    b = np.array([6, 8, 4])

    lp_RevisedSimplex(c, A, b)