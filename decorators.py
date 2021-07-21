
def decorator(func):
    def decorated(input_text):
        print('함수 시작')
        func(input_text)
        print('함수 끝')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)


hello_world('Hello World!')

def check_integer(func):
    def decoratored(input_h, input_v):
        if input_h > 0 and input_v > 0 :
            func(input_h, input_v)
        else :
            raise valueError('Input must be positive value')
    return decoratored

@check_integer
def rect_area(input_h, input_v):
    return input_h * input_v

@check_integer
def tri_area(input_h, input_v):
    return 1/2 * input_h * input_v
rect_area(3,4)
tri_area(3,4)