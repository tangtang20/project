import yaml
import os

#读取yaml文件
def load_yaml(path):
    base=os.path.dirname(os.path.abspath(__file__))
    file=open(os.path.join(base,path),'r',encoding='utf-8')
    #print(file.read())
    data=yaml.load(file,Loader=yaml.FullLoader)
    return data


if __name__=='__main__':
    print(load_yaml('../data/user.yaml'))