import paypalrestsdk
import config 

def makePayment(url_data):

    paypalrestsdk.configure({
      'mode': 'sandbox',
      'client_id': config.paypal_client_id,
      'client_secret': config.paypal_client_secret
    })
    
    payment = paypalrestsdk.Payment({
      "intent": "sale",
      "payer": {
        "payment_method": "paypal" },
      "redirect_urls": {
        "return_url": "http://localhost:8000/finalize?" + url_data,
        "cancel_url": "http://localhost:8000/reading?" + url_data},
    
      "transactions": [ {
        "amount": {
          "total": "20",
          "currency": "USD" },
        "description": "Payment for a custom astrology profile" } ] } )
    
    payment.create()
    
    return payment
    
    
def executePayment(payment_id, payer_id):
  
  paypalrestsdk.configure({
      'mode': 'sandbox',
      'client_id': config.paypal_client_id,
      'client_secret': config.paypal_client_secret
    })
  
  payment = paypalrestsdk.Payment.find(payment_id)
  return payment.execute({"payer_id": payer_id})  