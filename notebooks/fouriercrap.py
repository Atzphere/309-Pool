def fouriermodel(x, nterms):
    

# Number of terms in the Fourier series
num_terms = 5

# Generate x values for one period
x_values = np.linspace(0, L, 600)

# These arrays hold the Fourier series coefficients
a = [0 for _ in range(num_terms + 1)]
b = [0 for _ in range(num_terms + 1)]

a[0] = (1 / L) * np.trapz(trapezoid(x_values), x_values)  # get a0 using numerical integration

for n in range(1, num_terms + 1):
    a[n] = (2 / L) * np.trapz(trapezoid(x_values) * np.cos(2 * n * np.pi * x_values / L ), x_values)
    b[n] = (2 / L) * np.trapz(trapezoid(x_values) * np.sin(2 * n * np.pi * x_values / L), x_values)

# Create a function to calculate the Fourier series approximation for a given x
def fourier_series(x, num_terms):
    series_sum = a[0]  # Initialize with a0
    for n in range(1, num_terms + 1):
        series_sum += a[n] * np.cos(2 * n * np.pi * x / L ) + b[n] * np.sin(2 * n * np.pi * x / L)
    return series_sum

# Generate x values for 5 periods
x_values = np.linspace(- 2 * L , 2 * L, 1500)

# Evaluate the Fourier series for the given x values
approximation = [fourier_series(x, num_terms) for x in x_values]

# Plot the original function and the Fourier series approximation

plt.figure(figsize=(10, 6))
plt.plot(x_values, per_trapezoid(x_values,5), label="Original Function", color='blue')
plt.plot(x_values, approximation, label=f'Fourier Series (n={num_terms})', color='red')
plt.legend()
plt.title('Fourier Series Approximation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()