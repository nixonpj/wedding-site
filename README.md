# Wedding Website

A beautiful, custom-designed wedding website built with Hugo.

## Local Development

1. Install Hugo (if not already installed):
   ```bash
   brew install hugo
   ```

2. Run the development server:
   ```bash
   hugo server -D
   ```

3. Open your browser to `http://localhost:1313`

## Configuration

Edit `hugo.toml` to customize:
- Bride and groom names
- Wedding date
- Wedding location
- Site title

## Deployment

### Netlify (Recommended - Easiest)

1. Push your code to GitHub
2. Go to [Netlify](https://www.netlify.com/)
3. Click "New site from Git"
4. Connect your repository
5. Build settings:
   - Build command: `hugo --gc --minify`
   - Publish directory: `public`
6. Deploy!

Netlify will give you a free subdomain (e.g., `your-site.netlify.app`) or you can connect your own domain.

### Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in the project directory
3. Follow the prompts

### GitHub Pages

1. Set up GitHub Actions workflow (see `.github/workflows/gh-pages.yml`)
2. Push to GitHub
3. Enable GitHub Pages in repository settings

## Customization

- **Styles**: Edit `static/css/style.css`
- **Home Page**: Edit `layouts/index.html`
- **Content**: Add markdown files in `content/`

