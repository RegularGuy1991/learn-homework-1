"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

sold = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def sum_of_sold(array):               # функция принимает массив и задаёт переменную sold_sum
    sold_sum = 0                      
    for sold_value in array:          # перебирает массив и плюсует значение к переменной sold_sum
        sold_sum += sold_value
    return sold_sum              # возвращает сумму (sold_sum)
    

for one_product in sold:                                                #цикл перебирает массив 
      product_sum = sum_of_sold(one_product['items_sold'])              #задаёт переменную и вклаывает значение по ключу "items-sold"
      print(f'Суммарное количество продаж {one_product["product"]}: {product_sum}') 
      
for one_product in sold:                                    
      product_sum = sum_of_sold(one_product['items_sold'])     
      print(f'Среднее количество продаж {one_product["product"]}: {product_sum / len(one_product["items_sold"])}') 

for one_product in sold:                                    
      product_sum += sum_of_sold(one_product['items_sold'])     
print(f'Общее количество продаж: {product_sum}') 

def avg_of_sold(array):               
    avg_sum = 0                      
    for avg_value in array:          
        avg_sum += 1
    return avg_sum
       
avg_sum = 0   

for one_avg_sum in sold:                                    
      avg_value = avg_of_sold(one_avg_sum['items_sold']) 
      avg_sum += avg_value

print(f'Общее среднее количество продаж: {product_sum / avg_sum}')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    
    main()
