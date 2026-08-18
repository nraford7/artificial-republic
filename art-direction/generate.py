#!/usr/bin/env python3
"""Generate 'The Water Reads Back' image set via Recraft V4 Pro (fal.ai)."""
import os, sys, json, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
from io import BytesIO

KEY = os.environ["FAL_API_KEY"]
OUT = os.path.join(os.path.dirname(__file__), "..", "images")
os.makedirs(OUT, exist_ok=True)

SUFFIX = ("painterly cinematic atmosphere reminiscent of J.M.W. Turner, heavy dawn fog, "
          "desaturated dusk-teal and warm gold palette, fine film grain, low golden light, "
          "glassy still-water reflections, no people, no boats, contemplative and elegiac, "
          "wide cinematic composition")

JOBS = [
  ("hero", "A long low Renaissance arcade building along the Grand Canal in Venice at first light, "
           "seen across still glassy water, the repeating stone bays receding into thick fog, "
           "its reflection dissolving in the canal. " + SUFFIX),
  ("doge", "A single grand ornate Venetian palazzo doorway emerging alone from thick dawn fog at "
           "the water's edge of a canal, isolated, shadowed, the rest of the building lost in mist. " + SUFFIX),
  ("institutions", "Endless repeating stone arches of a Venetian arcade receding into fog along a "
           "canal, rhythmic identical bays fading one after another into grey mist, nobody present. " + SUFFIX),
  ("archive", "Near-abstract close view of dark Venetian canal water at dusk, a Renaissance stone "
           "facade dissolving in its own broken reflection, gentle ripples fragmenting the image. " + SUFFIX),
  ("council", "A narrow dark Venetian side canal between tall shadowed buildings at dusk, a single "
           "distant warm lantern glowing through fog, deep teal shadows, beautiful and quietly ominous. " + SUFFIX),
  ("closing", "Wide panoramic view of the Grand Canal in Venice at dawn, mist rising off the water, "
           "silhouetted domes and old merchant houses reflected in perfectly still glassy water, low gold sun. " + SUFFIX),
]

def gen(job):
    name, prompt = job
    body = json.dumps({"prompt": prompt, "image_size": {"width": 1365, "height": 768}, "num_images": 1}).encode()
    req = urllib.request.Request("https://fal.run/fal-ai/recraft/v4/pro/text-to-image", data=body,
        headers={"Authorization": f"Key {KEY}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.load(r)
        url = data["images"][0]["url"]
        raw = urllib.request.urlopen(url, timeout=180).read()
        img = Image.open(BytesIO(raw)).convert("RGB").resize((1600, 900), Image.LANCZOS)
        path = os.path.join(OUT, f"{name}.jpg")
        img.save(path, "JPEG", quality=82, optimize=True)
        return f"OK {name} -> {os.path.getsize(path)//1024}KB"
    except urllib.error.HTTPError as e:
        return f"FAIL {name}: {e.code} {e.read().decode()[:200]}"
    except Exception as e:
        return f"FAIL {name}: {e}"

with ThreadPoolExecutor(max_workers=6) as ex:
    for res in ex.map(gen, JOBS):
        print(res, flush=True)
