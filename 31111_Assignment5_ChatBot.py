
#problem="Is their any problem?"
#status="On the way"
#CL="Cancled"
#ON="Anytime"
resp={
    "cancel":"Your order is cancelled",
    "name":"My name is Bot123",        
    "Status":"On the way",
    "order":"What would you like to order"
    }

def error_message():
      print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

  
def order_Veg():
    Vegpz = input("And what kind of Pizza for your in Veg? \n[a] Margherita Pizza \n[b] Golden Corn Pizza \n[c] Jalapeno & Red Paprika Pizza \n[d] Crisp Capsicum & Fresh Tomato Pizza\n[e] Paneer Special Pizza \n[f] Peppy Paneer Pizza\n>").lower()
    if Vegpz == 'a':
        return 'Margherita Pizza'
    elif Vegpz == 'b':
        return 'Golden Corn Pizza'
    elif Vegpz == 'c':
        return 'Jalapeno & Red Paprika Pizza'
    elif Vegpz== 'd':
        return 'Crisp Capsicum & Fresh Tomato Pizza'
    elif Vegpz=='e':
        return 'Paneer Special Pizza'
    elif Vegpz=='f':
        return 'Peppy Paneer Pizza'
    else:
        error_message()
        
        return order_Veg()

def order_NVeg():
    Vegpz = input("And what kind of Pizza for your in Non Veg? \n[a] Pepperoni Pizza \n[b] Chicken Pizza \n[c] Meat Lovers Pizza \n[d] Cheese Chicken Pizza \n>").lower()
    if Vegpz == 'a':
        return 'Pepperoni Pizza'
    elif Vegpz == 'b':
        return 'Chicken Pizza'
    elif Vegpz == 'c':
        return 'Meat Lovers Pizza'
    elif Vegpz== 'd':
        return 'Cheese Chicken Pizza '
    else:
        error_message()
        
        return order_Veg()

def No_pizza():
    res=input("How many pizza would you like to order: ")
    return res

def Mode_Dil():
    res=input("[a] Delivery\n[b] Take away\n>").lower()
    if res == 'a':
        return "Delivery"
    elif res == 'b':
        return "Take away"
    
def Menu():
    res = input("What type of Pizza would you like oder ? \n[a] Order\n[b] Equiry\n>").lower()
    if res == 'a':
        return pizza_bot
    elif res == 'b':
        return User_Enquiry()
    

def Pizza_Type():
  res = input("What type of Pizza would you like oder ? \n[a] Veg\n[b] Non-Veg\n>").lower()
  if res == 'a':
    return order_Veg()
  elif res == 'b':
    return order_NVeg()
  
  else:
    error_message()
    return Pizza_Type()
  
def get_size():
  res = input('What size Pizza can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ').lower()
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    error_message()
    return get_size()

def pizza_bot():
  print("Welcome to the XYZ Pizza House")
  
  Pizza_type = Pizza_Type()
  size = get_size()
  pizzano =No_pizza()
  print("Alright, that's {} {} {}.".format(pizzano,size,Pizza_type))

  '''extra_options()'''
  
  name = input("Can I get your name please?")
  m=Mode_Dil()
  print("Mode: {}".format(m))
  print("Thanks, {}! Your order will be ready shortly".format(name))
  

def res(message):
    if message in resp: 
        bot286_message = resp[message]
    else: 
        bot286_message = "I'm sorry, I did not understand your selection."
    return bot286_message
def real(xtext): 
    if "name" in xtext: 
        ytext = "name"
    elif "cancel" in xtext: 
        ytext = "cancel"
    elif "order" in xtext: 
        ytext = "order"
    elif "status" in xtext:
        ytext="Status"
    else: 
        ytext = ""
    return ytext
    
def send_message(message): 
    response = res(message) 
    if "to order" in response:
        pizza_bot()
    else:
        print(response)
        
def User_Enquiry():
    print("Welcome")
    print("How can I help you?")
    while(1):
        my_input = input("--> ") 
        my_input = my_input.lower() 
        related_text = real(my_input) 
        send_message(related_text)
        if my_input == "exit" or my_input == "stop": 
            print("See you Again")
            break
        
User_Enquiry()