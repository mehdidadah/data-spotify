from sqlalchemy import create_engine


class Database:
    def __init__(self, db_name):
        self.engine = create_engine('sqlite:///' + db_name)

    def write(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace')