def sum_of_primes(upperbound: int):
    """Return the sum of probes between 0 and upper bound as an integer.

    PRECONDITION upperbound is a positive integer
    RETURN the sum of all prime numbers including upperbound"""
    not_primes = []
    prime = []
    if upperbound < 0:
        raise ValueError("Please enter a positive integer!")
    else:
        for i in range(2, upperbound + 1):
            if i not in not_primes:
                prime.append(i)
                for j in range(i*i, upperbound + 1, i):
                    not_primes.append(j)
        return sum(prime)


def main():
    print(sum_of_primes(11))
    print(sum_of_primes(100))


if __name__ == '__main__':
    main()
