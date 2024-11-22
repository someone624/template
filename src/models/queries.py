from sqlalchemy.orm import Session
from .user_model import User
from .product_model import Product

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_all_products(db: Session):
    return db.query(Product).all()

def create_user(db: Session, username: str, email: str, password_hash: str):
    db_user = User(username=username, email=email, password_hash=password_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_product(db: Session, name: str, description: str, price: float):
    db_product = Product(name=name, description=description, price=price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product