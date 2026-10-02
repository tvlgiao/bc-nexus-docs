# Set up the homepage

The homepage is a stack of blocks. Theme Styles › **Homepage** switches them on
and off, and Page Builder holds their content. A block you switch off leaves no
gap.

## Hero

The hero reads the **first slide of your carousel** (**Storefront › Home page
carousel**). Set the slide's image, heading, text, button label and link there.
Only the first slide is shown; drag a slide to the first position to use it.

- **Image:** at least 1920 × 1080, landscape, subject right of centre. The theme
  darkens the left side so the heading stays readable. On very wide screens the
  whole image is shown and its left edge fades into the background.
- **Accent word:** wrap a word in asterisks, for example `Fuel *your* game`. It
  shows in your accent colour.

Settings in Theme Styles › Homepage › *Hero section*:

| Setting | Effect |
|---|---|
| Show Hero | Shows or hides the hero |
| Small line above the hero heading | For example *Season 2026 Collection*. Empty hides it |
| Second hero button label / link | An outlined button next to the slide's button |
| Hero side panel | What sits beside the hero: Stats, Quote, Gallery or Product (see below) |
| Hero heading / description / button (used when the carousel is empty) | A working hero before you add any slide |

The row of sport links under the buttons is a widget in the `home_hero_links`
region. Edit or delete it in Page Builder.

### Hero side panel

| Choice | Shows | Content comes from |
|---|---|---|
| Stats | Three figures | Page Builder region `home_hero_stats` |
| Quote | An athlete quote | Page Builder region `home_hero_quote` |
| Gallery | A photo grid | Page Builder region `home_hero_gallery` |
| Product | Your first featured product | Nothing to set up |

An empty region hides the panel, and the hero copy then takes the full width.

## Flash sale strip

A red strip with a countdown and a button.

- **Flash sale deadline** takes a date and time such as `2026-12-31T23:59:59`.
  Empty hides the strip; after the deadline the strip hides itself.
- The label, heading and button are a widget in the `home_flash_sale` region.

## Free-shipping progress bar

**Free shipping threshold** is the cart total at which shipping becomes free,
as a plain number such as `150`. The cart page and the cart drawer show a bar
counting down to it. Empty hides the bar. Keep it in line with your real
shipping rules in **Settings › Shipping**.

## Product sections

| Setting | Effect |
|---|---|
| Show Featured Products | Products you marked *Featured* in the catalog |
| Featured products: small line / heading / View all link | The text above that section |
| Show New Arrivals | Your newest products |
| New arrivals: small line / heading / View all link | The text above that section |

The number of products in each section is set in **Products › Number of
products displayed**.

## Other blocks

| Block | Switch | Content |
|---|---|---|
| Trust bar (shipping, returns, secure checkout) | Show Trust Bar | Widget in `home_trust_bar` |
| Sport links strip | — | Widget in `home_below_trust` |
| Brand strip | Show Brands | Widget in `home_brand_strip` |
| From the blog | — | Your three latest blog posts |
| Shop the look | — | Photo grid widget in `home_social_grid`; the follow button links to your first social network |
| Newsletter | Show Newsletter | BigCommerce newsletter sign-up |

## Top bar

The strip above the header, set in Theme Styles › **Header and footer** ›
*Top bar*: a message, an optional link text and the link URL.

Avoid a fixed amount in the message ("over $150") unless it matches your real
free-shipping rule and currency. The right side of the top bar holds the
currency picker (shown when the store has two or more currencies) and the
dark/light switch.

## Menu

The header menu is your category tree. Top-level categories are the menu items.
Hovering one opens a mega menu: each second-level category is a column title and
its third-level categories are the links below. The `header_mega_feature--global`
region adds a promo tile to the mega menu.
