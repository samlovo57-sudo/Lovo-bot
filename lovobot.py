from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
from datetime import datetime

TOKEN = "8895548744:AAG7ofsBSaRQpsi4wStfrNvGX4hUIjWucs8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bienvenido a LOVO SIGNALS\n\n"
        "Comandos disponibles:\n"
        "/start\n"
        "/ayuda\n"
        "/senal\n"
        "/ping"
    )

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Comandos disponibles:\n\n"
        "/start - Iniciar bot\n"
        "/senal - Obtener una señal\n"
        "/ping - Verificar que el bot está activo\n"
        "/ayuda - Mostrar ayuda"
    )

async def senal(update: Update, context: ContextTypes.DEFAULT_TYPE):

    activos = [
        "EUR/USD OTC",
        "GBP/USD OTC",
        "USD/JPY OTC",
        "AUD/USD OTC",
        "EUR/JPY OTC",
        "USD/CAD OTC"
    ]

    activo = random.choice(activos)
    direccion = random.choice(["🟢 CALL", "🔴 PUT"])
    confianza = random.randint(82, 96)
    hora = datetime.now().strftime("%H:%M:%S")

    mensaje = f"""
🚀 LOVO SIGNALS

💱 Activo: {activo}
📈 Dirección: {direccion}
⏰ Hora: {hora}
⌛ Expiración: 1 minuto
🔥 Confianza: {confianza}%

⚠️ Señal de prueba.
"""

    await update.message.reply_text(mensaje)

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🟢 Bot en línea y funcionando.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ayuda", ayuda))
app.add_handler(CommandHandler("senal", senal))
app.add_handler(CommandHandler("ping", ping))

print("Bot iniciado...")
app.run_polling() 