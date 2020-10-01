'''
读写文件的类
'''
import configparser
import os

import yaml


class DataRead:
    def get_project_path(self):
        '''
        获取当前工程路径
        :return:
        '''
        current_file_path = os.path.realpath(__file__)  # E:\ApiAutoTest\JinRongZongHe\caw\DataRead.py
        dir_name = os.path.dirname(current_file_path)  # E:\ApiAutoTest\JinRongZongHe\caw\
        dir_name = os.path.dirname(dir_name)  # E:\ApiAutoTest\JinRongZongHe
        return dir_name + "\\"  # E:\ApiAutoTest\JinRongZongHe\

    def read_ini(self, file_path, key):
        '''
        读取ini文件，返回key对应的value
        :param file_path: 文件路径
        :param key: key
        :return: key对应的value
        '''
        real_file_path = self.get_project_path() + file_path
        config = configparser.ConfigParser()
        config.read(real_file_path)  # 读取ini配置文件
        value = config.get("env", key)  # 读取[env]里面的key
        return value

    def read_yaml(self, file_path):
        '''
        读取yaml文件
        :param file_path: yaml文件的路径，相对路径
        :return: yaml文件的内容
        '''
        real_file_path = self.get_project_path() + file_path
        with open(real_file_path, "r", encoding='utf-8') as f:
            file_content = f.read()
        # 用yaml的load方法把文本的文件内容转成字典的list
        content = yaml.load(file_content, Loader=yaml.FullLoader)
        return content


# 测试代码：用完可以删除。
if __name__ == '__main__':
    value = DataRead().read_ini(r"data_env\env.ini", "url")
    print(value)
    print(DataRead().get_project_path())

    print(DataRead().read_yaml(r"data_case\register_fail.yaml"))
