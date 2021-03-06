from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
LIT_CHAT = env.str("LIT_CHAT")
LOG_CHAT = env.str("LOG_CHAT")
UMONEY = env.str("UMONEY")
BITCOINQR = env.str("BITCOINQR")
BITCOIN = env.str("BITCOIN")