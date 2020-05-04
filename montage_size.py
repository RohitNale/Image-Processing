import numpy as np
# number of images in the folder
def montage_size(x):
    Num = []
    for i in range(1, x+1):
        if x% i == 0:
            Num.append(i)

    Diff = []
    for i in Num:
        for j in Num:
            if i*j==x:
                M = np.array([i,j,abs(i-j)])
                Diff.append(M)

    Diff = np.array(Diff)
    # select row with minimum difference between two numbers
    row = Diff[:,2].argmin()
    size = Diff[row,0:2]
    return (size[0], size[1])

if __name__ == '__main__':
    X = montage_size(10)
    print(X)
