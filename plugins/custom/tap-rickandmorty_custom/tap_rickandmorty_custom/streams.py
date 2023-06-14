"""Stream type classes for tap-rickandmorty_custom."""

from __future__ import annotations

from pathlib import Path

from singer_sdk import typing as th  # JSON Schema typing helpers

from tap_rickandmorty_custom.client import rickandmorty_customStream

# TODO: Delete this is if not using json files for schema definition
SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")
# TODO: - Override `UsersStream` and `GroupsStream` with your own stream definition.
#       - Copy-paste as many times as needed to create multiple stream types.

class CharacterStream(rickandmorty_customStream):
    """Define custom stream."""

    name = "character"
    path = "/character"
    primary_keys = ["id"]
    replication_key = None
    # Optionally, you may also use `schema_filepath` in place of `schema`:
    # schema_filepath = SCHEMAS_DIR / "users.json"  # noqa: ERA001
    schema = th.PropertiesList(
        th.Property("results", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("status", th.StringType),
            th.Property("species", th.StringType),
            th.Property("type", th.StringType),
            th.Property("gender", th.StringType),
            th.Property("origin", th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("url", th.StringType))
            ),
            th.Property("location", th.ObjectType(
                th.Property("name", th.StringType),
                th.Property("url", th.StringType))
            ),
            th.Property("image", th.StringType),
            th.Property("episode", th.ArrayType(th.StringType)),
            th.Property("url", th.StringType),
            th.Property("created", th.StringType),
        ))),
    ).to_dict()

class LocationStream(rickandmorty_customStream):
    """Define custom stream."""

    name = "location"
    path = "/location"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
            th.Property("results", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("type", th.StringType),
            th.Property("dimension", th.StringType),
            th.Property("residents", th.ArrayType(th.StringType)),
            th.Property("url", th.StringType),
            th.Property("created", th.StringType),
        ))),
    ).to_dict()

class EpisodeStream(rickandmorty_customStream):
    """Define custom stream."""

    name = "episode"
    path = "/episode"
    primary_keys = ["id"]
    replication_key = None
    schema = th.PropertiesList(
        th.Property("results", th.ArrayType(th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("name", th.StringType),
            th.Property("air_date", th.StringType),
            th.Property("episode", th.StringType),
            th.Property("characters", th.ArrayType(th.StringType)),
            th.Property("url", th.StringType),
            th.Property("created", th.StringType),
        ))),
    ).to_dict()
    