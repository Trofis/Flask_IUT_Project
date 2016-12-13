import yaml, os.path

Albums=yaml.load(
    open(
        os.path.join(
            os.path.dirname(__file__),
            "albums.yml")))


def get_sample():
    return Albums[0:10]
