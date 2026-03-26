# YouTube Clone

A Django-based YouTube-style video platform where users can register, upload videos, browse channels, watch adaptive streams, and react with likes or dislikes.

> **Stack:** Python 3.13 · Django 6 · SQLite · ImageKit · Vanilla JS

---

## Features

### Viewer Experience
- Browse the latest uploaded videos from the home feed
- Watch videos via HLS stream (with an optimised fallback URL)
- Like or dislike videos — one vote per authenticated user

### Creator Experience
- Register an account and sign in
- Upload videos up to **100 MB** (MP4, WebM, MOV, AVI)
- Optionally provide a custom thumbnail, or get one auto-generated
- View all your uploads on a personal channel page
- Delete your own videos

### Media Handling
- Video files and thumbnails are stored and delivered via **ImageKit**
- Thumbnails include a username watermark transformation
- Playback uses ImageKit transformations for optimisation and streaming

---

## Project Structure

```
YoutubeClone/
├── pyproject.toml
├── README.md
├── docs/
│   └── screenshots/        # README preview images
└── youtube/
    ├── manage.py
    ├── db.sqlite3
    ├── youtube/            # project settings, urls, ASGI/WSGI
    ├── accounts/           # authentication views, forms, urls
    ├── videos/             # models, upload flow, playback, voting
    ├── templates/          # shared base template
    └── static/             # global CSS and assets
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd YoutubeClone
```

### 2. Create and sync the environment

```bash
uv venv
uv sync
```

Or install dependencies from `pyproject.toml` manually inside a virtualenv.

### 3. Create a `.env` file

```env
IMAGEKIT_PUBLIC_KEY=your_imagekit_public_key
IMAGEKIT_PRIVATE_KEY=your_imagekit_private_key
IMAGE_KIT_BASE_URL=https://api.imagekit.io
IMAGEKIT_WEBHOOK_SECRET=optional_webhook_secret
```

| Variable | Required | Notes |
|---|---|---|
| `IMAGEKIT_PUBLIC_KEY` | ✅ | Used during upload calls |
| `IMAGEKIT_PRIVATE_KEY` | ✅ | Required by the ImageKit Python SDK |
| `IMAGE_KIT_BASE_URL` | Optional | Overrides the SDK default |
| `IMAGEKIT_WEBHOOK_SECRET` | Optional | Not used in the current app |

### 4. Apply migrations

```bash
uv run python youtube/manage.py migrate
```

### 5. Start the development server

```bash
uv run python youtube/manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## Routes

| Path | Description |
|---|---|
| `/` | Home feed |
| `/upload/` | Upload page (login required) |
| `/<video_id>` | Video detail and playback |
| `/channel/<username>/` | Creator channel page |
| `/accounts/register/` | Sign up |
| `/accounts/login/` | Sign in |

---

## Data Models

### `Video`

| Field | Type |
|---|---|
| `owner` | FK → User |
| `title` | CharField |
| `description` | TextField |
| `imagekit_file_id` | CharField |
| `video_url` | URLField |
| `thumbnail_url` | URLField |
| `views` / `likes` / `dislikes` | PositiveIntegerField |
| `created_at` / `updated_at` | DateTimeField |

### `VideoLike`

Stores one reaction per user per video (`+1` like, `-1` dislike). Enforces a unique `(user, video)` constraint to prevent duplicate votes.

---

## Development Notes

- Configured for local development with `DEBUG = True` and SQLite
- Media is handled by ImageKit — no local file storage needed
- No automated tests yet; Django system checks pass with 0 tests

```bash
uv run python youtube/manage.py check
uv run python youtube/manage.py test
```

---

## Roadmap

- [ ] Comments and subscriptions
- [ ] Search and filtering
- [ ] Playlists and watch history
- [ ] Creator dashboard
- [ ] Automated tests for upload, voting, and auth
- [ ] Production settings and deployment configuration