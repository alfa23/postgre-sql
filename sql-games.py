from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing instructions from "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for "Games" table
class FaveGames(base):
    __tablename__ = "FaveGames"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    console = Column(String)
    publisher = Column(String)
    year = Column(Integer, primary_key=False)
    genre = Column(String)


# instead of connecting to database directly, ask for a session
# create new instance of sessionmaker, then point to engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling Session() subclass defined above
session = Session()

# creating database using declarative_base subclass
base.metadata.create_all(db)


# creating records on Games table
super_mario_world = FaveGames(
    title="Super Mario World",
    console="SNES",
    publisher="Nintendo",
    year=1990,
    genre="Platform"
)

super_mario_64 = FaveGames(
    title="Super Mario 64",
    console="N64",
    publisher="Nintendo",
    year=1996,
    genre="Platform"
)

toy_commander = FaveGames(
    title="Toy Commander",
    console="DC",
    publisher="Sega",
    year=1999,
    genre="Action Adventure"
)

metropolis_street_racer = FaveGames(
    title="Metropolis Street Racer",
    console="DC",
    publisher="Sega",
    year=2000,
    genre="Racing"
)

timesplitters_2 = FaveGames(
    title="TimeSplitters 2",
    console="GC",
    publisher="Eidos Interactive",
    year=2002,
    genre="First Person Shooter"
)

destiny = FaveGames(
    title="Destiny",
    console="Xbox 360",
    publisher="Activision",
    year=2014,
    genre="First Person Shooter"
)

sea_of_thieves = FaveGames(
    title="Sea of Thieves",
    console="Xbox One",
    publisher="Microsoft Studios",
    year=2018,
    genre="Action Adventure"
)


# add each instance of games to session
# session.add(super_mario_world)
# session.add(super_mario_64)
# session.add(toy_commander)
# session.add(metropolis_street_racer)
# session.add(timesplitters_2)
# session.add(destiny)
# session.add(sea_of_thieves)


# updating a single record
# game = session.query(FaveGames).filter_by(id=6).first()
# game.title = "Destiny 2"
# game.console = "XBSS/X"
# game.publisher = "Bungie"
# game.year = 2020
# game.genre = "M.M.O.G."

# commit session to database
# session.commit()


# update multiple records
# full_names = session.query(FaveGames)
# for full_name in full_names:
#     if full_name.console == "SNES":
#         full_name.console = "Super Nintendo Entertainment System"
#     elif full_name.console == "N64":
#         full_name.console = "Nintendo 64"
#     elif full_name.console == "DC":
#         full_name.console = "Sega DreamCast"
#     elif full_name.console == "GC":
#         full_name.console = "Nintendo GameCube"
#     elif full_name.console == "XBSS/X":
#         full_name.console = "Xbox Series S/X"
#     else:
#         print("Console not defined")
#     session.commit()


# deleting a single record
gtitle = input("Enter a game title: ")
game = session.query(FaveGames).filter_by(title=gtitle).first()
# defensive programming
if game is not None:
    print("Game found: ", game.title)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(game)
        session.commit()
        print("Game has been deleted")
    else:
        print("Game not deleted")
else:
    print("No records found")


# query database to find all Games
games = session.query(FaveGames)
for game in games:
    print(
        game.id,
        game.title,
        game.console,
        game.publisher,
        game.year,
        game.genre,
        sep=" | "
    )
