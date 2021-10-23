from oops2.product_1 import *
from oops2.customer_1 import *
from oops2.Address_1 import *
def create():
    pid=int(input('Enter product id:'))
    pnm=input('Enter product name:')
    pp=float(input('Enter product price'))
    pqty=int(input('Enter product quantity:'))
    prod=product(pid,pnm,pp,pqty)
    print('--------------------------------------')
    cid=int(input('Enter customer id:'))
    cnm=input('Enter customer name:')
    cmob=int(input('Enter customer mobile no.:'))
    print('----------------------------------------')
    city=input('Enter city name:')
    state=input('Enter state name:')
    pincode=input('Enter pincode:')
    add=address(city,state,pincode)
    cust=customer(cid,cnm,cmob,prod,add)
    return cust

def display(cust):
    print('-----------CUSTOMER DETAILS-------------')
    print('Customer id',cust.custid)
    print('Customer name',cust.cname)
    print('Customer mobile no:',cust.mobno)
    print('-------------ADDRESS DETAILS-------------')
    addr=cust.add
    print('City:',addr.ct)
    print('State:',addr.st)
    print('Pincode:',addr.pin)
    print('--------------PRODUCT DETAILS---------------')
    prod=cust.prod #call product obj. from customer class
    print('Product id:',cust.prod.id)
    print('Product name:',cust.prod.name)
    print('Product price:',cust.prod.price)
    print('Product quantity:',cust.prod.qty)
    tot=0
    tot=tot+cust.prod.price * cust.prod.qty
    cgst=tot*0.06
    sgst=tot * 0.06
    ft=tot+cgst+sgst
    print('Cgst:',cgst)
    print('sgst:',sgst)
    print('Total bill:', tot)
    print('Final bill:',ft)
