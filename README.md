# openai-path
This repository has the objective to study and achieve position in openai

## Mathematical Formulas

### Algebra

#### Quadratic Formula
The solution to $ax^2 + bx + c = 0$ is:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

#### Binomial Theorem
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

#### Factoring Formulas
- Difference of squares: $a^2 - b^2 = (a + b)(a - b)$
- Perfect square trinomial: $a^2 + 2ab + b^2 = (a + b)^2$
- Perfect square trinomial: $a^2 - 2ab + b^2 = (a - b)^2$

### Calculus

#### Derivatives
- Power rule: $\frac{d}{dx}[x^n] = nx^{n-1}$
- Product rule: $\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$
- Quotient rule: $\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$
- Chain rule: $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$

#### Integrals
- Power rule: $\int x^n dx = \frac{x^{n+1}}{n+1} + C$ (for $n \neq -1$)
- Integration by parts: $\int u \, dv = uv - \int v \, du$
- Fundamental theorem of calculus: $\int_a^b f'(x) dx = f(b) - f(a)$

### Linear Algebra

#### Matrix Operations
- Matrix multiplication: $(AB)_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}$
- Determinant of 2×2 matrix: $\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$
- Inverse of 2×2 matrix: $\begin{pmatrix} a & b \\ c & d \end{pmatrix}^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

#### Eigenvalues and Eigenvectors
For matrix $A$ and eigenvector $v$ with eigenvalue $\lambda$:
$$Av = \lambda v$$

### Statistics and Probability

#### Probability
- Bayes' theorem: $P(A|B) = \frac{P(B|A)P(A)}{P(B)}$
- Expected value: $E[X] = \sum_{i} x_i P(X = x_i)$
- Variance: $\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$

#### Normal Distribution
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

### Trigonometry

#### Basic Identities
- Pythagorean identity: $\sin^2 \theta + \cos^2 \theta = 1$
- Double angle: $\sin(2\theta) = 2\sin \theta \cos \theta$
- Double angle: $\cos(2\theta) = \cos^2 \theta - \sin^2 \theta$

#### Sum and Difference Formulas
- $\sin(A + B) = \sin A \cos B + \cos A \sin B$
- $\cos(A + B) = \cos A \cos B - \sin A \sin B$

### Series and Sequences

#### Geometric Series
$$\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}, \quad |r| < 1$$

#### Arithmetic Series
$$\sum_{n=1}^{N} n = \frac{N(N+1)}{2}$$

### Complex Numbers

#### Euler's Formula
$$e^{i\theta} = \cos \theta + i\sin \theta$$

#### De Moivre's Theorem
$$(\cos \theta + i\sin \theta)^n = \cos(n\theta) + i\sin(n\theta)$$

---

*Note: All formulas are written in LaTeX format and will render properly in markdown viewers that support mathematical notation.*
