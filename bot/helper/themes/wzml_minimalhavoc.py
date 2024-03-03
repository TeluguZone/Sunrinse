#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = '𝑴𝒂𝒔𝒕𝒆𝒓'
    ST_BN1_URL = 'https://t.me/owner_of_qtmve'
    ST_BN2_NAME = '𝑼𝒑𝒅𝒂𝒕𝒆 '
    ST_BN2_URL = 'https://t.me/QTVS_BOT_X_CLOUD'
    ST_MSG = '''<i>ᴮᵒᵗ ˢᵗᵃʳᵗ ⁱⁿ ᴰᴹ!!
     ɴᴏᴡ ᴀʟʟ ʏᴏᴜʀ ʟɪɴᴋꜱ/ꜰɪʟᴇꜱ ᴡɪʟʟ ᴄᴏᴍᴇ ʜᴇʀᴇ ðŸ•º.</i>
<b>Type {help_command} ᴛᴏ ɢᴇᴛ ᴀ ʟɪꜱᴛ ᴏꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ</b>'''
    ST_BOTPM = '''<i>ɴᴏᴡ, ᴛʜɪꜱ ʙᴏᴛ ᴡɪʟʟ ꜱᴇɴᴅ ᴀʟʟ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴀɴᴅ ʟɪɴᴋꜱ ʜᴇʀᴇ. ꜱᴛᴀʀᴛ ᴜꜱɪɴɢ ...</i>'''
    ST_UNAUTH = '''<i>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴜꜱᴇʀ! ᴅᴇᴘʟᴏʏ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ðŸ•º<a href='https://t.me/owner_of_qtmve'> bot</i>'''
    OWN_TOKEN_GENERATE = '''<b>𝐓𝐞𝐦𝐩𝐨𝐫𝐚𝐫𝐲 𝐓𝐨𝐤𝐞𝐧 𝐢𝐬 𝐧𝐨𝐭 𝐲𝐨𝐮𝐫𝐬!!</b>\n\n<i>𝙆𝙞𝙣𝙙𝙡𝙮 𝙜𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙮𝙤𝙪𝙧 𝙤𝙬𝙣..</i>'''
    USED_TOKEN = '''<b>ᵀᵉᵐᵖᵒʳᵃʳʸ ᵀᵒᵏᵉⁿ ᵃˡʳᵉᵃᵈʸ ᵘˢᵉᵈ</b>\n\n<i>Kindly generate a new one.</i>'''
    LOGGED_PASSWORD = '''<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>'''
    ACTIVATE_BUTTON = 'Activate Temporary Token'
    TOKEN_MSG = '''<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}'''
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = 'âœ…ï¸ Activated âœ…'
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = '<b>Already Bot Login In!</b>'
    INVALID_PASS = '<b>Invalid Password!</b>\n\nKindly put the correct Password .'
    PASS_LOGGED = '<b>Bot Permanent Login Successfully!</b>'
    LOGIN_USED = '<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>'
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = 'ðŸ“‘ Log Display'
    WEB_PASTE_BT = 'ðŸ“¨ Web Paste (SB)'
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = 'ʙᴀꜱɪᴄ'
    USER_BT = 'ᴜꜱᴇʀꜱ'
    MICS_BT = 'Mics'
    O_S_BT = 'ᴏᴡɴᴇʀ & sᴜᴅᴏs'
    CLOSE_BT = 'ᴄʟᴏsᴇ' 
    HELP_HEADER = "ãŠ‚ <b><i>Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = '''âŒ¬ <b><i>BOT STATISTICS :</i></b>
â”– <b>ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :</b> {bot_uptime}

â”Ž <b><i>RAM ( MEMORY ) :</i></b>
â”ƒ {ram_bar} {ram}%
â”– <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

â”Ž <b><i>SWAP MEMORY :</i></b>
â”ƒ {swap_bar} {swap}%
â”– <b>U :</b> {swap_u} | <b>ғ :</b> {swap_f} | <b>ᴛ :</b> {swap_t}

â”Ž <b><i>ᴅɪsᴋ :</i></b>
â”ƒ {disk_bar} {disk}%
â”ƒ <b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ʀᴇᴀᴅ :</b> {disk_read}
â”ƒ <b>ᴛᴏᴛᴀʟ ᴅɪsᴋ ᴡʀɪᴛᴇ :</b> {disk_write}
â”– <b>ᴜ :</b> {disk_u} | <b>ғ :</b> {disk_f} | <b>ᴛ :</b> {disk_t}
    
    '''
    SYS_STATS = '''âŒ¬ <b><i>ᴏs sʏsᴛᴇᴍ :</i></b>
â”  <b>ᴏs ᴜᴘᴛɪᴍᴇ :</b> {os_uptime}
â”  <b>ᴏs ᴠᴇʀsɪᴏɴ :</b> {os_version}
â”– <b>ᴏs ᴀʀᴄʜ :</b> {os_arch}

âŒ¬ <b><i>ɴᴇᴛᴡᴏʀᴋ sᴛᴀᴛs :</i></b>
â”  <b>ᴜᴏʟᴏᴀᴅ ᴅᴀᴛᴀ:</b> {up_data}
â”  <b>ᴅᴏᴡʙʟᴏᴀᴅ ᴅᴇᴛᴀ:</b> {dl_data}
â”  <b>ᴘᴋʏs sᴇɴᴛ:</b> {pkt_sent}k
â”  <b>ᴘᴋʏs ʀᴇᴄᴇɪᴠᴇᴅ:</b> {pkt_recv}k
â”– <b>ᴛᴏᴛᴀʟ ɪ/𝟶 ᴅᴀᴛᴀ:</b> {tl_data}

â”Ž <b>ᴄᴘᴜ :</b>
â”ƒ {cpu_bar} {cpu}%
â”  <b>ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}
â”  <b>sʏsᴛᴇᴍ ᴀᴠɢ ʟᴏᴀᴅ :</b> {sys_load}
â”  <b>ᴘ-ᴄᴏʀᴇ(s) :</b> {ᴘ_ᴄᴏʀᴇ} | <b>ᴠ-ᴄᴏʀᴇ(s) :</b> {v_core}
â”  <b>ᴛᴏᴛᴀʟ ᴄᴏʀᴇ(s) :</b> {total_core}
â”– <b>ᴜsᴀʙʟᴇ ᴄᴘᴜ(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''âŒ¬ <b>ʀᴇᴘᴏ sᴛᴀᴛɪsᴛɪᴄs :</b>
â”  <b>ʙᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ :</b> {last_commit}
â”  <b>ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ :</b> {bot_version}
â”  <b>ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ :</b> {lat_version}
â”– <b>ʟᴀsᴛ ᴄʜᴀɴɢᴇʟᴏɢ :</b> {commit_details}

âŒ¬ <b>ʀᴇᴍᴀʀᴋs :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''âŒ¬ <b>ʙᴏᴛ ʟɪᴍɪᴛᴀᴛɪᴏɴs :</b>
â”  <b>ᴅɪʀᴇᴄᴛ ʟɪᴍɪᴛ :</b> {DL} GB
â”  <b>ᴛᴏʀʀᴇɴᴛ ʟɪᴍɪᴛ :</b> {TL} GB
â”  <b>ɢᴅʀɪᴠᴇ ʟɪᴍɪᴛ :</b> {GL} GB
â”  <b>ʏᴛ-ᴅʟᴘ ʟɪᴍɪᴛ :</b> {YL} GB
â”  <b>ᴘʟᴀʏʟɪsᴛ ʟɪᴍɪᴛ :</b> {PL}
â”  <b>ᴍᴇɢᴀ ʟɪᴍɪᴛ :</b> {ML} GB
â”  <b>ᴄʟᴏɴᴇ ʟɪᴍɪᴛ :</b> {CL} GB
â”– <b>ʟᴇᴇᴄʜ ʟɪᴍɪᴛ :</b> {LL} GB

â”Ž <b>ᴛᴏᴋᴇɴ ᴠᴀʟɪᴅɪᴛʏ :</b> {TV}
â”  <b>User ᴛɪᴍᴇ ʟɪᴍɪᴛ :</b> {UTI} / task
â”  <b>User ᴘᴀʀᴀʟʟᴇʟs ᴛᴀsᴋs :</b> {UT}
â”– <b>Bot ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>ʀᴇsᴛᴀʀᴛɪɴɢ--⋙..</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''âŒ¬ <b><i>ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅</i></b>
â”  <b>ᴅᴀᴛᴇ:</b> {date}
â”  <b>ᴛɪᴍᴇ:</b> {time}
â”  <b>ᴛɪᴍᴇᴢᴏɴᴇ:</b> {timz}
â”– <b>Version:</b> {version}'''
    RESTARTED = '''âŒ¬ <b><i>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ🛠</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>sᴛᴀʀᴛɪɴ_ ᴘɪɴɢ📡..</i>'
    PING_VALUE = '<b>ᴘᴏɴɢ</b>\n<code>{value} ᴍs..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ</i></b>
â”  <b>⚙️ᴍᴏᴅᴇ:</b> {Mode}
â”– <b>ʙʏ:</b> {Tag}\n\n"""
    LINKS_SOURCE = """âž² <b>🌐sᴏᴜʀᴄᴇ:</b>
â”– <b>ᴀᴅᴅᴇᴅ ᴏɴ!= :</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START =            "âž² <b><u>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ :</u></b>\nâ”ƒ\nâ”– <b>ʟɪɴᴋ:</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"
    L_LOG_START =           "âž² <b><u>ʟᴇᴇᴄʜ sᴛᴀʀᴛᴇᴅ :</u></b>\nâ”ƒ\nâ”  <b>👨‍🎓ᴜsᴇʀ :</b> {mention} ( #ID{uid} )\nâ”– <b>sᴏᴜʀᴄᴇ :</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>✅{Name}</i></b>\nâ”ƒ\n'
    SIZE =                  'â”  <b>sɪᴢᴇ: </b>{Size}\n'
    ELAPSE =                'â”  <b>ᴇʟᴀᴘᴇᴅ: </b>{Time}\n'
    MODE =                  'â”  <b>ᴍᴏᴅᴇ: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         'â”  <b>ᴛᴏᴛᴀʟ ғɪʟᴇs: </b>{Files}\n'
    L_CORRUPTED_FILES =     'â”  <b>ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs: </b>{Corrupt}\n'
    L_CC =                  'â”– <b>ʙʏ: </b>{Tag}\n\n'
    PM_BOT_MSG =            'âž² <b><i>ғɪʟᴇ(ss) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ</i></b>'
    L_BOT_MSG =             'âž² <b>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</b>'
    L_LL_MSG =              'âž² <b>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇss ᴠɪᴀ ʟɪɴᴋs...</b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                'â”  <b>ᴛʏᴘᴇ: </b>{Mimetype}\n'
    M_SUBFOLD =             'â”  <b>sᴜʙғᴏʟᴅᴇʀs: </b>{Folder}\n'
    TOTAL_FILES =           'â”  <b>: ғɪʟᴇs</b>{Files}\n'
    RCPATH =                'â”  <b>ᴘᴀᴛʜ: </b><code>{RCpath}</code>\n'
    M_CC =                  'â”– <b>ʙʏ: </b>{Tag}\n\n'
    M_BOT_MSG =             'âž² <b><i>ʟɪɴᴋ(s) have been sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      'â˜ï¸ ᴄʟᴏᴜᴅ ʟɪɴᴋ'
    SAVE_MSG =        'ðŸ“¨ sᴀᴠᴇ ᴍᴀssᴀɢᴇ
    RCLONE_LINK =     'â™»ï¸ ʀᴄʟᴏɴᴇ ʟɪɴᴋ'
    DDL_LINK =        'ðŸ“Ž {Serv} ʟɪɴᴋ'
    SOURCE_URL =      'ðŸ” sᴏᴜʀᴄᴇ ʟɪɴᴋ'
    INDEX_LINK_F =    'ðŸ—‚ ɪɴᴅᴇx ʟɪɴᴋ'
    INDEX_LINK_D =    'âš¡ ɪɴᴅᴇx ʟɪɴᴋ'
    VIEW_LINK =       'ðŸŒ ᴠɪᴇᴡ ʟɪɴᴋ'
    CHECK_PM =        'ðŸ“¥ ᴠɪᴇᴡ ɪɴ ʙᴏᴛ ᴘᴍ'
    CHECK_LL =        'ðŸ–‡ ᴠɪᴇᴡ ɪɴ ʟɪɴᴋs ʟᴏɢ'
    MEDIAINFO_LINK =  'ðŸ“ƒ ᴍᴇᴅɪᴀɪɴғᴏ'
    SCREENSHOTS =     'ðŸ–¼ sᴄʀᴇᴇɴsʜᴏᴛs'
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME =       '<b><i>👨‍🎓{Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\nâ”ƒ {Bar}'
    PROCESSED =         '\nâ”  <b>🔄ᴘʀᴏᴄᴇssᴇᴅ:</b> {Processed}'
    STATUS =            '\nâ”  <b>sᴛᴀᴛᴜs:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>⚙️ᴇᴛᴀ:</b> {Eta}'
    SPEED =             '\nâ”  <b>⚡sᴘᴇᴇᴅ:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\nâ”  <b>⏳ɴɢɪɴᴇ:</b> {Engine}'
    STA_MODE =          '\nâ”  <b>⛓️ᴍᴏᴅᴇ:</b> {Mode}'
    SEEDERS =           '\nâ”  <b>🌱sᴇᴇᴅᴇʀs:</b> {Seeders} | '
    LEECHERS =                                           '<b>ʟᴇᴇᴄʜᴇʀs:</b> {Leechers}'
    
    <a href='{https://t.me/QTVS_BOT_X_CLOUD}'>ǫᴛᴍᴠᴇ-x</a>"

    ####--------SEEDING----------
    SEED_SIZE =      '\nâ”  <b>sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\nâ”  <b>sᴘᴇᴇғᴅ: </b> {Speed} | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅ: </b> {Upload}'
    RATIO =          '\nâ”  <b>ʀᴀᴅɪᴏ: </b> {Ratio} | '
    TIME =                                         '<b>ᴛɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\nâ”  <b>ᴇɴɢɪɴᴇe:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\nâ”  <b>sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\nâ”  <b>ᴇɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\nâ”  <b>ᴜsᴇʀ"":</b> <code>{User}</code> | '
    ID =                                                        '<b>ɪᴅ:</b> <code>{Id}</code>'
    BTSEL =          '\nâ”  <b>sᴇʟᴇᴄᴛ:</b> {Btsel}'
    CANCEL =         '\nâ”– {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = 'âŒ¬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>\n'
    TASKS =  'â”  <b>ᴛᴀsᴋs_:</b> {Tasks}\n'
    BOT_TASKS = 'â”  <b>ᴛᴀsᴋs:</b> {Tasks}/{Ttask} | <b>ᴀᴠʟ:</b> {Free}\n'
    Cpu = 'â”  <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>ғ:</b> {free} [{free_p}%]'
    Ram = '\nâ”  <b>ʀᴀᴍ:</b> {ram}% | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}'
    DL = '\nâ”– <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = 'â«·'
    REFRESH = 'á´˜á´€É¢á´‡s\n{Page}'
    NEXT = 'â«¸'
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'ғɪʟᴇ/ғᴏʟᴅᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅʀɪᴠᴇ.\nʜᴇʀᴇ ᴀʀᴇ {content} ʟɪsᴛ ʀᴇsᴜʟᴛs:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>ᴄᴏᴜɴᴛɪɴɢ"":</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\nâ”ƒ\n'
    COUNT_SIZE = 'â”  <b>sɪᴢᴇ_: </b>{COUNT_SIZE}\n'
    COUNT_TYPE = 'â”  <b>ᴛʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  'â”  <b>sᴜʙғᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = 'â”  <b>ғɪʟᴇs_: </b>{COUNT_FILE}\n'
    COUNT_CC =   'â”– <b>ʙʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>sᴇᴀʀᴄʜɪɴɢ ғᴏʀ <i>{NAME}</i></b>'
    LIST_FOUND = '<b>ғᴏᴜɴᴅ {NO} ʀᴇsᴜʟᴛ ғᴏʀ <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'ɴᴏ!=  ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>ɴᴏ ᴀᴄᴛɪᴠᴇ ᴅᴏᴡɴʟᴏᴀᴅs!</i>
    
âŒ¬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>
â”  <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
â”– <b>ʀᴀᴍ:</b> {ram} | <b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = '''ãŠ‚ <b><u>ᴜsᴇʀ sɪᴛᴛɪɴɢs :</u></b>
        
â”Ž<b> ɴᴀᴍᴇ :</b> {NAME} ( <code>{ID}</code> )
â” <b> ᴜsᴇʀɴᴀᴍᴇ :</b> {USERNAME}
â” <b> ᴛᴇʟᴇɢʀᴀᴍ ᴅᴄ :</b> {DC}
â”–<b> ʟᴀɴɢᴜᴀɢᴇ :</b> {LANG}

âž² <u><b>ᴀᴠᴀɪᴀʙʟᴇ ᴀʀɢs:</b></u>
â€¢ <b>-s</b> or <b>-set</b>: sᴇᴛ ᴅɪʀᴇᴄᴛʟʏ ᴠɪᴀ ᴀʀɢ'''

    UNIVERSAL = '''ãŠ‚ <b><u>ᴜɴɪᴠᴇʀsᴀʟ sᴇᴛᴛɪɴɢs : {NAME}</u></b>

â”Ž<b> ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
â” <b> ᴅᴀɪʟʏ ᴛᴀsᴋs :</b> <code>{DT}</code> per day
â” <b> Last ʙᴏᴛ ᴜsᴇᴅ :</b> <code>{LAST_USED}</code>
â” <b> ᴜsᴇʀ Session :</b> <code>{USESS}</code>
â” <b> ᴍᴇᴅɪᴀɪɴғᴏ ᴍᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
â” <b> sᴀᴠᴇ ᴍᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
â”–<b> ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''ãŠ‚ <b><u>Mirror/ᴄʟᴏɴᴇ sɪᴛᴛɪɴɢs : {NAME}</u></b>

â”Ž<b> ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</b> <i>{RCLONE}</i>
â” <b> ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</b> <code>{MPREFIX}</code>
â” <b> ᴍɪʀʀᴏʀ sᴜғғɪx :</b> <code>{MSUFFIX}</code>
â” <b> ᴍɪʀʀᴏʀ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
â” <b> ᴅᴅʟ sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
â” <b> ᴜsᴇʀ ᴛᴅ ᴍᴏᴅᴇ :</b> <i>{TMODE}</i>
â” <b> ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴛᴅ(s) :</b> <i>{USERTD}</i>
â”–<b> ᴅᴀɪʟʏ!= ᴍɪʀʀᴏʀ :</b> <code>{DM}</code> per day'''

    LEECH = '''ãŠ‚ <b><u>ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

â”Ž<b> ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </b><code>{DL}</code> ᴘᴇʀ ᴅᴀʏ
â” <b> ʟᴇᴇᴄʜ ᴛʏᴘᴇ :</b> <i>{LTYPE}</i>
â” <b> ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
â” <b> ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
â” <b> ᴇǫᴜᴀʟ sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
â” <b> ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
â” <b> ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
â” <b> ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</b> <code>{LPREFIX}</code>
â” <b> ʟᴇᴇᴄʜ sᴜғғɪx :</b> <code>{LSUFFIX}</code>
â” <b> ʟᴇᴇᴄʜ ᴅᴜᴍᴘs :</b> <code>{LDUMP}</code>
â”–<b> ʟᴇᴇᴄʜ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>'''