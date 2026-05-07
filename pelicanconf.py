AUTHOR = "SEF Journal Club Contributors"
SITENAME = "SEF Journal Club"
SITEURL = ""

PATH = "content"
THEME = "themes/sef-journal-club"

STATIC_PATHS = ["extra", "2026-05-07-discussion-2"]
# STATIC_PATHS = ["extra"]
EXTRA_PATH_METADATA = {
    "extra/favicon.png": {"path": "favicon.png"},
    "extra/journal_club.png": {"path": "images/journal_club.png"},
}

MSTEAMS_URL = "https://teams.microsoft.com/l/team/19%3AfMEs9HaeZmiWN1uwiKLN8xy2H_dLIUH2tq6nLpkfoU01%40thread.tacv2/conversations?groupId=14fc94dd-2b1a-40ef-aa7b-c09c9f95ad14&tenantId=2b897507-ee8c-4575-830b-4f8267c3d307"
WHATSAPP_URL = "https://chat.whatsapp.com/H5VdEruRH3t1aLa2nvLr7R"

JINJA_GLOBALS = {
    "MSTEAMS_URL": MSTEAMS_URL,
    "WHATSAPP_URL": WHATSAPP_URL,
}

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
