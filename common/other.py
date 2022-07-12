import os
import yaml


def read_yaml_data(yaml_path):
    file_path = get_abs_path(project_name='web_test') + yaml_path
    try:
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            # print(data)
            return data
    except Exception as e:
        raise e


def get_abs_path(project_name):
    cur_path = os.path.abspath(os.path.dirname(__file__))

    # 获取myProject，也就是项目的根路径
    rootpath = cur_path[:cur_path.find(project_name + "\\") + len(project_name + "\\")]

    return rootpath


# getAbsPath(project_name='web_test')
# testDatas_01 = read_yaml_data(yaml_path='/datas/userdata.yaml')
