import logging


logging.basicConfig(filename="test.log",level=logging.ERROR,
                    format="%(asctime)s:%(levelname)s:%(msecs)d:%(pathname)s:%(process)d:%(message)s")

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    try:
        result  = x / y
    except ZeroDivisionError:
        logging.error("not dvi. 0")
    else:
        return result


num1 = 20
num2 = 0

add_result = add(num1, num2)
logging.info("Add: {} + {} = {}".format(num1, num2, add_result))
sub_result = sub(num1, num2)
logging.info("Sub: {} - {} = {}".format(num1, num2, sub_result))
mul_result = mul(num1, num2)
logging.info("MUL: {} * {} = {}".format(num1, num2, mul_result))
div_result = div(num1, num2)
logging.info("Div: {} / {} = {}".format(num1, num2, div_result))
