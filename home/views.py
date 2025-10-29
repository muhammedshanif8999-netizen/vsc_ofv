from django.shortcuts import render,redirect
from django.utils import timezone
from django.http import HttpResponse
from django.db.models import Case, When
from .models import *
from django.contrib.auth.models import User
from .forms import CostumerForm,SellerForm,ProductForm,ReviewForm

def dhomefn(request):
    request.session['user_id'] = False
    veg = Product.objects.filter(item_id=1).order_by('-id')[:5]
    fruit = Product.objects.filter(item__id=2).order_by('-id')[:5]
    reviews = Review.objects.all().order_by('-id')[:5]
    request.session['recent'] = []
    return render(request,'dhome.html',{"veg": veg, "fruit": fruit,'reviews': reviews})



def chomefn(request):
    veg = Product.objects.filter(item_id=1).order_by('-id')[:5]
    fruit = Product.objects.filter(item_id=2).order_by('-id')[:5]
    reviews = Review.objects.all().order_by('-id')[:5]
    r = request.session.get('recent', [])
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(r)])
    a = Product.objects.filter(id__in=r).order_by(preserved)
    return render(request, 'chome.html', {"veg": veg, "fruit": fruit, 'reviews': reviews, 'a': a})
    



def shomefn(request):
    return render(request,'shome.html')

def loginfn(request):
    return render(request,'login.html')



def cregisterfn(request):
        if request.method=='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('number')
            un = Costumer.objects.filter(username=username).first()
            e = Costumer.objects.filter(email=email).first()
            number = Costumer.objects.filter(number=phone).first()
            if un:
                crf = CostumerForm()
                return render(request,'cregister.html',{'er':"Username already taken",'crf':crf})
            elif e:
                crf = CostumerForm()
                return render(request,'cregister.html',{'er':"Email already taken",'crf':crf})
            elif number:
                crf = CostumerForm()
                return render(request,'cregister.html',{'er':"Phone number already taken",'crf':crf})
            else:
                crf = CostumerForm(request.POST,request.FILES)
                if crf.is_valid():
                    crf.save()
                    return render(request,'login.html',{'m': 'Registration successful. Please log in.'})
        else:
            crf = CostumerForm()
            return render(request,'cregister.html',{'crf':crf})

def sregisterfn(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        un = Seller.objects.filter(username=username).first()
        e = Seller.objects.filter(email=email).first()
        number = Seller.objects.filter(number=phone).first()
        if un:
            srf = SellerForm()
            return render(request,'sregister.html',{'er':"Username already taken",'srf':srf})
        elif e:
            srf = SellerForm()
            return render(request,'sregister.html',{'er':"Email already taken",'srf':srf})
        elif number:
            srf = SellerForm()
            return render(request,'sregister.html',{'er':"Phone number already taken",'srf':srf})
        else:
            srf = SellerForm(request.POST,request.FILES)
            if srf.is_valid():
                srf.save()
                return render(request,'login.html',{'m': 'Registration successful. Please log in.'})
    else:
        srf = SellerForm()
        return render(request,'sregister.html',{'srf':srf})



def cloginfn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        c = Costumer.objects.filter(username=username, password=password).first()
        if c:
            request.session['user_id'] = c.id
            return redirect('/chome/')
        else:
            return render(request, 'login.html', {'er': 'Invalid username or password'})
    else:
        return render(request,'login.html')

def sloginfn(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        s = Seller.objects.filter(username=username, password=password).first()
        if s:
            request.session['user_id'] = s.id
            return redirect('/shome/')
        else:
            return render(request, 'login.html', {'er': 'Invalid username or password'})
    else:
        return render(request,'login.html')



def cvegfn(request):
    veg = Product.objects.filter(item__id=1).order_by('-id')
    return render(request,'cveg.html',{"veg": veg})

def svegfn(request):
    try:
        user_id = request.session.get('user_id')
        veg = Product.objects.filter(seller__id=user_id , item__id=1).order_by('-id')
        return render(request,'sveg.html',{"veg":veg})
    except:
        return redirect('/login/')


def cfruitfn(request):
    fruit = Product.objects.filter(item__id=2).order_by('-id')
    return render(request,'cfruit.html',{"fruit": fruit})

def sfruitfn(request):
    user_id = request.session.get('user_id')
    fruit = Product.objects.filter(item__id=2 , seller__id=user_id).order_by('-id')
    return render(request,'sfruit.html',{"fruit":fruit})


def cprofilefn(request):
    try:
        user_id = request.session.get('user_id')
        cp = Costumer.objects.get(id=user_id)
        return render(request,'cprofile.html',{'cp':cp})
    except:
        return redirect('/login/')

def sprofilefn(request):
    try:
        user_id = request.session.get('user_id')
        sp = Seller.objects.get(id=user_id)
        return render(request,'sprofile.html',{'sp':sp})
    except:
        return redirect('/login/')


def cpefn(request):
    try:
        user_id = request.session.get('user_id')
        cp = CostumerForm(instance=Costumer.objects.get(id=user_id))
        if request.method == 'POST':
            cp = CostumerForm(request.POST, request.FILES, instance=Costumer.objects.get(id=user_id))
            if cp.is_valid():
                cp.save()
                return redirect('/cprofile/')
        return render(request,'cpe.html',{'cp':cp})
    except:
        return redirect('/login/')

    


def spefn(request):
    try:
        user_id = request.session.get('user_id')
        sp = SellerForm(instance=Seller.objects.get(id=user_id))
        if request.method == 'POST':
            sp = SellerForm(request.POST, request.FILES, instance=Seller.objects.get(id=user_id))
            if sp.is_valid():
                sp.save()
                return redirect('/sprofile/')
        return render(request,'spe.html',{'sp':sp})
    except:
        return redirect('/login/')





def saddfn(request):
    try:
        if request.method == 'POST':
            user_id = request.session.get('user_id')
            spf = ProductForm(request.POST, request.FILES)
            if spf.is_valid():
                product = spf.save(commit=False)
                org_price = product.org_price
                selling_price = product.selling_price
                if org_price > 0:
                    product.discount = round(((org_price - selling_price) / org_price) * 100, 2)
                else:
                    product.discount = 0
                product.seller = Seller.objects.get(id=user_id)
                product.save()
                return redirect('/sadd/')
            else:
                return redirect('/sadd/')
        else:
            spf = ProductForm()
            return render(request, 'sadd.html', {'spf': spf})
    except:
        return redirect('/login/')






def cviewfn(request, n_id):
    p = Product.objects.get(id=n_id)
    reviews = Review.objects.filter(product=p).order_by('-id')
    r = request.session.get('recent', [])
    if n_id in r:
        r.remove(n_id)
    r.insert(0, n_id)
    request.session['recent'] = r[:5]
    return render(request, 'cview.html', {'p': p, 'reviews': reviews})





def cartfn(request, p_id):
    
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        quantity = request.GET['quantity']
        product = Product.objects.get(id=p_id)
        amount = product.selling_price * int(quantity)
        points = int(amount) // 5
        product.stock = product.stock - int(quantity)
        product.save()
        if Cart.objects.filter(costumer=costumer, product=product).exists():
            c = Cart.objects.get(costumer=costumer, product=product)
            c.quantity = c.quantity + int(quantity)
            c.amount = c.amount+amount
            c.points = c.points + points
            c.save()
            return redirect('/viewcart/')
        else:
            c = Cart.objects.create(costumer=costumer, product=product, quantity=quantity, amount=amount, points=points)
            return redirect('/viewcart/')



def viewcartfn(request):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        p = Cart.objects.filter(costumer=user_id)
        tottal_amount = 0
        for item in p:
            tottal_amount += item.product.selling_price * item.quantity
        points = int(tottal_amount) // 5
        return render(request, 'ccart.html', {'p': p, 'tottal_amount': tottal_amount, 'points': points})
    except:
        return redirect('/login/')


def qeditfn(request, p_id):
    c = Cart.objects.get(id=p_id)
    old_quantity = int(c.quantity)
    new_quantity = int(request.GET['quantity'])
    c.quantity = new_quantity
    c.amount = new_quantity * c.product.selling_price
    c.points = int(c.amount) // 5
    c.save()
    product = Product.objects.get(id=c.product.id)
    if new_quantity > old_quantity:
        product.stock -= (new_quantity - old_quantity)
    elif new_quantity < old_quantity:
        product.stock += (old_quantity - new_quantity)
    product.save()
    return redirect('/viewcart/')


def cart_deletefn(request, p_id):
    c = Cart.objects.get(id=p_id)
    product = c.product
    product.stock += c.quantity
    product.save()
    c.delete()
    return redirect('/viewcart/')


def c_ordersfn(request, t_id, p_id):
    t_id = float(t_id)
    p_id = int(p_id)
    user_id = request.session.get('user_id')
    costumer = Costumer.objects.get(id=user_id)
    f = Orders.objects.filter(costumer=user_id).last()
    try:
        n = f.n + 1
    except:
        n = 1
    total_points = 0
    payment_method = request.POST.get('payment_method')
    if not payment_method:
        payment_method = "No payment"
    cart_items = Cart.objects.filter(costumer=user_id)
    for item in cart_items:
        total_points += item.points
        Order.objects.create(
            costumer=costumer,
            amount=item.amount,
            product=item.product,
            quantity=item.quantity,
            order_date=timezone.now(),
            seller=item.product.seller,
            status='Pending',
            n=n,
            points=item.points,
        )
        item.delete()
    costumer.points = int(p_id) + total_points
    costumer.save()
    Orders.objects.create(
        costumer=costumer,
        order_date=timezone.now(),
        amount=t_id,
        n=n,
        points=total_points,
        payment_method=payment_method,
    )
    return redirect('/c_orderlist/')



def c_orderlistfn(request):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        p = Orders.objects.filter(costumer=user_id).order_by('-order_date')
        return render(request, 'c_orders.html', {'p': p})
    except:
        return redirect('/login/')
    
def c_orderviewfn(request,p_id):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        p = Order.objects.filter(costumer=user_id,n = p_id)
        os = Orders.objects.get(costumer=user_id,n = p_id)
        return render(request, 'c_order_view.html', {'p': p,'os':os})
    except:
        return redirect('/login/')
    


def s_product_viewfn(request,p_id):
    p = Product.objects.get(id=p_id)
    reviews = Review.objects.filter(product=p).order_by('-id')
    return render(request,'s_product_view.html',{'p':p, 'reviews': reviews})

def product_deletefn(request,p_id):
    p = Product.objects.filter(id=p_id)
    p.delete()
    return redirect('/shome/')

def product_editfn(request, p_id):
    user_id = request.session.get('user_id')
    seller = Seller.objects.get(id=user_id)
    product = Product.objects.get(id=p_id)

    if request.method == 'POST':
        pf = ProductForm(request.POST, request.FILES, instance=product)
        if pf.is_valid():
            product = pf.save(commit=False)
            org_price = product.org_price
            selling_price = product.selling_price

            if org_price > 0:
                product.discount = round(((org_price - selling_price) / org_price) * 100, 2)
            else:
                product.discount = 0

            product.seller = seller
            product.save()
            return redirect('/shome/')
    else:
        pf = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'pf': pf, 'p': product})

def s_ordersfn(request):
    try:
        user_id = request.session.get('user_id')
        seller = Seller.objects.get(id=user_id)
        p = Order.objects.filter(seller=seller).order_by('-order_date')
        return render(request, 's_orders.html', {'p': p})
    except:
        return redirect('/login/')



def s_orderviewfn(request,p_id):
    p = Order.objects.get(id = p_id)
    return render(request, 's_order_view.html', {'p': p})


def status_editfn(request, p_id):
    if request.method == 'POST':
        o = Order.objects.get(id=p_id)
        status = request.POST.get('status')
        if status:
            o.status = status
            o.save()
        return redirect('/s_orders/')
    else:
        return redirect('/s_orders/')


def paymentfn(request, t_id):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        point = costumer.points
        if request.method == 'POST':
            amount = request.POST.get('amount')
            return render(request, 'payment_success.html', {'amount': amount})
        else:
            return render(request, 'payment.html',{'amount': t_id, 'point': point})
    except:
        return redirect('/login/')



def reviewfn(request, p_id):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        product = Product.objects.get(id=p_id)

        if request.method == 'POST':
            rf = ReviewForm(request.POST, request.FILES)
            if rf.is_valid():
                review = rf.save(commit=False)
                review.product = product
                review.costumer = costumer
                review.save()
                product.rating = Review.objects.filter(product=product).aggregate(models.Avg('rating'))['rating__avg']
                product.save()
                return redirect('/chome/')
        else:
            rf = ReviewForm()

        return render(request, 'review.html', {'rf': rf, 'product': product})
    except:
        return redirect('/login/')


def pointfn(request, amount, points):
    try:
        user_id = request.session.get('user_id')
        costumer = Costumer.objects.get(id=user_id)
        amount = float(amount)
        points = int(points)
        if points > 0:
            point_amount = points // 10
            if point_amount > amount:
                point_amount = amount
            new_amount = amount - point_amount
            used_points = int(point_amount * 10)
            remaining_points = costumer.points - used_points
            if remaining_points < 0:
                remaining_points = 0
            costumer.points = remaining_points
            costumer.save()

            return render(request, 'payment.html', {
                'amount': new_amount,
                'point': remaining_points
            })

        else:
            return render(request, 'payment.html', {
                'amount': amount,
                'point': points
            })
    except:
        return redirect('/login/')

    