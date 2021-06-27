from fastapi import FastAPI

app = FastAPI()

datas = {
    
    100: {
        "name": "Test",
        "stocks": [
            {
                "name": "CRM-US",
                "buy_in_price": 200,
                "quantity":100
            }
        ]
    },
    123: {
        "name": "Wu Kelvin",
        "stocks": [
            {
                "name": "AAPL",
                "buy_in_price": 150,
                "quantity":20
            },
            {
                "name": "GOOGL",
                "buy_in_price":2500,
                "quantity":2
            }
        ]
    },
    124: {
        "name": "Lui Wally",
        "stocks": [
            {
                "name": "TSLA",
                "buy_in_price": 650,
                "quantity":10
            },
            {
                "name": "FB",
                "buy_in_price":300,
                "quantity":10
            },
            {
                "name": "AMZN",
                "buy_in_price":3400,
                "quantity":3
            }
        ]
    },
    125: {
        "name": "Cheng Titus",
        "stocks": []
    }
    
}


@app.get("/get-client-detail")
async def get_client_detail(customer_id: int):
    customer = datas.get(customer_id, None)
    if not customer:
        return {"data":{}}
    return {
        "data": {
            "name": customer['name'],
            "phone": "0987878787",
            "email": f"{customer['name']}@example.com"
        }
    }

@app.get("/get-stocks")
async def hello_name(customer_id: int):
    customer = datas.get(customer_id, None)
    if not customer:
        return {"data":[]}
    return {
        "data": customer['stocks']
    }
