from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 LOVO BOT\n\nComandos:\n/start\n/ayuda\n/senal\n/mercado\n/ping"
    )

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/senal - señal demo\n"
        "/mercado - análisis simple\n"
        "/ping - comprobar bot"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot funcionando 24/7 en Render")

async def senal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tiempo = "2"

    if context.args and context.args[0] in ["1", "2", "5", "15"]:
        tiempo = context.args[0]

    decision = random.choice([
        "🟢 COMPRA",
        "🔴 VENTA",
        "🟡 ESPERAR"
    ])

    await update.message.reply_text(
        f"📊 LOVO SIGNAL\n\n💱 EUR/USD\n🎯 Señal: {decision}\n⏱ Temporalidad: {tiempo} minuto(s)"
    )

async def mercado(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📈 Análisis DEMO\n\nTendencia: Alcista\nEMA20 > EMA50\nRSI: 56.4"
    )

if not TOKEN:
    raise ValueError("Falta la variable BOT_TOKEN")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ayuda", ayuda))
app.add_handler(CommandHandler("senal", senal))
app.add_handler(CommandHandler("mercado", mercado))
app.add_handler(CommandHandler("ping", ping))

print("LOVO BOT iniciado...")
app.run_polling()
