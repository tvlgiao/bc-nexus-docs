# Products and cards

## Product cards

Every state on a product card is read from your catalog. There is nothing to
switch on in the theme.

| Card shows | Set it in |
|---|---|
| **Sale** label and struck-through price | A sale price on the product |
| **Sold out** label, faded image, disabled button | Inventory tracking with stock 0, and **Settings › Inventory › Show out of stock message** |
| **Only 3 left** | Inventory tracking, and **Settings › Inventory › Stock level display** set to *Show when low* |
| **Pre-order** label, release date, amber button | **Availability › Pre-order** with a release date |
| **Best seller**, **New** or any other label | A custom field named exactly `Badge`; its value is the label |
| Colour dots | A custom field named `Swatches` with hex colours, for example `#111111, #C8102E` |
| Short feature line | A custom field named `Features`, for example `Lightweight · Breathable` |
| **No reviews yet** | Shown when a product has no approved reviews |

A card shows **one label** at a time, in this order: Sold out, Pre-order, your
own label, Sale. The `Badge`, `Swatches` and `Features` fields are hidden from
the Specifications tab and the compare page.

The buy button follows the product: **Add to cart** for simple products,
**Choose options** when a size or colour must be picked, **Pre-order now** for
pre-order items. Adding to the cart opens the **cart drawer** instead of leaving
the page. Each card also has **Quick view** and a wishlist heart.

The cart drawer lists **You might also like** under the items, the same
suggestions BigCommerce shows after an add to cart in its default theme. They
come from your store's order history, so a new store shows none until orders
build up; there is nothing to switch on.

## Card and grid settings

| Setting (Theme Styles › Products) | Effect |
|---|---|
| Grid Columns | Products per row on category pages: 3 or 4 |
| Show Brand Name | Brand name above the product name |

Shoppers can switch between grid and list view on category, brand and search
pages; the choice is remembered on their device.

These features follow your **store settings**, so they stay the same whichever
theme you use:

| Feature | Where |
|---|---|
| Star ratings and reviews | **Settings › Display › Product ratings / reviews** |
| Wishlist | **Settings › Display › Wishlist** |
| Compare checkbox | **Settings › Display › Product comparisons** |
| Add to cart on cards | **Settings › Display › Show "Add to Cart" buttons** |

## Product page

- The trust promises under the buy button (shipping, returns, authenticity) are
  a widget in the `product_trust_badges` region. Edit them to match your policies.
- The **Size guide** button next to the size option opens the content of the
  `product_size_guide` region. Leave it empty and the button hides.
- **Related products** let shoppers tick several items and add them together.
  Products with options show their own *Choose options* button instead. The list
  is BigCommerce's related products (**Products › Edit › Related products**).

## Image descriptions

Give every product image a description (**Products › Edit › Images › Image
description**). Screen readers read it aloud, and search engines use it. When a
product comes in several colours, name the colour shown, for example
`Trail Runner Jacket, Red`, so shoppers who cannot see the photo know which one
it is.

## Writing descriptions

Quick view, list view and the compare page show a shortened description that
keeps the first paragraphs and drops headings and lists. Start each description
with one or two plain sentences that sum the product up.
