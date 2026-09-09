# Maintaining the profile

The public profile is `README.md`. Its illustrations are local SVGs in `assets/`; no external font, JavaScript, image host, or banner service is required. GitHub controls the surrounding page colors and Markdown layout. The illustrations retain their dark cyberpunk palette in both GitHub themes.

## Edit the artwork

Run from the repository root with Python 3:

```sh
python3 scripts/render-assets.py
```

Edit the generator to change the palette, labels, matrix rain, or project diagrams, then include both the generator and regenerated SVGs in the same commit. Generation is deterministic and uses only the Python standard library. The banner honors `prefers-reduced-motion` and has visible static content when animation is disabled. The contribution snake is generated separately by Platane/snk.

Palette: background `#090b16`, panels `#101525`, cyan `#56f4ff`, magenta `#ff4fa3`, foreground `#eff6ff`, secondary text `#9caec7`.

## Contribution animation

`.github/workflows/profile-activity.yml` uses [Platane/snk](https://github.com/Platane/snk), pinned to a reviewed commit, to generate `assets/generated/contribution-snake.svg` from the account's GitHub contribution calendar. The initial SVG was generated from real account data using the same action revision and palette; it is not a sample calendar.

- Runs daily at 00:23 UTC (07:23 Vietnam time), manually via **Actions → Refresh contribution signal → Run workflow**, or when this workflow changes on `main`.
- Uses the built-in `GITHUB_TOKEN`; no personal token or extra secret is needed.
- Commits only the generated SVG to `main`, and skips the commit if nothing changed.
- The README uses a committed relative image path, so the last successful image remains visible if a refresh fails.
- The workflow starts once the files reach `main`. GitHub Actions must be enabled and repository rules must allow the bot to push the generated asset. Scheduled workflows in inactive public repositories can be disabled by GitHub; re-enable/run the workflow if daily refresh stops.

The branch and account are intentionally fixed to `main` and `vulebaolong`. Update these values if the repository is renamed or reused. The workflow does not run in forks.

## Content sources and editorial choices

- Supplied `VuLeBaoLong_Software_Engineer.pdf` and the portfolio's `src/data/portfolio.ts` support the professional summary, skills, PrediX, MegaPro, employment, education, and contact links.
- PrediX and MegaPro are professional projects, linked to their product sites rather than represented as public source repositories. Other professional projects remain discoverable through the portfolio.
- `deploy-kit` was checked against the local Go CLI implementation and the public repository. The linked public CLI supports YAML configuration, Docker image builds, SSH transfer, and Docker Compose deployment. The separate local Wails desktop app is not presented as part of that public repository.
- `observability-stack` was checked against its local README and public files: Alloy Docker discovery/relabeling, Loki, Grafana, and Docker Compose. It is presented as infrastructure work, not as a Go application.
- Employment dates differ between the supplied CV and portfolio. The profile deliberately omits dates instead of choosing an unverified timeline.
- JavaScript course badges, personal social accounts, view counters, old banners, and large icon lists were removed from the displayed profile to keep the focus on Go and product delivery. Existing legacy files in `asset/` remain available but are not referenced.
- No language percentage chart is used: repository byte counts would overemphasize historical JavaScript projects and would not measure professional Go experience.

## Visual reference and checks

The falling-character motif was inspired by the supplied `hainguyen011/assets/matrix-banner.svg`. All new artwork is independently authored SVG code; no reference artwork was copied.

The README was rendered with GitHub's Markdown API and inspected in Chromium using GitHub-style Markdown CSS at desktop and mobile widths, in light and dark themes. Local preview files and screenshots live in ignored `.preview/`. These are a local approximation of GitHub's surrounding layout, not a deployed profile. Validate the workflow with `actionlint`, and use `git diff --check` before committing.
