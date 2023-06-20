"""Stream type classes for tap-rickandmorty_custom."""

from __future__ import annotations
from pathlib import Path
from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_rickandmorty_custom.client import rickandmorty_customStream
import requests
from typing import Any

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

    # Testando parent-child com episode
    # def get_child_context(self, record: dict, context: dict | None) -> dict | None:
    #     return {"character_results": record["results"]}
    
    def get_next_page_token(self, response: requests.Response, previous_token: Any | None) -> Any | None:
        next = response.json()['info']['next']

        if next != None:
            next_page = next.split("/")[4]
            next_page_token = next_page.split("=")[1]
        else:
            return None

        if int(next_page_token) <= 5:
            return next_page_token
        
        return None
    
    # def get_url_params(self, context: dict | None, next_page_token: Any | None) -> dict[str, Any]:
    #     params = {}

    #     # if next_page_token:
    #     #     params["page"] = next_page_token

    #     params["name"] = "rick"
    #     params["status"] = "alive"

    #     return params

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

    # Testando parent-child
    # parent_stream_type = CharacterStream
    # ignore_parent_replication_key = True

    name = "episode"
    path = "/episode"
    primary_keys = None # ["id"]
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
    
