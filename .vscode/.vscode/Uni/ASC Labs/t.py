# #Membership functions
# import numpy as np 
# import skfuzzy as fuzz
# import matplotlib.pyplot as plt

# #define the universe
# x=np.arange(0,11,1)
# print(x)

# trap_mf=fuzz.trapmf(x,[2, 5, 8, 10])
# #plot the membership function
# plt.plot(x,trap_mf,label='Trapazoidal MF', color='b')
# plt.title('Trapazoidal Membership Function')
# plt.xlabel('x')
# plt.ylabel('Membership Degree')
# plt.legend()
# plt.grid()
# plt.show()

# #Triangular Membership Function
# import numpy as np 
# import skfuzzy as fuzz
# import matplotlib.pyplot as plt

# #define the universe
# x = np.arange(0, 11, 1)
# print(x)

# tri_mf = fuzz.trimf(x, [2, 5, 8])

# #plot the membership function
# plt.plot(x, tri_mf, label='Triangular MF', color='g')
# plt.title('Triangular Membership Function')
# plt.xlabel('x')
# plt.ylabel('Membership Degree')
# plt.legend()
# plt.grid()
# plt.show()

#both
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

#define the universe
x = np.arange(0, 11, 1)
print(x)

# define the trapezoidal membership function
trap_mf = fuzz.trapmf(x, [2, 5, 8, 10])

# define the triangular membership function
tri_mf = fuzz.trimf(x, [2, 5, 8])

# plot both membership functions
plt.plot(x, trap_mf, label='Trapezoidal MF', color='b')
plt.plot(x, tri_mf, label='Triangular MF', color='g')
plt.title('Membership Functions')
plt.xlabel('x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid()
plt.show()

