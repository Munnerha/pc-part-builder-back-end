# seed.py

from sqlalchemy.orm import sessionmaker
from data.component_data import components_list
from config.environment import DATABASE_URL
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

try:
    print("seeding the database...")
    db = SessionLocal()

    db.add_all(components_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)