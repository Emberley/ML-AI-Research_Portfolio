# Portfolio Website

A Jekyll static site for showcasing ML / AI research projects.

## Folder Structure

```
portfolio-website/
├── _config.yml          # Jekyll site configuration
├── _layouts/
│   └── default.html     # Base HTML layout
├── _includes/           # Reusable HTML partials (nav, footer, …)
├── index.html           # Home page
├── about.md             # About page
├── projects/
│   └── index.html       # Projects listing page
├── assets/
│   ├── css/
│   │   └── style.css    # Custom stylesheet
│   └── images/          # Site images / screenshots
└── Gemfile              # Ruby dependency specification
```

## Local Development

### Prerequisites
- Ruby 3.1+
- Bundler (`gem install bundler`)

### Install and Run
```bash
cd portfolio-website
bundle install
bundle exec jekyll serve --livereload
# Site available at http://localhost:4000
```

## Deploying to GitHub Pages

1. Push the `portfolio-website/` folder contents to the `gh-pages` branch
   **or** configure GitHub Pages to build from the `portfolio-website/` folder
   on the `main` branch.
2. Update `url` and `baseurl` in `_config.yml` to match your GitHub Pages URL.

## Adding a New Project Card

1. Open `projects/index.html`.
2. Copy the commented-out card template and fill in the title, description,
   tags, and link.
3. Commit and push — the site will rebuild automatically on GitHub Pages.
