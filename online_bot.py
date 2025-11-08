import os
import random
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

# توکن ربات
TOKEN = os.getenv('TOKEN', '8231085757:AAHVk2agQEKM1mFZ3ULk9fQiqjLEttT8HZ0')

def start(update, context):
    user = update.message.from_user
    update.message.reply_text(
        f"🏭 **سیستم آنلاین تولیدی PU - نسخه سرور**\n\n"
        f"👋 سلام {user.first_name}!\n"
        f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        "📊 **دستورات مدیریتی:**\n"
        "• /register - ثبت اطلاعات شرکت\n"
        "• /new_order - ثبت سفارش جدید\n"
        "• /price_list - لیست قیمت مواد\n"
        "• /calculator - ماشین حساب تولید\n"
        "• /support - پشتیبانی فنی\n"
        "• /status - وضعیت سیستم\n\n"
        "🌐 **آنلاین 24/7 - نسخه سرور ابری**"
    )

def register_company(update, context):
    update.message.reply_text(
        "🏢 **ثبت اطلاعات شرکت تولیدی:**\n\n"
        "لطفا اطلاعات شرکت خود را به این فرمت ارسال کنید:\n\n"
        "📋 **فرمت:**\n"
        "شرکت: [نام شرکت]\n"
        "تلفن: [شماره تماس]\n"
        "آدرس: [شهر و منطقه]\n\n"
        "📝 **مثال:**\n"
        "شرکت: تولیدی کفش پویا\n"
        "تلفن: 09123456789\n"
        "آدرس: تهران، شهرک صنعتی"
    )

def new_order(update, context):
    order_info = """
    📝 **ثبت سفارش تولید جدید:**

    🏷️ **انواع محصول:**
    • دمپایی اسپرت PU
    • دمپایی راحتی بیمارستانی  
    • دمپایی کودک
    • دمپایی لاکچری

    🔢 **مقادیر پیشنهادی:**
    • 500 جفت (شروع تولید)
    • 1000 جفت (مقدار بهینه)
    • 5000 جفت (تخفیف حجمی)

    💰 **برای محاسبه قیمت: /calculator**
    """
    update.message.reply_text(order_info)

def price_list(update, context):
    prices = """
    📋 **لیست قیمت مواد اولیه (هزار تومان):**

    🧪 **پلی یورتان (PU):**
    • PU نرم: 45-55
    • PU سخت: 50-60

    🌟 **دیگر مواد:**
    • EVA: 25-35
    • ترموپلاستیک: 30-40

    🏭 **هزینه تولید (هر جفت):**
    • تزریق: 3-6 هزار
    • مونتاژ: 2-4 هزار
    """
    update.message.reply_text(prices)

def production_calculator(update, context):
    calculator = """
    🧮 **ماشین حساب تولید:**

    💰 **500 جفت:**
    • کل: 14-21 میلیون
    • هر جفت: 28-42 هزار

    💰 **1000 جفت:**
    • کل: 23-34 میلیون  
    • هر جفت: 23-34 هزار
    """
    update.message.reply_text(calculator)

def support(update, context):
    support_text = """
    📞 **پشتیبانی فنی:**\n
    • فنی: 09123456789
    • فروش: 09129876543
    • لجستیک: 09127654321
    """
    update.message.reply_text(support_text)

def status(update, context):
    update.message.reply_text("🟢 **وضعیت سیستم: فعال و آنلاین**")

def handle_message(update, context):
    """پردازش پیام‌های متنی"""
    text = update.message.text
    
    if 'شرکت:' in text and 'تلفن:' in text:
        update.message.reply_text("✅ اطلاعات شرکت ثبت شد! /new_order")
    elif 'سفارش' in text.lower():
        update.message.reply_text("📝 برای ثبت سفارش: /new_order")

def main():
    print("🚀 در حال راه‌اندازی نسخه آنلاین ربات...")
    
    # راه‌اندازی با نسخه سازگار
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    
    # ثبت دستورات
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register_company))
    dispatcher.add_handler(CommandHandler("new_order", new_order))
    dispatcher.add_handler(CommandHandler("price_list", price_list))
    dispatcher.add_handler(CommandHandler("calculator", production_calculator))
    dispatcher.add_handler(CommandHandler("support", support))
    dispatcher.add_handler(CommandHandler("status", status))
    
    # پردازش پیام‌های متنی
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    print("✅ ربات آنلاین فعال شد!")
    print("🌐 در حال اتصال به سرورهای تلگرام...")
    
    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
