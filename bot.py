# importing Telegram API
import pickle
import matplotlib.pyplot as plt
from telegram import ParseMode
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import ConversationHandler
import os
import skyline as sk

# t.me/LPSkyline_bot

warning = u'\U000026A0'
buildings = u'\U0001F303'
buildings2 = u'\U0001F306'
saved = u'\U0001F4BE'
loaded = u'\U0001F4E4 '


# defining callback function for the /start command
def start(update, context):
    username = update.effective_chat.username
    missatge = ("Benvingut al SkylineBot %s!" + buildings2 + buildings) % username
    if 'skyline_ids' not in context.user_data:
        context.user_data['skyline_ids'] = {}
    if 'visitor' not in context.user_data:
        visitor = sk.SkylineVisitor()
        context.user_data['visitor'] = visitor
    context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)


def help(update, context):
    info = '''
    Comandes del bot:
    /start
            Inicia la conversa amb el Bot.

    /help
            Llista totes les comandes possibles del bot
            amb una breu descripcio

    /author
            Mostra el nom complet de l'autor del projecte
            i el seu correu electrònic de la facultat.

    /operacions
            Mostra tots els tipus d'operacions: crear, assignar, modificar skylines.

    /lst
            Mostra els identificadors definits i la seva corresponent àrea.

    /clean
            Esborra tots els identificadors definits

    /save id
            Guarda un skyline definit amb el nom id.sky

    /load id
            Carrega un skyline de l’arxiu id.sky
    '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=info)


def author(update, context):
    missatge = """
    David Carballo Montalbán\n(david.carballo@est.fib.upc.edu)"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=missatge)


def operacions(update, context):
    info = '''
    <u><b>Creació d’edificis</b></u>

     · <b>Simple</b> <code>(xmin, alçada, xmax)</code>
                xmin, xmax: especifiquen la posició d’inici i final (Coord X)
                alçada: l’alçada de l’edifici.
                    <i>Ex: (1, 2, 3)</i>

     · <b>Compostos</b>  <code>[(xmin, alçada, xmax), ...] </code>
            Defineix diversos edificis amb una llista d’edificis simples.
                            <i>Ex: [(1, 2, 3), (3, 4, 6)]</i>

     · <b>Aleatoris</b>  <code>{n, h, w, xmin, xmax}</code>
            Construeix n edificis, amb una alçada aleatòria entre 0 i h,
            amb una amplada aleatòria entre 1 i w,
            i una posició d’inici i de final aleatòria entre xmin i xmax.

     <u><b>Declarar skylines</b></u>
     · Assignacií --  <code> ID := skyline</code>
                    <i>Ex:  a := (1, 2, 3)      b := a * 3</i>

     <u><b>Operadors d’skylines</b></u>

     · Unió  --  <code>skyline + skyline</code>
     · Intersecció   --   <code>skyline * skyline</code>
     · Replicar N vegades    --    <code>skyline * N</code>
     · Moure a la dreta  --  <code>skyline + N</code>
     · Moure a la esquerra   --   <code>skyline - N</code>
     · Reflectir -- <code>-skyline</code>

        '''
    context.bot.send_message(chat_id=update.effective_chat.id, text=info, parse_mode=ParseMode.HTML)


def lst(update, context):
    if (not context.user_data['skyline_ids']):
        context.bot.send_message(chat_id=update.effective_chat.id, text=warning + " No hi hi cap identificador definit!\n-> Segueix els passos de la comanda /operacions")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="-----[ IDENTIFICADORS ]-----")
        ids = context.user_data['skyline_ids']
        for key in ids:
            (area, ymax) = sk.get_info(ids[key])
            context.bot.send_message(chat_id=update.effective_chat.id, text="Skyline %s -> area: %s" % (key, area))


def clean(update, context):
    if 'skyline_ids' in context.user_data:
        context.user_data['skyline_ids'] = {}
    context.bot.send_message(chat_id=update.effective_chat.id, text="Neteja feta")


def expr(update, context):
    msg = update.message.text
    v = context.user_data['visitor']
    result = sk.compile(msg, v)
    if(type(result) == list):
        # Print the result of skylines operation
        if not result:
            context.bot.send_message(chat_id=update.effective_chat.id, text=warning + "Skyline buit")
        fitxer = "result.png"
        p = sk.get_plot(result)
        p.plot()
        plt.savefig(fitxer, bbox_inches='tight')
        (area, ymax) = sk.get_info(result)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fitxer, 'rb'))
        context.bot.send_message(chat_id=update.effective_chat.id, text="area: %s \nalçada: %s" % (area, ymax))
        os.remove(fitxer)
    else:
        # Get the last skyline added (all skylines, this skyline_id)
        ident = result[1]
        fitxer = "%s.png" % ident
        context.user_data['skyline_ids'] = result[0]
        p = sk.get_plot(context.user_data['skyline_ids'][ident])
        p.plot()
        plt.savefig(fitxer, bbox_inches='tight')
        (area, ymax) = sk.get_info(context.user_data['skyline_ids'][ident])
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(fitxer, 'rb'))
        context.bot.send_message(chat_id=update.effective_chat.id, text="area: %s \nalçada: %s" % (area, ymax))
        os.remove(fitxer)


def save(update, context):
    try:
        if(len(context.args) < 1):
            context.bot.send_message(chat_id=update.effective_chat.id, text=warning + 'No s\'han afegit arguments: /save id')
        else:
            ids = context.args[0]
            if 'skyline_ids' not in context.user_data:
                context.bot.send_message(chat_id=update.effective_chat.id, text='El Skyline %s s\'ha guardat buit!' % (ids))
            else:
                name = ids + '.sky'
                identificadors = context.user_data['skyline_ids']
            pickle_out = open(name, 'wb')
            pickle.dump(identificadors, pickle_out)
            pickle_out.close()
            context.bot.send_message(chat_id=update.effective_chat.id, text=saved + ' Skyline %s guardat correctament!' % (ids))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='Error al guardar el skyline %s' % (ids))


def load(update, context):
    try:
        ids = context.args[0]
        name = ids + '.sky'
        pickle_in = open(name, 'rb')
        identificadors = pickle.load(pickle_in)
        pickle_in.close()
        context.user_data['skyline_ids'] = identificadors
        context.bot.send_message(chat_id=update.effective_chat.id, text=loaded + ' Skyline %s carregat!' % (ids))
    except Exception as e:
        print(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text=warning + 'Error al carregar l\'arxiu' + warning)


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# handling callbacks functions to the commands
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('operacions', operacions))
dispatcher.add_handler(CommandHandler('lst', lst))
dispatcher.add_handler(CommandHandler('clean', clean))
dispatcher.add_handler(CommandHandler('save', save))
dispatcher.add_handler(CommandHandler('load', load))

dispatcher.add_handler(MessageHandler(Filters.text, expr, pass_user_data=True))

# starting the bot
updater.start_polling()
