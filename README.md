<h1 align="center">🎬 YouTube Clone</h1>

<p align="center">
  A full-stack Django-based video platform inspired by YouTube  
</p>

<p align="center">
  <img src="docs/screenshots/home-feed.png" width="80%" />
</p>

---

## ✨ Features

### 👀 Viewer Experience
- Browse latest uploaded videos
- Watch videos with streaming playback (HLS supported)
- Like / Dislike system (1 vote per user)
- View counts & video stats

### 🎥 Creator Experience
- User authentication (Register/Login)
- Upload videos (MP4, WebM, MOV, AVI)
- Optional custom thumbnails
- Auto-generated thumbnails
- Channel page for each creator
- Delete own videos

### ⚡ Media Handling
- ImageKit integration for storage & delivery
- Optimized video streaming
- Dynamic thumbnail generation

---

## 🛠️ Tech Stack

- 🐍 Python 3.13
- 🌐 Django 6
- 🗄️ SQLite
- ☁️ ImageKit (media storage)
- 🎨 HTML, CSS, JavaScript
- 🔐 python-dotenv

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

```bash
YoutubeClone/
│── pyproject.toml
│── README.md
│── docs/
│   └── screenshots/
│── youtube/
│   ├── manage.py
│   ├── db.sqlite3
│   ├── youtube/
│   ├── accounts/
│   ├── videos/
│   ├── templates/
│   └── static/
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repo
```bash
git clone <your-repo-url>
cd YoutubeClone
```

### 2️⃣ Setup environment
```bash
uv venv
uv sync
```

### 3️⃣ Create `.env`
```env
IMAGEKIT_PUBLIC_KEY=your_key
IMAGEKIT_PRIVATE_KEY=your_key
IMAGE_KIT_BASE_URL=https://api.imagekit.io
```

### 4️⃣ Run migrations
```bash
uv run python youtube/manage.py migrate
```

### 5️⃣ Start server
```bash
uv run python youtube/manage.py runserver
```

👉 Open: http://127.0.0.1:8000/

---

## 🌐 Routes

| Route | Description |
|------|------------|
| `/` | Home Feed |
| `/upload/` | Upload Video |
| `/<video_id>` | Video Page |
| `/channel/<username>/` | Channel Page |
| `/accounts/login/` | Login |
| `/accounts/register/` | Register |

---

## 🧠 Data Models

### 🎬 Video
- Title, Description  
- Video URL & Thumbnail  
- Views, Likes, Dislikes  

### 👍 VideoLike
- Stores user reactions  
- `1 = Like`, `-1 = Dislike`  
- Prevents duplicate votes  

---

## 🚧 Roadmap

- 💬 Comments system  
- 🔔 Subscriptions  
- 🔍 Search & filtering  
- 📜 Watch history  
- 📊 Creator dashboard  
- 🧪 Automated testing  

---

## 💡 Why This Project?

This is not just a UI clone.

It includes:
- Full backend logic  
- Authentication system  
- Media upload pipeline  
- Streaming integration  

👉 A solid real-world full-stack project 💪

---

## 🤝 Contributing

Feel free to fork, improve, and submit PRs 🚀

---

## ⭐ Show Some Love

If you like this project:

- ⭐ Star the repo  
- 🍴 Fork it  
- 📢 Share it  

---

<p align="center">Made with ❤️ by Goutham</p>
