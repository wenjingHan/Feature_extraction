# coding:utf8

import os

opensmile_path = "./opensmile/bin/SMILExtract"
config_file_path = "./opensmile/config_file_238dimension/is13lld.conf"
emo_class = {'an':0, 'di':1, 'fe':2, 'ha':3, 'sa':4, 'su':5} # an: anger  di: disgust  fe: fear  ha:happy  sa:sad  su: surprise

def featureEx238(filepath, featurepath):
    num = 0
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if not file.endswith(".wav"):
                print("not audio file:", file)
                continue
            else:
                wavpath = os.path.join(root, file)
                instname = file.strip(".wav")
                classlabel = file.strip(".wav").split("_")[-2]
                print(instname, classlabel)
                new_featurepath = root.replace(filepath, featurepath)
                if not os.path.exists(new_featurepath):
                    os.makedirs(new_featurepath)
                commond = opensmile_path+" -I "+wavpath+" -C "+config_file_path+" -O "+\
                            os.path.join(new_featurepath, file.replace('.wav', '.csv'))+" -instname "+str(emo_class[classlabel])+" -headercsvlld 0"
                print(commond)
                os.system(commond)
                num += 1
    return num

if __name__ == "__main__":
    filepath = "./audio/eNTERFACE/"
    featurepath = "./features/238_eNTERFACE/"
    num = featureEx238(filepath, featurepath)
    print("num:",num)
    print("Feature Ex finished!!!")
