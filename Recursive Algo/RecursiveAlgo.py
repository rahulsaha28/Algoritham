class Ob(object):
    def __init__(self):
        self.a = 0;


def multi(a, b):

    if b==1:
        return a;
    else:
        return a + multi(a,b-1);


def fact(a, c):

    print(str(c));
    if a == 0:
        return 1;
    else:
        return a * fact(a-1,c);

a = Ob();
# print(multi(2,300))
print(fact(5,a))

