#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = 'ᴍᴀsᴛᴇʀ'
    ST_BN1_URL = 'https://t.me/owner_of_qtmve'
    ST_BN2_NAME = 'ᴜᴘᴅᴀᴛᴇs'
    ST_BN2_URL = 'https://t.me/QTVS_BOT_X_CLOUD'
    ST_MSG = '''<i>ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ɪɴ ᴅᴍ!!
    ɴᴏᴡ ᴀʟʟ ʏᴏᴜʀ ʟɪɴᴋs/Files ᴡɪʟʟ ᴄᴏᴍᴇ ʜᴇʀᴇ 🕺.</i>
<b>ᴛʏᴘᴇ {help_command} ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs</b>'''
    ST_BOTPM = '''<i>Now, This bot will send all your files and links here. Start Using ...</i>'''
    ST_UNAUTH = '''<i>You Are not authorized user! Deploy your Own bot Contact 🕺<a href='https://t.me/owner_of_qtmve'> bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>'''
    USED_TOKEN = '''<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>ᴛᴇᴍᴘ ᴛᴏᴋᴇɴ:</b> <code>{token}</code>
<b>ᴠᴀʟɪᴅɪᴛʏ:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = '✅️ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ✅'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>ᴀʟʀᴇᴀᴅʏ ʙᴏᴛ ʟᴏɢɪɴ ɪɴ!</b>'
    INVALID_PASS = '<b>ɪɴᴠᴀʟɪᴅ ᴘᴀssᴡᴏʀᴅ!</b>\n\ᴋɪɴᴅʟ ᴘᴜᴛ ᴛʜᴇ ᴄᴏʀʀᴇᴄᴛ ᴘᴀssᴡᴏʀᴅ .'
    PASS_LOGGED = '<b>Bot ᴘᴇʀᴍᴀɴᴇɴᴛ ʟᴏɢɪɴ ʏSuccessfully!</b>'
    LOGIN_USED = '<b>ʙᴏᴛ ʟᴏɢɪɴ ᴜsᴀɢᴇ :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = '📑 Log ᴅɪsᴘʟᴀy'
    WEB_PASTE_BT = '📨 ᴡᴇʙ ᴘᴀsᴛᴇ (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'ʙᴀsɪ'
    USER_BT = 'ᴜsᴇ'
    MICS_BT = 'ᴍɪᴄ'
    O_S_BT = 'ᴏᴡɴᴇʀ&sᴜᴅ'
    CLOSE_BT = 'ᴄʜᴏsᴇᴄʜ'
    HELP_HEADER = "㊂ <b><i>ʜᴇʟᴘ ɢᴜɪᴅᴇ ᴍᴇɴᴜ!</i></b>\n\n<b>NOTE: <i>ᴄʟɪᴄᴋ ᴏɴ ᴀɴʏ CMD ᴛᴏ sᴇᴇ ᴍᴏʀᴇ ᴍɪɴᴏʀ ᴅᴇᴛᴀʟɪs.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''⌬ <b><i>BOT STATISTICS :</i></b>
┖ <b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</b> {bot_uptime}

┎ <b><i>ʀᴀᴍ ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ <b><i>sᴡᴀᴘ ᴍᴇᴍᴏʀʏ :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ <b><i>ᴅɪsᴋ :</i></b>
┃ {disk_bar} {disk}%
┃ <b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ʀᴇᴀᴅ :</b> {disk_read}
┃ <b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ᴡʀɪᴛᴇ :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    '''
    SYS_STATS = '''⌬ <b><i>ᴏs sʏsᴛᴇᴍ :</i></b>
┠ <b>ᴏs ᴜᴘᴛɪᴍᴇ :</b> {os_uptime}
┠ <b>ᴏs ᴠᴇʀsɪᴏɴ :</b> {os_version}
┖ <b>ᴏs ᴀʀᴄʜ :</b> {os_arch}

⌬ <b><i>ɴᴇᴛᴡᴏʀᴋ sᴛᴀᴛs :</i></b>
┠ <b>ᴜᴘʟᴏᴀᴅ ᴅᴀᴛᴀ:</b> {up_data}
┠ <b>ᴅᴏᴡɴʟᴏᴀᴅ ᴅᴀᴛᴀ:</b> {dl_data}
┠ <b>ᴘᴋᴛs sᴇɴᴛ:</b> {pkt_sent}k
┠ <b>ᴘᴋᴛs ʀᴇᴄᴇɪᴠᴇᴅ:</b> {pkt_recv}k
┖ <b>ᴛᴏᴛᴀʟ I/O ᴅᴀᴛᴀ:</b> {tl_data}

┎ <b>ᴄᴘᴜ :</b>
┃ {cpu_bar} {cpu}%
┠ <b>ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}
┠ <b>sʏsᴛᴇᴍ ᴀᴠɢ ʟᴏᴀᴅ :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>ᴛᴏᴛᴀʟ ᴄᴏʀᴇ(s) :</b> {total_core}
┖ <b>ᴜsᴀʙʟᴇ ᴄᴘᴜ(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''⌬ <b><i>ʀᴇᴘᴏ sᴛᴀᴛɪsᴛɪᴄs :</i></b>
┠ <b>ʙᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ :</b> {last_commit}
┠ <b>ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ :</b> {bot_version}
┠ <b>ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ :</b> {lat_version}
┖ <b>ʟᴀsᴛ ᴄʜᴀɴɢᴇʟᴏɢ :</b> {commit_details}

⌬ <b>ʀᴇᴍᴀʀᴋs :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''⌬ <b><i>ʙᴏᴛ ʟɪᴍɪᴛᴀᴛɪᴏɴs :</i></b>
┠ <b>ᴅɪʀᴇᴄᴛ Limitʟɪᴍɪᴛ :</b> {DL} GB
┠ <b>ᴛᴏʀʀᴇɴᴛ ʟɪᴍɪᴛ :</b> {TL} GB
┠ <b>ɢᴅʀɪᴠᴇ ʟɪᴍɪᴛ :</b> {GL} GB
┠ <b>ʏᴛ-ᴅʟᴛ ʟɪᴍɪᴛ :</b> {YL} GB
┠ <b>ᴘʟᴀʏʟɪsᴛ ʟɪᴍɪᴛ :</b> {PL}
┠ <b>ᴍᴇɢᴀ ʟɪᴍɪᴛ :</b> {ML} GB
┠ <b>ᴄʟᴏɴᴇ ʟɪᴍɪᴛ :</b> {CL} GB
┖ <b>ʟᴇᴇᴄʜ ʟɪᴍɪᴛ :</b> {LL} GB

┎ <b>ᴛᴏᴋᴇɴ ᴠᴀʟɪᴅɪᴛʏ :</b> {TV}
┠ <b>ᴜsᴇʀ ᴛɪᴍᴇ ʟɪᴍɪᴛ :</b> {UTI} / task
┠ <b>ᴜsᴇʀ ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</b> {UT}
┖ <b>ʙᴏᴛ ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>ʀᴇsᴛᴀʀᴛɪɴɢ--->>...</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''⌬ <b><i>ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ 🔥!</i></b>
┠ <b>ᴅᴀᴛᴇ:</b> {date}
┠ <b>ᴛɪᴍᴇ:</b> {time}
┠ <b>ᴛɪᴍᴇᴢᴏɴᴇ:</b> {timz}
┖ <b>ᴠᴇʀsɪᴏɴ:</b> {version}'''
    RESTARTED = '''⌬ <b><i>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ!</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>sᴛᴀʀᴛɪɴɢ ᴘɪɴɢ..</i>'
    PING_VALUE = '<b>ᴘᴏɴɢ</b>\n<code>{value} ms..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ</i></b>
┠ <b>ᴍᴏᴅᴇ:</b> {Mode}
┖ <b>ʙʏ:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>sᴏᴜʀᴄᴇ:</b>
┖ <b>ᴀᴅᴅᴇᴅ ᴏɴ:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "➲ <b><u>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ :</u></b>\n┃\n┖ <b>ʟɪɴᴋ:</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"
    L_LOG_START =           "➲ <b><u>ʟᴇᴇᴄʜ sᴛᴀʀᴛᴇᴅ :</u></b>\n┃\n┠ <b>ᴜsᴇʀ :</b> {mention} ( #ID{uid} )\n┖ <b>sᴏᴜʀᴄᴇ :</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>ɴᴀᴍᴇ {ɴᴀᴍᴇ}</i></b>\n┃\n'
    SIZE =                  '┠ <b>sɪᴢᴇ: </b>{Size}\n'
    ELAPSE =                '┠ <b>ᴇʟᴀᴘsᴇᴅ: </b>{Time}\n'
    MODE =                  '┠ <b>ᴍᴏᴅᴇ: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         '┠ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs: </b>{Files}\n'
    L_CORRUPTED_FILES =     '┠ <b>ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs: </b>{Corrupt}\n'
    L_CC =                  '┖ <b>ʙʏ: </b>{Tag}\n\n'
    PM_BOT_MSG =            '➩ <b><i>ғɪʟᴇs(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ</i></b>'
    L_BOT_MSG =             '➩ <b><i>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>'
    L_LL_MSG =              '➩ <b><i>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇss ᴠɪᴀ ʟɪɴᴋs...</i></b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                '┠ <b>ᴛʏᴘᴇ: </b>{Mimetype}\n'
    M_SUBFOLD =             '┠ <b>sᴜʙғᴏʟᴅᴇʀs: </b>{Folder}\n'
    TOTAL_FILES =           '┠ <b>ғɪʟᴇs: </b>{Files}\n'
    RCPATH =                '┠ <b>ᴘᴀᴛʜ: </b><code>{RCpath}</code>\n'
    M_CC =                  '┖ <b>ʙʏ: </b>{Tag}\n\n'
    M_BOT_MSG =             '➲ <b><i>ʟɪɴᴋ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      '☁️ ᴄʟᴏᴜᴅ ʟɪɴ'
    SAVE_MSG =        '📨 sᴀᴠᴇ ᴍᴀssᴀɢ'ᴇ
    RCLONE_LINK =     '♻️ ʀᴄʟᴏɴᴇ ʟɪɴ'
    DDL_LINK =        '📎 {Serv} Link'
    SOURCE_URL =      '🔐 sᴏᴜʀᴄᴇ ʟɪɴ'
    INDEX_LINK_F =    '🗂 ɪɴᴅᴇx ʟɪɴ'
    INDEX_LINK_D =    '⚡ ɪɴᴅᴇx ʟɪɴ'
    VIEW_LINK =       '🌐 ᴠɪᴇᴡ ʟɪɴ'
    CHECK_PM =        '📥 ᴠɪᴇᴡ ɪɴ ʙᴏᴛ ᴘ'
    CHECK_LL =        '🖇 ᴠɪᴇᴡ ɪɴ ʟɪɴᴋs ʟᴏ'
    MEDIAINFO_LINK =  '📃 ᴍᴇᴅɪᴀɪɴғ'
    SCREENSHOTS =     '🖼 sᴄʀᴇᴇɴsʜᴏᴛ'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>🎞 ɴᴀᴍᴇ {Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\n┃ {Bar}'
    PROCESSED =         '\n┠ <b>🚀ᴘʀᴏᴄᴇssᴇᴅ:</b> {Processed}'
    STATUS =            '\n┠ <b>sᴛᴀᴛᴜs:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>ᴇᴛᴀ:</b> {Eta}'
    SPEED =             '\n┠ <b>⚡sᴘᴇᴇᴅ:</b> {Speed}'
    ELAPSED =                                     ' | <b>ᴇʟᴀᴘsᴇᴅ:</b> {Elapsed}'
    ENGINE =            '\n┠ <b>⛓️ᴇɴɢɪɴᴇ:</b> {Engine}'
    STA_MODE =          '\n┠ <b>⚙️ᴍᴏᴅᴇ:</b> {Mode}'
    SEEDERS =           '\n┠ <b>🌱sᴇᴇᴅᴇʀs:</b> {Seeders} | '
    LEECHERS =                                           '<b>🐌ʟᴇᴇᴄʜᴇʀs:</b> {Leechers}'

    ####--------SEEDING----------
    SEED_SIZE =      '\n┠ <b>sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\n┠ <b>sᴘᴇᴇᴅ: </b> {Speed} | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅᴇᴅ: </b> {Upload}'
    RATIO =          '\n┠ <b>ʀᴀᴛɪᴏ: </b> {Ratio} | '
    TIME =                                         '<b>ᴛɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\n┠ <b>ᴇɴɢɪɴᴇ:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\n┠ <b>sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\n┠ <b>ᴇɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n┠ <b>🫅ᴜsᴇʀ:</b> <code>{User}</code> | '
    ID =                                                        '<b>🆔ID:</b> <code>{Id}</code>'
    BTSEL =          '\n┠ <b>🦠Select:</b> {Btsel}'
    CANCEL =         '\n┖ {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = '⌬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>\n'
    TASKS =  '┠ <b>ᴛᴀsᴋs:</b> {Tasks}\n'
    BOT_TASKS = '┠ <b>ᴛᴀsᴋs:</b> {Tasks}/{Ttask} | <b>ᴀᴠʟ:</b> {Free}\n'
    Cpu = '┠ <b>ᴄᴘᴜ:</b> {cpu}% | '
    FREE =                      '<b>F:</b> {free} [{free_p}%]'
    Ram = '\n┠ <b>ʀᴀᴍ:</b> {ram}% | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}'
    DL = '\n┖ <b>ᴅʟ:</b> {DL}/s | '
    UL =                        '<b>ᴜʟ:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = '⫷'
    REFRESH = 'ᴘᴀɢᴇs\n{Page}'
    NEXT = '⫸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'ғɪʟᴇ/ғᴏʟᴅᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅʀɪᴠᴇ.\ɴʜᴇʀ ᴀʀᴇ {content} ʟɪsᴛ ʀᴇsᴜʟᴛs:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>ᴄᴏᴜɴᴛɪɴɢ:</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\n┃\n'
    COUNT_SIZE = '┠ <b>sɪᴢᴇ: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = '┠ <b>ᴛʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  '┠ <b>sᴜʙғᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = '┠ <b>ғɪʟᴇs: </b>{COUNT_FILE}\n'
    COUNT_CC =   '┖ <b>ʙʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>sᴇᴀʀᴄʜɪɴɢ. .  ғᴏ <i>{NAME}</i></b>'
    LIST_FOUND = '<b>ғᴏᴜɴᴅ {NO} ʀᴇsᴜʟᴛ ғᴏʀ <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'ɴᴏ ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>ɴᴏ ᴀᴄᴛɪᴠᴇ ᴅᴏᴡɴʟᴏᴀᴅs!</i>
    
⌬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>
┠ <b>ᴄᴘᴜ:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>ʀᴀᴍ:</b> {ram} | <b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''㊂ <b><u>ᴜsᴇʀ sᴇᴛᴛɪɴɢs :</u></b>
        
┎<b> ɴᴀᴍᴇ :</b> {NAME} ( <code>🆔{ID}</code> )
┠<b> Username :</b> 🫅{USERNAME}
┠<b> ᴛᴇʟᴇɢʀᴀᴍ DC :</b> {DC}
┖<b> ʟᴀɴɢᴜᴀɢᴇ :</b> {LANG}

➲ <u><b>ᴀᴠᴀɪʟᴀʙʟᴇ ᴀʀɢs:</b></u>
• <b>-s</b> or <b>-sᴇᴛ</b>: sᴇᴛ ᴅɪʀᴇᴄᴛʟʏ ᴠɪᴀ Arg'''

    UNIVERSAL = '''㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
┠<b> ᴅᴀɪʟʏ ᴛᴀsᴋs :</b> <code>{DT}</code> ᴘᴇʀ ᴅᴀʏ
┠<b> ʟᴀsᴛ ʙᴏᴛ U𝟸sed :</b> <code>{LAST_USED}</code>
┠<b> ᴜsᴇʀ sᴇssɪᴏɴ :</b> <code>{USESS}</code>
┠<b> ᴍᴇᴅɪᴀɪɴғᴏ ᴍᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
┠<b> sᴀᴠᴇ ᴍᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
┖<b> ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''㊂ <b><u>ᴍɪʀʀᴏʀ/ᴄʟᴏɴᴇ sᴇᴛᴛɪɴɢs : {NAME}</u></b>

┎<b> ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</b> <i>{RCLONE}</i>
┠<b> ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</b> <code>{MPREFIX}</code>
┠<b> ᴍɪʀʀᴏʀ sᴜғғɪx :</b> <code>{MSUFFIX}</code>
┠<b> ᴍɪʀʀᴏʀ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
┠<b> ᴅᴅʟ sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
┠<b> ᴜsᴇʀ ᴛᴅ ᴍᴏᴅᴇ :</b> <i>{TMODE}</i>
┠<b> ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴛᴅ(s) :</b> <i>{USERTD}</i>
┖<b> ᴅᴀɪʟʏ ᴍɪʀʀᴏʀ :</b> <code>{DM}</code> ᴘᴇʀ day'''

    LEECH = '''㊂ <b><u>ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ 🫅{NAME}</u></b>

┎<b> ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </b><code>{DL}</code> ᴘᴇʀ ᴅᴀʏ
┠<b> ʟᴇᴇᴄʜ ᴛʏᴘᴇ :</b> <i>{LTYPE}</i>
┠<b> ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
┠<b> ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
┠<b> ᴇǫᴜᴀʟ sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
┠<b> ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
┠<b> ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
┠<b> ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</b> <code>{LPREFIX}</code>
┠<b> ʟᴇᴇᴄʜ sᴜғғɪx :</b> <code>{LSUFFIX}</code>
┠<b> ʟᴇᴇᴄʜ ᴅᴜᴍᴘs :</b> <code>{LDUMP}</code>
┖<b> ʟᴇᴇᴄʜ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>'''
