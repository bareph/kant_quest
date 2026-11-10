# 상품 클래스
class Product:
    ## 카운트 변수 만들기
    product_id = 0
    ## init 만들기(name, price, qty)
    def __init__(self, name, price, qty):
        Product.product_id += 1
        self.id = Product.product_id
        self.name = name
        self.price = price
        self.qty = qty

# 장바구니 클래스
class Cart:
    def __init__(self):
        self.items = {}
    ## 장바구니 여부 확인
    def count_of(self, product):
        if product.id in self.items:
            return self.items[product.id][1]
        return 0
    ## 장바구니 더하기
    def add(self, product, count):
        if product.id in self.items:
            self.items[product.id][1] += count
        else:
            self.items[product.id] = [product, count]

    ## 장바구니 빼기
    def remove(self, product_id):
        if product_id not in self.items:
            return False
        self.items[product_id][1] -= self.count
        if self.items[product_id][1] <= 0:
            del self.items[product_id]
        return True

    ## 장바구니 초기화
    def clear(self):
        self.items = {}

    ## 빈 장바구니 확인
    def empty(self):
        return len(self.items) == 0
    
    ## -- 결제 -------------------------------------
    ### 장바구니 합계
    def subtotal(self):
        total = 0
        for product, count in self.items.values():
            total += product.price * count
        return total

    def shipping(self):
        if self.empty():
            return 0
        if self.subtotal() >= 30000:
            return 0

        return 3000

    def total(self):
        return self.subtotal() + self.shipping()

    def print_summary(self):
        print('-' * 40)
        for product, count in self.items.values():
            line = product.price * count
            print(f'{product.name} x {count} {line:>10,}원')
        print('-' * 40)
        print(f'상품 합계 {self.subtotal():,}원')
        print(f'배송비 {self.shipping():,}원')
        print(f'결제 금액 {self.total():,}원')
        print('-' * 40)


# 쇼핑몰 클래스
class Shop:
    def __init__(self):
        self.products = [
            Product("무선 이어폰", 89000, 3),
            Product("텀블러", 15000, 10),
            Product("보조배터리", 32000, 5),
            Product("마우스패드", 9000, 0),
            Product("USB 허브", 18000, 4),
        ]
        self.cart = Cart()
    ## 입력
    def input_number(self, message):
        # ========숫자가 아니면 None을 돌려준다.=============
        text = input(message)
        if text.isdigit():
            return int(text)
        print('숫자를 입력해 주세요.')
        return None

    def find_product(self, product_id):
            for product in self.products:
                if product.id == product_id:
                    return product
            return None

    def show_products(self):
        for p in self.products:
            if p.qty == 0:
                qty_text = '품절'
            else :
                qty_text = f'재고 {p.qty}개'
            print(f'{p.id}. {p.name} {p.price:,}원 ({qty_text})')


    def add_to_cart(self):
        pid = self.input_number('상품 번호: ')
        if pid is None:
            return
        product = self.find_product(pid)
        if product is None:
            print('없는 상품입니다.')
            return
        if product.qty == 0:
            print('품절된 상품입니다.')
            return

        count = self.input_number('수량: ')
        if count is None:
            return
        if count < 1:
            print('수량은 1개 이상이여야 합니다.')
            return

        available = product.qty - self.cart.count_of(product)
        if count > available:
            print(f'재고가 부족합니다. (담을 수 있는 수량: {available})개.')
            return

        self.cart.add(product, count)
        print(f'{product.name} {count}개를 답았습니다.')

    def remove_from_cart(self):
        pass

    def show_cart(self):
        pass

    def checkout(self):
        pass

    def run(self):
        while True:
            print('-' * 46)
            print('1. 상품 목록, 2. 담기, 3. 빼기, 4. 장바구니, 5. 쿠폰, 6. 결제, q. 종료')
            print('-' * 46)
            choice = input('선택: ').strip()

            if choice == '1':
                self.show_products()
            elif choice == '2':
                self.add_to_cart()
            elif choice == '3':
                self.remove_from_cart()
            elif choice == '4':
                self.show_cart()
            elif choice == '5':
                print('서비스 준비 중입니다.')
            elif choice == '6':
                self.checkout()
            elif choice == 'q':
                print('프로그램을 종료합니다.')
                break
            else :
                print('잘못된 입력입니다.')
            print()

def main():
    shop = Shop()
    shop.run()

main()