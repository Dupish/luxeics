
import os


import luxeics

import yaml
input_filename = "New"


with open( input_filename + '.yml', 'r' ) as stream:
               
            
            
            input_dict = yaml.load(stream, Loader=yaml.SafeLoader)
            

            directory	= input_dict['control']['folder']


path = f"{os.getcwd()}{os.sep}Photon_Density{os.sep}{directory}{os.sep}Yml_Files"







object = os.scandir(path)

for n in object :
    





        luxeics.main_program(  f'{path}{os.sep}{n.name}' )
        print(n.name)
object.close()






