from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Pizza(Base):
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    orders = relationship("Order", back_populates="pizza")

    def to_json(self):
        return {"id": self.id, "name": self.name, "price": self.price}


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    pizza_id = Column(Integer, ForeignKey("pizzas.id"))
    pizza = relationship("Pizza", back_populates="orders")

    def to_json(self):
        return {"id": self.id, "pizza": self.pizza.to_json()}


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True)
    review = Column(String)

    def to_json(self):
        return {"id": self.id, "review": self.review}


# Setting up the engine and session
engine = create_engine("sqlite:///pizzadb.db")
Session = sessionmaker(bind=engine)
