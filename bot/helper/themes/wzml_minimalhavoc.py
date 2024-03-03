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
    SYS_STATS = '''➣ <b><i>ᴏs sʏsᴛᴇᴍ :</i></b>
➣  <b>ᴏs ᴜᴘᴛɪᴍᴇ :</b> {os_uptime}
➣  <b>ᴏs ᴠᴇʀsɪᴏɴ :</b> {os_version}
➣ <b>ᴏs ᴀʀᴄʜ :</b> {os_arch}

➣ <b><i>ɴᴇᴛᴡᴏʀᴋ sᴛᴀᴛs :</i></b>
➣ <b>ᴜᴏʟᴏᴀᴅ ᴅᴀᴛᴀ:</b> {up_data}
➣ <b>ᴅᴏᴡʙʟᴏᴀᴅ ᴅᴇᴛᴀ:</b> {dl_data}
➣ <b>ᴘᴋʏs sᴇɴᴛ:</b> {pkt_sent}k
➣ <b>ᴘᴋʏs ʀᴇᴄᴇɪᴠᴇᴅ:</b> {pkt_recv}k
 ➣ <b>ᴛᴏᴛᴀʟ ɪ/𝟶 ᴅᴀᴛᴀ:</b> {tl_data}

➣ <b>ᴄᴘᴜ :</b>
➣ {cpu_bar} {cpu}%
➣  <b>ᴄᴘᴜ ғʀᴇǫᴜᴇɴᴄʏ :</b> {cpu_freq}
➣ <b>sʏsᴛᴇᴍ ᴀᴠɢ ʟᴏᴀᴅ :</b> {sys_load}
➣  <b>ᴘ-ᴄᴏʀᴇ(s) :</b> {ᴘ_ᴄᴏʀᴇ} | <b>ᴠ-ᴄᴏʀᴇ(s) :</b> {v_core}
 ➣ <b>ᴛᴏᴛᴀʟ ᴄᴏʀᴇ(s) :</b> {total_core}
➣ <b>ᴜsᴀʙʟᴇ ᴄᴘᴜ(s) :</b> {cpu_use}
    '''
    REPO_STATS = '''âŒ¬ <b>ʀᴇᴘᴏ sᴛᴀᴛɪsᴛɪᴄs :</b>
➣ <b>ʙᴏᴛ ᴜᴘᴅᴀᴛᴇᴅ :</b> {last_commit}
➣ <b>ᴄᴜʀʀᴇɴᴛ ᴠᴇʀsɪᴏɴ :</b> {bot_version}
➣ <b>ʟᴀᴛᴇsᴛ ᴠᴇʀsɪᴏɴ :</b> {lat_version}
➣ <b>ʟᴀsᴛ ᴄʜᴀɴɢᴇʟᴏɢ :</b> {commit_details}
 
 ➣ <b>ʀᴇᴍᴀʀᴋs :</b> <code>{remarks}</code>
    '''
    BOT_LIMITS = '''<b>ʙᴏᴛ ʟɪᴍɪᴛᴀᴛɪᴏɴs :</b>
➣ <b>ᴅɪʀᴇᴄᴛ ʟɪᴍɪᴛ :</b> {DL} GB
➣ <b>ᴛᴏʀʀᴇɴᴛ ʟɪᴍɪᴛ :</b> {TL} GB
➣ <b>ɢᴅʀɪᴠᴇ ʟɪᴍɪᴛ :</b> {GL} GB
➣ <b>ʏᴛ-ᴅʟᴘ ʟɪᴍɪᴛ :</b> {YL} GB
➣ <b>ᴘʟᴀʏʟɪsᴛ ʟɪᴍɪᴛ :</b> {PL}
➣ <b>ᴍᴇɢᴀ ʟɪᴍɪᴛ :</b> {ML} GB
➣ <b>ᴄʟᴏɴᴇ ʟɪᴍɪᴛ :</b> {CL} GB
➣ <b>ʟᴇᴇᴄʜ ʟɪᴍɪᴛ :</b> {LL} GB

➣ <b>ᴛᴏᴋᴇɴ ᴠᴀʟɪᴅɪᴛʏ :</b> {TV}
➣ <b>User ᴛɪᴍᴇ ʟɪᴍɪᴛ :</b> {UTI} / task
➣ <b>User ᴘᴀʀᴀʟʟᴇʟs ᴛᴀsᴋs :</b> {UT}
➣ <b>Bot ᴘᴀʀᴀʟʟᴇʟ ᴛᴀsᴋs :</b> {BT}
    '''
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = '<i>ʀᴇsᴛᴀʀᴛɪɴɢ--⋙..</i>'
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = '''âŒ¬ <b><i>ʀᴇsᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ✅</i></b>
➣ <b>ᴅᴀᴛᴇ:</b> {date}
➣ <b>ᴛɪᴍᴇ:</b> {time}
➣ <b>ᴛɪᴍᴇᴢᴏɴᴇ:</b> {timz}
➣ <b>Version:</b> {version}'''
    RESTARTED = '''<b><i>ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ🛠</i></b>'''
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = '<i>sᴛᴀʀᴛɪɴ_ ᴘɪɴɢ📡..</i>'
    PING_VALUE = '<b>ᴘᴏɴɢ</b>\n<code>{value} ᴍs..</code>'
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """<b><i>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ</i></b>
➣ <b>⚙️ᴍᴏᴅᴇ:</b> {Mode}
➣ <b>ʙʏ:</b> {Tag}\n\n"""
    LINKS_SOURCE = """ <b>🌐sᴏᴜʀᴄᴇ:</b>
➣ <b>ᴀᴅᴅᴇᴅ ᴏɴ!= :</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""
    
    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➩ <b><u>ᴛᴀsᴋ sᴛᴀʀᴛᴇᴅ :</u></b>\n┃\n┖ <b>ʟɪɴᴋ:</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"
    L_LOG_START =  "➩ <b><u>ʟᴇᴇᴄʜ sᴛᴀʀᴛᴇᴅ :</u></b>\n┃\n┠ <b>ᴜsᴇʀ :</b> {mention} ( #ID{uid} )\n┖ <b>Source :</b> <a href='{msg_link}'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME =                  '<b><i>✅{Name}</i></b>\nâ”ƒ\n'
    SIZE = '┠ <b>Size: </b>{Size}\n'
    ELAPSE =➩ <b>ᴇʟᴀᴘᴇᴅ: </b>{Time}\n'
    MODE =                  ➣ <b>ᴍᴏᴅᴇ: </b>{Mode}\n'

    # ----- LEECH -------
    L_TOTAL_FILES =         ➣ <b>ᴛᴏᴛᴀʟ ғɪʟᴇs: </b>{Files}\n'
    L_CORRUPTED_FILES =     ➣ <b>ᴄᴏʀʀᴜᴘᴛᴇᴅ ғɪʟᴇs: </b>{Corrupt}\n'
    L_CC =                  ➣ <b>ʙʏ: </b>{Tag}\n\n'
    PM_BOT_MSG =            ➣ <b><i>ғɪʟᴇ(ss) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴀʙᴏᴠᴇ</i></b>'
    L_BOT_MSG =             ➣ <b>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</b>'
    L_LL_MSG =              ➣ <b>ғɪʟᴇ(s) ʜᴀᴠᴇ ʙᴇᴇɴ sᴇɴᴛ. ᴀᴄᴄᴇss ᴠɪᴀ ʟɪɴᴋs...</b>\n'
    
    # ----- MIRROR -------
    M_TYPE =                ➣  <b>ᴛʏᴘᴇ: </b>{Mimetype}\n'
    M_SUBFOLD =             ➣  <b>sᴜʙғᴏʟᴅᴇʀs: </b>{Folder}\n'
    TOTAL_FILES =           ➣ <b>: ғɪʟᴇs</b>{Files}\n'
    RCPATH =                ➣ <b>ᴘᴀᴛʜ: </b><code>{RCpath}</code>\n'
    M_CC =                  ➣ <b>ʙʏ: </b>{Tag}\n\n'
    M_BOT_MSG =             ➣ <b><i>ʟɪɴᴋ(s) have been sᴇɴᴛ ᴛᴏ ʙᴏᴛ ᴘᴍ (ᴘʀɪᴠᴀᴛᴇ)</i></b>'
    # ----- BUTTONS -------
    CLOUD_LINK =      'â˜ï¸ ᴄʟᴏᴜᴅ ʟɪɴᴋ'
    SAVE_MSG =        'ðŸ“¨ sᴀᴠᴇ ᴍᴀssᴀɢᴇ'
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
    STATUS_NAME =       '<b><i>👨‍🎓ɴᴀᴍᴇ {Name}</i></b>'

    #####---------PROGRESSIVE STATUS-------
    BAR =               '\nâ”ƒ {Bar}'
    PROCESSED =         '\nâ”  <b>🔄ᴘʀᴏᴄᴇssᴇᴅ:</b> {Processed}'
    STATUS =            '\nâ”  <b>sᴛᴀᴛᴜs:</b> <a href="{Url}">{Status}</a>'
    ETA =                                                ' | <b>⚙️ᴇᴛᴀ:</b> {Eta}'
    SPEED =             '\nâ”  <b>⚡sᴘᴇᴇᴅ:</b> {Speed}'
    ELAPSED =                                     ' | <b>Elapsed:</b> {Elapsed}'
    ENGINE =            '\n <b>⏳ɴɢɪɴᴇ:</b> {Engine}'
    STA_MODE =          '\n <b>⛓️ᴍᴏᴅᴇ:</b> {Mode}'
    SEEDERS =           '\n  <b>🌱sᴇᴇᴅᴇʀs:</b> {Seeders} | '
    LEECHERS =                                           '<b>ʟᴇᴇᴄʜᴇʀs:</b> {Leechers}'
    
####--------SEEDING----------
    SEED_SIZE =      '\nâ”  <b>sɪᴢᴇ: </b>{Size}'
    SEED_SPEED =     '\nâ”  <b>sᴘᴇᴇғᴅ: </b> {Speed} | '
    UPLOADED =                                     '<b>ᴜᴘʟᴏᴀᴅ: </b> {Upload}'
    RATIO =          '\n  <b>ʀᴀᴅɪᴏ: </b> {Ratio} | '
    TIME =                                         '<b>ᴛɪᴍᴇ: </b> {Time}'
    SEED_ENGINE =    '\n  <b>ᴇɴɢɪɴᴇe:</b> {Engine}'

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE =    '\nâ”  <b>sɪᴢᴇ: </b>{Size}'
    NON_ENGINE =     '\nâ”  <b>ᴇɴɢɪɴᴇ:</b> {Engine}'

    ####--------OVERALL MSG FOOTER----------
    USER =              '\n  <b>ᴜsᴇʀ"":</b> <code>{User}</code> | '
    ID =                                                        '<b>ɪᴅ:</b> <code>{Id}</code>'
    BTSEL =          '\nâ”  <b>sᴇʟᴇᴄᴛ:</b> {Btsel}'
    CANCEL =         '\nâ”– {Cancel}\n\n'

    ####------FOOTER--------
    FOOTER = 'âŒ¬ <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>\n'
    TASKS =    <b>ᴛᴀsᴋs_:</b> {Tasks}\n'
    BOT_TASKS =  <b>ᴛᴀsᴋs:</b> {Tasks}/{Ttask} | <b>ᴀᴠʟ:</b> {Free}\n'
    Cpu =   <b>CPU:</b> {cpu}% | '
    FREE =                      '<b>ғ:</b> {free} [{free_p}%]'
    Ram = '\n  <b>ʀᴀᴍ:</b> {ram}% | '
    uptime =                     '<b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}'
    DL = '\n <b>DL:</b> {DL}/s | '
    UL =                        '<b>UL:</b> {UL}/s'

    ###--------BUTTONS-------
    PREVIOUS = 'â«·'
    REFRESH = 'á´˜á´€É¢á´‡s\n{Page}'
    NEXT = ''
    # ---------------------

    #STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = 'ғɪʟᴇ/ғᴏʟᴅᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴅʀɪᴠᴇ.\nʜᴇʀᴇ ᴀʀᴇ {content} ʟɪsᴛ ʀᴇsᴜʟᴛs:'
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = '<b>ᴄᴏᴜɴᴛɪɴɢ"":</b> <code>{LINK}</code>'
    COUNT_NAME = '<b><i>{COUNT_NAME}</i></b>\nâ”ƒ\n'
    COUNT_SIZE =  <b>sɪᴢᴇ_: </b>{COUNT_SIZE}\n'
    COUNT_TYPE =  <b>ᴛʏᴘᴇ: </b>{COUNT_TYPE}\n'
    COUNT_SUB =  <b>sᴜʙғᴏʟᴅᴇʀs: </b>{COUNT_SUB}\n'
    COUNT_FILE = <b>ғɪʟᴇs_: </b>{COUNT_FILE}\n'
    COUNT_CC =    <b>ʙʏ: </b>{COUNT_CC}\n'
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = '<b>sᴇᴀʀᴄʜɪɴɢ ғᴏʀ <i>{NAME}</i></b>'
    LIST_FOUND = '<b>ғᴏᴜɴᴅ {NO} ʀᴇsᴜʟᴛ ғᴏʀ <i>{NAME}</i></b>'
    LIST_NOT_FOUND = 'ɴᴏ!=  ʀᴇsᴜʟᴛ ғᴏᴜɴᴅ ғᴏʀ <i>{NAME}</i>'
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = '''<i>ɴᴏ ᴀᴄᴛɪᴠᴇ ᴅᴏᴡɴʟᴏᴀᴅs!</i>
    
 <b><i>ʙᴏᴛ sᴛᴀᴛs</i></b>
 <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
 <b>ʀᴀᴍ:</b> {ram} | <b>ᴜᴘᴛɪᴍᴇ:</b> {uptime}
    '''
    # ---------------------

    # USER Setting --> user_setting.py 
    USER_SETTING = ''' <b><u>ᴜsᴇʀ sɪᴛᴛɪɴɢs :</u></b>
        
<b> ɴᴀᴍᴇ :</b> {NAME} ( <code>{ID}</code> )
 <b> ᴜsᴇʀɴᴀᴍᴇ :</b> {USERNAME}
 <b> ᴛᴇʟᴇɢʀᴀᴍ ᴅᴄ :</b> {DC}
 <b> ʟᴀɴɢᴜᴀɢᴇ :</b> {LANG}

 <u><b>ᴀᴠᴀɪᴀʙʟᴇ ᴀʀɢs:</b></u>
 <b>-s</b> or <b>-set</b>: sᴇᴛ ᴅɪʀᴇᴄᴛʟʏ ᴠɪᴀ ᴀʀɢ'''

    UNIVERSAL = '''<b><u>ᴜɴɪᴠᴇʀsᴀʟ sᴇᴛᴛɪɴɢs : {NAME}</u></b>

<b> ʏᴛ-ᴅʟᴘ ᴏᴘᴛɪᴏɴs :</b> <b><code>{YT}</code></b>
<b> ᴅᴀɪʟʏ ᴛᴀsᴋs :</b> <code>{DT}</code> per day
<b> Last ʙᴏᴛ ᴜsᴇᴅ :</b> <code>{LAST_USED}</code>
<b> ᴜsᴇʀ Session :</b> <code>{USESS}</code>
<b> ᴍᴇᴅɪᴀɪɴғᴏ ᴍᴏᴅᴇ :</b> <code>{MEDIAINFO}</code>
<b> sᴀᴠᴇ ᴍᴏᴅᴇ :</b> <code>{SAVE_MODE}</code>
<b> ᴜsᴇʀ ʙᴏᴛ ᴘᴍ :</b> <code>{BOT_PM}</code>'''

    MIRROR = '''ãŠ‚ <b><u>Mirror/ᴄʟᴏɴᴇ sɪᴛᴛɪɴɢs : {NAME}</u></b>

<b> ʀᴄʟᴏɴᴇ ᴄᴏɴғɪɢ :</b> <i>{RCLONE}</i>
<b> ᴍɪʀʀᴏʀ ᴘʀᴇғɪx :</b> <code>{MPREFIX}</code>
<b> ᴍɪʀʀᴏʀ sᴜғғɪx :</b> <code>{MSUFFIX}</code>
<b> ᴍɪʀʀᴏʀ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{MREMNAME}</code>
<b> ᴅᴅʟ sᴇʀᴠᴇʀ(s) :</b> <i>{DDL_SERVER}</i>
<b> ᴜsᴇʀ ᴛᴅ ᴍᴏᴅᴇ :</b> <i>{TMODE}</i>
<b> ᴛᴏᴛᴀʟ ᴜsᴇʀ ᴛᴅ(s) :</b> <i>{USERTD}</i>
<b> ᴅᴀɪʟʏ!= ᴍɪʀʀᴏʀ :</b> <code>{DM}</code> per day'''

    LEECH = ''' <b><u>ʟᴇᴇᴄʜ sᴇᴛᴛɪɴɢs ғᴏʀ {NAME}</u></b>

<b> ᴅᴀɪʟʏ ʟᴇᴇᴄʜ : </b><code>{DL}</code> ᴘᴇʀ ᴅᴀʏ
<b> ʟᴇᴇᴄʜ ᴛʏᴘᴇ :</b> <i>{LTYPE}</i>
 <b> ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ :</b> <i>{THUMB}</i>
<b> ʟᴇᴇᴄʜ sᴘʟɪᴛ sɪᴢᴇ :</b> <code>{SPLIT_SIZE}</code>
 <b> ᴇǫᴜᴀʟ sᴘʟɪᴛs :</b> <i>{EQUAL_SPLIT}</i>
<b> ᴍᴇᴅɪᴀ ɢʀᴏᴜᴘ :</b> <i>{MEDIA_GROUP}</i>
<b> ʟᴇᴇᴄʜ ᴄᴀᴘᴛɪᴏɴ :</b> <code>{LCAPTION}</code>
<b> ʟᴇᴇᴄʜ ᴘʀᴇғɪx :</b> <code>{LPREFIX}</code>
<b> ʟᴇᴇᴄʜ sᴜғғɪx :</b> <code>{LSUFFIX}</code>
<b> ʟᴇᴇᴄʜ ᴅᴜᴍᴘs :</b> <code>{LDUMP}</code>
<b> ʟᴇᴇᴄʜ ʀᴇᴍɴᴀᴍᴇ :</b> <code>{LREMNAME}</code>'''
