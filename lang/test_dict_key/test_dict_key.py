from lang.test_dict_key.ClassEnum import ClassEnum

VAR_FOR_KEY = 'test'

dict2 = dict(x=3)

if __name__ == "__main__":
    print({VAR_FOR_KEY: 'value'})
    print({ClassEnum.VAR_FOR_KEY: 'value'})
    print({ClassEnum.VAR_FOR_KEY2: 'value'})
    print({ClassEnum.VAR_FOR_KEY.value: 'value'})
