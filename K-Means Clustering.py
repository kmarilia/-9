import numpy as np
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, n_clusters=3, max_iters=100, random_state=42):
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.random_state = random_state
        self.centroids = None
        self.labels = None
    
    def fit(self, X):
        np.random.seed(self.random_state)
        n_samples = X.shape[0]
        
        # Инициализация центроидов случайными точками
        random_indices = np.random.choice(n_samples, self.n_clusters, replace=False)
        self.centroids = X[random_indices]
        
        for _ in range(self.max_iters):
            # Шаг 1: назначение кластеров
            distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            
            # Шаг 2: пересчёт центроидов
            new_centroids = np.array([X[self.labels == k].mean(axis=0) for k in range(self.n_clusters)])
            
            # Проверка сходимости
            if np.allclose(self.centroids, new_centroids):
                break
            self.centroids = new_centroids
    
    def predict(self, X):
        distances = np.linalg.norm(X[:, np.newaxis] - self.centroids, axis=2)
        return np.argmin(distances, axis=1)

# Пример использования
if __name__ == "__main__":
    # Генерация тестовых данных
    np.random.seed(42)
    cluster1 = np.random.randn(50, 2) + [0, 0]
    cluster2 = np.random.randn(50, 2) + [5, 5]
    cluster3 = np.random.randn(50, 2) + [5, 0]
    X = np.vstack([cluster1, cluster2, cluster3])
    
    # Применение K-Means
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)
    labels = kmeans.labels
    
    # Визуализация
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:, 1], 
                c='red', marker='X', s=200, label='Центроиды')
    plt.title("K-Means Clustering")
    plt.legend()
    plt.show()
    
    print("Центроиды:")
    print(kmeans.centroids)