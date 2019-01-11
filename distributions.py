import matplotlib.pyplot as plt
from math import factorial, sqrt

def binomial(n, k):
    return factorial(n)/(factorial(n - k) * factorial(k))

def bd(n, k, p):
    return binomial(n, k) * p**k * (1 - p)**(n - k)

n = int(input("Insert number of trials: ")) #trials
probability = float(input("Insert probability of success: ")) #probability of success
#E = 0
E = n * probability
var = E * (1 - probability)

if probability > 1 or probability < 0:
    print("\nError: Invalid Probability Value")
    exit(1)

print()

for i in range(n + 1):
    print("%d: %f" % (i, bd(n, i, probability)))
    #E += i * bd(n, i, probability)
    plt.bar(i, bd(n, i, probability), color='c')

print("\nE(x) = %f\nvar(x) = %f\nσ = %f" % (E, var, sqrt(var)))

plt.gca().set_facecolor('k')
plt.suptitle("Binomial Distribution")
plt.title("n = %d    Success Probability = %f" % (n, probability))
plt.xlabel("Successful Trials")
plt.ylabel("Binomial Probability P(X = x)")
plt.show()
