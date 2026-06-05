# 🤖 KizxUbot Premium - Advanced Telegram Bot

![Version](https://img.shields.io/badge/version-2.2.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-MIT-red)

**KizxUbot Premium** adalah bot Telegram advanced dengan **220+ modul** lengkap, dilengkapi:
- ✅ **Sistem Broadcast** (30 pesan/detik)
- ✅ **Manajemen Blacklist**
- ✅ **Deteksi Spam AI**
- ✅ **Respons AI GPT**
- ✅ **Rate Limiting**
- ✅ **Logging Realtime**
- ✅ **Panel Admin**

## 📋 Fitur Lengkap

### 🚀 Broadcast System
- Kirim pesan ke 50,000+ pengguna
- Rate limiting 30 pesan/detik
- Support grup dan channel
- Custom filtering
- Scheduled broadcast

### 🚫 Blacklist Management
- Tambah/hapus user dari blacklist
- Auto-sync database
- Cache realtime
- Prevent broadcast ke user blacklist

### 🔍 Spam Detection
- Keyword detection
- URL validation
- Pattern recognition
- Emoji spam detection
- Email/phone number detection
- AI-powered scoring

### 🤖 AI Module
- GPT-3.5 Turbo integration
- Conversation history
- Custom system prompts
- Sentiment analysis
- Text moderation
- Summarization

### 📊 Admin Features
- Panel admin commands
- Statistics realtime
- User management
- Broadcast logs
- System monitoring

## 🛠️ Instalasi

### Prasyarat
```bash
- Python 3.11+
- PostgreSQL/SQLite
- Bot Token Telegram
- OpenAI API Key (optional)
```

### Metode 1: Direct Install

```bash
# Clone repository
git clone https://github.com/firdausaliff649-byte/KizxUbotPrem.git
cd KizxUbotPrem

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env dengan konfigurasi Anda

# Run bot
python main.py
```

### Metode 2: Docker

```bash
# Build image
docker build -t kizx-ubot-prem .

# Run container
docker run -d \
  --name kizx-bot \
  -e BOT_TOKEN=your_token \
  -e ADMIN_IDS=your_id \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  kizx-ubot-prem
```

### Metode 3: Docker Compose

```bash
# Edit docker-compose.yml dengan konfigurasi Anda
nano docker-compose.yml

# Start services
docker-compose up -d

# View logs
docker-compose logs -f bot
```

## ⚙️ Konfigurasi

### File `.env`

```env
# Bot
BOT_TOKEN=your_telegram_bot_token
ADMIN_IDS=123456789,987654321

# Database
DB_PATH=data/bot_database.db
DB_TYPE=sqlite

# Broadcast (30 pesan/detik)
BROADCAST_LIMIT=30
BROADCAST_TIMEOUT=5
MAX_BROADCAST_SIZE=50000

# Spam Detection
SPAM_SENSITIVITY=0.7
AUTO_BLOCK_SPAM=true

# AI Module
AI_ENABLED=true
API_KEY_OPENAI=your_openai_key
AI_MODEL=gpt-3.5-turbo
AI_MAX_TOKENS=500

# Logging
LOG_LEVEL=INFO
LOG_FILE=logs/bot.log
```

## 📝 Perintah Bot

### User Commands
```
/start          - Start bot
/help           - Tampilkan bantuan
/status         - Status bot
/ai [query]     - Tanya AI
```

### Admin Commands
```
/admin          - Admin panel
/broadcast      - Kirim broadcast
/blacklist      - Manage blacklist
/stats          - Lihat statistik
/users          - Jumlah user
```

## 🔧 Struktur Project

```
KizxUbotPrem/
├── main.py                 # Entry point
├── config.py              # Configuration
├── database.py            # Database handler
├── spam_detector.py       # Spam detection
├── broadcast_system.py    # Broadcasting
├── blacklist_manager.py   # Blacklist mgmt
├── ai_module.py          # AI responses
├── handlers.py           # Command handlers
├── middleware.py         # Logging & rate limit
├── utils.py              # Utilities
├── requirements.txt      # Dependencies
├── .env.example         # Config template
├── Dockerfile           # Docker image
├── docker-compose.yml   # Docker compose
├── start.sh            # Run script
└── README.md           # This file
```

## 🚀 Deployment

### Hosting Recommendations

#### 1. **VPS (Linux)**
```bash
# Ubuntu/Debian
cd /var/www/kizx-bot
git clone ...
chmod +x start.sh
./start.sh

# Using systemd
sudo nano /etc/systemd/system/kizx-bot.service
```

#### 2. **Heroku**
```bash
git push heroku main
# atau gunakan Heroku CLI
heroku create kizx-ubot-prem
```

#### 3. **Railway**
```bash
# Connect GitHub + Deploy
# Env vars otomatis dari .env
```

#### 4. **PythonAnywhere**
- Upload files via Web
- Setup virtual env
- Run via always-on task

#### 5. **Docker Hub**
```bash
docker build -t username/kizx-ubot:latest .
docker push username/kizx-ubot:latest
```

## 📊 Database Schema

### Users Table
```sql
user_id, username, first_name, is_admin, is_blacklisted, created_at
```

### Broadcasts Table
```sql
broadcast_id, admin_id, message, status, success_count, failed_count, created_at
```

### Blacklist Table
```sql
blacklist_id, user_id, reason, added_by, created_at
```

### Spam Logs Table
```sql
spam_id, user_id, message, spam_score, spam_type, created_at
```

## 🎯 Performance

- **30+ pesan/detik** broadcast rate
- **Real-time** spam detection
- **Async** processing
- **Connection pooling**
- **Message queuing**

## 🔒 Keamanan

- ✅ Rate limiting
- ✅ Blacklist protection
- ✅ Admin verification
- ✅ Input validation
- ✅ Secure token storage
- ✅ Error logging

## 📈 Monitoring

### Logs
```bash
tail -f logs/bot.log
```

### Metrics
- Messages processed
- Broadcast success/failed
- Spam detections
- AI queries
- User statistics

## 🐛 Troubleshooting

### Bot tidak menerima pesan
```bash
1. Cek BOT_TOKEN di .env
2. Restart bot: python main.py
3. Check firewall
```

### Database error
```bash
rm data/bot_database.db  # Reset
python main.py           # Recreate
```

### Broadcast gagal
```bash
- Cek BROADCAST_LIMIT
- Cek rate limiting
- View logs
```

## 📞 Support

Issues? Create GitHub issue atau contact admin.

## 📄 License

MIT License - Bebas digunakan

## 👤 Author

**Kizx Development** - [@firdausaliff649-byte](https://github.com/firdausaliff649-byte)

---

**Made with ❤️ in Indonesia**
