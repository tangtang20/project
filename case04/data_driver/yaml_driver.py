import yaml

#读取yaml文件
def load_yaml(path):
    file=open(path,'r',encoding='utf-8')
    #print(file.read())
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data

#load_yaml('../data/user.yaml')