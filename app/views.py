from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Customer, Cart,OrderPlaced
from django.views import View
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import UserSignup, Customerform
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class Home(View):
    
    def get(self, request):
        phone = Product.objects.filter(category="M")
        laptop = Product.objects.filter(category="L")
        topwear = Product.objects.filter(category="TP")
        bottomwear = Product.objects.filter(category="BW")
        return render(request, 'app/home.html',
                      {"phone": phone, "laptop": laptop, "topwear": topwear, "bottomwear": bottomwear})


# def product_detail(request,id):
# # # #  return render(request, 'app/productdetail.html')
class Product_detail(View):
    def get(self, request, id):
        pr = Product.objects.get(id=id)
        itemexists=False
        itemexists=Cart.objects.filter(Q (product=pr.id) & Q(user=request.user)).exists()
        print(itemexists,'0000000000')
        return render(request, 'app/productdetail.html', {"pr": pr,'itemexists':itemexists})


# def add_to_cart(request,id):
class Add_to_cart(View):
 def get(self,request,id):
     if request.user.is_authenticated:
        user=request.user
        p=Product.objects.get(id=id)
        cart = Cart(user=user,product=p)
        cart.save()
        return HttpResponseRedirect('/showcart')
     else:
         return HttpResponseRedirect('/login')
    
class Delete_from_cart(View):
    def get(self,request):
        if request.user.is_authenticated :
            try:
                c=Cart.objects.get(pk=int(request.GET['id']))
                c.delete()
            except Exception as e:
                    print("error",e)
                    return HttpResponse('ok')
        else:
            return HttpResponseRedirect('/')
class CartProductQuantity(View):
    def get(self, request):
        if request.method == 'GET':
            pid = request.GET.get('id')
            action=request.GET.get('action')
            print(pid,'iiiiiiiddddddd')
            try:
                cart = Cart.objects.get(Q(product__id=int(pid))& Q(user=request.user))
                print(cart)
                crt = cart.quantity
                print(action)
                if action=='pluscart':
                    newcrt = crt + 1
                else:
                    newcrt=max(crt-1,1)
                cart.quantity=newcrt
                cart.save()

                
                amount=0.0
                samount=70
                tamount=0
                total=[p for p in Cart.objects.all() ]
                if total:
                    for p in total:
                        a=(p.quantity*p.product.discount_price)
                        print(a)
                        amount+=a
                tamount=amount +samount
                return JsonResponse({'new_quantity': newcrt,'amount':amount,'tamount':tamount})  # Return as JSON object
            except Cart.DoesNotExist:
                return HttpResponse("Cart not found")
            except Exception as e:
                print(e)
                return HttpResponse(e)        
def removecart(request):
    
    if request.user.is_authenticated:
        user=request.user
        
        
        
        cartid=request.GET.get('id')
        
        crt=get_object_or_404(Cart,id=cartid)
        crt.delete()
        cart=Cart.objects.filter(user=user)
        amount=0.0
        samount=70
        tamount=0
        if cart:
            for p in cart:
                a=(p.quantity*p.product.discount_price)
                print(a)
                amount+=a
            tamount=amount +samount
            print(tamount)
        return JsonResponse({
                "tamount":tamount, "amount":amount})    

def showcart(request):
 if request.user.is_authenticated:
    user=request.user
    
          
    cart=Cart.objects.filter(user=user)
    amount=0.0
    samount=70
    tamount=0
    total=[p for p in Cart.objects.all() if p.user==user]
  
    pquantity=len(cart)
    if cart:
        for p in cart:
           a=(p.quantity*p.product.discount_price)
           print(a)
           amount+=a
           tamount=amount +samount
        print(tamount)

    return render(request, 'app/addtocart.html',{'cart':cart,'tamount':tamount,'amount':amount})
 else:
     return HttpResponseRedirect('/login')


def deleteitem(request,id):
 cart=Cart.objects.get(id=id)
 print(cart)
 cart.delete()
 return render(request, 'app/addtocart.html',{'cart':cart})

def buy_now(request):
    return render(request, 'app/buynow.html')


class Profile(View):
    def get(self, request):
        form = Customerform()
        return render(request, 'app/profile.html', {'form': form, 'active': 'btn-primary'})

    def post(self, requset):
        form = Customerform(requset.POST)
        if form.is_valid():
            id = requset.user
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            locality = form.cleaned_data['locality']
            zipcode = form.cleaned_data['zipcode']
            dt = Customer(user=id, name=name, state=state, locality=locality, zipcode=zipcode, city=city)
            dt.save()
            form = Customerform()
        return render(requset, 'app/profile.html', {'form': form, 'active': 'btn-primary'})


def address(request):
    user=request.user
    form = Customer.objects.filter(user=user)
    return render(request, 'app/address.html', {'form': form, "active": "btn-primary"})


def orders(request):
    order=OrderPlaced.objects.filter(user=request.user)

    return render(request, 'app/orders.html',{'orders':order})


def change_password(request):
    return render(request, 'app/changepassword.html')


def mobile(request, data=None):
    phone = Product.objects.filter(category="M")
    if data == None:
        return render(request, 'app/mobile.html', {"phone": phone})
    elif data == "redmi" or data == "samsung":
        return render(request, 'app/mobile.html')


def laptop(request, data=None):
    laptop = Product.objects.filter(category="L")
    print(laptop)
    return render(request, 'app/laptop.html', {"laptop": laptop})


def topwear(request):
    laptop = Product.objects.filter(category="TP")
    return render(request, 'app/laptop.html', {"laptop": laptop})


def btwear(request, ):
    laptop = Product.objects.filter(category="BW")
    return render(request, 'app/laptop.html', {"laptop": laptop})


# [yt]

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class Customerregistration(View):
    def get(self, request):
        crform = UserSignup()
        return render(request, 'app/customerregistration.html', {"form": crform})

    def post(self, request):
        crform = UserSignup(request.POST)
        print("this si post ")
        if crform.is_valid():
            crform.save()
            messages.success(request, "your account has been created")


        else:
            print("this is invalid valuse")
        return render(request, 'app/customerregistration.html', {"form": crform})


def checkout(request):
    cust= Customer.objects.filter(user=request.user)  
    print(cust,'cust ')
    
    items=Cart.objects.filter(user=request.user)
    print(items,'item')
    amount=0
    samount=70
    tamount=0
    cart_prod=[p for p in Cart.objects.all() if p.user==request.user]
    if cart_prod:
        for p in cart_prod:
            a=(p.quantity*p.product.discount_price)
            amount+=a
        tamount=amount+samount
    return render(request, 'app/checkout.html',{'tamount':tamount,'cust':cust,'items':items})



def paymentdone(requset):
    user=requset.user
    custid=requset.GET.get('custid')
    cust=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=cust,product=c.product,quantity=c.quantity).save()
        c.delete()
    print(user,custid)
    return redirect('orders')