from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine("mysql+pymysql://root:Shashi2000.@localhost:3306/retail_db")

    df.to_sql("orders", con=engine, if_exists="replace", index=False)

    print("Data loaded into MySQL")