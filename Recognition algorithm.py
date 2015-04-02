import numpy as np          #import the libraries we need for our code

def Average(ip1,ip2):       # Define average function (Rember and update ip)
    op = (ip1 + ip2)/2
    return op

def difference(ip1,ip2):
    op = ip1 - ip2
    return op

def CalcEigen(ip):
    op = np.linalg.eig(Con)
    return op

def Covarience(ip1,ip2):
    op = np.dot(ip1,ip2)
    return op

x = ([0],[1],[5],[3])      # Matrix 1
y = ([5],[5],[4],[7])      # Matrix 2 
C =  [[0,0],[0,0],[0,0],[0,0]]
x = np.array(x)
y = np.array(y)

############ Main ###########
        
z = Average(x,y)            # Average image
D0 = difference(x,z)        # Differnce 1
D1 = difference(y,z)        # Differnce 2
D = [D0,D1]                 # Set of Difference matrices


#Create covarience matrix component A

for j in range(0,len(D)):        # Collumn iteration
    for i in range(0,len(D0)):   # Row iteration 
        C[i][j] = D[j][i][0]

C = np.array(C)
Ct = C.T                    #Transpose Matrix
Con = Covarience(C,Ct)      # Calculate Convarience matrix

# Obtain Eigenvalue of covarience matrix
E = CalcEigen(Con)

for i in range(0,4):        # Seperate out eigenvectors
    print(E[1][i])
    U = E[1][i]
print(U)

print("END")
