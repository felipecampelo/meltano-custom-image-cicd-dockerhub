"""RickAndMorty tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_rickandmorty_custom import streams


class Taprickandmorty_custom(Tap):
    """RickAndMorty tap class."""

    name = "tap-rickandmorty_custom"

    # TODO: Update this section with the actual config values you expect:
    # config_jsonschema = th.PropertiesList(
    #     th.Property(
    #         "last_page",
    #         th.StringType,
    #         required=True,
    #     ),
    # ).to_dict()

    def discover_streams(self) -> list[streams.RickAndMortyStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            # streams.CharacterStream(self),
            # streams.LocationStream(self),
            streams.EpisodeStream(self),
        ]


# if __name__ == "__main__":
#     TapRickAndMorty.cli()
