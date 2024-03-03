"""
    models.py

    Creates bunch of tables
"""


from peewee import MySQLDatabase, Model, SQL, ForeignKeyField
from peewee import AutoField, CharField, TextField, IntegerField, DateTimeField
from dotenv import dotenv_values

config = dotenv_values(".env")

# Define your database connection
database = MySQLDatabase(
    config["DB_NAME"],
    user=config["DB_USR"],
    password=config["DB_USR_PASSWD"],
    host=config["DB_HOST"],
    port=3306,
)


# pylint: disable=too-few-public-methods
class BaseModel(Model):
    """
    Base model class that defines the database connection for all models.
    """

    class Meta:
        """
        Defines the database.
        """

        database = database


class User(BaseModel):
    """
    Represents a user in the system.

    Attributes:
        id (AutoField): Auto-incrementing primary key representing the user's unique identifier.
        email (CharField, optional): Email address of the user.
        username (CharField): Username of the user, must be unique.
        password (CharField): Password of the user.
        description (TextField, optional): Textual description or bio of the user.
        coins (IntegerField): Integer representing the number of coins the user possesses.
        joined_at (DateTimeField): DateTimeField representing the date
                and time when the user joined the system.
    """

    id = AutoField(primary_key=True)
    email = CharField(max_length=320, null=True)
    username = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)
    description = TextField(null=True)
    coins = IntegerField(default=0)
    joined_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])


class Item(BaseModel):
    """
    Represents an item in the system.

    Attributes:
        id (AutoField): Auto-incrementing primary key representing the item's unique identifier.
        name (CharField): Name of the item.
        creator_id (IntegerField): ID of the user who created the item.
        description (TextField, optional): Textual description of the item.
        price (IntegerField): Price of the item.
        created_at (DateTimeField): DateTimeField representing the date
                and time when the item was created.
        updated_at (DateTimeField): DateTimeField representing the date
                and time when the item was last updated.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    creator_id = IntegerField()
    description = TextField(null=True)
    price = IntegerField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_at = DateTimeField(
        constraints=[SQL("DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")]
    )


class Friend(BaseModel):
    """
    Represents a friendship between two users.

    Attributes:
        user_id (ForeignKeyField): A foreign key referencing
                the ID of the user who initiated the friendship.
        friend_id (ForeignKeyField): A foreign key referencing
                the ID of the user who received the friend request.
    """

    user_id = ForeignKeyField(User, backref="friends")
    friend_id = ForeignKeyField(User, backref="friend_of")


class Follower(BaseModel):
    """
    Represents a follower relationship between two users.

    Attributes:
        follower_id (IntegerField): ID of the user who is following.
        followee_id (IntegerField): ID of the user who is being followed.
    """

    follower_id = IntegerField()
    followee_id = IntegerField()


class Game(BaseModel):
    """
    Represents a game in the system.

    Attributes:
        id (AutoField): Auto-incrementing primary key representing the game's unique identifier.
        name (CharField): Name of the game.
        description (TextField, optional): Description of the game.
        creator_id (IntegerField): ID of the user who created the game.
        visits (IntegerField): The number of times people visited the game.
        created_at (DateTimeField): DateTimeField representing the date
                and time when the game was created.
        updated_at (DateTimeField): DateTimeField representing the date
                and time when the game was last updated.
    """

    id = AutoField(primary_key=True)
    name = CharField(max_length=255)
    description = TextField(null=True)
    creator_id = IntegerField()
    visits = IntegerField(default=0)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_at = DateTimeField(
        constraints=[SQL("DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")]
    )


class Group(BaseModel):
    """
    Represents a group in the system.

    Attributes:
        id (AutoField): Auto-incrementing primary key representing the group's unique identifier.
        description (TextField, optional): Description of the group.
        owner_id (IntegerField): ID of the user who owns the group.
    """

    id = AutoField(primary_key=True)
    description = TextField(null=True)
    owner_id = IntegerField()


class GroupMember(BaseModel):
    """
    Represents a membership of a user in a group.

    Attributes:
        group_id (IntegerField): ID of the group.
        user_id (IntegerField): ID of the user who joined the group.
    """

    group_id = IntegerField()
    user_id = IntegerField()


class Session(BaseModel):
    """
    Represents a session in the system.

    Attributes:
        discord_id (CharField): Discord user ID of the user.
        account_id (IntegerField): Account user ID of the user from Auto Conversation.
    """

    discord_id = CharField(max_length=255, unique=True)
    account_id = IntegerField()