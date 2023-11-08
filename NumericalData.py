import random

class DifferentialPrivacy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def add_noise(self, true_result):
        sensitivity = 1  # Sensitivity of the query (maximum difference when one row is added or removed)

        # Calculate the Laplace noise
        scale = sensitivity / self.epsilon
        noise = random.uniform(-scale, scale)

        # Add noise to the true result
        noisy_result = true_result + noise

        return noisy_result

# Example usage
if __name__ == "__main__":
    epsilon = 0.5  # Privacy parameter (lower values provide stronger privacy)
    dp = DifferentialPrivacy(epsilon)

    true_result = 100  # The true result of a query
    noisy_result = dp.add_noise(true_result)

    print(f"True Result: {true_result}")
    print(f"Noisy Result: {noisy_result}")
