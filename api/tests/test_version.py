from api import __version__


async def test_version() -> None:
    assert __version__ == "0.0.0"
