import stripe
from django.conf import settings
from django.shortcuts import render

def payment_view(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        token = request.POST.get('stripeToken')
        amount = 1000  # Amount in cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency='usd',
                source=token,
                description='Payment for products/services'
            )
            return render(request, 'payment/success.html')
        except stripe.error.CardError as e:
            error_message = e.error.message
            return render(request, 'payment/error.html', {'error_message': error_message})

    return render(request, 'payment/payment.html')

