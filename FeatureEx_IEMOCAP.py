# coding:utf8

import os

opensmile_path = "./opensmile/bin/SMILExtract"
config_file_path = "./opensmile/config_file_238dimension/is13lld.conf"
emo_class = {'ang': 0, 'hap': 1, 'exc': 1, 'neu': 2, 'sad': 3} # ang: anger     hap: happy      exc: excited        neu: neutral
cv_class = {'Ses01F':0, 'Ses01M':1, 'Ses02F':2, 'Ses02M':3, 'Ses03F':4, 'Ses03M':5, 'Ses04F':6, 'Ses04M':7, 'Ses05F':8, 'Ses05M':9}

def featureEx238(filepath, featurepath):
	num = 0
	for root, dirs, files in os.walk(filepath):
		for file in files:
			if '.wav' not in file:
				print("not audio file:", file)
				continue
			try:
				wavpath = os.path.join(root, file)
				instname = file.strip(".wav")
				classlabel = file.strip(".wav").split("_")[-1]
				if not os.path.exists(featurepath):
					os.makedirs(featurepath)
				print(instname, classlabel)
				commond = opensmile_path+ " -I "+ wavpath + " -C "+config_file_path+" -O "+\
							os.path.join(featurepath, file.replace('.wav', '.csv'))+' -instname '+str(emo_class[classlabel]) + ' -headercsvlld 0'
				print(commond)
				os.system(commond)
				filelistpath = os.path.join(featurepath, "CV0-10/")
				if not os.path.exists(filelistpath):
					os.makedirs(filelistpath)
				cv_txt = str(cv_class[ instname.split("_")[0] ]) + '.txt'
				with open(os.path.join(filelistpath, cv_txt), 'a+') as fin:
					fin.write("../."+os.path.join(featurepath, file.replace('.wav', '.csv'))+'\n')
				num += 1
			except BaseException as reason:
				print('featureExLLD error!' + str(reason))
				print('error!' + wavpath)
				continue
	return num

if __name__ == "__main__":
	filepath = "./audio/IEMOCAP/"
	featurepath = "./features/238_IEMOCAP/"
	num = featureEx238(filepath, featurepath)
	print("num:",num)
	print("Feature Ex finished!!!")
