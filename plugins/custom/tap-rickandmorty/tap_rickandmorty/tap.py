"""RickAndMorty tap class."""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_rickandmorty import streams


class TapRickAndMorty(Tap):
    """RickAndMorty tap class."""

    name = "tap-rickandmorty"

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
            streams.CharacterStream(self),
            streams.LocationStream(self),
            streams.EpisodeStream(self),
        ]


# if __name__ == "__main__":
#     TapRickAndMorty.cli()
