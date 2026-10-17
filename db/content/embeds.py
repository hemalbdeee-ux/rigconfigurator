"""Real-world fit embeds per guide: install videos (YouTube) and owner posts (Reddit), shown through each platform's own
embed. Keyed by "make/model/gen/category" (same as an article module's KEY). build_articles_sql.py merges each list into
that article's JSON as "embeds". Rules: only public posts and videos; never download or re-host the media; the
note says what the reader should look at; every entry was checked by a person before it was added.

Entry shapes:
  {"kind": "youtube", "id": "<11-char video id>", "title": "...", "channel": "...", "note": "..."}
  {"kind": "reddit", "url": "https://www.reddit.com/r/<sub>/comments/<id>/<slug>/", "title": "...", "sub": "<sub>", "author": "<user>", "note": "..."}
"""

EMBEDS: dict[str, list[dict]] = {
}
