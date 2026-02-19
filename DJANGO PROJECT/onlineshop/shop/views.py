from django.shortcuts import render, redirect

# Dummy products (no database)
PRODUCTS = {
    1: {'name': 'Laptop', 'price': 50000},
    2: {'name': 'Mobile', 'price': 20000},
    3: {'name': 'Headphones', 'price': 2000},
}

# 1️⃣ Product Page
def products(request):
    return render(request, 'products.html', {'products': PRODUCTS})


# 2️⃣ Add to Cart (Session)
def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    
    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    return redirect('cart')


# 3️⃣ Cart Page
def cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for key, quantity in cart.items():
        product = PRODUCTS[int(key)]
        subtotal = product['price'] * quantity
        total += subtotal
        
        items.append({
            'name': product['name'],
            'price': product['price'],
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {'items': items, 'total': total})


# 4️⃣ Checkout Page
def checkout(request):
    request.session['cart'] = {}
    return render(request, 'success.html')
