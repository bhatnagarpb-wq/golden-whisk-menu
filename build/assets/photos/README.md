# Gallery photos

Real photos of completed custom orders, shown in the "A Few Recent
Favourites" gallery section. `originals/` holds the untouched source
files; the `.b64` files alongside this README are what `generate.py`
actually reads and inlines into `dist/index.html`.

## How the `.b64` files were produced

Each original was:

1. Center-cropped to a square at full resolution (`sips -c`),
2. Downsampled to 640×640 (`sips -Z 640`), and
3. Converted to WebP at quality 80 (`cwebp -q 80`) — roughly a 3x size
   reduction over an equivalent-quality JPEG, which matters more than
   usual here since these are inlined as base64 (~33% size overhead)
   rather than served as separate files.
4. Base64-encoded (`base64 -i file.webp -o file.b64`).

To reprocess (e.g. after swapping in a new original), from this
directory:

```sh
f=your_photo   # without extension, matching the dict key in generate.py's GALLERY list
W=$(sips -g pixelWidth "originals/$f.jpg" | awk '/pixelWidth/{print $2}')
H=$(sips -g pixelHeight "originals/$f.jpg" | awk '/pixelHeight/{print $2}')
MIN=$((W<H?W:H))
sips -c "$MIN" "$MIN" "originals/$f.jpg" --out "/tmp/${f}_sq.jpg"
sips -Z 640 -s format jpeg -s formatOptions 90 "/tmp/${f}_sq.jpg" --out "/tmp/${f}_640.jpg"
cwebp -q 80 "/tmp/${f}_640.jpg" -o "/tmp/${f}.webp"
base64 -i "/tmp/${f}.webp" -o "$f.b64"
```

`cwebp` isn't installed by default on macOS — `brew install webp`. If
you crop/resize by hand instead (e.g. in an image editor), keep the
final output square and no larger than ~640×640; anything bigger just
inflates every future page load for no visible benefit at the size
these render on a card.
