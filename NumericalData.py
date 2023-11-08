
import random

# CLASS FOR NUMERICAL DATA
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

# CLASS FOR STRINGS
class CommentPrivacy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def add_noise_to_comment(self, comment):
        noise = self.generate_noise(len(comment))
        noisy_comment = ''.join([chr(ord(c) + n) for c, n in zip(comment, noise)])
        return noisy_comment

    def generate_noise(self, length):
        noise = [random.uniform(-self.epsilon, self.epsilon) for _ in range(length)]
        return noise

# NUMERICAL DATA SAMPLE
if __name__ == "__main__":
    epsilon = 0.5  # Privacy parameter (lower values provide stronger privacy)
    dp = DifferentialPrivacy(epsilon)

    true_result = 100  # The true result of a query
    noisy_result = dp.add_noise(true_result)

    print(f"True Result: {true_result}")
    print(f"Noisy Result: {noisy_result}")

# COMMENTS SAMPLE
if __name__ == "__main__":
    epsilon = 0.1  # Privacy parameter (lower values provide stronger privacy)
    cp = CommentPrivacy(epsilon)

    original_comment = "I love this feature!"
    noisy_comment = cp.add_noise_to_comment(original_comment)

    print(f"Original Comment: {original_comment}")
    print(f"Noisy Comment: {noisy_comment}")