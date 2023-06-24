from app.db import Session, Pizza, Order, Review
import json


def get_pizza_info(pizza_name: str):
    session = Session()
    pizza = session.query(Pizza).filter(Pizza.name == pizza_name).first()
    session.close()
    if pizza:
        return json.dumps(pizza.to_json())
    else:
        return "Pizza not found"


def create_order(pizza_name: str):
    session = Session()
    pizza = session.query(Pizza).filter(Pizza.name == pizza_name).first()
    if pizza:
        order = Order(pizza=pizza)
        session.add(order)
        session.commit()
        session.close()
        return "Order created"
    else:
        session.close()
        return "Pizza not found"

def create_review(review_text: str):
    session = Session()
    review = Review(review=review_text)
    session.add(review)
    session.commit()
    session.close()
    return "Review created"

api_functions = {
    "create_review": create_review,
    "create_order": create_order,
    "get_pizza_info": get_pizza_info,
}

### Function