from sqlalchemy import create_engine, URL

# URL format: dialect+driver://username:password@host:port/database
url = URL.create(
    drivername="postgresql+psycopg2",
    username="testuser",
    password="testpassword",
    host="localhost",
    port=5432,
    database="testuser",
)
engine = create_engine(url, echo=True)
