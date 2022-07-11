import os
import platform

import yaml


def GetPlatformInfo():
    if platform.system() == 'Windows':
        return 1
    elif platform.system() == 'Linux':
        return 2
    elif platform.system() == 'Darwin':
        return 3


def GetRootPath(project_name):
    """
        获取项目绝对路径 mac 和 windows 文件路径 斜杠有差异 需要调整以下代码获取正确的绝对路径
    """
    curPath = os.path.abspath(os.path.dirname(__file__))
    if GetPlatformInfo == 1:
        rootPath = curPath[:curPath.find(project_name + "\\") + len(project_name + "\\")]
    else:
        rootPath = curPath[:curPath.find(project_name + "/") + len(project_name + "/")]
    return rootPath


def read_yaml_data(yaml_path):
    if GetPlatformInfo != 1:
        yaml_path = str(yaml_path).replace("\\", '/')
    file_path = GetRootPath(project_name="") + yaml_path

    try:
        with open(file_path, encoding='UTF-8') as yaml_file:
            datas = yaml.safe_load(yaml_file)

        return datas
    except BaseException as e:
        raise e
        return {}


da = read_yaml_data('/datas/userdata.yaml')
print(da)
