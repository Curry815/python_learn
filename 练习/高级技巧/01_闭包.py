"""
闭包优点：
    无需定义全局变量即可实现通过函数，持续的访问、修改某个值
    闭包使用的变量的所用于在函数内，难以被错误的调用修改
缺点：
    由于内部函数持续引用外部函数的值，所以会导致这一部分内存空间不被释放，一直占用内存。
"""

def account_factory(init_acount=0):
    def atm(num, deposit=True):
        nonlocal init_acount
        if deposit:
            init_acount += num
            print(f"存款：+{num}元，账户余额：{init_acount}")
        else:
            init_acount -= num
            print(f"取款：-{num}元，账户余额：{init_acount}")
    return atm

fn = account_factory()
fn(300)
fn(200)
fn(100, False)