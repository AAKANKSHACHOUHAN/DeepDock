def morgan_fingp(fname):
    nbits=1024
    radius=2
    #fp = []
    fsplit = fname.split('/')[-1]
    #to_skip = done_dict[fsplit]
    ref2  = open(fp+'/'+fn+'/'+fsplit,'a')
    #print(fname,to_skip)
    with open(fname,'r') as ref:
        ref.readline()
        #for count in range(to_skip):
        #    ref.readline()
        for line in ref:
            smile,zin_id = line.rstrip().split()
            arg = np.zeros((1,))
            try:
                DataStructs.ConvertToNumpyArray(AllChem.GetMorganFingerprintAsBitVect(Chem.MolFromSmiles(smile),radius,nBits=nbits),arg)

                ref2.write((',').join([zin_id]+[str(elem) for elem in np.where(arg==1)[0]]))
                ref2.write('\n')
            except:
                print(line)
                pass
