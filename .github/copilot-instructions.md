# Copilot / AI Agent Instructions for HazardHub

This repository currently contains documentation and a simple HTML sample. The authoritative overview is in `README.md` and further work is expected to include a React frontend, a Node/Express backend, a Python YOLOv8 component, and a MySQL database.

Keep this file short and actionable — focus on repository-specific facts and where to look.

**Quick context**
- **Project:** HazardHub — safety monitoring and incident reporting (see [README.md](README.md)).
- **Current repo files of interest:** [sample.html](sample.html) (UI example) and [README.md](README.md).
- **Planned components (from README):** React frontend, Node/Express backend, Python + YOLOv8 detector, MySQL DB.

**What to do first (always)**
- Read [README.md](README.md) for the product overview and integration points.
- Inspect the repository root for common folders: `client/`, `frontend/`, `server/`, `backend/`, `api/`, `detector/`, or `python/` — these typically contain the main code for each component.
- Open [sample.html](sample.html) to understand any existing UI placeholders or static assets.

**Where integrations live (how to find them)**
- Backend: look for `server/`, `api/`, or `backend/`. Expect Node/Express code and `package.json` with `start`/`dev` scripts.
- Frontend: look for `client/` or `frontend/` with a React app, `package.json`, `src/`, and `public/` folders.
- Detector / AI: look for a `python/`, `detector/`, or `yolo/` folder containing Python code, requirements (`requirements.txt` or `pyproject.toml`), and model references.
- Database: MySQL connection details are likely in backend environment files or a `config/` directory — search for `.env`, `config.js`, or `db/`.

**Common commands to try (only if matching files exist)**
- Install Node deps: `npm install` (run in the folder containing `package.json`).
- Start Node server: `npm start` or `npm run dev` (check `package.json` scripts first).
- Run Python detector: create a venv and install `requirements.txt`, then run entry script (e.g., `python detect.py`).

**Code / style patterns to preserve**
- The README emphasizes role-based access (employees vs administrators) and YOLOv8-based image detection — prefer small, focused changes that keep those boundaries intact.
- Keep UI elements consistent with the QR-code-based reporting flow described in the README. If adding pages/components, place them under `client/src/pages/` or `frontend/src/pages/` if those directories exist.

**Testing, linting, and CI**
- No CI or tests were found in the repo root. If you add project-level tests, put them under `tests/` at the same level as the component they exercise (e.g., `server/tests/` or `client/tests/`).

**When editing / adding files**
- Keep changes scoped to the relevant component directory (frontend vs backend vs detector).
- If you add environment variables, document expected names and example values in `README.md` and add a `.env.example` at the repo root or within the component folder.

**If you can't find expected components**
- The README lists components that may not yet be present. If a component (e.g., `backend/`) is missing, create a small scaffold and include a README inside that directory describing how to run it.

**Examples from this repo**
- UI placeholder: see [sample.html](sample.html) for the repo's current HTML example — search and replace that with real components when a React app is added.
- Project overview and technologies: see [README.md](README.md) for the confirmed stack and integration responsibilities.

**Merge guidance (if this file exists)**
- Preserve any project-specific instructions already present. If there are contradictions between this file and `README.md`, prefer `README.md` for product/architecture facts and this file for AI-agent operating conventions.

If something in this guidance is unclear or you want me to expand a section (run commands, scaffold component, or add example envs), tell me which area to flesh out next.
