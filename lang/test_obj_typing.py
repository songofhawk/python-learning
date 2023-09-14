import json

from objtyping import to_primitive


class TestCustom:
    s:str
    q:int


if __name__ == '__main__':
    obj = TestCustom()
    obj.s = 'class_name'
    obj.q = 18
    print(json.dumps(to_primitive(obj)))
