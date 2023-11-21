import numpy as np
import matplotlib.pyplot as plt


x = np.array([4.45888061,
4.655406328,
4.811629883,
5.511647423,
6.381185531,
6.582252346,
6.770897288,
6.902998421,    
6.911480146,
7.149602668,
7.374813168])


y = np.array([3.633329828,
3.081099725,
3.194856985,
2.875587745,
2.250357562,
2.181625082,
2.047525228,
2.006629134,
1.990873277,
1.830197417,
1.804854367])


w = [
0.004810351183,
0.04358205349,
0.002305015826,
0.002828796494,
0.002533967172,
0.001959275057,
0.002527373645,
0.002802550752,
0.002248514688,
0.002271931896,
0.005540350303
]

Energy = [86.39075,
105.1519375,
122.9318188,
247.558625,
590.6275,
722.1640625,
872.0940625,
995.2544375,
1003.731813,
1273.599813,
1595.29375]



Efficiency = [37.83860311,
21.78234381,
24.40668293,
17.73584522,
9.491128899,
8.860693922,
7.748701094,
7.438201857,
7.32192504,
6.235117457,
6.079086068]

Efficiency_error = [
    0.1820169692,
0.9493192731,
0.05625779042,
0.05017109678,
0.02405020905,
0.01736053659,
0.01958386293,
0.02084593821,
0.016463456,
0.01416576223,
0.03368026634
]




def chi2(x,y):
    chi2 = 0
    for i in range(0,len(x)):
        chi2 += (y[i]-x[i])**2
        # print(chi2)
    return chi2



def fit_exp(z,x):
    #z is the model x is the ln energy 
    n = len(z[0])
    exp = []
    for item in x:
        value = 0
        for i in range(0,n):    
            value += z[0][i]*item**(n-i-1)
            # print(i)
        exp.append(np.exp(value) )
    # print(exp)
    return np.array(exp)








w = np.array([1/i**2 for i in w])
print(w)


z = np.polyfit(x, y, 5, w = w,cov = True)
print(z[1])
Energy_test = np.linspace(Energy[0],Energy[-1],1000)
x_test = np.log(Energy_test)

x_test2 = np.log(Energy)




print(chi2(Efficiency,fit_exp(z,x_test2))/len(z[0]))
plt.scatter(Energy,Efficiency,s=0.001)
plt.errorbar(Energy,Efficiency, yerr = Efficiency_error,fmt=".",capsize= 3)
plt.plot(Energy_test, fit_exp(z,x_test))

plt.xlabel("Energy(keV)")
plt.ylabel("Efficiency(percentage)")
plt.title("Efficiency Calibration for SeGA")

plt.show()



