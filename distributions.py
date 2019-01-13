import matplotlib.pyplot as plt
from math import factorial, sqrt

def binomial(n, k):
    return factorial(n)/(factorial(n - k) * factorial(k))

def bd(n, k, p):
    return binomial(n, k) * p**k * (1 - p)**(n - k)

choice = int(input("1) Binomial Distribution\n2) Geometric Distribution\n\nChoice: "))
while choice not in range(1,3):
	choice = int(input("Error: Invalid choice!\n\nChoice: "))

probability = float(input("\nInsert probability of success: ")) #probability of success
	
if probability > 1 or probability < 0:
    print("\nError: Invalid Probability Value")
    exit(1)

if choice == 1:
	n = int(input("Insert number of trials: ")) #trials

	plt.suptitle("Binomial Distribution")
	plt.title("n = %d    Success Probability = %f" % (n, probability))
	plt.xlabel("Successful Trials")

	#E = 0
	E = n * probability
	var = E * (1 - probability)

	print()

	for i in range(n + 1):
	    print("%d: %f" % (i, bd(n, i, probability)))
	    #E += i * bd(n, i, probability)
	    plt.bar(i, bd(n, i, probability), color='c')

elif choice == 2:

	plt.suptitle("Geometric Distribution")
	plt.title("Success Probability = %f" % (probability))
	plt.xlabel("Trials Until Success")

	E = 1 / probability
	var = (1 - probability) / probability ** 2

	print()

	k = 1
	p = probability

	while(p > 0.0000009):
		print("%d: %f" % (k, p))
		plt.bar(k, p, color='r')
		k += 1
		p = ((1 - probability) ** (k - 1)) * probability

print("\nE(x) = %f\nvar(x) = %f\nσ = %f" % (E, var, sqrt(var)))

plt.gca().set_facecolor('k')
plt.ylabel("Binomial Probability P(X = x)")
plt.show()
