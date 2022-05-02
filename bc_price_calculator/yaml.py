import yaml


def yaml_loader(filepath):
    with open(filepath, "r") as fd:
        data = yaml.load(fd)
        return data


def yaml_dump(filepath, data):
    with open(filepath, "w") as fd:
        yaml.dump(data, fd)


with open("test.yaml", "r") as fd:
    data = yaml.load(fd, Loader=yaml.FullLoader)
    print(data)
