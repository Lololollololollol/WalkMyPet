import sqlalchemy
import sqlalchemy.orm
from my_web_app.data.modelbase import SqlAlchemyBase
# noinspection PyUnresolvedReferences
import my_web_app.data.album
# noinspection PyUnresolvedReferences
import my_web_app.data.track
# noinspection PyUnresolvedReferences
import my_web_app.data.account


class DbSessionFactory:
    factory = None

    @staticmethod
    def global_init(db_file):
        if DbSessionFactory.factory:
            return

        if not db_file or not db_file.strip():
            raise Exception("You must specify a data file.")

            # How to create the DB schema
            # (create_all(): inspects the db type that it needs to manage
            # - create DB/table/relationship.
            # (engine- implicit relationship gets wired together. - no need to track the engine rf. another place
            # only creates a new one - no update for the existing tables)
            # also create the database file

            # one and only time creating the instance of engine per DB
        conn_str = 'sqlite:///' + db_file
        print("Connecting to db with conn string: {}".format(conn_str))
        # While creating the DB, pass a single information(file) for connection to LiteSQL(file-based embedded DB)
        # echo = True -> turn on all the debug output
        engine = sqlalchemy.create_engine(conn_str, echo=True)

        # How to create the DB schema
        # (create_all(): inspects the db type that it needs to manage
        # - create DB/table/relationship.
        # (engine- implicit relationship gets wired together. - no need to track the engine rf. another place
        # only creates a new one - no update for the existing tables)
        # also create the database file
        SqlAlchemyBase.metadata.create_all(engine)
        # Create a unit of work
        DbSessionFactory.factory = sqlalchemy.orm.sessionmaker(bind=engine)

    @staticmethod
    def create_session():
        return DbSessionFactory.factory()
