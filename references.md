# References

## 2026-09-18 — macOS install steps updated for JIT deprecation

- **Issue:** macOS install docs still used conda napari / split pip steps that conflict with the September 2026 JIT deprecation workaround.
- **Root cause:** Apple Silicon and Intel Macs need pinned pip installs rather than the previous conda napari path.
- **Solution:** Added a September 2026 JIT note to both Mac tabs. Apple Silicon now uses `pip install "empanada-napari==1.2.4"`. Intel uses a single `--only-binary=:all:` pip install with pinned numpy, torch, numba, opencv, napari, and empanada-napari.
- **Changes:** `docs/getting_started/install.rst`
- **Prevention:** Revisit these Mac install commands once JIT-compatible wheels are available; keep Intel pins explicit.

## 2026-09-18 — Install compiler callout changed from note to Suggested

- **Issue:** The install page used a generic `note` for compiler prerequisites.
- **Root cause:** The intended callout was a suggestion to verify git/gcc/g++, not a generic note with mixed Python/compiler text.
- **Solution:** Replaced `.. note::` with `.. admonition:: Suggested` and the compiler check message.
- **Changes:** `docs/getting_started/install.rst`
- **Prevention:** Keep prerequisite callouts titled by intent (Suggested/Important) rather than a generic note.

## 2026-09-18 — Quote napari extras and drop quantized Intel note

- **Issue:** `pip install napari[all]==0.6.6` is invalid in many shells because `[all]` is treated as a glob. A quantized-model Intel-only note was also outdated.
- **Solution:** Use `pip install "napari[all]==0.6.6"` as step 3 and keep `pip install empanada-napari==1.2.4` as step 4 on Windows, Linux, and Apple Silicon. Removed the “Run Quantized Model” Intel note from modules and tutorials index pages.
- **Changes:** `docs/getting_started/install.rst`, `docs/modules/index.rst`, `docs/tutorials/index.rst`
- **Prevention:** Always quote pip extras (`"pkg[extra]==ver"`) in docs commands.

## 2026-09-16 — Getting Started Microsoft Forms show “form does not exist”

- **Issue:** Embedded Microsoft Forms on Getting Started / FAQ show “form does not exist” locally and on Read the Docs (https://empanada.readthedocs.io/en/latest/getting_started/index.html).
- **Root cause:** The form IDs themselves are no longer valid on Microsoft Forms (deleted, unpublished, or expired). Updating `forms.office.com` → `forms.cloud.microsoft` does not restore them.
- **Solution:** Removed the Microsoft Forms embeds and related registration/share-form sections from the docs for now. FAQ “Share your model” keeps the Zenodo link only.
- **Changes:** `docs/getting_started/index.rst`, `docs/faq/index.rst`
- **Prevention:** When adding forms again, use valid ResponsePage URLs and confirm they open before publishing; keep a non-embed fallback.
