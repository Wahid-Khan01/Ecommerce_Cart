from django.shortcuts import render
from django.http import HttpResponse
from.models import Product, Contact, Order, OrderUpdates,Service
from math import ceil
import json
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nslides = n//4 + ceil((n/4)-(n//4))
    # allprods = [[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    serv = Service.objects.all().order_by('-title')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    # print(catprods)
    for cat in cats:
        product = Product.objects.filter(category=cat)
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([product, range(1, nSlides), nSlides])
    params = {'allProds':allProds, 'serv':serv}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    thank=False
    if request.method=="POST":
        require_fields = ['name','email','phone','desc']
        if any(not request.POST.get(field) for field in require_fields):
            return render(request, 'shop/contact.html', {'error':True})
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank=True
    return render(request, 'shop/contact.html', {'thank':thank})


def tracker(request):
    if request.method == 'POST':
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order= Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdates.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time': item.timestamp})
                    response = json.dumps({'status':'success','updates':updates,'itemsJson': order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"Failed"}')
        except Exception as e:
            return HttpResponse('{"status":"Error"}')
    return render(request, 'shop/tracker.html')


def searchMatch(query, i):
    if query in i.desc.lower() or query in i.product_name.lower() or query in i.category.lower():
        return True
    else:
        return False
    
def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    # print(catprods)
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        product = [i for i in prodtemp if searchMatch(query, i)]
        n = len(product)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(product) != 0:
            allProds.append([product, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<3:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'shop/search.html', params)


def productView(request, myid):
    product = Product.objects.filter(id=myid).first()
    # print(product)
    # print(myid)
    return render(request, 'shop/prodView.html', {'product':product})


def checkout(request):
    if request.method == 'POST':
        required_fields = ['name', 'amount', 'email', 'address', 'city', 'state', 'zip_code', 'phone']
        if any(not request.POST.get(field) for field in required_fields):
            return render(request, 'shop/checkout.html', {'error': True})
        items_json =request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '') + ' ' + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json,name=name,email=email,city=city,state=state,zip_code=zip_code,phone=phone,address=address,amount=amount)
        order.save()
        update = OrderUpdates(order_id=order.order_id, update_desc= 'Your Order has been placed! Thankyou for Ordering with us!' )
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id':id})
    return render(request, 'shop/checkout.html')

def calculator(request):
    if request.method == 'POST':
        if request.POST.get('num1','num2') == "":
            return render(request, 'shop/calculator.html', {'error':True})
        c = 0
        n1 = eval(request.POST.get('num1', ''))
        n2 = eval(request.POST.get('num2', ''))
        opr = request.POST.get('opr', '')
    try:
        if opr == '+':
            c = n1+n2
        elif opr == '-':
            c = n1-n2
        if opr == '*':
            c = n1*n2
        if opr == '/':
            c = n1/n2
    except:
        c = 'Invalid Operation'

    return render(request, 'shop/calculator.html', {'c':c})

