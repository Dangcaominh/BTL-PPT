import os
from pymep.realParser import eval

class function:
    # Hàm tạo
    def __init__(self, input=""):
        self.data = input
    # Nhập hàm
    def input(self):
        info = input("Nhap ham f(x)= ")
        self.data = info
    # Gọi hàm
    def __call__(self, input):
        return eval(self.data, input)
    
    #----------------------------------------------------------------------------------------------------------------------------
    # Phương pháp dây cung (Secant)
    # Tham số đầu vào
    # a, b là hai giá trị lặp ban đầu
    # eps là sai số cho trước, giá trị mặc định là 10^(-6)
    # N là số lần lặp tối đa, giá trị mặc định là 100
    # Độ phức tạp O(N)
    def Secant(self, a, b, eps = 0.000001, N = 100):
        x = min(a, b)
        y = max(a, b)
        for i in range(N):
            if abs(x - y) <= eps:
                return (x + y)/2
            elif self(y) != self(x):
                z = y - (self(y)*(y - x))/(self(y) - self(x))
                x = y
                y = z
            elif self(x) == 0:  
                # self(x) = self(y) = 0
                return x
            else:
                # self(x) = self(y) != 0
                print("Runtime Error: This method doesn't converge to the desired zero. Let's try to modify two initial values.") 
                return '?'
        return (x + y)/2
    
    #----------------------------------------------------------------------------------------------------------------------------
    # Phương pháp False Position
    # Tham số đầu vào
    # a, b là hai giá trị lặp ban đầu
    # eps là sai số cho trước, giá trị mặc định là 10^(-6)
    # N là số lần lặp tối đa, giá trị mặc định là 100
    # Độ phức tạp O(N)
    def FalsiMethod(self, a, b, eps = 0.000001, N = 100):
        x = min(a, b)
        y = max(a, b)
        if self(x)*self(y) > 0:
            print("Runtime Error: f(x) and f(y) must have opposite signs")
            return '?'
        else:
            for i in range(N):
                if abs(x - y) <= eps:
                    return (x + y)/2
                elif self(y) != self(x):
                    z = (x*self(y) - y*self(x))/(self(y) - self(x))
                    if self(z)*self(y) <= 0:
                        x = min(y, z)
                        y = max(y, z)
                    else: 
                    # self(z)*self(x) <= 0
                        y = max(x, z)
                        x = min(x, z)
                elif self(x) == 0:
                    # self(x) = self(y) = 0
                    return x
            if abs(self(x)) >= abs(self(y)):
                return y
            else:
                return x
    
    #----------------------------------------------------------------------------------------------------------------------------
    # Phương pháp Steffensen (Modified Newton Method)
    # Tham số đầu vào
    # x là giá trị lặp ban đầu
    # eps là sai số cho trước, giá trị mặc định là 10^(-6)
    # N là số lần lặp tối đa, giá trị mặc định là 100
    # Độ phức tạp O(N)
    def Steffensen(self, x, eps = 0.000001, N = 100):
        for i in range(N):
            y = self(x)
            z = self(y)
            if z - 2*y + x != 0:
                p = x - ((y - x)**2 / (z - 2*y + x))
                if abs(x - p) <= eps:
                    return p
                else:
                    x = p
            elif y == x:
                return x
            elif z == y:
                return y
            else:
                print("Runtime Error: This method doesn't converge to the desired zero. Let's try to modify the initial value.") 
                return '?'

#================================================================================================================================
#=======================================================  MAIN CODE  ============================================================
#================================================================================================================================

# Tạo biến f có kiểu là function (class)
f = function()

# Nhập hàm f
f.input()

while 1:
    # Clear terminal
    os.system('cls')

    print("Các tác vụ")
    print("1. Nhập lại hàm f(x)")
    print("2. Tính giá trị của hàm ")
    print("3. Tìm nghiệm f(x) = 0 bằng Secant Method")
    print("4. Tìm nghiệm f(x) = 0 bằng False Position Method")
    print("5. Tìm nghiệm f(x) = x bằng Modified Newton Method")
    print("0. Kết thúc")
    option = int(input("Chọn tác vụ: "))
    if option == 0:
        break
    elif option == 1:
        f.input()
        os.system("pause")
    elif option == 2:
        x = input("Nhập giá trị x: ")
        print(f"f(x) = {f(x)}")
        os.system("pause")
    elif option == 3:
        a = float(input("Nhập giá trị a: "))
        b = float(input("Nhập giá trị b: "))
        eps = float(input("Nhập sai số: "))
        N = int(input("Nhập số lần lặp tối đa: "))
        print(f"Nghiệm của phương trình f(x) = 0 là x = {f.Secant(a, b, eps, N)}")
        os.system("pause")
    elif option == 4:
        a = float(input("Nhập giá trị a: "))
        b = float(input("Nhập giá trị b: "))
        eps = float(input("Nhập sai số: "))
        N = int(input("Nhập số lần lặp tối đa: "))
        print(f"Nghiệm của phương trình f(x) = 0 là x = {f.FalsiMethod(a, b, eps, N)}")
        os.system("pause")
    elif option == 5:
        x = float(input("Nhập giá trị x: "))
        eps = float(input("Nhập sai số: "))
        N = int(input("Nhập số lần lặp tối đa: "))
        print(f"Nghiệm của phương trình f(x) = x là x = {f.Steffensen(x, eps, N)}")
        os.system("pause")

