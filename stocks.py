
def stock_purchases():
    amazon = 3000
    apple = 100
    fb = 250
    google = 1400
    msft = 200

    # Given the prices above and a client's investment budget, how much stock can they buy?
    # 1.1 TODO: Ask the client's name (use the string: "What is your name? ") and save it into a variable
    client_name = input("What is your name? ")

    # 1.2 TODO: Ask the client how many dollars they would like to invest (use the string: "How much would you like to invest? $")
    # and save it into a variable
    # NOTE: When you use the `input` function to get user input, what do numbers get saved as?
    investment_amount_str = input("How much would you like to invest? $")

    investment_amount = int(investment_amount_str)

    # 1.3 TODO: Uncomment the line below to ask the client which stock they're interested in.
    # NOTE: Take a look at how this input string prints out
    stock_name = input("\nWhich stock are you interested in? Enter the full name:\nAmazon\nApple\nFacebook\nGoogle\nMicrosoft\nStock Name: ")
    
    # Now that you have all of the client info, you can check how much they can purchase of the stock
    # they're interested in.

    # 1.4 TODO: Use `if/elif/else` conditional logic to determine how much stock the client can buy,
    # and save it in a variable
    if stock_name.lower() == "amazon":
     shares_to_buy = int(investment_amount/amazon)
     stock_price = amazon
    elif stock_name.lower() == "apple":
     shares_to_buy = int(investment_amount/apple)
     stock_price = apple
    elif stock_name.lower() == "facebook":
     shares_to_buy = int(investment_amount / fb)
     stock_price = fb
    elif stock_name.lower() == "google":
     shares_to_buy = int(investment_amount / google)
     stock_price = google
    elif stock_name.lower() == "microsoft":
     shares_to_buy = int(investment_amount / msft)
     stock_price = msft
    else:
     print("Invalid stock name entered.")
     return
    # shares_to_buy = 0  # Set shares_to_buy to 0 for invalid stock names

    # 1.5 TODO: Once you've calculated the number of stocks that can be purchased,
    # Use an f-string to print the result for the client, ala:
    print(f"{client_name} has ${investment_amount} to invest and can buy {shares_to_buy} shares of {stock_name} at the current price of ${stock_price}.")

   

    # Alex has $5000 to invest and can buy 50 shares of Apple at the current price of $100.

    # print(f"{client_name} has ${investment_amount} to invest and can buy {shares_to_buy} shares of  {stock_name} at the current price of ${stock_price}.")
