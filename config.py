# -*- coding: utf-8 -*-
"""
Configuration file for KizxUbot Premium
"""

import os
from dotenv import load_dotenv

load_dotenv()

# Bot Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN", "8796670391:AAESeHo9zhwB6RU4ebqik-MBZTjgNLvyU-4")
BOT_USERNAME = "KizxUbot"
BOT_VERSION = "2.2.0"

# Admin Configuration
ADMIN_IDS = [int(id.strip()) for id in os.getenv("ADMIN_IDS", "1234567890").split(",")]

# Database Configuration
DB_PATH = os.getenv("DB_PATH", "data/bot_database.db")
DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # sqlite, postgresql, mysql

# Broadcast Configuration
BROADCAST_LIMIT = int(os.getenv("BROADCAST_LIMIT", "30"))  # Messages per second
BROADCAST_TIMEOUT = int(os.getenv("BROADCAST_TIMEOUT", "5"))  # Timeout per message
MAX_BROADCAST_SIZE = int(os.getenv("MAX_BROADCAST_SIZE", "50000"))  # Max recipients

# Blacklist Configuration
BLACKLIST_AUTO_UPDATE = os.getenv("BLACKLIST_AUTO_UPDATE", "true").lower() == "true"
BLACKLIST_SYNC_INTERVAL = int(os.getenv("BLACKLIST_SYNC_INTERVAL", "300"))  # 5 minutes

# Spam Detection Configuration
SPAM_SENSITIVITY = float(os.getenv("SPAM_SENSITIVITY", "0.7"))
SPAM_KEYWORDS_FILE = os.getenv("SPAM_KEYWORDS_FILE", "data/spam_keywords.json")
AUTO_BLOCK_SPAM = os.getenv("AUTO_BLOCK_SPAM", "true").lower() == "true"

# AI Module Configuration
AI_ENABLED = os.getenv("AI_ENABLED", "true").lower() == "true"
API_KEY_OPENAI = os.getenv("API_KEY_OPENAI", "")
API_KEY_GROQ = os.getenv("API_KEY_GROQ", "")
AI_MODEL = os.getenv("AI_MODEL", "gpt-3.5-turbo")
AI_MAX_TOKENS = int(os.getenv("AI_MAX_TOKENS", "500"))

# Rate Limiting
RATE_LIMIT_ENABLED = os.getenv("RATE_LIMIT_ENABLED", "true").lower() == "true"
RATE_LIMIT_MESSAGES = int(os.getenv("RATE_LIMIT_MESSAGES", "5"))  # Messages
RATE_LIMIT_SECONDS = int(os.getenv("RATE_LIMIT_SECONDS", "10"))  # Per seconds

# Logging Configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.getenv("LOG_FILE", "logs/bot.log")
LOG_MAX_BYTES = int(os.getenv("LOG_MAX_BYTES", "10485760"))  # 10MB
LOG_BACKUP_COUNT = int(os.getenv("LOG_BACKUP_COUNT", "5"))

# Webhook Configuration (for hosting)
WEBHOOK_ENABLED = os.getenv("WEBHOOK_ENABLED", "false").lower() == "true"
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://yourdomain.com/webhook")
WEBHOOK_PORT = int(os.getenv("WEBHOOK_PORT", "8443"))

# Performance Configuration
WORKER_THREADS = int(os.getenv("WORKER_THREADS", "10"))
CONNECTION_POOL_SIZE = int(os.getenv("CONNECTION_POOL_SIZE", "20"))

# API Configuration
API_TIMEOUT = int(os.getenv("API_TIMEOUT", "30"))  # seconds
API_RETRY_COUNT = int(os.getenv("API_RETRY_COUNT", "3"))

# Features
FEATURES = {
    "broadcast": True,
    "blacklist": True,
    "spam_detection": True,
    "ai_responses": True,
    "admin_panel": True,
    "user_stats": True,
    "auto_blocking": True,
    "webhook_support": WEBHOOK_ENABLED,
}

# Message Templates
MESSAGES = {
    "welcome": "👋 Welcome to <b>KizxUbot Premium</b>!\n\n"
               "🎯 <b>Features:</b>\n"
               "• 220+ Advanced Modules\n"
               "• AI-powered Responses\n"
               "• Broadcasting System\n"
               "• Blacklist Management\n"
               "• Real-time Spam Detection\n\n"
               "Type /help for more information.",
    
    "help": "<b>📚 Available Commands:</b>\n\n"
            "/start - Start the bot\n"
            "/help - Show this help menu\n"
            "/status - Bot status\n"
            "/ai - Ask AI\n"
            "/broadcast - Send broadcast\n"
            "/blacklist - Manage blacklist\n"
            "/stats - View statistics\n"
            "/admin - Admin panel (admin only)\n",
    
    "unauthorized": "❌ You don't have permission to use this command.",
    
    "error": "⚠️ An error occurred: {error}",
}

# Ensure data directory exists
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
