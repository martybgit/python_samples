def test_var_args(*argv):
    #print("first normal arg:", f_arg)

    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

def greet_me(**kwargs):
    if kwargs is not None:
        #print(arg1,arg2,arg3,arg4)
        for key, value in kwargs.items():
            print("%s == %s" %(key,value))

greet_me(arg1='yasoob',arg2='python',arg3='eggs',arg4='test')
#greet_me(**kwargs)

def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)