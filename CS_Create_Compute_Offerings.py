from cs import CloudStack
cs = CloudStack(endpoint='http://X.X.X.X:8080/client/api',key='',secret='')

### Here is you CPU and RAM Combination which you want to create, change accordingly ###
### In this script i want to create below combination of compute offering with storage tag and host tages.
#input_value={1:1, 2:4, 4:8, 6:12, 8:16}
input_value={2:4, 4:8 }
### Here Define you network rate  #####
network_speed=700
### Here Define your CPU speed in MHz
cpu_speed=2000
### Here Difine you Storage Tag, if not then you must remive the tag parameters in below defined fucntions
storage_tags="DHKTMVPCSAS"
### here to define the storage Tag, if not then you must remove hosttags value from below fuctions.
###host_tags="TEST"
#### here define you prefix of the name of compute offering.
#### In this example we are follow 'DH_EC_1C_2R'
compute_offerin_name="DH_KTM_VPC"

### here, defining you functions which will create compute offerings
def create_compute_offering(f_name, description, no_of_cpu, ram, ):
    result=cs.createServiceOffering(name=f_name, displaytext=description, tags=storage_tags, cpuNumber=no_of_cpu, cpuSpeed=cpu_speed, memory=ram, networkrate=network_speed, storageType='shared', provisioningType='thin', customized='false',  offerha='true', limitcpuuse='false', isvolatile='false')
    print(result)

#### here we are driving the value from above input_values and will call our function.
for i in input_value.keys():
    final_name=compute_offerin_name + '_' + str(i) + 'C' + '_' + str(input_value[i]) + 'R' + '_' + str(network_speed) + 'M'
    final_des=str(i) + 'vCore' + ' ' + str(input_value[i]) + 'GB' + 'RAM'
    no_of_cpu=str(i)
    ram=(input_value[i] * 1024)
    create_compute_offering(final_name, final_des, no_of_cpu, ram)
