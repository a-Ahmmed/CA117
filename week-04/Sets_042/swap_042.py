def swap_keys_values(dt):
    dtnew = {dt[key] : key for key in dt}
    return dtnew