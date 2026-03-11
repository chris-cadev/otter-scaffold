# Customizing the Favicon

Replace the default favicon with your own:

1. Go to [favicon.io/favicon-converter/](https://favicon.io/favicon-converter/)
2. Upload your image (PNG, JPG, or SVG recommended)
3. Download the generated favicon package
4. Extract and replace files in `src/assets/favicon/`:
   - `favicon.ico`
   - `favicon-16x16.png`
   - `favicon-32x32.png`
   - `apple-touch-icon.png`
   - `android-chrome-192x192.png`
   - `android-chrome-512x512.png`
5. Rebuild the frontend:
   ```bash
   pdm run build
   ```
