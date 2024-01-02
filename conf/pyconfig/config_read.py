import os
import yaml.constructor

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 配置目录
conf_module = os.path.join(base_path, "config")


class ConfigRead:
    def __init__(self, conf_module):
        assert os.path.exists(conf_module), 'conf_module路径不存在'
        self.conf_module = conf_module

    def get_config(self, file_name):
        file_path = os.path.join(self.conf_module, file_name)
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = f.read()
                data = yaml.safe_load(data)
                return data
            except Exception as e:
                pass
        return {}


configRead = ConfigRead(conf_module)
