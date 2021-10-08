import os
import yaml
input_filename = "New"
with open( input_filename + '.yml', 'r' ) as stream:
               
            
            
            input_dict = yaml.load(stream, Loader=yaml.SafeLoader)
            

            directory	=input_dict['control']['folder']


parent_dir = f"{os. getcwd()}{os.sep}Photon_Density"
path1 = os.path.join(parent_dir, directory)
os.mkdir(path1)



print(f"Path = {path1}")



path = os.path.join(path1, "Yml_Files")
os.mkdir(path)




n = 1             # Number of times the parameters are changed
r = 1             #  Number of runs

'''

Energy= I0 * pi* (w0 **2)* T_fwhm
I0= (omega*m*a0)**2/(8*pi*alpha)

a0*w0= constant

'''

a0=0.1       
w0=5

constant = a0 * w0
Energy = 0
print(f"Energy:{Energy}")

print("Process Initiated")


for j in range(r):
    for i in range(n):
        with open( input_filename + '.yml', 'r' ) as stream:
               
            
            
            input_dict = yaml.load(stream, Loader=yaml.SafeLoader)
            sigma1= 5+i*5

            input_dict['beam']['sigmaT']=sigma1
            input_dict['control']['name']=f'{path1}{os.sep}H_Five{os.sep}SigmaT{sigma1}'
            input_dict['laser']['w0']=sigma1
            input_dict['laser']['a0']=constant/sigma1
            input_filename1 = f'SigmaT{sigma1}'
	    
	    



        with open(      f'{path}\SigmaT{sigma1}'+'.yml', 'w') as file:
            documents = yaml.dump(input_dict, file)

        

        


        
print ("!Files Ready!" )