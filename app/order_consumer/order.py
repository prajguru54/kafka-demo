from .db_conf import Base
from sqlalchemy import Column, Integer, Float


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    total_cost = Column(Float)

    def __repr__(self):
        return f"<Order(id={self.id}, user_id={self.user_id}, total_cost={self.total_cost})>"
