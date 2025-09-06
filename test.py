import numpy as np
import cvxpy
import math

def poly_fit(samples, degree, resolution):
    """
    Args:
        samples: [[x_1,y_1],...,[x_i,y_i]] points to fit...
        degree: max polynomial degree to fit
        resolution: log_10(resolution) is number of decimal digits allowed for coefficients, set resolution = -1 to fit to float64 (?)
    Returns:
        list l of best fitting polynomial coefficients (l[0] being constant term)
    """
    if resolution != -1:
        print(f"Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has fixed decimal digit count, resolution {1/resolution}")
    else:
        print(f"Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has float64 resolution")

    m=len(samples) #sample count
    n=degree+1
    r=resolution #log_10(r) is number of decimal digits allowed in coefficients

    y = np.array([ p[1] for p in samples ])
    A = np.array([ [p[0]**i for i in range(degree+1)] for p in samples ])
    if r == -1:
        c = cvxpy.Variable(n, integer= False)
    else:
        c = cvxpy.Variable(n, integer= True)

    obj = cvxpy.Minimize(cvxpy.norm(A @ c/abs(r) - y, 2))
    prob = cvxpy.Problem(obj)
    sol = prob.solve(solver = 'ECOS_BB')

    if r == -1:
        return c.value
    
    decimal_digits=int(math.log10(r))
    return [ format(np.round(j/resolution,decimal_digits),"."+str(decimal_digits)+"f") for j in c.value]


samples=[[1,1],[2,2],[3,4.2],[0,0]]
polynomial_degree_for_fit=2

print(f"For fixed sample set {samples} and fixed degree {polynomial_degree_for_fit}, running experiments with different resolutions...")

print(poly_fit(samples, polynomial_degree_for_fit,10000))
print(poly_fit(samples, polynomial_degree_for_fit,1000))
print(poly_fit(samples, polynomial_degree_for_fit,100))
print(poly_fit(samples, polynomial_degree_for_fit,10))
print(poly_fit(samples, polynomial_degree_for_fit,1))
print(poly_fit(samples, polynomial_degree_for_fit,-1))

