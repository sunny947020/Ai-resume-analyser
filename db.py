from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATABASE_URL = "mysql+mysqldb://2sXYCCKnqrtVBQA.root:<PASSWORD>@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/sys?ssl_mode=VERIFY_IDENTITY&ssl_ca=/etc/ssl/cert.pem

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {
            "ssl": true
            
        }
    }
)

sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()