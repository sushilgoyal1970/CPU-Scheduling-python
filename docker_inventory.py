import os 
data=[]
data2=[]
b=os.system("docker inspect -f '{{.Name }}' $(docker ps -q)>docker_inventory")
with open("docker_inventory", "r") as f: 
    for each in f:
        data.append(each)
with open("docker_inventory", "w") as f:
    for i in data:
        f.write(i.rstrip("\n\r")+"   ansible_connection=docker\n")
