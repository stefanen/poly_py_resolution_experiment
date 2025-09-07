import numpy as np
import cvxpy
import math
import  matplotlib. pyplot  as  plt
def poly_fit(samples, degree, resolution):
    """
    Args:
        samples: [[x_1,y_1],...,[x_i,y_i]] points to fit...
        degree: degree of polynomial to fit (coefficient count - 1)
        resolution: number of decimal digits allowed for coefficients, set resolution = -1 to fit to float64
    Returns:
        a tuple (score,c) where
        list c of best fitting polynomial coefficients (c[0] being constant term)
        and score is the valuable of the objective function with coefficients c
    """
    m=len(samples) #sample count
    n=degree+1 #number of coefficients
    y = np.array([ p[1] for p in samples ])
    A = np.array([ [p[0]**i for i in range(degree+1)] for p in samples ])
    
    if resolution != -1:
        print(f"Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has at most {resolution} decimal digits")
        r=10**resolution
        c = cvxpy.Variable(n, integer= True)
    else:
        print(f"Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has full float64 resolution")
        r=1
        c = cvxpy.Variable(n, integer= False)


    #The problem is to find c that minimizes |(A*c/r -y)^2|
    #A=[[1,x_1,x_1^2,...],...[1,x_m,x_m^2,...]]
    #y=[y_1,y_2,...,y_m]

    objective_function = cvxpy.Minimize(cvxpy.norm(A @ c/abs(r) - y, 2))
    prob = cvxpy.Problem(objective_function)
    sol = prob.solve(solver = 'ECOS_BB')
    #print(sol)

    if resolution == -1:
        return (c.value, sol)

    return ([ np.round(j/r,resolution) for j in c.value],sol)
    #return [ format(np.round(j/r,resolution),"."+str(resolution)+"f") for j in c.value]


def coeffs_to_str(coeffs, resolution):
    if resolution == -1:
        res=f"coeff-constraint: double, p(t)="
    else:
        res=f"coeff-constraint: {resolution} decimal digits, p(t)="
    i=0
    for coeff in coeffs:
        if i!=0:
            res+=" + "
        res+=str(coeff)+"*t^"+str(i)
        i=i+1
    return res

def run_experiment(sample, degree, max_res, do_plot=False):
    print(f"Running poly_fit experiment for samples {sample} and degree {degree} for various resolutions...")
    print(f"")
    x_range = np.linspace(0, 10, 10)
    if do_plot:
        plt.scatter([p[0] for p in sample], [p[1] for p in sample], color="red", zorder=5, label="sample points")
    for i in range(-1,max_res+1):
        result=poly_fit(sample, degree,i)
        if do_plot:
            plt.plot(x_range, y_values(x_range, result[0]), label=coeffs_to_str(result[0], i))
        print(f"result: best coefficients = {result[0]}, score={result[1]}")

    if do_plot:
        plt.legend(loc="upper left")
        plt.show()


def y_values(x, coeffs):
    o = len(coeffs)
    y = 0
    for i in range(o):
        y += coeffs[i]*x**i
    return y



sample_1=[[1,1],[2,2],[3,5],[0,0]]
sample_2=[[1,1.2],[2,3.1],[3,0.5],[4,5.7]]
run_experiment(sample_2,2,3,True)

