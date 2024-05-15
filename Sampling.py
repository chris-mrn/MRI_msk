class sample_strategy:
    def __init__(self, strategy):
        self.strategy = strategy

    def sample(self, data, n_samples):
        return self.strategy.sample(data, n_samples)
