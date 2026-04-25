<div align="center">

# 🎬 YouTube Clone

**A full-stack video platform inspired by YouTube — built with Django.**

Upload videos. Stream content. Engage with creators.

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=flat-square&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6-092E20?style=flat-square&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![ImageKit](https://img.shields.io/badge/ImageKit-blue?style=flat-square)
![HLS](https://img.shields.io/badge/HLS_Streaming-supported-success?style=flat-square)

<img src="docs/screenshots/home-feed.png" width="85%" />

</div>

---

## ✨ Features

### 👀 Viewer Experience
| Feature | Description |
|---|---|
| 🎞️ **Video Streaming** | Watch videos with HLS-supported streaming playback |
| 👍 **Like / Dislike** | One vote per user, enforced server-side |
| 📊 **View Counts** | Per-video stats tracked on every watch |

### 🎥 Creator Experience
| Feature | Description |
|---|---|
| 🔐 **Auth** | Register, log in, manage your account |
| ⬆️ **Upload Videos** | Supports MP4, WebM, MOV, AVI |
| 🖼️ **Thumbnails** | Upload custom thumbnails or get auto-generated ones |
| 📺 **Channel Page** | Dedicated page for every creator |
| 🗑️ **Delete Videos** | Remove only your own content |

### ⚡ Media Handling
| Feature | Description |
|---|---|
| ☁️ **ImageKit** | Cloud storage and optimized media delivery |
| 🎬 **Video Streaming** | Efficient, buffered video playback |
| 🖼️ **Dynamic Thumbnails** | Auto-generated when none is provided |

---

## 🛠️ Tech Stack

**Backend** — Python 3.13 · Django 6 · SQLite

**Frontend** — HTML · CSS · JavaScript

**Media** — ImageKit (storage & delivery) · HLS streaming

**Tooling** — `uv` · python-dotenv

---

## 📸 Screenshots

### 🏠 Home Feed
<img src="docs/screenshots/home-feed.png" width="100%" />

### ▶️ Video Player
<img src="docs/screenshots/video-player.png" width="100%" />

### ⬆️ Upload Flow
<img src="docs/screenshots/upload-flow.png" width="100%" />

### 👤 Channel Page
<img src="docs/screenshots/channel-info.png" width="100%" />

---

## 📁 Project Structure

```
YoutubeClone/
├── pyproject.toml
├── README.md
├── docs/
│   └── screenshots/
└── youtube/
    ├── manage.py
    ├── db.sqlite3
    ├── youtube/          # Project settings
    ├── accounts/         # Auth — register, login
    ├── videos/           # Upload, stream, like/dislike
    ├── templates/        # HTML templates
    └── static/           # CSS, JS, assets
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd YoutubeClone
```

### 2. Install dependencies

```bash
uv venv
uv sync
```

### 3. Create `.env`

```env
IMAGEKIT_PUBLIC_KEY=your_key
IMAGEKIT_PRIVATE_KEY=your_key
IMAGE_KIT_BASE_URL=https://api.imagekit.io
```

### 4. Run migrations

```bash
uv run python youtube/manage.py migrate
```

### 5. Start the server

```bash
uv run python youtube/manage.py runserver
```

> App running at → `http://127.0.0.1:8000/`

---

## 🌐 Routes

| Route | Description |
|---|---|
| `/` | Home feed |
| `/upload/` | Upload a video |
| `/<video_id>` | Watch a video |
| `/channel/<username>/` | Creator channel page |
| `/accounts/login/` | Log in |
| `/accounts/register/` | Register |

---

## 🧠 Data Models

### 🎬 Video
- Title, Description
- Video URL & Thumbnail URL
- View count, Like count, Dislike count

### 👍 VideoLike
- Tracks per-user reactions
- `1` = Like · `-1` = Dislike
- Prevents duplicate votes

---

## 🚀 Why This Project?

This isn't a UI-only clone. It's a **complete full-stack build** that covers:

- ✅ Backend logic with Django views and models
- ✅ User authentication system
- ✅ Media upload and cloud storage pipeline
- ✅ HLS video streaming integration
- ✅ Engagement system (likes, dislikes, views)

A solid, real-world project to learn or demonstrate full-stack Python development.

---

## 🗺️ Roadmap

- [ ] Comments system
- [ ] Subscriptions & notifications
- [ ] Search and filtering
- [ ] Watch history
- [ ] Creator dashboard with analytics
- [ ] Automated testing

---

## 🤝 Contributing

Fork the repo, make your changes, and open a PR. All contributions welcome! 🚀

---

## ⭐ Show Some Love

If this project helped you or you think it's cool:

- ⭐ **Star** the repo
- 🍴 **Fork** it and build on top
- 📢 **Share** it with others

---

<div align="center">
  Made with ❤️ by <strong>Goutham</strong>
</div>