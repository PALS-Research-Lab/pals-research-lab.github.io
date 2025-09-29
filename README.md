# PALS Research Lab Website

This is the official website for the PALS Research Lab, hosted on GitHub Pages.

## Website Structure

The website includes the following sections:
- **Header**: Lab title and tagline
- **Mission**: Research lab's mission statement
- **People**: Team members (PI, graduate students, undergraduate researchers)
- **Research Areas**: Project areas and research focus
- **Contact**: Location, email, and phone information
- **Join Us**: Opportunities and HubSpot integration for applications

## Customization

To customize the website content:

1. **Title and Tagline**: Edit the `<h1>` and tagline `<p>` in the header section of `index.html`
2. **Mission Statement**: Replace the placeholder text in the mission section
3. **Team Members**: Update the people cards with actual names, photos, and bios
4. **Research Areas**: Modify the project cards with your actual research focuses
5. **Contact Information**: Update location, email, and phone details
6. **HubSpot Integration**: Replace `https://your-hubspot-page-url-here` with your actual HubSpot page URL

## Adding Team Member Photos

Replace the placeholder image URLs (`https://via.placeholder.com/...`) with actual photos:
1. Add photos to the repository (create an `images` folder)
2. Update the `src` attributes in the image tags
3. Recommended image size: 200x200px for consistent display

## Styling

The website uses a responsive design with:
- Professional blue color scheme
- Mobile-responsive layout
- Smooth scrolling navigation
- Hover effects and transitions
- Print-friendly styles

## Local Development

To test the website locally:
```bash
python3 -m http.server 8080
```
Then open `http://localhost:8080` in your browser.

## GitHub Pages

This website is automatically deployed via GitHub Pages when changes are pushed to the main branch.
