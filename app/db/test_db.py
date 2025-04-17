from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/car_dealer"

try:
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()
    print("✅ Connected to the database successfully!")
except Exception as e:
    print("❌ Failed to connect:")
    print(e)