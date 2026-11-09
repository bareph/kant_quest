
class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.item_cart = []

    def add_item(self, item):
        self.item_cart.append(item)

    def show_item(self):
        return self.item_cart

cart = Cart()

item_a = Item('무선 이어폰', 89000, 3)
item_b = Item('텀블러', 15000, 10)
item_c = Item('보조배터리', 32000, 5)
item_d = Item('마우스패드', 9000, 0)
item_e = Item('USB 허브', 18000, 4)

cart.add_item(item_a)
cart.add_item(item_b)
cart.add_item(item_c)
cart.add_item(item_d)
cart.add_item(item_e)

def show_list():    
    for number, item in enumerate(cart.show_item(), start=1):
        if item.price == 0:
            print(f'{number}번 : {item.name} |  {item.price} 원 | (품절)')
        else :
            print(f'{number}번 : {item.name} |  {item.price} 원 | (재고 {item.qty} 개)')
    
# 실행 화면
def intro():
    print('-' * 50)
    print('1. 상품목록, 2. 담기, 3. 빼기, 4. 장바구니, 5. 쿠폰, 6. 결제, q. 종료')
    print('-' * 50)

def sellect_what():
    sellect_info = input('원하시는 버튼을 입력하세요\n1. 상품목록, 2. 담기, 3. 빼기, 4. 장바구니, 5. 쿠폰, 6. 결제, q. 종료\n')

def main():
    intro()
    sellect_what()

main()
