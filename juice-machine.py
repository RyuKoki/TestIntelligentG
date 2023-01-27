# File: juice-machine.py

class JuiceMachine():

    def __init__(self):
        self.total_price    = 0
        self.total_cash     = 0
        self.coin_type = { "ten": 10, "five": 5, "two": 2, "one": 1 }

    def cashier(self, goods=""):
        # prices of each menu
        price_orange_juice  = 13
        price_apple_juice   = 15
        price_kiwi_juice    = 22
        # "1" instead of orange juice
        # "2" instead of apple juice
        # "3" instead of kiwi juice
        input_orders = goods.replace( " ", "" ).split( "," )
        # counting each menu
        amount_orange_juice = input_orders.count("1")
        amount_apple_juice  = input_orders.count("2")
        amount_kiwi_juice   = input_orders.count("3")
        # calculate the total price
        self.total_price = float( (amount_orange_juice*price_orange_juice)+(amount_apple_juice*price_apple_juice)+(amount_kiwi_juice*price_kiwi_juice) )
        return self.total_price

    def payment(self, coins=""):
        # "a" instead of 1 baht,    "b" instead of 2 baht
        # "c" instead of 5 baht,    "d" instead of 10 baht
        input_cash = coins.replace( " ", "" ).split( "," )
        # counting each coin type
        amount_one_coin     = input_cash.count("a")
        amount_two_coin     = input_cash.count("b")
        amount_five_coin    = input_cash.count("c")
        amount_ten_coin     = input_cash.count("d")
        # calculate the total cash payment
        self.total_cash = float( (amount_one_coin*self.coin_type['one'])+(amount_two_coin*self.coin_type["two"])+(amount_five_coin*self.coin_type["five"])+(amount_ten_coin*self.coin_type["ten"]) )
        return self.total_cash

    def change(self):
        cash_change = self.total_cash - self.total_price
        if ( cash_change < 0 ):
            # condition for customer miss the total cash
            return False
        elif ( cash_change == 0 ):
            return True
        else:
            total_change = {}
            changing = cash_change
            # minimum number of coin for changing
            for c in self.coin_type:
                if ( changing >= self.coin_type[c] ):
                    total_change[c] = int(changing) // self.coin_type[c]
                    changing = changing % self.coin_type[c]
            return [cash_change, total_change]

if __name__ == "__main__":
    juice_machine = JuiceMachine()
    # customer request orders
    orders = str( input("เลือกน้ำผลไม้ ([1]=น้ำส้ม, [2]=น้ำแอปเปิ้ล, [3]=น้ำกีวี่) >> ") )
    total_price = juice_machine.cashier(orders)
    print( "ยอดชำระเงิน: {:.2f} บาท".format(total_price) )
    # customer pay for goods
    cash = str( input("กรุณาชำระเงิน ([a]=1บาท, [b]=2บาท, [c]=5บาท, [d]=10บาท) >> ") )
    total_cash = juice_machine.payment(cash)
    print( "จำนวนเงิน: {:.2f} บาท".format(total_cash) )
    # condition for customer miss the total cash
    if not ( juice_machine.change() ):
        print("การชำระเงินไม่ถูกต้อง!!")
    elif ( juice_machine.change()==True ):
        print("ขอบคุณค่ะ")
    else:
        # print( juice_machine.change() )
        all_change = juice_machine.change()
        if ( len(all_change[1]) != 0 ):
            print("========เงินทอน========")
            for coin in all_change[1]:
                if ( coin == "ten" ):
                    print("เหรียญสิบบาท จำนวน\t{}\tเหรียญ".format(all_change[1][coin]))
                elif ( coin == "five" ):
                    print("เหรียญห้าบาท จำนวน\t{}\tเหรียญ".format(all_change[1][coin]))
                elif ( coin == "two" ):
                    print("เหรียญสองบาท จำนวน\t{}\tเหรียญ".format(all_change[1][coin]))
                else:
                    print("เหรียญบาท จำนวน\t{}\tเหรียญ".format(all_change[1][coin]))
            print("เงินทอนทั้งหมด\t{:.2f}\tบาท".format(all_change[0]))
            print("ขอบคุณค่ะ")
