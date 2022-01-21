def check_group_is_int_instance(*args):
    result =  all(isinstance(x, int) for x in args)
    assert result == True, 'Class instance attributes must be integers'
