from sqlalchemy import create_engine, URL, text
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

# with session_pool() as session:  # the second call returns the same session
#     session.execute(text("select 1"))
#     # session.commit()

# with session_pool() as session:
#     query = text(
#         """
#     CREATE TABLE users
# (
#     telegram_id   BIGINT PRIMARY KEY,
#     full_name     VARCHAR(255) NOT NULL,
#     username      VARCHAR(255),
#     language_code VARCHAR(255) NOT NULL,
#     created_at    TIMESTAMP DEFAULT NOW(),
#     referrer_id   BIGINT,
#     FOREIGN KEY (referrer_id)
#         REFERENCES users (telegram_id)
#         ON DELETE SET NULL
# );
#     """
#     )
#     session.execute(query)
#     # and commit the changes
#     session.commit()


with session_pool() as session:
    insert_query = text(
        """
    INSERT INTO users (telegram_id, full_name, username, language_code, referrer_id)
    VALUES (1, 'John Doe', 'johndoe', 'en', NULL),
              (2, 'Jane Doe', 'janedoe', 'en', 1);
    """
    )
    session.execute(insert_query)
    session.commit()

    select_query = text(
        """
    SELECT * FROM users;
    """
    )
    result = session.execute(select_query)
    for row in result:
        print(row)
