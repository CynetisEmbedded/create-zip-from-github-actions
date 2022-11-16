import shutil
import yaml

zip_version = 0

with open('info.yaml','r') as yaml_file:
    data_from_yaml = yaml.safe_load(yaml_file)
    zip_version = data_from_yaml['version']

#zip_file_name = "src_v{}-{}".format(zip_version,'release')
zip_file_name = "code_release"

shutil.make_archive(zip_file_name, 'zip', 'src')
