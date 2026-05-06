# SEF Journal Club

Website for the SEF Journal Club, with details of future and past meetings, and
links to the papers discussed.

## Local Development

To run locally:

- Make sure that Python and [uv](https://docs.astral.sh/uv/) are installed
- Clone the repository and navigate to the project directory
- Run `uv sync` to install dependencies
- Run `poe serve` to start the server

## Deployment

The website is deployed on [Cloudflare Pages](https://pages.dev/) at
[https://sef-journal-club.pages.dev/](https://sef-journal-club.pages.dev/).
It's configured to automatically deploy when changes are pushed to the `m`
branch.
