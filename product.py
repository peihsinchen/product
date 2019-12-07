products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入價格：')
    # p = []
    # p.append(name)
    # p.append(price)
    # 上方三行 等於 p = [name, price]
    # products.append(p) 這行+上行等於下行
    products.append([name, price])
print(products)