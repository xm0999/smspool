# SMSPool.py
Unofficial API wrapper for [SMSPool.net](https://www.smspool.net/). With this wrapper you are able to call all endpoints with functions.  
[Join the SMSPool.net Discord server](https://discord.gg/Rcb526SEFw).
<br>
<br>
## Table Of Contents
- [SMSPool.net Documentation](https://github.com/xm0999/smspool/edit/main/README.md#smspoolnet-api-documentation)
- [Getting Started](https://github.com/xm0999/smspool/blob/main/README.md#getting-started)
- [Main Documentation](https://github.com/xm0999/smspool/blob/main/README.md#main-documentation)
    - [client()](https://github.com/xm0999/smspool/blob/main/README.md#client)
    - [get_countries()](https://github.com/xm0999/smspool/blob/main/README.md#get_countries)
    - [get_services()](https://github.com/xm0999/smspool/blob/main/README.md#get_services)
    - [get_balance()](https://github.com/xm0999/smspool/blob/main/README.md#get_balance)
    - [get_order_history()](https://github.com/xm0999/smspool/blob/main/README.md#get_order_history)
    - [get_active_orders()](https://github.com/xm0999/smspool/blob/main/README.md#get_active_orders)
- [SMS Documentation](https://github.com/xm0999/smspool/blob/main/README.md#sms-documentation)
    - [get_service_price(country, service, pool(not required))](https://github.com/xm0999/smspool/blob/main/README.md#get_service_pricecountry-service-poolnot-required)
    - [purchase_sms(country, service, pool)](https://github.com/xm0999/smspool/blob/main/README.md#purchase_smscountry-service-poolnot-required)
    - [check_sms(order_id)](https://github.com/xm0999/smspool/blob/main/README.md#check_smsorder_id)
    - [resend_sms(order_id)](https://github.com/xm0999/smspool/blob/main/README.md#resend_smsorder_id)
    - [cancel_sms(order_id)](https://github.com/xm0999/smspool/blob/main/README.md#cancel_smsorder_id)
    - [archieve_sms_orders(order_id)](https://github.com/xm0999/smspool/blob/main/README.md#archive_sms_ordersorder_id)
- [Rentals Documentation](https://github.com/xm0999/smspool/blob/main/README.md#sms-documentation)
    - [get_rentals(type)](https://github.com/xm0999/smspool/blob/main/README.md#get_rentalstype)
    - [purchase_rental(rental_id, days, service_id)](https://github.com/xm0999/smspool/blob/main/README.md#purchase_rentalrental_id-days-service_id)
    - [get_rental_message(rental_code)](https://github.com/xm0999/smspool/blob/main/README.md#purchase_rentalrental_id-days-service_id)
    - [get_rental_status(rental_code)](https://github.com/xm0999/smspool/blob/main/README.md#get_rental_statusrental_code)
    - [refund_rental(rental_code)](https://github.com/xm0999/smspool/blob/main/README.md#refund_rentalrental_code)
    - [extend_rental(rental_code, days)](https://github.com/xm0999/smspool/blob/main/README.md#extend_rentalrental_code-days)  
<br>

## SMSpool.net API Documentation
Checkout the official API documentation here [https://www.smspool.net/article/how-to-use-the-smspool-api](https://www.smspool.net/article/how-to-use-the-smspool-api#).
<br>  
## Getting Started
To get started you have to install the smspool npm package
```
pip install smspool
```

After that we can import smspool
``` python
from smspool import smspool
sms = smspool(apikey="YOUR_API_KEY")

countries = sms.get_countries()
print(countries)
```
<br>

# Main Documentation

### smspool()
To assign an api key to the client use the client() method.
``` python
sms = smspool(apikey="YOUR_API_KEY")
```
[Get your api key here](https://www.smspool.net/my/settings#apikey)

---

### get_countries()
Returns the list of countries supported by smspool.net

Response:
```json
[
  {
    "ID": "1",
    "name": "United States",
    "region": "Americas"
  },
  {
    "ID": "2",
    "name": "United Kingdom",
    "region": "Europe"
  },
  {
    "ID": "3",
    "name": "Netherlands",
    "region": "Europe"
  },
]
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#country_endpoint)  

---

### get_services(country)
Returns the list of services supported by smspool.net in the given country

Response:
```json
[
  {
    "ID": "1",
    "name": "service1"
  },
  {
    "ID": "2",
    "name": "service2"
  },
  {
    "ID": "3",
    "name": "service3"
  },
]
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#service_endpoint)  

---

### get_balance()
Returns the balance of the account
API Key required!

Response:
```json
{
  "balance": "1.00"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#balance_endpoint)  

---

### get_order_history()
Returns the order history of the account
API Key required!  

[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#order_history_endpoint)  
---

### get_active_orders()
Returns the active orders of the account  
API Key required!

Response:
```json
{
   "timestamp":"2022-05-24 21:20:07",
   "order_code":"ABCDEFGH",
   "phonenumber":"123456789",
   "code":"0",
   "full_code":"0",
   "short_name":"US",
   "service":"Service",
   "status":"pending",
   "expiry":"1653420607"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#active_orders_endpoint)  

<br>

# SMS Documentation

### get_service_price(country, service, pool(not required))
Returns the price of the service in the given country
API Key required!

`country` = The country code/ID that you can retrieve from the country endpoint.  
`service` = The service ID/name that you can retrieve from the service endpoint.
`pool` = The pool you'd like to order from is not required, in case it's empty it'll automatically select a suitable pool. Pools can be selected by number or by name (for example Alpha).

Response:
```json
{
   "timestamp":"2022-05-24 21:20:07",
   "order_code":"ABCDEFGH",
   "phonenumber":"123456789",
   "code":"0",
   "full_code":"0",
   "short_name":"US",
   "service":"Service",
   "status":"pending",
   "expiry":"1653420607"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#price_endpoint)  

---

### purchase_sms(country, service, pool(not required))
Purchases the service in the given country
API Key required!

`country` = The country code/ID that you can retrieve from the country endpoint.  
`service` = The service ID/name that you can retrieve from the service endpoint.  
`pool` = The pool you'd like to order from is not required, in case it's empty it'll automatically select a suitable pool. Pools can be selected by number or by name (for example Alpha).

Response:
```json
{
   "success":1,
   "number":"123456789",
   "order_id":"ABCDEFG",
   "country":"United States",
   "service":"Service",
   "pool":5,
   "expires_in":599,
   "message":""
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#order_sms_endpoint)  

---

### check_sms(order_id)
Checks the status of the order
API Key required!  

`order_id` = The order_id you received from the Order SMS endpoint.

Response:
```json
{
  "status": 3,
  "sms": "00000",
  "full_sms": "full SMS"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#check_sms_endpoint)  

---

### resend_sms(order_id)
Resends the SMS
API Key required!  

`order_id` = The order_id you received from the Order SMS endpoint.

Response:
```json
{
  "success":1,
  "message":"Number has been requested again",
  "resend":0
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#resend_sms_endpoint)  

---

### cancel_sms(order_id)
Cancels the SMS
API Key required!  

`order_id` = The order_id you received from the Order SMS endpoint.

Response:
```json
{
  "success": 1
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#cancel_sms_endpoint)  

---

### archive_sms_orders(order_id)
Archive all SMS orders.
API Key required!  

`order_id` = The order_id you received from the Order SMS endpoint.

Response:
```json
{
   "success":1,
   "message":"All your inactive orders have been archived."
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#archive_sms_endpoint)  

<br>

# Rentals Documentation

### get_rentals(type)
Returns the list of rentals

`type` = 0/1
1 = Extendable  
0 = one-time  

Response:
```json
{
   "0":{
      "name":"United States",
      "region":"Americas",
      "pricing":"{\"7\":18,\"14\":25,\"30\":30}"
   }
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#retrieve_rentals_endpoint)  

---

### purchase_rental(rental_id, days, service_id)
Purchase the rental.  
API Key required!  

`rental_id` = The rental ID was retrieved from the "Retrieve all rentals" endpoint.  
`days` = The number of days you'd like to rent for.  
`service_id` = Specify a service ID to only purchase a line for that service and get 50% off. Only works for US extendable rentals.  

Response:
```json
{
   "success":1,
   "message":"",
   "phonenumber":"123456789",
   "days":30,
   "rental_code":"ABCDEFG",
   "expiry":"1653758381"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#order_rental_endpoint)  

---

### get_rental_message(rental_code)
Returns the rental message
API Key required!  

`rental_code` = The retrieved rental code from the `Order rental` endpoint.  

Response:
```json
{
   "success":1,
   "messages":{
      "0":{
         "ID":6,
         "sender":null,
         "message":"Message 1",
         "timestamp":"11 May 2022 18:39:54"
      },
      "1":{
         "ID":6,
         "sender":null,
         "message":"Message 2",
         "timestamp":"11 May 2022 01:11:35"
      }
   },
   "source":"6"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#rental_messages_endpoint)  

---

### get_rental_status(rental_code)
Returns the rental status
API Key required!  

`rental_code` = The retrieved rental code from the "Order rental" endpoint.  

Response:
```json
{
   "success":1,
   "status":{
      "expiry":1654495533,
      "available":1,
      "phonenumber":"123456789",
      "activeFor":90
   }
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#retrieve_rental_status_endpoint)  

---

### refund_rental(rental_code)
Refund a rental.  
API Key required!  

`rental_code` = The retrieved rental code from the `Order rental` endpoint.  

Response:
```json
{
   "success":1,
   "message":"Your rental has been refunded!"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#refund_rental_endpoint)  

---

### extend_rental(rental_code, days)
Refund a rental.  
API Key required!  

`rental_code` = The retrieved rental code from the `Order rental` endpoint.  
`days` = The amount of days you'd like to extend it with.  

Response:
```json
{
   "success":1,
   "message":"Your rental has been succesfully extended!"
}
```
[Checkout the official documentation](https://www.smspool.net/article/how-to-use-the-smspool-api#extend_rental_endpoint)  

## How can I contribute to this project?
Before you start working on a feature or fix open a issue. After that fork the project and change anything you want. I will review the pull request and merge it to the main branch.
