from django.http import HttpResponse
from django.shortcuts import render
from .models import ZipcodeInfo, Buyers, CreditCards, Categories, ProductListings, Sellers
import csv

def practice(request):
    with open('Sellers.csv','r',encoding='utf-8') as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
            for row in data_reader:
                        Sellers.objects.create(
email = row[0],
routing_number = row[1],
account_number = row[2],
balance = row[3]
)
    return HttpResponse("Successful!")

def index(request):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

def checkinginfo(request, email):
    buyers = Buyers.objects.filter(email=email)
    creditcards = CreditCards.objects.filter(owner_email=email)
    context = {'buyers': buyers, 'creditcards':creditcards}
    return render(request, 'checkinginfo.html', context)




alist = {}
def category(request):
    products = ProductListings.objects.all()
    for product in products:
        if product.product_name not in alist:
            alist[product.product_name] = [product.seller_email]

        elif product.product_name in alist and product.seller_email not in alist[product.product_name]:
            #else:
            alist[product.product_name].append(product.seller_email)

    context = {'alist':alist}
    return render(request, 'category.html', context)



def product_detail(request, product_name):
    products = ProductListings.objects.all().filter(product_name=product_name)
    sellers = Sellers.objects.all()
    context = {'products':products, 'sellers':sellers}
    return render(request, 'product_detail.html', context)
