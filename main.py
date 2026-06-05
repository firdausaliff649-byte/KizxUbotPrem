#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KizxUbot Premium - Advanced Telegram Bot with AI & Broadcasting
Version: 2.2.0
Author: Kizx Development
Description: Full-featured bot with 220+ modules, AI, broadcast, blacklist management
"""

import os
import sys
import asyncio
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Aiogram imports
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage

# Local imports
from config import (
    BOT_TOKEN, 
    ADMIN_IDS, 
    BROADCAST_LIMIT,
    LOG_LEVEL,
    DB_PATH,
    API_KEY_OPENAI
)
from database import Database
from spam_detector import SpamDetector
from broadcast_system import BroadcastSystem
from blacklist_manager import BlacklistManager
from ai_module import AIModule
from handlers import (
    register_admin_handlers,
    register_user_handlers,
    register_broadcast_handlers,
    register_blacklist_handlers,
    register_ai_handlers
)
from middleware import LoggingMiddleware, RateLimitMiddleware
from utils import setup_logging, get_bot_stats

# Setup logging
logger = setup_logging()
logger.setLevel(getattr(logging, LOG_LEVEL))

class KizxUbot:
    """Main bot class managing all operations"""
    
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.storage = MemoryStorage()
        self.dp = Dispatcher(storage=self.storage)
        self.db = Database(DB_PATH)
        self.spam_detector = SpamDetector()
        self.broadcast_system = BroadcastSystem(self.bot, self.db)
        self.blacklist_manager = BlacklistManager(self.db)
        self.ai_module = AIModule(API_KEY_OPENAI)
        
        logger.info("🤖 KizxUbot Premium initialized")
    
    async def setup_handlers(self):
        """Register all handlers"""
        register_admin_handlers(self.dp, self.db, self.broadcast_system, self.blacklist_manager)
        register_user_handlers(self.dp, self.db, self.spam_detector)
        register_broadcast_handlers(self.dp, self.broadcast_system, self.blacklist_manager)
        register_blacklist_handlers(self.dp, self.blacklist_manager)
        register_ai_handlers(self.dp, self.ai_module)
        logger.info("✅ All handlers registered")
    
    async def setup_middleware(self):
        """Register middleware"""
        self.dp.message.middleware(LoggingMiddleware())
        self.dp.message.middleware(RateLimitMiddleware())
        logger.info("✅ Middleware configured")
    
    async def on_startup(self):
        """Bot startup event"""
        logger.info("🚀 Bot starting up...")
        await self.db.init()
        await self.setup_handlers()
        await self.setup_middleware()
        
        # Send startup notification to admins
        try:
            for admin_id in ADMIN_IDS:
                await self.bot.send_message(
                    admin_id,
                    "✅ <b>KizxUbot Premium</b> started!\n\n"
                    "📊 Status: <code>ONLINE</code>\n"
                    f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                    "🔧 Modules: 220+\n"
                    "🎯 Ready for operations!",
                    parse_mode="HTML"
                )
        except Exception as e:
            logger.error(f"Failed to send startup notification: {e}")
        
        logger.info("✅ Startup complete")
    
    async def on_shutdown(self):
        """Bot shutdown event"""
        logger.info("🛑 Bot shutting down...")
        await self.db.close()
        await self.bot.session.close()
        logger.info("✅ Shutdown complete")
    
    async def run(self):
        """Run the bot"""
        try:
            await self.on_startup()
            logger.info("🌟 Bot polling started")
            await self.dp.start_polling(self.bot, allowed_updates=self.dp.resolve_used_update_types())
        except KeyboardInterrupt:
            logger.info("Bot interrupted by user")
        except Exception as e:
            logger.error(f"Error running bot: {e}", exc_info=True)
        finally:
            await self.on_shutdown()

async def main():
    """Main entry point"""
    logger.info("=" * 50)
    logger.info("KizxUbot Premium - Starting")
    logger.info("=" * 50)
    
    bot = KizxUbot()
    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        sys.exit(1)
