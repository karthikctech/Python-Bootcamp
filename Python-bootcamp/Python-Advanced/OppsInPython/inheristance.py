# single inheristance

class father():
    f_name = "vijay"
    f_age = 51
class son(father):
    s_name = "secret"
    s_age = 25
obj = son()
print("father name is : ", obj.f_name)
print("son name is : ", obj.s_name)

# multilevel inheristance

class gfather():
    gf_name = "vijay"
    gf_age = 95
class father(gfather):
    f_name = "secret"
    f_age = 65
class son(father):
    s_name = "sivan swamy"
    s_age = 25
    
obj = son()
print("gfather name is : ", obj.gf_name)
print("father name is : ", obj.f_name)
print("son name is : ", obj.s_name)


# multiple inheritance



class gfather():
    gf_name = "vijay"
    gf_age = 95
class father(gfather):
    f_name = "secret"
    f_age = 65
class son(father):
    s_name = "sivan swamy"
    s_age = 25
    
obj = son()
print("gfather name is : ", obj.gf_name)
print("father name is : ", obj.f_name)
print("son name is : ", obj.s_name)





















