from sqlalchemy import create_engine
from api_connection_and_data_structure import *

# create a connection to the PostgreSQL database
engine = create_engine('postgresql://postgres:databasetestwsc@localhost:5432/postgres')

df.to_sql("premier_league_fantasy_players", engine, if_exists="replace", index=False)