
"""Music catalog and playlist manager."""

import json
import random
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE songs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        artist TEXT,
        plays INTEGER
    )
    """
)


def add_song(title, artist, plays=0, playlist=None):
    """Add a song to the catalog and return the updated playlist."""
    if playlist is None:
        playlist = []

    conn.execute(
        "INSERT INTO songs (title, artist, plays) VALUES (?, ?, ?)",
        (title, artist, plays),
    )
    playlist.append(title)
    return playlist


def shuffle_pick():
    """Return the ID of a randomly selected song, or None if empty."""
    ids = [row[0] for row in conn.execute("SELECT id FROM songs")]
    return random.choice(ids) if ids else None


def popularity(title):
    """Return the popularity category for a song."""
    row = conn.execute(
        "SELECT plays FROM songs WHERE title = ?", (title,)
    ).fetchone()

    if row is None:
        return "unknown"

    return "popular" if row[0] > 100 else "niche"


def save_playlist(playlist):
    """Serialize a playlist to a JSON string."""
    return json.dumps(playlist)


def load_playlist(blob):
    """Load a playlist from a JSON string."""
    return json.loads(blob)


def total_plays():
    """Return the total number of plays across all songs."""
    try:
        result = conn.execute(
            "SELECT SUM(plays) FROM songs"
        ).fetchone()
        return result[0] if result[0] is not None else 0
    except sqlite3.Error:
        return 0


def main():
    """Demonstrate the music catalog functionality."""
    playlist = add_song("Aurora", "Nila", 250)
    add_song("Monsoon", "Kavya", 40, playlist)

    blob = save_playlist(playlist)
    loaded_playlist = load_playlist(blob)

    if len(loaded_playlist) > 1:
        print("multi-song playlist")

    print(
        popularity("Aurora"),
        popularity("Monsoon"),
        shuffle_pick(),
        total_plays(),
    )


if __name__ == "__main__":
    main()
