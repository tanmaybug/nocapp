# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository layout

Monorepo with two coupled apps:

- `frontend/` — Vue 3 + TypeScript + Vite + Vuetify 3 + Pinia + vue-router. Package name `noc-portal`.
- `backend/` — FastAPI + SQLAlchemy + Postgres + Redis (async client). Entry point `backend/main.py`.
- `docker-compose.dev.yml` — orchestrates postgres, pgadmin, redis, backend, frontend for local dev.
- `uploads/` (at repo root) — mounted into the backend container; user-uploaded files land here.

Domain: NOC (No Objection Certificate) portal for educational institutions. Two user roles drive the entire UI/route structure: `INSTITUTION` (applicants) and `DEPARTMENT` (reviewers). A third level `STATE` exists in the login flow but has no module wired up.

## Common commands

All dev work runs through Docker Compose from the **repo root**:

```bash
docker-compose -f docker-compose.dev.yml up -d         # start all services
docker-compose -f docker-compose.dev.yml up backend pgadmin   # subset
docker-compose -f docker-compose.dev.yml logs -f       # tail logs
docker-compose -f docker-compose.dev.yml down          # stop
```

Service URLs: frontend `:5173`, backend `:8000`, backend Swagger `:8000/api/docs` (dev only — disabled when `ENV != "development"`), pgAdmin `:5050`, Postgres `:54320`, Redis `:6379`.

### Frontend (`frontend/`)

```bash
npm run dev          # vite dev server
npm run lint         # eslint over src/**/*.{ts,tsx,vue}
npm run lint:fix
npm run build        # runs lint, then vue-tsc -b, then vite build — all three must pass
npm run preview
```

There is no test runner configured. `npm run build` is the full CI-equivalent local check.

### Backend (`backend/`)

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload   # what docker-compose runs
```

No test runner, no migrations framework — schema lives in `backend/migrations/nocdb_*.sql` as a raw SQL dump applied manually.

## Architecture

### Frontend module pattern

Each user-facing area under `src/modules/{auth,department,institution}/` follows the same shape:

```
modules/<name>/
  <name>.routes.ts   # default-exports a RouteRecordRaw, attached in src/router/index.ts
  pages/             # route-level components
  components/        # building blocks for those pages
  services/          # axios calls (import `api` from @/services/api)
  stores/            # Pinia stores; index.ts re-exports the module's stores
```

Top-level `src/router/index.ts` composes the three module routes plus `/dashboard` (role-based redirect) and a 404. `src/router/guards.ts` provides `authGuard` (checks `useAuthStore`, enforces `meta.roles`) and `guestGuard`. Every protected route attaches `authGuard` in its module routes file with `meta.roles`.

`src/services/api.ts` is the **single axios instance** — it injects `Authorization: Bearer <token>` from `localStorage.user` on every request. Don't create new axios instances; import this one.

`src/stores/dialogStore.ts` is a global alert/confirm queue — call `useDialogStore().showDialog({type:'ALERT'|'CONFIRM', title, message, onConfirm?, onCancel?})` from anywhere. The dialog UI is mounted once in `App.vue` via `components/common/DialogBox.vue`.

Async store actions follow a uniform status state machine: `'initialized' | 'processing' | 'processed' | 'failed'` (exported as `STATUS` / `Status` from `src/types/common.ts`). Backend responses follow `ApiEnvelope<T> = { status_code, message, data }`.

### Frontend lint/style rules (enforced by eslint.config.js)

- **No semicolons** — `semi: ['error', 'never']`.
- **Use `type` aliases, not `interface`** — `@typescript-eslint/consistent-type-definitions` is set to `type`.
- TS is strict, `noUnusedLocals`, `noUnusedParameters`, `noFallthroughCasesInSwitch` all on.
- Path alias `@/*` → `src/*` (both in tsconfig.app.json and vite.config.ts).

### Vite dev proxy

`vite.config.ts` proxies `/v1` → `process.env.VITE_API_BASE_URL`. Frontend code should call backend paths as `/v1/...` (or relative to `VITE_API_BASE_URL`); the backend mounts every router with `prefix="/v1"` in `backend/config/router.py`.

### Backend layered structure

Per-feature layering:

```
controllers/V1/<area>/<thing>Controller.py   # FastAPI APIRouter, defines routes
  └─ services/<area>/<thing>Repo.py          # data access (SQLAlchemy queries) — yes, named *Repo but called a "service"
     └─ models/<thing>Model.py               # SQLAlchemy ORM models
  └─ dtos/<thing>DTO.py                      # Pydantic request/response models
  └─ mappers/<thing>Mapper.py                # DTO ↔ ORM model conversion (dtotodb / dbtodto)
```

Routes are aggregated in `backend/config/router.py` and included with `prefix="/v1"`. **When adding a new controller, you must register it in `config/router.py` or it will not be reachable.**

All responses use the envelope `helpers.response.APIResponse` = `{status_code, message, data}` — match this shape in new endpoints, since the frontend expects `response.data?.data ?? response.data`.

### Auth flow (important — non-standard)

1. `core/Middleware/Auth_middleware.py` runs on every request. It checks `request.url.path` against a **hardcoded `protected_paths` list** using `startswith`. Any new protected endpoint must be added to that list explicitly — there is no decorator-based protection. Unprotected paths skip auth entirely.
2. Tokens are JWT (`HS256`, key in `utils/token.py`), but the encoded string is **reversed** before storage/transmission and reversed again on validate/decode. `create_token` / `validate_token` / `decode_token` handle this — don't call `jwt.encode/decode` directly.
3. Auth accepts either `Authorization: Bearer <token>` header **or** `?token=` query param (the query-param path is used for file/PDF download links).
4. Decoded user is attached to `request.state.user`. `core/Dependencies/auth.py` exposes `get_current_user` (requires `stake_level_id == 3`, institution), `get_current_admin` (== 2, department), `get_current_user_admin` (intended for both but currently has a buggy condition — preserve when refactoring).
5. `stake_level_id` mapping: `1=STATE`, `2=DEPARTMENT`, `3=INSTITUTION`. The login controller maps this to the role string the frontend stores.

### CORS

`core/Middleware/Custom_CORS_middleware.py` (not the FastAPI built-in) is installed. Allowed origins come from `settings.FRONTEND_URL`, plus `DEV_URL_1` / `DEV_URL_2` in development. The built-in `CORSMiddleware` block in `main.py` is intentionally commented out — leave it that way.

### Config & env

`backend/config/config.py` uses `pydantic-settings` to load `backend/.env` (see `.env.example`). Required keys: Postgres connection, `ENV`, `FRONTEND_URL`, `DEV_URL_1/2`, `REDIS_HOST/PORT`. `MAX_FILE_SIZE` / `MAX_PDF_FILE_SIZE` defaults are 2MB.

Docker compose passes `.env.development` from the repo root into the backend container as `env_file`.

### Database

`config/DB/DBConfig.py` builds a single SQLAlchemy engine; `get_db()` is the FastAPI dependency that yields a session and runs `SELECT 1` for liveness on every request (noisy but intentional — keep it). Models extend the `Base` declared there.

There is **no Alembic / migration tool**. Schema changes go in `backend/migrations/nocdb_*_schema_with_data..sql` (filename includes the date) and are applied by hand.

## Cross-cutting conventions to follow

- New institution endpoints: add the controller under `controllers/V1/institution/`, register it in `config/router.py`, add its path prefix to `Auth_middleware.protected_paths`, expose a service in `frontend/src/modules/institution/services/institution.service.ts`.
- File uploads go through `POST /v1/institution/fileUpload` (returns a `fileId`), then `POST /v1/institution/saveFile` to associate the uploaded file with a document type. The shared UI is `frontend/src/components/ui/FileUploadField.vue`; reuse it instead of building a new uploader.
- When unsure about an existing backend route's auth status, check `Auth_middleware.protected_paths` — the protection model is allowlist by prefix.
