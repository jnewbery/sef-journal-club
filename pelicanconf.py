AUTHOR = "SEF Journal Club Contributors"
SITENAME = "SEF Journal Club"
SITEURL = ""

PATH = "content"
THEME = "themes/sef-journal-club"

TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"

# Show future-dated articles (upcoming meetings)
WITH_FUTURE_DATES = True

# Clean URLs: /2025-03-15-meeting-1
ARTICLE_URL = "{slug}"
ARTICLE_SAVE_AS = "{slug}/index.html"

PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}/index.html"

DEFAULT_PAGINATION = False

# Feeds (disable for dev)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable tag/category/author pages we don't use
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
