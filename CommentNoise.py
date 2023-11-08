import random

class CommentPrivacy:
    def __init__(self, epsilon):
        self.epsilon = epsilon

    def add_noise_to_comment(self, comment):
        noise = self.generate_noise(len(comment))
        noisy_comment = ''.join([chr(ord(c) + int(n)) for c, n in zip(comment, noise)])
        return noisy_comment

    def generate_noise(self, length):
        noise = [random.uniform(-self.epsilon, self.epsilon) for _ in range(length)]
        return noise

# Example usage
if __name__ == "__main__":
    epsilon = 1.5  # Privacy parameter (lower values provide stronger privacy)
    cp = CommentPrivacy(epsilon)

    original_comment = "I love this feature!"
    noisy_comment = cp.add_noise_to_comment(original_comment)

    print(f"Original Comment: {original_comment}")
    print(f"Noisy Comment: {noisy_comment}")
