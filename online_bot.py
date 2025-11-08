import os
import random
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# توکن ربات
TOKEN = os.getenv('TOKEN', '8231085757:AAHVk2agQEKM1mFZ3ULk9fQiqjLEttT8HZ0')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    await update.message.reply_text(
        f"🏭 **سیستم آنلاین تولیدی PU**\n\n"
        f"👋 سلام {user.first_name}!\n"
        "📊 **دستورات:**\n"
        "• /register - ثبت شرکت\n"
        "• /new_order - سفارش جدید\n"
        "• /price_list - قیمت مواد\n"
        "• /calculator - ماشین حساب\n"
        "• /support - پشتیبانی\n"
        "• /status - وضعیت سیستم\n\n"
        "🌐 **آنلاین 24/7**"
    )

async def register_company(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏢 **ثبت اطلاعات شرکت:**\n\n"
        "فرمت:\nشرکت: نام\nتلفن: شماره\nآدرس: آدرس"
    )

async def new_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    order_info = """
    📝 **سفارش جدید:**
    
    • دمپایی اسپرت PU
    • دمپایی راحتی
    • دمپایی کودک
    
    💰 /calculator
    """
    await update.message.reply_text(order_info)

async def price_list(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prices = """
    📋 **قیمت مواد (هزار تومان):**
    
    🧪 PU: 45-55
    🌟 EVA: 25-35
    🏭 تولید: 3-6
    """
    await update.message.reply_text(prices)

async def production_calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    calculator = """
    🧮 **ماشین حساب:**
    
    🔹 500 جفت:
    • کل: 14-21 میلیون
    • هر جفت: 28-42 هزار
    """
    await update.message.reply_text(calculator)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📞 پشتیبانی: 09123456789")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 سیستم فعال و آنلاین")

def main():
    logging.basicConfig(level=logging.INFO)
    print("🚀 راه‌اندازی ربات آنلاین...")
    
    application = Application.builder().token(TOKEN).build()
    
    # دستورات
    commands = [
        ("start", start),
        ("register", register_company),
        ("new_order", new_order),
        ("price_list", price_list),
        ("calculator", production_calculator),
        ("support", support),
        ("status", status)
    ]
    
    for command, handler in commands:
        application.add_handler(CommandHandler(command, handler))
    
    print("✅ ربات آنلاین فعال شد!")
    application.run_polling()

if __name__ == '__main__':
    main()
