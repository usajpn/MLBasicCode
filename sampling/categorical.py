import random

def sample_one(probs):
    z = sum(probs.values()) # 1
    remaining = random.uniform(0, z)
    for k, v in probs.items():
        remaining -= v
        if remaining <= 0:
            return k


def main():
    probs = {
        'A': 0.5,
        'B': 0.3,
        'C': 0.2
    }

    N = 10000
    samples = {k: 0 for k in probs.keys()}

    for _ in range(N):
        sample = sample_one(probs)
        samples[sample] += 1

    print('Result:')
    for k, v in samples.items():
        print('{}: {:.3f} ({}/{})'.format(k, v/N, v, N))


if __name__ == "__main__":
    main()
