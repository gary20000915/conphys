"""
In this script, we learn how to use zfill to generate N sequent data files.

2023.04.16

"""
import glob
from pathlib import Path


def create_data_files(N=10, header="data",digits=5,folder="data"):

    # check if the folder exists, if not create one
    Path(folder).mkdir(parents=True, exist_ok=True) 

    # loop all file names 
    for n in range(N):

        # the filename includes its relative path
        fname = folder+'/'+header+'_'+str(n).zfill(digits)+'.txt'
        f = open(fname, mode="w")
        f.close()

    return


def get_files_method1(folder="data"):

    # get files that match the pattern
    pattern = 'data_*[0,3,5][0-4].txt'
    fns = sorted(Path(folder).glob(pattern))
    print(fns)

    for fn in fns:
        f = open(fn,mode="r")
        line = f.readlines()
        f.close()
    return

def get_files_method2(folder="data"):

    pattern = folder+'/data_*[0,3,5][0-4].txt'
    fns = sorted(glob.glob(pattern))
    print(fns)

if __name__=='__main__':

    create_data_files(N=100, header="data", digits=5, folder="data")
    get_files_method1(folder="data")
    get_files_method2(folder="data")