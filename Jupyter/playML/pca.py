import numpy as np

class PCA:
    def __init__(self, n_components):
        """初始化PCA模型"""
        assert n_components >= 1, "n_components must be bigger than 0."
        self.n_components = n_components
        self.components_ = None

    def fit(self, X, eta = 0.01, n_iters = 1e4):
        assert self.n_components <= X.shape[1], "n_components must be not bigger than the feature number of X."
        def f(X, w):
            return np.sum(X.dot(w) ** 2) / len(X)
        def df(X, w):
            return X.T.dot(X.dot(w)) * 2 / len(X)
        def direction(w):  # 求单位向量
            return w / np.linalg.norm(w)
        def demean(X):  # 需要对原始数据做demean处理 - 归零
            return X - np.mean(X, axis=0)
        def first_component(X, initial_w, eta=0.001, n_iters=1e4, epsilon=1e-8):
            w = direction(initial_w)
            i_iter = 0
            while (i_iter < n_iters):
                last_w = w
                gradient = df(X, w)
                w = w + eta * gradient
                w = direction(w)
                if np.abs(f(X, w) - f(X, last_w)) < epsilon:
                    break
                i_iter += 1
            return w

        X_pca = demean(X)
        self.components_ = np.empty(shape=(self.n_components, X.shape[1]))
        for i in range(self.n_components):
            initial_w = np.random.random(X_pca.shape[1])
            w = first_component(X_pca, initial_w)
            self.components_[i, :] = w
            X_pca = X_pca - (X_pca.dot(w)).reshape(-1, 1) * w
        return self

    def transform(self, X):
        """将给定的X映射到各主成分分量中"""
        assert self.components_.shape[1] == X.shape[1], "n_components must be equal to the feature number of X."
        return X.dot(self.components_.T)

    def inverse_transform(self, X_k):
        """将给定的X_k反向映射到原来的特征空间"""
        assert self.components_.shape[0] == X_k.shape[1], "n_components must be equal to the feature number of X_k."
        return X_k.dot(self.components_)
    def first_n_components(n, X, eta = 0.001, n_iters=1e4, epsilon=1e-8):

        def first_component(X, initial_w, eta=0.001, n_iters=1e4, epsilon=1e-8):
            def f(X, w):
                return np.sum(X.dot(w) ** 2) / len(X)

            def df(X, w):
                return X.T.dot(X.dot(w)) * 2 / len(X)

            def direction(w):  # 求单位向量
                return w / np.linalg.norm(w)

            w = direction(initial_w)
            i_iter = 0

            while (i_iter < n_iters):
                last_w = w
                gradient = df(X, w)
                w = w + eta * gradient
                w = direction(w)
                if np.abs(f(X, w) - f(X, last_w)) < epsilon:
                    break
                i_iter += 1
            return w

        def demean(X):  # 需要对原始数据做demean处理 - 归零
            return X - np.mean(X, axis=0)

        X_pca = X.copy()
        res = []
        X_pca = demean(X_pca)
        for i in range(n):
            initial_w = np.random.random(X_pca.shape[1])
            w = first_component(X_pca, initial_w)
            res.append(w)
            X_pca = X_pca - (X_pca.dot(w)).reshape(-1, 1) * w

        return res

    def __repr__(self):
        return "PCA(n_components = %d)" % self.n_components