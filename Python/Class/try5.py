
dict = {
        "bpi":{ 
            "USD":{
                "code":"USD",
                "symbol":"&#36;",
                "rate":"29,819.0157",
                "description":"United States Dollar",
                "rate_float":29819.0157
                }
             }
        }

m = "USD"

for n in dict["bpi"]:
    print(dict['bpi']['USD']["rate_float"])

