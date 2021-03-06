o
    %?bW/  ?                   @   s,  d dl Z d dl mZ d dlZd dlmZ d dlmZmZmZ d dl	m
Z
 d dlmZmZ d dlmZmZ d dlZd dlZd dlmZ d dlZd dl	Z	ed	d
? dZdZdZeej? dej? dej? dej? d??Ze? Zd ad ad ad a G dd? de!?Z"e"? Z#dd? Z$dd? Z%e&dk?red? e'dej(? dej? d??)dej*? dej+? ??? edej+? ej(? ej+? dej? dej+? dej? d ej,? ??Z-e-d!kr?d"ne.e-?Z-g Z/ee-d#??2Z0e1e-?D ]$Z2e0?3e%? e ?d$e4te? e d%  ?? d&t? d't? d(t? d)t ? ?
? q?W d  ? dS 1 ?sw   Y  dS dS )*?    N)?system)?	b64encode)?init?Fore?Style??choice)?RLock?Thread)?time?sleep)?ThreadPoolExecutorT)ZconvertzData/Avatarszanti-captcha.comZBanditNuker123?[z-->?]z Captcha Key:  c                   @   s$   e Zd Ze? Zddd?Zdd? ZdS )?SynchronizedEchoTc                 C   s   |st ? | _d S d S ?N)r	   ?
print_lock)?selfZglobal_lock? r   ?token_gen.py?__init__   s   ?zSynchronizedEcho.__init__c                 C   s4   | j ? t|? W d   ? d S 1 sw   Y  d S r   )r   ?print)r   ?msgr   r   r   ?__call__"   s   
"?zSynchronizedEcho.__call__N)T)?__name__?
__module__?__qualname__r	   r   r   r   r   r   r   r   r      s    
r   c                  C   s    t dddd??? ?? } t?| ?S )Nzusernames.txt?cp437?ignore)?encoding?errors)?open?read?
splitlines?randomr   )Z	usernamesr   r   r   ?username'   s   
r%   c                  C   s?  ?zd} t dd??}dt|?? ???  } W d   ? n1 sw   Y  tjddidddd	d
ddddddddd?| d????}|jddd??? ?d?|jd< d|jd< d}tj	dt
? d?tddddd ?d!?dd"??? }|?d#?d$kr?ttj? tj? tj? d%tj? d&tj? d'tj? d(|?d)?? d*tj? ?? td$7 at? W  d   ? W S |?d+?}d$}d }|?stj	dt
? d,?t|d-?dd"??? }|?d.?d/k?r?|?d0??d1?}td27 a|j	d3d4|jd t? |d5?dd"?at?? ?d6?}||jd7< |jd= d8|jd9< d:|jd;< |jd<= d=|jd>< d?d?d@? tdA?D ??}|dB7 }t?t?t??}	tdC |	 }
t?t |
? dD?? ? ??!dE?}|j"dF|t#dGdH|? ?dI?dd"?}|j$dJk?rvt dKdL??}|?%|? dM?? W d   ? n	1 ?sbw   Y  t&d27 a&t? W  d   ? W S d}t'?(? }|?)dN? |?*? }t?+|?}dO|dPdQdRddSdTdUdVdddddWdXdYdZ?d[d$g d\d]?d\i d^d$d_d`?da?db?}|?,t?-|?? |?.?  t/|?d$k?r?t?dc| ?j0}t/|?d$k?s?tjdd| deddd
dfdgdhdidjd
dkdl?dm?j?dn??1do?d2 }dp|jd7< dq|jd9< |j	dr|d ds?dd"?}|j$dtk?r~ttj? tj? tj? d%tj? d&tj? d'tj? du?
? |j	dr|d ds?dd"?}|j$dtk?rct dvdL??}|?%|? dM?? t&d27 a&t? W  d   ? W  d   ? W S 1 ?s]w   Y  nt2tj? tj? tj? d%tj? dwtj? d'tj? dx?
? 	 |?? }ttj? tj? tj? d%tj? dwtj? d'tj? dy|?? ?d6?? dztj? ?? t3d27 a3t d{dL??}|?%|? d|t#? d||?? ?d6?? dM?? |?.?  W d   ? n	1 ?s?w   Y  t d}dL??}|?%|?? ?d6?? dM?? |?.?  W d   ? n	1 ?s?w   Y  |r?W d   ? n	1 ?sw   Y  W n; t4?yM } z.ttj? tj? tj? d%tj? d&tj? d'tj? d~|? tj? ?? ttj0? td27 aW Y d }~nd }~ww t?  d S )N? zProxies.txt?rzhttp://?localezen-USz*/*z
keep-alivezapplication/json?1zdiscord.comzhttps://discord.com/?emptyZcorszsame-originZtrailerszNMozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0a  eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=)?Accept?Accept-Language?
ConnectionzContent-Type?DNT?Host?Referer?Sec-Fetch-Dest?Sec-Fetch-Mode?Sec-Fetch-SiteZTE?
User-Agent?X-Track)Zcookies?headersZproxiesz&https://discord.com/api/v9/experiments?   )?timeout?fingerprintzX-Fingerprintzhttps://discord.comZOriginzhttps://api.z/createTaskZHCaptchaTaskProxylessz$f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34)?typeZ
websiteURLZ
websiteKeyZ	userAgent)?	clientKeyZtask)?jsonr8   ZerrorIdr   r   ?-r   z createTask - ZerrorDescription?!?taskIdz/getTaskResult)r;   r?   ?statusZreadyZsolutionZgRecaptchaResponse?   z(https://discord.com/api/v9/auth/registerT)Zconsentr9   r%   ?captcha_key?tokenZAuthorizationz https://discord.com/channels/@mer0   ZbugReporterEnabledzX-Debug-Optionsr5   a  eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTUuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk1LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA4OTI0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==zX-Super-Propertiesc                 s   s   ? | ]}t d ?V  qdS )ZabcdefghijklmnopqrstuvwxyzNr   )?.0?ir   r   r   ?	<genexpr>Z   s   ? z generateToken.<locals>.<genexpr>?
   z@OxiHasGithub.com?\?rb?asciiz$https://discord.com/api/v9/users/@mez
2000-01-01zdata:image/png;base64,)?email?passwordZdate_of_birth?avatari?  zLocked_tokens.txt?a?
z+wss://gateway.discord.gg/?v=6&encoding=json?   ?=   ZWindowsZChromezen-GBzsMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36z90.0.4430.212Z10ZstableZ85108Znull)?osZbrowserZdeviceZsystem_localeZbrowser_user_agentZbrowser_versionZ
os_versionZreferrerZreferring_domainZreferrer_currentZreferring_domain_currentZrelease_channelZclient_build_numberZclient_event_sourceZdndF)r@   ZsinceZ
activitiesZafk?0?????)Zguild_hashesZhighest_last_message_idZread_state_versionZuser_guild_settings_version)rC   ZcapabilitiesZ
propertiesZpresence?compressZclient_state)?op?dz0http://104.128.232.196:12345/api/getInbox?email=z'https://click.discord.com/ls/click?upn=zUtext/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8zclick.discord.comZdocumentZnavigateZnonez?1zNMozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0)r+   r,   r-   r.   r/   r1   r2   r3   zSec-Fetch-UserzUpgrade-Insecure-Requestsr4   )r6   ?location?=Z	undefinedzhttps://discord.com/verifyz&https://discord.com/api/v9/auth/verify)rC   rB   i?  z# Captcha on email verify, retrying!zUnverified_tokens.txt?+z' Succesfully passed captcha on 2nd try!z Token generated - ? z
Tokens.txt?:zTokens_unformat.txtz Error: )5r!   r   ?	readlines?strip?httpxZClient?getr<   r6   Zpost?
captchaApi?
captchaKey?s_printr   ?MAGENTAr   ?BRIGHT?RESET?	RESET_ALL?erroredTokens?generateToken?solvedr%   ZregReq?join?ranger$   rR   ?listdir?folder?base64r   r"   ?decodeZpatchrL   Zstatus_code?write?failedTokens?	websocketZ	WebSocketZconnectZrecv?loads?send?dumps?close?len?text?splitr   ?generatedTokens?	Exception)?proxy?fZclientr?   ZcaptchaTriesZsolvedCaptchaZcaptchaDatarC   rK   rN   rM   ZimggZuserDataZ	shittokenZ	emailDataZwsZresponseZeventZauthZ
emailTokenZ
shittoken1?g?er   r   r   ri   +   s?   ?4
,F?
	""



 ??/??<

4??>4J&
?
?????R>
??
ri   ?__main__?clsuk  


                    ████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗     ██████╗ ███████╗███╗   ██╗
                    ╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║    ██╔════╝ ██╔════╝████╗  ██║
                       ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║    ██║  ███╗█████╗  ██╔██╗ ██║
                       ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║    ██║   ██║██╔══╝  ██║╚██╗██║
                       ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║    ╚██████╔╝███████╗██║ ╚████║
                       ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                                           
                                      z<  Marcc#6666     |     Github.com/Futmarcc
                
rO   u   █z1                                                 ??z
 Threads: r&   rA   )Zmax_workersu&   title Token Generator by Marcc#6666ㅣ?<   u   /mㅣSuccess u
   ㅣFailed u	   ㅣError u    ㅣ Solved )5rR   r   r_   ro   r   Zcoloramar   r   r   r$   r   Z	threadingr	   r
   r   r   rs   Zconcurrent.futuresr   r<   rn   ra   rL   ?inputZREDZGREENrf   rb   ZgenStartTimer{   rr   rh   rj   ?objectr   rc   r%   ri   r   r   re   ?replaceZWHITErd   rg   ZthreadAmount?intZthreads?exrl   ?xZsubmit?roundr   r   r   r   ?<module>   s\    
(
c
???<
<?$??