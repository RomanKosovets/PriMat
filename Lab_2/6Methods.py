import numpy as np
import matplotlib.pyplot as plt


def right_hand_derivative(f, x_values, h):
    return [(f(x + h) - f(x)) / h for x in x_values]


def left_hand_derivative(f, x_values, h):
    return [(f(x) - f(x - h)) / h for x in x_values]


def central_difference(f, x_values, h):
    derivatives = []
    # Вычисляем производную в первой точке
    first_derivative = (-3 * f(x_values[0]) + (4 * f(x_values[1])) - f(x_values[2])) / (2 * h)
    derivatives.append(first_derivative)
    # Вычисляем производные в остальных точках
    for i in range(1, len(x_values) - 1):
        x = x_values[i]
        derivative = (f(x) - f(x - h)) / h
        derivatives.append(derivative)
    # Вычисляем производную в последней точке
    last_derivative = (f(x_values[-3]) - (4 * f(x_values[-2])) + (3 * f(x_values[-1]))) / (2 * h)
    derivatives.append(last_derivative)
    return derivatives


def func(x):
    return x ** 2


def func2(x):
    return np.sin(x) * x ** 3


def func_derivative(x):
    return 2 * x


def func2_derivative(x):
    return 3 * x ** 2 * np.sin(x) + x ** 3 * np.cos(x)


def standard_deviation(numerical_values, true_values):
    differences = numerical_values - true_values
    return np.sqrt((differences ** 2).mean())


h = 0.01
a = 0
b = 100
n = round((b - a) / h)
x_line = np.linspace(a, b, n)

func1_integration = (10 ** 6) / 3
func2_integration = 29994 * np.sin(100) - 999400 * np.cos(100)
print("Аналитическое значение первой функции:", func1_integration)
print("Аналитическое значение второй функции:", func2_integration)

h_values = [h / 2 ** i for i in range(5)]
sd_central_func1 = [standard_deviation(central_difference(func, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                       func_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]
sd_left_func1 = [standard_deviation(left_hand_derivative(func, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                    func_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]
sd_right_func1 = [standard_deviation(right_hand_derivative(func, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                     func_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]

fig, axs = plt.subplots(4, 2)
fig.set_figheight(12)
fig.set_figwidth(10)
fig.subplots_adjust(hspace=1)
fig.subplots_adjust(wspace=0.5)

axs[0][0].plot(x_line, func_derivative(x_line))  # аналитически
axs[1][0].plot(x_line, right_hand_derivative(func, x_line, h))  # правая разностная производная
axs[2][0].plot(x_line, left_hand_derivative(func, x_line, h))  # левая разностная производная
axs[3][0].plot(x_line, central_difference(func, x_line, h))  # центральная разностная производная
axs[0][1].plot(x_line, func(x_line))

axs[1][1].plot(h_values, sd_central_func1)  # зависимость ср.кв. центральная производная
axs[2][1].plot(h_values, sd_left_func1)  # зависимость ср.кв. левая производная
axs[3][1].plot(h_values, sd_right_func1)  # зависимость ср.кв. правая производная

axs[0][0].set_title("f(x)'=2x аналитическим путем")
axs[1][0].set_title("f(x)'=2x правая разностная производная")
axs[2][0].set_title("f(x)'=2x левая разностная производная")
axs[3][0].set_title("f(x)'=2x центральная разностная производная")
axs[0][1].set_title("f(x) = x^2")

axs[1][1].set_title("Ср.Кв. x^2 центральная разностная производная")
axs[2][1].set_title("Ср.Кв. x^2 левая разностная производная")
axs[3][1].set_title("Ср.Кв. x^2 правая разностная производная")

plt.show()

sd_central_func2 = [standard_deviation(central_difference(func2, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                       func2_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]
sd_left_func2 = [standard_deviation(left_hand_derivative(func2, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                    func2_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]
sd_right_func2 = [standard_deviation(right_hand_derivative(func2, np.linspace(a, b, round((b - a) / h_s)), h_s),
                                     func2_derivative(np.linspace(a, b, round((b - a) / h_s)))) for h_s in h_values]

fig2, axs2 = plt.subplots(4, 2)
fig2.set_figheight(12)
fig2.set_figwidth(10)
fig2.subplots_adjust(hspace=1)
fig2.subplots_adjust(wspace=0.5)

axs2[0][0].plot(x_line, func2_derivative(x_line))  # аналитически
axs2[1][0].plot(x_line, right_hand_derivative(func2, x_line, h))  # правая разностная производная
axs2[2][0].plot(x_line, left_hand_derivative(func2, x_line, h))  # левая разностная производная
axs2[3][0].plot(x_line, central_difference(func2, x_line, h))  # центральная разностная производная
axs2[0][1].plot(x_line, func2(x_line))

axs2[1][1].plot(h_values, sd_central_func1)  # зависимость ср.кв. центральная производная
axs2[2][1].plot(h_values, sd_left_func2)  # зависимость ср.кв. левая производная
axs2[3][1].plot(h_values, sd_right_func2)  # зависимость ср.кв. правая производная

axs2[0][0].set_title("f(x)'=3x^2*sin(x) + x^3*cos(x)\n аналитическим путем")
axs2[1][0].set_title("f(x)'=3x^2*sin(x) + x^3*cos(x)\n правая разностная производная")
axs2[2][0].set_title("f(x)'=3x^2*sin(x) + x^3*cos(x)\n левая разностная производная")
axs2[3][0].set_title("f(x)'=3x^2*sin(x) + x^3*cos(x)\n центральная разностная производная")
axs2[0][1].set_title("f(x) = sin(x)*x^3")

axs2[1][1].set_title("Ср.Кв. sin(x)*x^3 центральная разностная производная")
axs2[2][1].set_title("Ср.Кв. sin(x)*x^3 левая разностная производная")
axs2[3][1].set_title("Ср.Кв. sin(x)*x^3 правая разностная производная")

plt.show()

print("\nЗначения среднеквадратичного отклонения для производных:")
print(standard_deviation(right_hand_derivative(func, x_line, h), func_derivative(x_line)))  # ср. от. правая пр. func
print(standard_deviation(left_hand_derivative(func, x_line, h), func_derivative(x_line)))  # ср. от. левая пр. func
print(standard_deviation(central_difference(func, x_line, h), func_derivative(x_line)))  # ср. от. центральная пр. func
print(
    standard_deviation(right_hand_derivative(func2, x_line, h), func2_derivative(x_line)))  # ср. от. правая  пр. func2
print(standard_deviation(left_hand_derivative(func2, x_line, h), func2_derivative(x_line)))  # ср. от. левая  пр. func2
print(
    standard_deviation(central_difference(func2, x_line, h), func2_derivative(x_line)))  # ср. от. центральная пр. func2


def left_rectangles(f, start, end, step):
    step_num = round((end - start) / step)
    x = np.linspace(start, end, step_num)
    return sum([step * f(xi - step) for xi in x])


def right_rectangles(f, start, end, step):
    n = round((end - start) / step)
    x = np.linspace(start, end, n)
    return sum([step * f(xi) for xi in x])


def middle_rectangles(f, start, end, step):
    n = round((end - start) / step)
    x = np.linspace(start, end, n)
    return sum([step * f(xi - (step / 2)) for xi in x])


def trapezoidal(f, start, end, step):
    n = round((end - start) / step)
    x = np.linspace(start, end, n)
    return sum([(step / 2) * (f(xi) + f(xi - step)) for xi in x])


def simpson(f, start, end, step):
    n = round((end - start) / step)
    x = np.linspace(start, end, n)
    return sum([(step / 6) * (f(xi) + 4 * f(xi - step / 2) + f(xi - step)) for xi in x])


print("\nЗначения производных через методы для первой функции:")
print("Метод левых прямоугольников:", left_rectangles(func, a, b, h))
print("Метод правых прямоугольников:", right_rectangles(func, a, b, h))
print("Метод средних прямоугольников:", middle_rectangles(func, a, b, h))
print("Формула трапеций:", trapezoidal(func, a, b, h))
print("Формула Симпсона", simpson(func, a, b, h))

print("\nЗначения производных через методы для второй функции:")
print("Метод левых прямоугольников:", left_rectangles(func2, a, b, h))
print("Метод правых прямоугольников:", right_rectangles(func2, a, b, h))
print("Метод средних прямоугольников:", middle_rectangles(func2, a, b, h))
print("Формула трапеций:", trapezoidal(func2, a, b, h))
print("Формула Симпсона", simpson(func2, a, b, h))

sd_left_func = [standard_deviation(left_rectangles(func, a, b, h_step), func1_integration) for h_step in h_values]
sd_right_func = [standard_deviation(right_rectangles(func, a, b, h_step), func1_integration) for h_step in h_values]
sd_middle_func = [standard_deviation(middle_rectangles(func, a, b, h_step), func1_integration) for h_step in h_values]
sd_trapezoid_func = [standard_deviation(trapezoidal(func, a, b, h_step), func1_integration) for h_step in h_values]
sd_simpson_func = [standard_deviation(simpson(func, a, b, h_step), func1_integration) for h_step in h_values]

sd_left_func2 = [standard_deviation(left_rectangles(func2, a, b, h_step), func2_integration) for h_step in h_values]
sd_right_func2 = [standard_deviation(right_rectangles(func2, a, b, h_step), func2_integration) for h_step in h_values]
sd_middle_func2 = [standard_deviation(middle_rectangles(func2, a, b, h_step), func2_integration) for h_step in h_values]
sd_trapezoid_func2 = [standard_deviation(trapezoidal(func2, a, b, h_step), func2_integration) for h_step in h_values]
sd_simpson_func2 = [standard_deviation(simpson(func2, a, b, h_step), func2_integration) for h_step in h_values]

fig, axs = plt.subplots(5, 2)
fig.set_figheight(16)
fig.set_figwidth(12)
fig.subplots_adjust(hspace=0.5)

axs[0][0].plot(h_values, sd_left_func)
axs[1][0].plot(h_values, sd_right_func)
axs[2][0].plot(h_values, sd_middle_func)
axs[3][0].plot(h_values, sd_trapezoid_func)
axs[4][0].plot(h_values, sd_simpson_func)

axs[0][0].set_title("Ср.Кв. x^2 метод левых прямоугольников")
axs[1][0].set_title("Ср.Кв. x^2 метод правых прямоугольников")
axs[2][0].set_title("Ср.Кв. x^2 метод средних прямоугольников")
axs[3][0].set_title("Ср.Кв. x^2 метод трапеций")
axs[4][0].set_title("Ср.Кв. x^2 метод Симпсона")

axs[0][1].plot(h_values, sd_left_func2)
axs[1][1].plot(h_values, sd_right_func2)
axs[2][1].plot(h_values, sd_middle_func2)
axs[3][1].plot(h_values, sd_trapezoid_func2)
axs[4][1].plot(h_values, sd_simpson_func2)

axs[1][1].set_title(" Ср.Кв. sin(x)*x^3 метод правых прямоугольников")
axs[0][1].set_title(" Ср.Кв. sin(x)*x^3 метод левых прямоугольников")
axs[2][1].set_title(" Ср.Кв. sin(x)*x^3 метод средних прямоугольников")
axs[3][1].set_title(" Ср.Кв. sin(x)*x^3 метод трапеци")
axs[4][1].set_title(" Ср.Кв. sin(x)*x^3 метод Симпсона")

plt.show()
