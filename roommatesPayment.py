with open('check.txt','r') as check_list, open('product_list.txt','r') as product_list:
    total_cost = float(0.00)
    
    for checlist_line1 in check_list:                       #total balance
        check_row = checlist_line1.split(",")
        total_cost += float(check_row[1])
    print(f'Total spent: {total_cost} euro')

with open('check.txt','r') as check_list, open('product_list.txt','r') as product_list:
    balance_roommate = float(0.00)
    item_purchased = 0
    print(f'Item not purchased:')
    for productlist_line in product_list:
        product_row = productlist_line.split(",")
        check_list.seek(0)                                   #listenin en başına geri dönüyor
        for checklist_line in check_list:
            check_row1 = checklist_line.split(",")
            if product_row[0] == check_row1[0]:              #product and check equals
                if int(product_row[1]) > 0:                       #product count decreaser
                    balance_roommate += float(check_row1[1])
                    product_row[1] = int(product_row[1])
                    product_row[1] -= 1
                    item_purchased +=1
                else:
                    break
            if int(product_row[1]) == 0:                                 #item that are in product list and checklist with same amount
                break                                                   #productlist te olan ve tamamı alınmışlar için (gerektiği kadar alınmışlar için)
        if product_row[0] not in check_row1[0]:                         # item not purchased
            print(f'\t{int(product_row[1])} {product_row[0]}')
        else:
            if int(product_row[1])-item_purchased > 0:
               print(f'\t{int(product_row[1])-item_purchased} {product_row[0]}')
            else:
                continue
    print(f'Money from roommate: {round(balance_roommate,2)} euro')

