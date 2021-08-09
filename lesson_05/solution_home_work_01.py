def three_args(arg_1=None, arg_2=None, arg_3=None):
    if arg_1:
        print('var1=', arg_1)
    if arg_2:
        print('var2=', arg_2)
    if arg_3:
        print('var3=', arg_3)


three_args(arg_3=10, arg_1=2)
