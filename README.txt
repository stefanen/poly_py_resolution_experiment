Example output: (just single experiment)

Running poly_fit experiment for samples [[1, 1.2], [2, 3.1], [3, 0.5], [4, 5.7]] and degree 2 for various resolutions...

Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has full float64 resolution
result: best coefficients = [ 4.02499999 -3.03499999  0.825     ], score=2.7503636123247412
Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has at most 0 decimal digits
result: best coefficients = [np.float64(5.0), np.float64(-4.0), np.float64(1.0)], score=2.7910571477846275
Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has at most 1 decimal digits
result: best coefficients = [np.float64(3.9), np.float64(-2.9), np.float64(0.8)], score=2.751363298439611
Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has at most 2 decimal digits
result: best coefficients = [np.float64(4.0), np.float64(-3.01), np.float64(0.82)], score=2.7503817916791116
Trying to find best fitting c_i for p(x)=sum(c_i*x^i) , where each c_i has at most 3 decimal digits
result: best coefficients = [np.float64(4.025), np.float64(-3.035), np.float64(0.825)], score=2.7503636123247412

