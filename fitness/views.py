from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from fitness.models import *
from backend.models import *
from django.contrib import messages
import  razorpay
from django.http import JsonResponse



# Create your views here.

def index_page(request):
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request, 'index.html',{'x':x})

def about_page(request):
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request, 'About.html',{x:'x'})

def class_page(request):
    work = Workout.objects.all()
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request,"Classes.html", {'work':work,x:'x'})

def video(request, vid):
    work = Workout.objects.get(id=vid)
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request, "Video.html", {'work':work,x:'x'})

def save_class(request):
    if request.method=="POST":
        nam=request.POST.get('name')
        ag = request.POST.get('age')
        eml = request.POST.get('email')
        crnt = request.POST.get('current')
        dsrd = request.POST.get('desired')
        hgt = request.POST.get('height')
        obj=ClassDB(Name=nam,Age=ag,Email=eml,Current_weight=crnt,Desired_weight=dsrd,Height=hgt)
        obj.save()
        return redirect(class_page)

def contact_page(request):
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request,"Contact.html",{x:'x'})
def save_contact(request):
    if request.method=="POST":
        namee=request.POST.get('name')
        emll = request.POST.get('email')
        msg = request.POST.get('message')
        obj=ContactDB(Name=namee,Email=emll,Message=msg)
        obj.save()
        return redirect(contact_page)

def diet_page(request):
    day = Days.objects.all()
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request,"Deit.html",{"day":day,x:'x'} )


def single_diet(request, day_id):
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    # Get the specific Day
    day = get_object_or_404(Days, pk=day_id)

    # Get the selected interval from the request, if any
    selected_interval_id = request.GET.get('interval')

    # Retrieve all intervals for the current day
    intervals = Interval.objects.all()

    # Filter the FoodItems based on the day and selected interval
    if selected_interval_id:
        diet = FoodItems.objects.filter(day=day, interval_id=selected_interval_id)
    else:
        # If no interval is selected, don't show any food items
        diet = []
    return render(request, 'single_diet.html', {'day': day, 'intervals': intervals, 'diet': diet,x:'x'})


def diet_detail(request,interval_id,):
    time = get_object_or_404(Interval, pk=interval_id)
    diet = FoodItems.objects.filter(interval=time)
    return render(request,"diet_detail.html",{'time':time,'diet':diet})


def sign_in(request):
    return render(request,"Login.html", )

def sign_up(request):
    return render(request,"Sign_up.html", )

def save_signup(request):
    if request.method=="POST":
        user =request.POST.get('username')
        pswd = request.POST.get('password')
        con_pass = request.POST.get('confirm')
        eml = request.POST.get('email')
        obj=SignupDB(User_name=user,Password=pswd,Confirm_password=con_pass,Email=eml)
        obj.save()
        return redirect(user_login)

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if SignupDB.objects.filter(User_name=un,Password=pswd).exists():
            request.session['User_name']=un
            request.session['Password']=pswd
            messages.success(request,"Welcome...!")
            return redirect(index_page)
        else:
            messages.warning(request,"")
            return redirect(sign_in)
    else:
        messages.warning(request, "")
        return redirect(sign_in)

def user_logout(request):
    del request.session['User_name']
    del request.session['Password']
    return redirect(sign_in)

def product(request):
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    product = ProductDB.objects.all()
    Supplements = ProductDB.objects.filter(Category="Supplements")
    Medications = ProductDB.objects.filter(Category="Medications")
    return render(request, "product.html", {'product':product,'Supplements': Supplements, 'Medications': Medications,x:'x'})

def single_product(request,item_id):
    product = get_object_or_404(ProductDB, id=item_id)
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    x = cart.count()
    return render(request,"single_product.html",{'product':product,x:'x'})

#
# def save_cart(request):
#     if request.method=="POST":
#         nam=request.POST.get('user')
#         pname = request.POST.get('pro_name')
#         quan = request.POST.get('quantity')
#         pri = request.POST.get('price')
#         tot_pri = request.POST.get('total')
#         try:
#             x = ProductDB.objects.get(Product_Name=pname)
#             img = x.Product_Image
#         except ProductDB.DoesNotExist:
#             img = None
#         obj=CartDB(UserName=nam,Product_Name=pname,Quantity=quan,Price=pri,TotalPrice=tot_pri,Product_Image=img)
#         obj.save()
#         return redirect(cart_page)
#
# def cart_page(request):
#     sub_total = 0
#     shipping_amount = 0
#     total_amount = 0
#     cart = CartDB.objects.filter(UserName=request.session['User_name'])
#     for i in cart:
#         sub_total += i.TotalPrice
#         if sub_total > 500:
#             shipping_amount = 50
#         else:
#             shipping_amount = 100
#         total_amount = sub_total + shipping_amount
#     return render(request,"cart.html",{'cart':cart,'sub_total':sub_total,'shipping_amount':shipping_amount,'total_amount':total_amount})

def delete_cart(request,c_id):
    category=CartDB.objects.filter(id=c_id)
    category.delete()
    return redirect(cart_page)

def checkout_cart(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    cart = CartDB.objects.filter(UserName=request.session['User_name'])
    for i in cart:
        sub_total += i.TotalPrice
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount
    return render(request, "Checkout.html", {'cart': cart, 'sub_total': sub_total, 'shipping_amount': shipping_amount,
                                         'total_amount': total_amount})

def save_checkout(request):
    if request.method=="POST":
        name=request.POST.get('name')
        plac = request.POST.get('place')
        phone = request.POST.get('phone')
        eml = request.POST.get('email')
        adrs = request.POST.get('address')
        pin = request.POST.get('pincode')
        msg = request.POST.get('message')
        tot = request.POST.get('ototal')
        obj=CheckoutDB(Name=name,Place=plac,Mobile=phone,Email=eml,Address=adrs,Pin_code=pin,Message=msg,TotalPrice=tot)
        obj.save()
        return redirect(payment)

# def payment(request):
#     customer = CheckoutDB.objects.order_by('-id').first()
#     payy = customer.TotalPrice
#     amount = int(payy*100)
#     payy_str=str(amount)
#     if request.method == 'POST':
#         order_currency = 'INR'
#         client = razorpay.Client(auth=('rzp_test_mJFX2vCAoYiHq6','6g0dI0uyVS01hifxfXKuktiA'))
#         payment = client.order.create({'amount':amount,'currency':order_currency})
#     return render(request,"Payment.html",{'customer':customer,'payy_str':payy_str})




def payment(request):
    customer = CheckoutDB.objects.order_by('-id').first()
    payy = customer.TotalPrice
    amount = int(payy * 100)
    payy_str = str(amount)

    if request.method == 'POST':
        order_currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_mJFX2vCAoYiHq6', '6g0dI0uyVS01hifxfXKuktiA'))

        payment = client.order.create({
            'amount': amount,
            'currency': order_currency,
        })


        return redirect('index_page')

    return render(request, "Payment.html", {'customer': customer, 'payy_str': payy_str})





# Custom login required decorator
def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("User_name"):
            return redirect('/User_Login/?next=' + request.path)
        return view_func(request, *args, **kwargs)
    return wrapper

@custom_login_required
def add_to_favorites(request, pro_id):
    product = get_object_or_404(ProductDB, id=pro_id)
    username = request.session.get("User_name")
    user = SignupDB.objects.filter(User_name=username).first()
    if not user:
        return redirect('user_login')

    FavoriteSong.objects.get_or_create(user=user, song=product)
    return redirect('favorites_view')

@custom_login_required
def remove_from_favorites(request, pro_id):
    product = get_object_or_404(ProductDB, id=pro_id)
    username = request.session.get("User_name")
    user = SignupDB.objects.filter(User_name=username).first()
    if not user:
        return redirect('user_login')

    FavoriteSong.objects.filter(user=user, song=product).delete()
    return redirect('favorites_view')

@custom_login_required
def favorites_view(request):  # ✅ Fixed here: removed item_id
    username = request.session.get("User_name")
    user = SignupDB.objects.filter(User_name=username).first()
    if not user:
        return redirect('user_login')

    favorites = FavoriteSong.objects.filter(user=user).select_related('song')
    return render(request, 'Wishlist.html', {'favorites': favorites})




def save_cart(request):
    if request.method == "POST":
        user_name = request.POST.get('user')
        product_name = request.POST.get('pro_name')
        quantity = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        total_price = float(request.POST.get('total'))

        # Check if the product already exists in the cart for the current user
        cart_item = CartDB.objects.filter(UserName=user_name, Product_Name=product_name).first()

        if cart_item:
            # Update quantity and total price if product already exists in the cart
            cart_item.Quantity += quantity
            cart_item.TotalPrice = cart_item.Quantity * price
            cart_item.save()
        else:
            # Add new item to the cart
            try:
                product = ProductDB.objects.get(Product_Name=product_name)
                product_image = product.Product_Image
            except ProductDB.DoesNotExist:
                product_image = None

            cart_item = CartDB(
                UserName=user_name,
                Product_Name=product_name,
                Quantity=quantity,
                Price=price,
                TotalPrice=total_price,
                Product_Image=product_image
            )
            cart_item.save()

        return redirect('cart_page')  # Redirect to cart page after saving


def cart_page(request):
    sub_total = 0
    shipping_amount = 0
    total_amount = 0
    cart = CartDB.objects.filter(UserName=request.session['User_name'])

    for item in cart:
        sub_total += item.TotalPrice
        if sub_total > 500:
            shipping_amount = 50
        else:
            shipping_amount = 100
        total_amount = sub_total + shipping_amount

    # Display messages if there are any
    messages.info(request, "Your cart has been cleared after successful payment.") if cart.count() == 0 else None

    return render(request, "cart.html", {
        'cart': cart,
        'sub_total': sub_total,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount
    })

