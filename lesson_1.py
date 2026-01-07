from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

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

session_pool = sessionmaker(bind=engine)

# session = session_pool()  # the first call creates a new session
# session.execute("")
# session.commit()
# session.close()

with session_pool() as session:  # the second call returns the same session
    print(session)
    session.execute("")
    session.commit()
